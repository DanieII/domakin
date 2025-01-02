from django.urls import path
from .views import (
    dashboard_view,
    FamilyCreateView,
    accept_family_invitation_view,
    create_family_invitation_view,
)

urlpatterns = [
    path("dashboard", dashboard_view, name="dashboard"),
    path("create", FamilyCreateView.as_view(), name="create_family"),
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
