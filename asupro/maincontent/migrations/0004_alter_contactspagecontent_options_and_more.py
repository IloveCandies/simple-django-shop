# Generated by Django 4.0 on 2021-12-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincontent', '0003_rename_requsitestpagecontent_requsitespagecontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactspagecontent',
            options={'verbose_name': 'контент', 'verbose_name_plural': 'Контент страницы  "Контакты"'},
        ),
        migrations.AlterModelOptions(
            name='mainpagecontent',
            options={'verbose_name': 'контент', 'verbose_name_plural': 'Контент страницы "Компания"'},
        ),
        migrations.AlterModelOptions(
            name='partnerspagecontent',
            options={'verbose_name': 'контент ', 'verbose_name_plural': 'Контент страницы "Партнеры"'},
        ),
        migrations.AlterModelOptions(
            name='requsitespagecontent',
            options={'verbose_name': 'контент', 'verbose_name_plural': 'Контент страницы "Реквизиты"'},
        ),
        migrations.AlterField(
            model_name='contactspagecontent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mainpagecontent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='partnerspagecontent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='requsitespagecontent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]