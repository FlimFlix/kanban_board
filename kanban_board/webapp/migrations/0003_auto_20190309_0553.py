# Generated by Django 2.1.7 on 2019-03-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190309_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Очередь', 'turn'), ('В работе', 'underway'), ('Сделано', 'done')], default='turn', max_length=20),
        ),
    ]