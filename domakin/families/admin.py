from django.contrib import admin
from .models import Family, FamilyMember


class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    inlines = [FamilyMemberInline]
