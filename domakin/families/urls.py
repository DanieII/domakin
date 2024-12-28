from django.urls import path
from .views import (
    FamilyCreateView,
    FamilyDetailView,
    accept_family_invitation_view,
    create_family_invitation_view,
)

urlpatterns = [
    path("create", FamilyCreateView.as_view(), name="create_family"),
    path("dashboard", FamilyDetailView.as_view(), name="dashboard"),
    path(
        "invitations/create",
        create_family_invitation_view,
        name="create_family_invitation",
    ),
    path(
        "invitations/accept/<uuid:invitation_id>",
        accept_family_invitation_view,
        name="accept_family_invitation",
    ),
]
