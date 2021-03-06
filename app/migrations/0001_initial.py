# Generated by Django 2.2.4 on 2019-09-23 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aspian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('matricule', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cadidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Seceretary General', 'Seceretary General'), ('Assistant Secretary General', 'Assistant Secretary General'), ('Finacial Secretary', 'Finacial Secretary'), ('Treasurer', 'Treasurer'), ('Webmaster', 'Webmaster'), ('Public Relations Officer', 'Public Relations Officer'), ('Assistant Webmaster', 'Assistant Webmaster'), ('Project Coordinator', 'Project Coordinator'), ('Assistant Project Coordinator', 'Assistant Project Coordinator')], max_length=200)),
                ('aspian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Aspian')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Election')),
            ],
        ),
    ]
