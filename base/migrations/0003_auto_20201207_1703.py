# Generated by Django 3.0.4 on 2020-12-07 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_staff_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Staff', 'verbose_name_plural': 'Staff users'},
        ),
        migrations.RemoveField(
            model_name='issue',
            name='prescription',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='receipt',
        ),
        migrations.AddField(
            model_name='visit',
            name='prescription',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='base.Prescription'),
        ),
        migrations.AddField(
            model_name='visit',
            name='receipt',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='receipt', to='base.Receipt'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
    ]