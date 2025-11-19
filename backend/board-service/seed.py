from django.contrib.auth.models import User
from board_service.models import Board

def run_seed():
    # Seed users
    if User.objects.count() == 0:
        User.objects.create_user(username="demo1", password="demo1")
        User.objects.create_user(username="demo2", password="demo2")
        User.objects.create_user(username="demo3", password="demo3")
        print("Users seeded.")
    else:
        print("Users already exist.")

    # Seed boards
    if Board.objects.count() == 0:
        Board.objects.create(name="Demo Board 1", owner_id=1)
        Board.objects.create(name="Team Sketch", owner_id=2)
        Board.objects.create(name="UX Ideas", owner_id=3)
        print("Boards seeded.")
    else:
        print("Boards already exist.")
