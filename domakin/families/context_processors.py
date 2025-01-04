def user_family(request):
    if request.user.is_authenticated and hasattr(request.user, "familymember"):
        return {"user_family": request.user.familymember.family}

    return {"user_family": None}
