from django.contrib.auth import get_user_model
from faker import Faker


def run():
    fake = Faker()

    User = get_user_model()

    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

        print(f"Created superuser : {username} {email} | Password : {password}")
    else:
        print("User already exists.")
