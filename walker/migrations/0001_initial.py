# Generated by Django 4.2 on 2023-06-02 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantInfo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('상호명', models.CharField(max_length=50)),
                ('상권업종중분류명', models.CharField(max_length=50)),
                ('도로명주소', models.CharField(max_length=50)),
                ('경도', models.FloatField()),
                ('위도', models.FloatField()),
            ],
            options={
                'db_table': 'restaurant_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AllUsersOrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('상권업종중분류명', models.CharField(max_length=50)),
                ('상호명', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AllUsersOrderCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('닭오리요리', models.IntegerField(default=0)),
                ('별식퓨전요리', models.IntegerField(default=0)),
                ('부페', models.IntegerField(default=0)),
                ('분식', models.IntegerField(default=0)),
                ('양식', models.IntegerField(default=0)),
                ('일식수산물', models.IntegerField(default=0)),
                ('제과제빵떡케익', models.IntegerField(default=0)),
                ('중식', models.IntegerField(default=0)),
                ('커피점카페', models.IntegerField(default=0)),
                ('패스트푸드', models.IntegerField(default=0)),
                ('한식', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
    ]