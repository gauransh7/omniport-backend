# Generated by Django 2.2.3 on 2019-11-03 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('kernel', '0002_relationships'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='department',
        ),
        migrations.AddField(
            model_name='branch',
            name='entity_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'shell'), ('model', 'department')), models.Q(('app_label', 'shell'), ('model', 'centre')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='entity_object_id',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
    ]
