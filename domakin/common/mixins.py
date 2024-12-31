from django.shortcuts import redirect, reverse
from django.views.generic import View


class FamilyRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "familymember"):
            return redirect(reverse("create_family"))

        return super().dispatch(request, *args, **kwargs)


class NotInFamilyRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, "familymember"):
            return redirect(reverse("dashboard"))

        return super().dispatch(request, *args, **kwargs)
