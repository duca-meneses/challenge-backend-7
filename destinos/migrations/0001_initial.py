# Generated by Django 4.2.3 on 2023-07-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destino",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
                ("foto", models.ImageField(blank=True, upload_to="foto/destinos")),
                ("preco", models.FloatField(max_length=10)),
            ],
        ),
    ]
