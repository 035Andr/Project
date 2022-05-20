from django.db import models
from users.models import User


class Project(models.Model):  # проекты <==> пользователи, многие ко многим
    name = models.CharField(max_length=64, verbose_name='название проекта')
    repository_url = models.URLField(verbose_name='ссылка на репозиторий')
    users = models.ManyToManyField(User, verbose_name='пользователь')

    def __str__(self):
        users = ', '.join([str(num) for num in User.objects.filter(project__id=self.pk)])
        return f'{self.name} ({users})'

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class Todo(models.Model):  # заметка уникальна, => автор, проект. one to many

    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                verbose_name='проект')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, # CASCADE
                             verbose_name='пользователь-создатель')
    title = models.CharField(max_length=64, verbose_name='заголовок')
    text = models.TextField(verbose_name='заметка')
    is_active = models.BooleanField(verbose_name='активна', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):   # преобразуем модель в строку
        return f'{self.title} ({self.project.name}) - {self.user}'

    def delete(self):     # Переопределение метода delete
        self.is_active = False if self.is_active else True
        self.save()

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'

