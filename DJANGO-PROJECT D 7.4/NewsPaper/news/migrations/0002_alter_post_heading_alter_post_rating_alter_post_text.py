# Generated by Django 4.0.2 on 2022-03-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
