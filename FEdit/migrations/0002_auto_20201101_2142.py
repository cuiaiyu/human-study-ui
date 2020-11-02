# Generated by Django 3.1.2 on 2020-11-01 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FEdit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('question_ref_image', models.ImageField(upload_to='')),
                ('question_query_image', models.ImageField(upload_to='')),
                ('question_type', models.CharField(max_length=200)),
                ('choices', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FEdit.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]