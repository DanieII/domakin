from django.db import models
from families.models import Family, FamilyMember


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    completed_by = models.ForeignKey(
        FamilyMember, on_delete=models.SET_NULL, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
