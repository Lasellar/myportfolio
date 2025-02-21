# Generated by Django 5.1.6 on 2025-02-20 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('modelmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.modelmixin')),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='projects/')),
                ('url', models.URLField(blank=True)),
            ],
            bases=('main.modelmixin',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('modelmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.modelmixin')),
            ],
            bases=('main.modelmixin',),
        ),
    ]
