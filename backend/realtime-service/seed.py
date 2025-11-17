from realtime_service.models import Stroke

def run():
    if Stroke.objects.count() == 0:
        Stroke.objects.create(board_id=1, data={"points": [[0,0],[10,10]]})
        print("Strokes created!")
    else:
        print("Strokes already exist, skipping.")
