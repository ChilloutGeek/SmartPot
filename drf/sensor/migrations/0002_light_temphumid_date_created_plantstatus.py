# Generated by Django 4.2 on 2023-04-29 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='temphumid',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='PlantStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('lux', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.light')),
                ('surrounding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.temphumid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
