# Generated by Django 4.1.7 on 2023-02-25 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_remove_event_rules_event_rules"),
    ]

    operations = [
        migrations.RemoveField(model_name="event", name="rules",),
        migrations.RemoveField(model_name="segment", name="rules",),
        migrations.AddField(
            model_name="rules",
            name="event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rules",
                to="events.event",
            ),
        ),
        migrations.AddField(
            model_name="segmentrule",
            name="segment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rules",
                to="events.segment",
            ),
        ),
    ]