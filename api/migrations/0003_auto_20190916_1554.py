# Generated by Django 2.2.5 on 2019-09-16 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20190915_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.BooleanField(default=False)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Quantity')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='buyer',
            field=models.ManyToManyField(to='api.Cart'),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Quantity'),
            preserve_default=False,
        ),
    ]