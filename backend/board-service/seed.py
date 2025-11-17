from django.contrib.auth.models import User
from board_service.models import Board

def run():
    # Create users if they don't exist
    if User.objects.count() == 0:
        User.objects.create_user(username="user1", password="password1")
        User.objects.create_user(username="user2", password="password2")
        User.objects.create_user(username="user3", password="password3")
        print("Users created!")

    # Create boards
    if Board.objects.count() == 0:
        Board.objects.create(name="Demo Board 1", owner=User.objects.get(username="user1"))
        Board.objects.create(name="Team Sketch", owner=User.objects.get(username="user2"))
        Board.objects.create(name="UX Ideas", owner=User.objects.get(username="user3"))
        print("Boards created!")
    else:
        print("Boards already exist, skipping.")