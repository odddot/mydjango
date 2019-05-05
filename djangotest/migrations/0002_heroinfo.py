# Generated by Django 2.2.1 on 2019-05-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangotest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=128)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangotest.BookInfo')),
            ],
        ),
    ]