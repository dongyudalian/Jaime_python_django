# Generated by Django 3.2.5 on 2021-08-05 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Edname', models.CharField(max_length=255)),
                ('Edinfo', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'special_edition',
            },
        ),
    ]
