def is_admin(user):
    # return True
    return user.is_authenticated and user.role == 1
