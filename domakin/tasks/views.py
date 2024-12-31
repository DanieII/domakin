from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView
from common.decorators import family_required
from .models import Task
from common.mixins import FamilyRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(ListView):
    model = Task
    template_name = "components/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(family=self.request.user.familymember.family)

        return queryset


class TaskCreateView(LoginRequiredMixin, FamilyRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description"]
    template_name = "components/task_form.html"

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

        tasks = Task.objects.filter(family=self.request.user.familymember.family)

        return render(self.request, "components/task_list.html", {"tasks": tasks})


@login_required
@family_required
def task_complete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task and task.family == request.user.familymember.family:
        task.is_completed = True
        task.save()

    tasks = Task.objects.filter(family=request.user.familymember.family)

    return render(request, "components/task_list.html", {"tasks": tasks})
