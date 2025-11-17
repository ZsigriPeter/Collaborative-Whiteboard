from django.contrib.auth.models import User

def run(): 
    if User.objects.count()==0:
        User.objects.create_superuser(username="admin",password="admin123")
        User.objects.create_user(username="alice",password="alice123")
        User.objects.create_user(username="bob",password="bob123")
        User.objects.create_user(username="charlie",password="charlie123")
        print("Users created!")
    else:
        print("Users already exist")