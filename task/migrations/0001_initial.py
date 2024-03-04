# Generated by Django 5.0.3 on 2024-03-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('high', 'Высокий'), ('medium', 'Средний'), ('low', 'Низкий')], max_length=10)),
                ('status', models.CharField(choices=[('in_progress', 'В процессе'), ('completed', 'Завершено'), ('postponed', 'Отложено')], max_length=15)),
            ],
        ),
    ]