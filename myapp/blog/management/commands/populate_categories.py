from typing import Any
from blog.models import Category
from django.core.management import BaseCommand


class Command(BaseCommand):
    help="This commands insert category data"

    def handle(self, *args: Any, **options: Any):
        #Delete all exists data
        Category.objects.all().delete()
        
        categories = ['Sports','Technology','Science','Art','Food']

        for category_name in categories:
            Category.objects.create(name=category_name)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))