# Generated by Django 4.2.2 on 2023-07-01 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_service.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlawFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('', ''), ('Injection', 'Injection'), ('Broken Authentication', 'Broken Authentication'), ('Sensitive data exposure', 'Sensitive data exposure'), ('XML External Entities (XXE)', 'XML External Entities (XXE)'), ('Security misconfigurations', 'Security misconfigurations'), ('Cross Site Scripting (XSS)', 'Cross Site Scripting (XSS)'), ('Broken Access control', 'Broken Access control'), ('Insecure Deserialization', 'Insecure Deserialization'), ('Availability', 'Availability'), ('Integrity', 'Integrity'), ('Confidentiality', 'Confidentiality')], max_length=100)),
                ('severity', models.CharField(choices=[('', ''), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=10, validators=[user_service.models.validate_choice])),
                ('description', models.CharField(blank=True, max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
