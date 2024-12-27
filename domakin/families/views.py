from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Family, FamilyMember
from django.contrib.auth.mixins import LoginRequiredMixin


class FamilyCreateView(LoginRequiredMixin, CreateView):
    model = Family
    fields = ["name"]
    success_url = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, "familymember"):
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)

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
