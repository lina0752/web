from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    priority_choices = [
        ('high', 'Высокий'),
        ('medium', 'Средний'),
        ('low', 'Низкий'),
    ]
    priority = models.CharField(max_length=10, choices=priority_choices)
    status_choices = [
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
        ('postponed', 'Отложено'),
    ]
    status = models.CharField(max_length=15, choices=status_choices)

    def __str__(self):
        return self.title

