# Generated by Django 2.1.8 on 2019-04-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Styling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garments',
            name='gender',
            field=models.CharField(choices=[('women', 'women'), ('men', 'men'), ('trans', 'trans')], max_length=255),
        ),
    ]