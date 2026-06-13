from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    DELIVERY_TYPES = [
        ('SH', 'Самовывоз'),
        ('CR', 'Курьерская доставка'),
        ('PP', 'Пункт выдачи заказов'),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Покупатель')
    comment = models.TextField(max_length=256, null=True, blank=True, default='Комментарии отсутствуют', verbose_name='Комментарий к заказу')
    delivery_address = models.CharField(max_length=256, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=DELIVERY_TYPES, default='SH', verbose_name='Тип доставки')
    created_at = models.DateTimeField(
        editable=False,
        verbose_name='Дата оформления заказа',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        editable=False,
        verbose_name='Дата изменения заказа',
        auto_now=True,
    )
    finish_at = models.DateTimeField(
        verbose_name='Дата завершения заказа',
        null=True,
        blank=True
    )

    clothes = models.ManyToManyField('catalogue.Clothe', through='PosOrder', verbose_name='Одежда')

    def __str__(self):
        return f'#{self.pk} - {self.user.first_name} {self.user.last_name} ({self.created_at})'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class PosOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT, verbose_name='Заказ')
    clothe = models.ForeignKey('catalogue.Clothe', on_delete=models.PROTECT, verbose_name='Одежда')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Количество в заказе')
    discount = models.PositiveSmallIntegerField(default=0, verbose_name='Скидка')

    class Meta:
        verbose_name='Позиция в заказе'
        verbose_name_plural='Позиции в заказе'