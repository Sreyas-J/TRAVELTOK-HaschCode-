# Generated by Django 4.1.7 on 2023-03-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_age_user_gender_user_location_user_preference'),
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DEST', models.CharField(max_length=200, null=True)),
                ('BEACHES', models.IntegerField(null=True)),
                ('HISTORICAL', models.IntegerField(null=True)),
                ('WILDLIFE', models.IntegerField(null=True)),
                ('HILLSTATIONS', models.IntegerField(null=True)),
                ('MODERN_INFRASTRUCTURE', models.IntegerField(null=True)),
                ('REC', models.IntegerField(null=True)),
            ],
        ),
    ]