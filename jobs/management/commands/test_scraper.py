from django.core.management.base import BaseCommand
from jobs.scraper import scrape_remoteok

class Command(BaseCommand):
    help = 'Test job scraper with print output'

    def handle(self, *args, **kwargs):
        scrape_remoteok()
