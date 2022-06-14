# Generated by Django 4.0.3 on 2022-06-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0006_remove_knowledge_languages_knowledge_english_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='english',
            field=models.CharField(choices=[('Basico', 'Basico'), ('Intermediario', 'Intermediário'), ('Avançado', 'Avançado')], default='Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='spanish',
            field=models.CharField(choices=[('Basico', 'Basico'), ('Intermediario', 'Intermediário'), ('Avançado', 'Avançado')], default='Nenhum', max_length=50),
        ),
    ]