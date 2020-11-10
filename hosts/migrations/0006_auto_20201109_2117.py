# Generated by Django 3.1.3 on 2020-11-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0005_remove_vulnerability_affected_host'),
        ('hosts', '0005_auto_20201109_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='host',
            field=models.ManyToManyField(blank=True, related_name='host_list', to='vulnerabilities.Vulnerability'),
        ),
    ]