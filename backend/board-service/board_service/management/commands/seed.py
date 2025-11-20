# board_service/management/commands/seed.py

from django.core.management.base import BaseCommand
from django.db import connection
from board_service.models import Board

class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Running seed script...")

        # Check if the table exists at the PostgreSQL level
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'board_service_board'
                );
            """)
            table_exists = cursor.fetchone()[0]

        if not table_exists:
            self.stdout.write(self.style.WARNING(
                "Table board_service_board does not exist yet. Run migrations first or wait for them to complete."
            ))
            return

        if Board.objects.exists():
            self.stdout.write("Boards already exist! Skipping seeding.")
            return

        demo_boards = [
            {"title": "Demo Board 1", "owner": 1},
            {"title": "Demo Board 2", "owner": 1},
            {"title": "Team Planning", "owner": 2},
        ]

        for data in demo_boards:
            Board.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded boards!"))