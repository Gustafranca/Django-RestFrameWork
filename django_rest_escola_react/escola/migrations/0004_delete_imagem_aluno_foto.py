# Generated by Django 4.1.7 on 2023-05-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_imagem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
