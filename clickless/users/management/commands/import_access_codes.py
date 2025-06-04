from django.core.management.base import BaseCommand
from users.models import AccessCode
from datetime import datetime

class Command(BaseCommand):
    help = 'Import access codes from SQL dump file'

    def handle(self, *args, **options):
        # Sample data from your SQL dump
        access_codes = [
            ('0053JMXG', '2024-06-20 00:00:00.000000', '2025-05-08 23:59:59.000000', 162, '2025-03-28 00:00:00', 0),
            ('0122HWHX', '2024-06-20 00:00:00.000000', '2025-04-14 23:59:59.000000', 143, '2025-03-04 00:00:00', 3),
            ('0182AOBV', '2024-06-20 00:00:00.000000', None, None, None, None),
            ('0252BPPW', '2024-06-20 00:00:00.000000', '2025-02-02 23:59:59.000000', 121, '2024-12-23 00:00:00', 6),
            ('0352DJEI', '2024-06-20 00:00:00.000000', None, None, None, None),
        ]

        for code_data in access_codes:
            access_code, created_at, expired_at, user_id, activated_at, completed_survey_week = code_data
            
            # Convert string dates to datetime objects
            created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f')
            if expired_at:
                expired_at = datetime.strptime(expired_at, '%Y-%m-%d %H:%M:%S.%f')
            if activated_at:
                activated_at = datetime.strptime(activated_at, '%Y-%m-%d %H:%M:%S')

            # Create or update the access code
            AccessCode.objects.update_or_create(
                access_code=access_code,
                defaults={
                    'created_at': created_at,
                    'expired_at': expired_at,
                    'user_id': user_id,
                    'activated_at': activated_at,
                    'completed_survey_week': completed_survey_week
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported access codes')) 