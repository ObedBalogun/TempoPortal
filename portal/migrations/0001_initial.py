# Generated by Django 2.0.7 on 2019-01-05 22:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=250)),
                ('staff_email', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='VisitRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='')),
                ('status', models.NullBooleanField()),
                ('token', models.CharField(max_length=30)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Staff')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Visitor')),
            ],
        ),
    ]