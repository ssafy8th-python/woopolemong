from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0003_alter_portfolio_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='p_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
