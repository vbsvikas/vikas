# Generated by Django 2.1.2 on 2018-11-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb_pdf',
            field=models.FileField(blank=True, default='default2.pdf', upload_to=''),
        ),
    ]
