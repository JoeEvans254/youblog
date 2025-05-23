from django.db import migrations, models
import django.db.models.deletion

def populate_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    categories = [
        {'name': 'Technology', 'slug': 'technology'},
        {'name': 'Lifestyle', 'slug': 'lifestyle'},
        {'name': 'Travel', 'slug': 'travel'},
        {'name': 'Food', 'slug': 'food'},
        {'name': 'Health', 'slug': 'health'},
        {'name': 'Education', 'slug': 'education'},
    ]
    for cat in categories:
        Category.objects.get_or_create(name=cat['name'], slug=cat['slug'])

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]
    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.RunPython(populate_categories),
    ]