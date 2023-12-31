from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=70)),
                ('genre', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('how_often', models.CharField(choices=[('N', 'Never'), ('S', 'Sometimes'), ('A', 'Always')], max_length=1)),
                ('priority', models.IntegerField()),
                ('category', models.CharField(choices=[('F', 'Fun'), ('W', 'Work'), ('H', 'Health')], max_length=1)),
            ],
        ),
    ]
