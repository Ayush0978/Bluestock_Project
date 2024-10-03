from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # No dependencies for the initial migration
    ]

    operations = [
        migrations.CreateModel(
            name='IPO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='logos/')),
                ('company_name', models.CharField(max_length=255)),
                ('price_band', models.CharField(max_length=50)),
                ('open_date', models.DateField(default=django.utils.timezone.now)),
                ('close_date', models.DateField(default=django.utils.timezone.now)),
                ('issue_size', models.CharField(max_length=50)),
                ('issue_type', models.CharField(max_length=50)),
                ('listing_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=50)),
                ('ipo_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('listing_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('listing_gain', models.DecimalField(max_digits=5, decimal_places=2)),
                ('cmp', models.DecimalField(max_digits=10, decimal_places=2)),
                ('current_return', models.DecimalField(max_digits=5, decimal_places=2)),
                ('rhp_pdf', models.FileField(upload_to='documents/')),
                ('drhp_pdf', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
