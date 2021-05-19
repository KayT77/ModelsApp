# Generated by Django 3.2.3 on 2021-05-16 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('year_of_graduation', models.IntegerField()),
                ('Certificate_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsApp.certificate_type')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsApp.department')),
                ('Grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsApp.grade')),
                ('School', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsApp.school')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='Faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsApp.faculty'),
        ),
    ]