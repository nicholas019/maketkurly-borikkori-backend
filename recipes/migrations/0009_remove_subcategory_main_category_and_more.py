# Generated by Django 4.1 on 2022-08-23 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipecomment_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='main_category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='main_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipes.maincategory'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=150)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.content')),
            ],
            options={
                'db_table': 'content_images',
            },
        ),
    ]
