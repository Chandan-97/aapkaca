# Generated by Django 3.2.18 on 2023-05-07 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caservice', '0004_alter_caservice_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caservice.caservice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('service', 'user')},
                'index_together': {('service', 'user')},
            },
        ),
    ]
