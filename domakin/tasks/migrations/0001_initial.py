# Generated by Django 5.1.4 on 2024-12-29 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('families', '0005_familyinvitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='families.familymember')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='families.family')),
            ],
        ),
    ]
