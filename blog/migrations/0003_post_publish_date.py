from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="publish_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
