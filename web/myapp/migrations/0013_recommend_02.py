# Generated by Django 4.2.1 on 2023-05-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rename_busdata_map_00_rename_map_1_map_01'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend_02',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('competing_hotels_count', models.IntegerField()),
                ('competing_hotels_min_distance', models.FloatField()),
                ('competing_hotels_max_distance', models.FloatField()),
                ('competing_hotels_avg_distance', models.FloatField()),
                ('bus_stops_count', models.IntegerField()),
                ('subway_stations_count', models.IntegerField()),
                ('nearest_bus_stop_distance', models.FloatField()),
                ('avg_bus_stop_distance', models.FloatField()),
                ('nearest_subway_station_distance', models.FloatField()),
                ('avg_subway_station_distance', models.FloatField()),
                ('monthly_average_boarding_traffic', models.FloatField()),
                ('monthly_average_alighting_traffic', models.FloatField()),
                ('monthly_total_traffic', models.FloatField()),
                ('tourist_spots_count', models.IntegerField()),
                ('shopping_malls_count', models.IntegerField()),
                ('nearest_tourist_spot_distance', models.FloatField()),
                ('avg_tourist_spot_distance', models.FloatField()),
                ('nearest_shopping_mall_distance', models.FloatField()),
                ('avg_shopping_mall_distance', models.FloatField()),
            ],
        ),
    ]