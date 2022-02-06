from django.db import models

# Create your models here.
from django.db import models

class Topic (models.Model):
    name_topic=models.CharField(max_length=256,verbose_name='раздел')
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return f"{self.name_topic}"

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tag = models.ManyToManyField(Topic, related_name='topic', through='Article_Topic')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Article_Topic(models.Model):
    tag = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='positions', verbose_name='раздел')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='positions')

    class Meta:
        verbose_name = 'Тематики статьи'
        verbose_name_plural = 'Тематики статьи'