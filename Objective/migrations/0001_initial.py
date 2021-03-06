# Generated by Django 2.1.7 on 2019-04-03 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('complete_date', models.DateField()),
                ('local_leader', models.CharField(max_length=10)),
                ('correlative_leader', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Done'), (3, 'Warning')])),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20)),
                ('objective', models.CharField(max_length=200)),
                ('key_result', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Objective.Objective'),
        ),
    ]
