from django.shortcuts import redirect, reverse


def family_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, "familymember"):
            return redirect(reverse("create_family"))

        return view_func(request, *args, **kwargs)

    return wrapper


def not_in_family_required(view_func):
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, "familymember"):
            return redirect(reverse("dashboard"))

        return view_func(request, *args, **kwargs)

    return wrapper
