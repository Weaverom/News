from django.core.management.base import BaseCommand
from news.models import Post, Category


class Command(BaseCommand):
    help = "Обнуляет новости в категории"

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы уверены что хотите удалить все статьи в категории {options["category"]}&? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Все посты из категории {category.name} удалены'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Указанная категория не найдена'))



