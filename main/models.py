from django.db import models

class Cards(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Название проекта')
    slug = models.SlugField(max_length = 200, verbose_name = 'URL', unique = True)
    image = models.ImageField(upload_to = 'card_images', verbose_name= 'Изображение карточки')
    
    class Meta:
        db_table = 'card'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def __str__(self):
        return self.name
    
class CardsBig(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Название проекта')
    image = models.ImageField(upload_to = 'card_big_images', verbose_name = 'Крупное изображение проекта')
    skills = models.CharField(max_length = 500, verbose_name = 'Скиллы')
    cards = models.ForeignKey(to = Cards, on_delete = models.CASCADE, verbose_name = 'Карточка')
    
    
    class Meta:
        db_table = 'card_big'
        verbose_name = 'Карточку'
        verbose_name_plural = 'Карточки'
     
    def __str__(self):
        return self.name