# Generated by Django 2.0.7 on 2019-01-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20190107_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitrequests',
            name='visit_type',
            field=models.CharField(choices=[('', 'Select Visit Type'), ('Personal', 'Personal'), ('Official/Business', 'Official/Business')], default='SELECT VISIT TYPE', max_length=50),
        ),
    ]