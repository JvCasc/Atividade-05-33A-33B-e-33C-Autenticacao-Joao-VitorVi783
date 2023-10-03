from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdojv', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Filmes',
        ),
    ]
