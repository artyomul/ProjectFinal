# Generated by Django 4.0 on 2021-12-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dictionary', '0003_remove_vocab_user_id_vocab_user_alter_vocab_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocab',
            name='user',
        ),
        migrations.AddField(
            model_name='vocab',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
