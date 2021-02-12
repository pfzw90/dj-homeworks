from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('release_date', models.DateField()),
                ('image', models.URLField()),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
