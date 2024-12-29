from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from .models import Task
from common.mixins import FamilyRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(family=self.request.user.familymember.family)

        return queryset


class TaskCreateView(LoginRequiredMixin, FamilyRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description"]

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = form_class(**self.get_form_kwargs())
        form.fields["title"].widget.attrs.update(
            {"class": "input input-bordered", "placeholder": "Заглавие"}
        )
        form.fields["description"].widget.attrs.update(
            {
                "class": "textarea textarea-bordered",
                "placeholder": "Описание",
                "rows": "3",
            }
        )

        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.family = self.request.user.familymember.family
        self.object.save()

        return redirect("tasks")
