# Generated by Django 4.0.4 on 2022-06-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(default='Central', max_length=255)),
                ('title', models.CharField(default='Tsavo', max_length=255)),
                ('image_url', models.CharField(default='//cdn.weatherapi.com/weather/64x64/day/116.png', max_length=255)),
                ('experience', models.CharField(default='i loved it', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nearby_town', models.CharField(default='nairobi', max_length=255)),
                ('weather_text', models.CharField(blank=True, default='warm', max_length=255)),
                ('degree_celcius', models.IntegerField(blank=True, default=20)),
                ('weather_url', models.URLField(blank=True, max_length=256)),
            ],
        ),
    ]
