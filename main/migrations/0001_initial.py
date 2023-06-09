# Generated by Django 4.1 on 2023-03-20 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_alter_cetatean_options_cetatean_mail_cetatean_nume_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CNP', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=20)),
                ('numar', models.CharField(max_length=50)),
                ('cetatenie', models.CharField(max_length=50)),
                ('loc_nastere', models.CharField(max_length=100)),
                ('domiciliu', models.CharField(max_length=100)),
                ('autoritate_emitenta', models.CharField(max_length=100)),
                ('data_emitere', models.DateField()),
                ('data_expirare', models.DateField()),
                ('link_descarcare_document', models.CharField(max_length=100)),
                ('cetatean', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='authentication.cetatean')),
            ],
            options={
                'verbose_name': 'Buletin',
                'verbose_name_plural': 'Buletine',
            },
        ),
    ]
