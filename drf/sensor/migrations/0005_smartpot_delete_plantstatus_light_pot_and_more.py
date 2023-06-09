# Generated by Django 4.2 on 2023-05-01 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sensor', '0004_remove_plantstatus_lux_remove_plantstatus_moisture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartPot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PlantStatus',
        ),
        migrations.AddField(
            model_name='light',
            name='pot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensor.smartpot'),
        ),
        migrations.AddField(
            model_name='soilmoisture',
            name='pot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensor.smartpot'),
        ),
        migrations.AddField(
            model_name='temphumid',
            name='pot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensor.smartpot'),
        ),
    ]
