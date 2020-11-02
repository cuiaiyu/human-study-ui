# Generated by Django 3.1.2 on 2020-11-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FEdit', '0004_remove_question_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_query_image',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='C', max_length=1),
        ),
        migrations.AddField(
            model_name='question',
            name='query_image_A',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='question',
            name='query_image_B',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1),
        ),
    ]