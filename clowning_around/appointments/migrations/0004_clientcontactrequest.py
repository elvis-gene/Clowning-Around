# Generated by Django 3.1.7 on 2021-04-19 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_remove_rating_emoji_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=500)),
                ('client_name', models.CharField(max_length=50)),
            ],
        ),
    ]