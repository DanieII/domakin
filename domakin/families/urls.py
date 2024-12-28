from django.urls import path
from .views import FamilyCreateView, FamilyDetailView

urlpatterns = [
    path("create", FamilyCreateView.as_view(), name="create_family"),
    path("dashboard", FamilyDetailView.as_view(), name="dashboard"),
]
