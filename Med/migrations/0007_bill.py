# Generated by Django 4.1.7 on 2023-06-06 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Med', '0006_appointment_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appoints', to='Med.appointment')),
            ],
        ),
    ]
