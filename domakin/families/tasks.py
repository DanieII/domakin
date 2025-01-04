from celery import shared_task
from django.db.models import Count
from .models import Family


@shared_task
def weekly_reset():
    families = Family.objects.all()

    for family in families:
        # Increase the wins of the family member with the most completed tasks
        weekly_winner = (
            family.familymember_set.annotate(num_tasks=Count("task"))
            .order_by("-num_tasks")
            .first()
        )
        if weekly_winner.num_tasks:
            weekly_winner.wins += 1
            weekly_winner.save()

        # Reset the family's completed tasks
        family.task_set.all().filter(is_completed=True).delete()
