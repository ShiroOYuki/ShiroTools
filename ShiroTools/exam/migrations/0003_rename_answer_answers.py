# Generated by Django 4.2.4 on 2024-06-22 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_rename_questionanswer_answer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Answers',
        ),
    ]
