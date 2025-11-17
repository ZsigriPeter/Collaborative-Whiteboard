from whiteboard.models import Board

def run():
    if Board.objects.count() == 0:
        Board.objects.create(name="Demo Board 1", owner_id=1)
        Board.objects.create(name="Team Sketch", owner_id=2)
        Board.objects.create(name="UX Ideas", owner_id=3)
        print("Boards created!")
    else:
        print("Boards already exist, skipping.")
