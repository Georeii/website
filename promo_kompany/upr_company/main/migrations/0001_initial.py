# Generated by Django 4.1.6 on 2023-03-31 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField()),
                ('street', models.TextField()),
                ('num_home', models.CharField(max_length=10)),
                ('entrase', models.FloatField()),
                ('company', models.ManyToManyField(to='main.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='people',
            field=models.ManyToManyField(to='main.people'),
        ),
        migrations.CreateModel(
            name='Bypass_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.FloatField()),
                ('open_close', models.FloatField()),
                ('reaction', models.FloatField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.home')),
            ],
        ),
    ]
