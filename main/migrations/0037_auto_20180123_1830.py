# Generated by Django 2.0 on 2018-01-23 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0036_auto_20180113_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'middle_name', 'last_name'], 'permissions': (('can_view_customer', 'Can view customer'),)},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'permissions': (('can_view_reservation', 'Can view reservation'), ('can_view_reservation_detail', 'Can view reservation detail'))},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['room_no'], 'permissions': (('can_view_room', 'Can view room'),)},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['first_name', 'middle_name', 'last_name'], 'permissions': (('can_view_staff', 'Can view staff'), ('can_view_staff_detail', 'Can view staff detail'))},
        ),
        migrations.AddField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Customer'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='staff',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='main.Staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
