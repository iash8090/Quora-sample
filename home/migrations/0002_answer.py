# Generated by Django 4.2.3 on 2023-07-26 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=50)),
                ('ans', models.TextField()),
                ('like', models.IntegerField()),
                ('date', models.DateField()),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question')),
            ],
        ),
    ]