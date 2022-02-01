# Generated by Django 3.2.11 on 2022-01-29 18:08

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_subscribe_banning_subscriptions_to_yourself'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='subscribe',
            name='banning_subscriptions_to_yourself',
        ),
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.CheckConstraint(check=models.Q(('user_subscriber', django.db.models.expressions.F('user_author')), _negated=True), name='prevent self_follow'),
        ),
    ]
