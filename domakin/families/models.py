from django.contrib.auth import get_user_model
from django.db import models
import uuid

UserModel = get_user_model()


class Family(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FamilyMember(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name

    def completed_tasks_count(self):
        return self.family.task_set.filter(completed_by=self).count()


class FamilyInvitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    family = models.OneToOneField(Family, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.family.name
