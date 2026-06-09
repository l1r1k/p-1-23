from django.db import models

# Create your models here.

COMMON_LENGTH = 100
MAX_LENGTH = 255
COMMON_LENGTH_TEXT = 512
MAX_LENGTH_TEXT = 1024

class Category(models.Model):
    name = models.CharField(
        max_length=COMMON_LENGTH,
        null=False,
        unique=True,
        verbose_name='Название категории',
        help_text='Необходимо в поле указать название категории',
    )
    description = models.TextField(
        max_length=COMMON_LENGTH_TEXT,
        null=True,
        blank=True,
        default='Отсутствует',
        verbose_name='Описание категории',
        help_text='Указывайте описание категории, если считаете, что категория неочивидна'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

def get_current_year():
    from datetime import datetime
    return datetime.now().year

def get_current_season():
    from datetime import datetime
    seasons = {
        1: 'WI',
        2: 'WI',
        3: 'SP',
        4: 'SP',
        5: 'SP',
        6: 'SU',
        7: 'SU',
        8: 'SU',
        9: 'AU',
        10: 'AU',
        11: 'AU',
        12: 'WI'
    }
    return seasons[datetime.now().month]

class Collection(models.Model):
    seasons = [
        ('WI', 'Зима'),
        ('SP', 'Весна'),
        ('SU', 'Лето'),
        ('AU', 'Осень'),
    ]


    name = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        unique=True,
        verbose_name='Название коллекции',
        help_text='Необходимо в поле указать название коллекции',
    )
    description = models.TextField(
        max_length=MAX_LENGTH_TEXT,
        null=True,
        blank=True,
        default='Отсутствует',
        verbose_name='Описание коллекции',
        help_text='Подробно опишите добавляемую коллекцию, чтобы пользователи могли ознакомиться с ней'
    )
    year = models.PositiveIntegerField(
        null=True,
        blank=False,
        default=get_current_year,
        verbose_name='Год выхода коллекции',
        help_text='Укажите год выхода коллекции',
    )
    season = models.CharField(
        max_length=2,
        choices=seasons,
        blank=False,
        default=get_current_season,
        verbose_name='Время года выхода коллекции',
        help_text='Выберите время года, когдая вышла коллекция или же под какое время года данная коллекция'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

class Clothe(models.Model):
    name = models.CharField(
        max_length=COMMON_LENGTH,
        verbose_name='Название одежды',
        help_text='Укажите название одежды'
    )
    description = models.TextField(
        max_length=MAX_LENGTH_TEXT,
        verbose_name='Описание одежды',
        null=True,
        blank=False,
        default='Отсутствует',
        help_text='Укажите подробное описание одежды'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Стоимость одежды',
        help_text='Укажите стоимость одежды, вплоть до копеек'
    )
    color = models.CharField(
        max_length=COMMON_LENGTH,
        verbose_name='Цвет одежды',
        help_text='Укажите цвет одежды'
    )
    size = models.PositiveSmallIntegerField(
        verbose_name='Размер одежды',
        help_text='Укажите размер одежды'
    )
    photo = models.ImageField(
        upload_to='img/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='Изображение одежды',
        help_text='Выберите и загрузите изображение одежды со своего компьютера',
        default='img/no-photo.jpg'
    )
    is_exists = models.BooleanField(
        verbose_name='Наличие одежды',
        default=True
    )

    created_at = models.DateTimeField(
        editable=False,
        verbose_name='Дата добавления одежды',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        editable=False,
        verbose_name='Дата изменения одежды',
        auto_now=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'