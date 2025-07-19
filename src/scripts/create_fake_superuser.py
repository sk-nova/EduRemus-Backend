from django.contrib.auth import get_user_model
from faker import Faker

# ==========================================
# Script to create a fake Django superuser
# ==========================================


def run():
    # Initialize Faker for generating fake data
    fake = Faker()

    # Get the custom or default User model
    User = get_user_model()

    # Generate fake credentials
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    # Check if the username already exists
    if not User.objects.filter(username=username).exists():
        # Create a new superuser with fake credentials
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Created superuser : {username} {email} | Password : {password}")
    else:
        # Inform if the user already exists
        print("User already exists.")


# ==========================================
