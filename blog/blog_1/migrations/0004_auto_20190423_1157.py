# Generated by Django 2.1 on 2019-04-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_1', '0003_user_file_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_file',
            name='user_img',
            field=models.FileField(default='static/images/users/user.jpg', upload_to='./static/images/users/'),
        ),
    ]
