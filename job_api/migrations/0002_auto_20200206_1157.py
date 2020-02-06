# Generated by Django 2.2.5 on 2020-02-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='HR_email',
            new_name='hr_email',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_description',
            new_name='job_description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Title',
            new_name='salary',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Keywords',
        ),
        migrations.AddField(
            model_name='job',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='job_title', max_length=50),
        ),
    ]
