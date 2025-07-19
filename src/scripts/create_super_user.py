from django.contrib.auth import get_user_model


def run(*args) -> None:
    """
    Creates a Django superuser if it does not already exist.

    Usage:
        python manage.py runscript create_super_user

    Example:
        This script will create a superuser with the following credentials:
            username: shadaab-karim
            first_name: Shadaab
            last_name: Karim
            email: karimshadaab510@gmail.com
            password: +ocAdretrET7axls5apl

    Returns:
        None
    """
    # Get the custom User model
    User = get_user_model()

    kwargs = {}
    for arg in args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            kwargs[key] = value

    print("Args : ", args)
    print("Kwargs : ", kwargs)

    # Superuser credentials
    username: str = "shadaab-karim"
    first_name: str = "Shadaab"
    last_name: str = "Karim"
    email: str = "karimshadaab510@gmail.com"
    password: str = "+ocAdretrET7axls5apl"

    # Check if the superuser already exists
    if not User.objects.filter(username=username).exists():
        # Create the superuser
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        print(f"✅ Superuser '{username}' created.")
    else:
        print(f"ℹ️ Superuser '{username}' already exists.")
