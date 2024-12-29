from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import Family, FamilyInvitation, FamilyMember
from django.contrib.auth.mixins import LoginRequiredMixin
from common.mixins import FamilyRequiredMixin, NotInFamilyRequiredMixin


class FamilyCreateView(LoginRequiredMixin, NotInFamilyRequiredMixin, CreateView):
    model = Family
    fields = ["name"]
    success_url = reverse_lazy("index")

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = form_class(**self.get_form_kwargs())
        form.fields["name"].widget.attrs.update(
            {"class": "input input-bordered", "placeholder": "Име на семейството"}
        )

        return form

    def form_valid(self, form):
        self.object = form.save()

        FamilyMember.objects.create(
            user=self.request.user, family=self.object, is_admin=True
        )

        return redirect(self.get_success_url())


class FamilyDetailView(LoginRequiredMixin, FamilyRequiredMixin, DetailView):
    model = Family
    template_name = "families/dashboard.html"
    context_object_name = "family"

    def get_object(self, queryset=None):
        user_family = self.request.user.familymember.family

        return user_family


@login_required
def create_family_invitation_view(request):
    if not hasattr(request.user, "familymember"):
        return redirect(reverse("create_family"))

    family = request.user.familymember.family
    invitation = getattr(family, "familyinvitation", None)

    if not invitation:
        invitation = FamilyInvitation.objects.create(family=family)

    invitation_link = request.build_absolute_uri(
        reverse("accept_family_invitation", args=[invitation.id])
    )

    return render(
        request,
        "components/family_invitation.html",
        {"invitation_link": invitation_link},
    )


@login_required
def accept_family_invitation_view(request, invitation_id):
    if hasattr(request.user, "familymember"):
        return redirect(reverse("create_family"))

    invitation = FamilyInvitation.objects.get(id=invitation_id)
    family = invitation.family

    FamilyMember.objects.create(user=request.user, family=family)
    invitation.delete()

    return redirect("dashboard")
