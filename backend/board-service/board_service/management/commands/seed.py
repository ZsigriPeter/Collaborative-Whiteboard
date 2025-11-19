from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from board_service.models import Board

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

        # Boards
        if Board.objects.count() == 0:
            Board.objects.create(name="Demo Board 1", owner_id=1)
            Board.objects.create(name="Team Sketch", owner_id=2)
            Board.objects.create(name="UX Ideas", owner_id=3)
            print("Boards created!")
        else:
            print("Boards already exist!")
