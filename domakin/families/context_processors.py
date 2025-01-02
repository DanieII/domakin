def user_family(request):
    if request.user.is_authenticated:
        return {"user_family": request.user.familymember.family}

    return {"user_family": None}
