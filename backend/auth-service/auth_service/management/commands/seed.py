from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seeds the database with initial user data."

    def handle(self, *args, **kwargs):
        self.stdout.write("Running seed script...")

        if User.objects.exists():
            self.stdout.write("Users already exist! Skipping seeding.")
            return

        demo_users = [
            {"username": "admin", "password": "admin123", "is_superuser": True, "is_staff": True},
            {"username": "john", "password": "password123"},
            {"username": "emma", "password": "password123"},
        ]

        for user in demo_users:
            self.create_user(user)

        self.stdout.write(self.style.SUCCESS("Users created!"))

    def create_user(self, data):
        username = data["username"]
        password = data["password"]
        is_superuser = data.get("is_superuser", False)
        is_staff = data.get("is_staff", False)

        user = User(
            username=username,
            is_superuser=is_superuser,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save()
