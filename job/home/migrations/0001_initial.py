# Generated by Django 3.2.9 on 2021-11-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link_em',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
                'db_table': 'email',
            },
        ),
    ]
