# Generated by Django 3.2.9 on 2021-11-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpCode', models.CharField(max_length=150)),
                ('EmpName', models.EmailField(blank=True, max_length=254)),
                ('Dept', models.CharField(max_length=50)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Experience', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
