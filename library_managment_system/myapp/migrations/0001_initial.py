# Generated by Django 3.2.13 on 2022-06-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookrecords',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=30)),
                ('book_type', models.CharField(max_length=30)),
                ('author_name', models.CharField(max_length=30)),
                ('recent_transaction_date', models.CharField(max_length=30)),
            ],
        ),
    ]
