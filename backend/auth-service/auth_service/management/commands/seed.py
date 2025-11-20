from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **kwargs):
        # Users
        if User.objects.count() == 0:
            User.objects.create_user("user1", password="pass")
            User.objects.create_user("user2", password="pass")
            User.objects.create_user("user3", password="pass")
            print("Users created!")
        else:
            print("Users already exist!")
