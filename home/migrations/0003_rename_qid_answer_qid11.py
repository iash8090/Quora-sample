# Generated by Django 4.2.3 on 2023-07-26 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='qid',
            new_name='qid11',
        ),
    ]
