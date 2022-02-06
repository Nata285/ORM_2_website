from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Topic, Article_Topic

class Article_TopicInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

class Article_TopicInline(admin.TabularInline):
    model = Article_Topic
    formset = Article_TopicInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','text','published_at']
    inlines = [Article_TopicInline ]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name_topic']
