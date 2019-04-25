# Generated by Django 2.1 on 2019-04-25 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_1', '0006_article_article_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_time', models.DateTimeField(auto_now_add=True)),
                ('collection_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_1.Article')),
                ('collection_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
