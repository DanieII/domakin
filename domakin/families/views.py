from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from common.decorators import family_required
from families.tasks import reset_family_tasks
from .models import Family, FamilyInvitation, FamilyMember
from django.contrib.auth.mixins import LoginRequiredMixin
from common.mixins import NotInFamilyRequiredMixin


@login_required
@family_required
def dashboard_view(request):
    return render(request, "families/dashboard.html")


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
