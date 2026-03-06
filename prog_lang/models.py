from django.db import models

class ProgLang(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите язык програмирование')
    description = models.TextField(verbose_name='описание языка програмирование')
    image = models.ImageField(upload_to='proglang/', verbose_name='загрузите фото')
    created_date_lang = models.PositiveBigIntegerField(verbose_name='год создание яп',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'язык програмирование'
        verbose_name_plural = 'языки програмирование'
        


