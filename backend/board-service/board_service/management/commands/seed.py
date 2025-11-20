from django.core.management.base import BaseCommand
from board_service.models import Board

class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **kwargs):
        # Boards
        if Board.objects.count() == 0:
            Board.objects.create(name="Demo Board 1", owner_id=1)
            Board.objects.create(name="Team Sketch", owner_id=2)
            Board.objects.create(name="UX Ideas", owner_id=3)
            print("Boards created!")
        else:
            print("Boards already exist!")
