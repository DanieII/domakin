from django.urls import path
from .views import FamilyCreateView

urlpatterns = [path("create", FamilyCreateView.as_view(), name="create_family")]
