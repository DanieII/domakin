# Generated by Django 5.1.4 on 2025-01-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0005_familyinvitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='wins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
