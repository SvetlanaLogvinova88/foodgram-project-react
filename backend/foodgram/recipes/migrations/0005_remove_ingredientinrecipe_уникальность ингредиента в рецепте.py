# Generated by Django 3.2.11 on 2022-03-07 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20220307_0922'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='ingredientinrecipe',
            name='уникальность ингредиента в рецепте',
        ),
    ]
