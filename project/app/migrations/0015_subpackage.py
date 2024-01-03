# Generated by Django 3.2.12 on 2024-01-03 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_subpackage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subpackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('test1', models.CharField(max_length=50)),
                ('test2', models.CharField(max_length=50)),
                ('test3', models.CharField(max_length=50)),
                ('test4', models.CharField(max_length=50)),
                ('test5', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='img')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.packages')),
            ],
        ),
    ]
