from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from board_service.models import Board

class Command(BaseCommand):
    help = "Seed initial board data"

    def handle(self, *args, **options):
        if Board.objects.count() == 0:
            Board.objects.create(name="Demo Board 1", owner=User.objects.get(username="alice"))
            Board.objects.create(name="Team Sketch", owner=User.objects.get(username="bob"))
            Board.objects.create(name="UX Ideas", owner=User.objects.get(username="charlie"))
            self.stdout.write("Boards created!")
        else:
            self.stdout.write("Boards already exist. Skipping.")
