# Generated by Django 3.2.19 on 2023-06-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20230608_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../claire-2_rtqtiu.jpg', upload_to='images/'),
        ),
    ]