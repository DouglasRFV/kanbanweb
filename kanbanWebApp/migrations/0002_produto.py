# Generated by Django 3.1.2 on 2020-11-10 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanbanWebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanbanWebApp.setor')),
            ],
        ),
    ]