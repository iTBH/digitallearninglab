# Generated by Django 2.2.4 on 2019-08-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_content_json_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='privacy',
            field=models.IntegerField(blank=True, choices=[(0, 'Unbekannt'), (1, 'Es werden keinerlei Daten erhoben'), (2, 'Personenbezogene Daten wie z.B. Logins werden geschützt auf dem Server abgelegt. Es greift die EU-Datenschutz-Grundverordnung.'), (3, 'Personenbezogene Daten werden erhoben. Dritte haben Zugriff auf diese Daten. Es greift die EU-Datenschutz-Grundverordnung.'), (4, 'Personenbezogene Daten werden erhoben. Es greift NICHT die EU-Datenschutz-Grundverordnung.')], null=True, verbose_name='Datenschutz'),
        ),
        migrations.AlterField(
            model_name='trend',
            name='category',
            field=models.IntegerField(blank=True, choices=[(0, 'Keine Angaben'), (1, 'Forschung'), (2, 'Portal'), (3, 'Praxisbeispiel'), (4, 'Veröffentlichung')], null=True, verbose_name='Kategorie'),
        ),
    ]
