# Generated by Django 2.1.5 on 2019-12-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webber', '0003_post_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('who', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
