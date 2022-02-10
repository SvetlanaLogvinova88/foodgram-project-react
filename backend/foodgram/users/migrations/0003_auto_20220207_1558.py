# Generated by Django 3.2.11 on 2022-02-07 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220206_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='user_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Автор, на которого подписывается подписчик'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='user_subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик'),
        ),
    ]
