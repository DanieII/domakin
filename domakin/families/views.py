from django.shortcuts import redirect
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
        family = form.save()

        FamilyMember.objects.create(
            user=self.request.user, family=family, is_admin=True
        )

        return super().form_valid(form)


class FamilyDetailView(LoginRequiredMixin, FamilyRequiredMixin, DetailView):
    model = Family
    template_name = "families/dashboard.html"
    context_object_name = "family"

    def get_object(self, queryset=None):
        user_family = self.request.user.familymember.family

        return user_family
