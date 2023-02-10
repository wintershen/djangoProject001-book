# Generated by Django 3.2.12 on 2022-02-10 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_press'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('press', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.press')),
            ],
        ),
    ]
