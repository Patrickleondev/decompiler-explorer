
import hashlib
import os
from django.core.management.base import BaseCommand
from django.core.files import File
from explorer.models import Binary

class Command(BaseCommand):
    help = 'Imports binaries from a directory for CTF challenges'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Directory containing binaries to import')

    def handle(self, *args, **options):
        directory = options['directory']

        if not os.path.exists(directory):
            self.stdout.write(self.style.ERROR(f'Directory "{directory}" does not exist'))
            return

        count = 0
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                # Skip if it's not a file or if it's too large (unless configured otherwise)
                if not os.path.isfile(file_path):
                    continue

                with open(file_path, 'rb') as f:
                    file_content = f.read()
                    file_hash = hashlib.sha256(file_content).hexdigest()

                    if Binary.objects.filter(hash=file_hash).exists():
                        self.stdout.write(f'Skipping {filename} ({file_hash}) - already exists')
                        continue

                    self.stdout.write(f'Importing {filename} ({file_hash})...')
                    
                    # Create Binary object
                    binary = Binary(hash=file_hash)
                    # Django's File object wrapper
                    django_file = File(f, name=filename)
                    binary.file.save(filename, django_file)
                    binary.save()
                    count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} binaries'))
