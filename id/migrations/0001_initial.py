# Generated by Django 3.0.3 on 2020-02-13 21:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='username')),
                ('cpf', models.CharField(blank=True, max_length=255, null=True, verbose_name='cpf')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('active', models.CharField(blank=True, max_length=255, null=True, verbose_name='active')),
                ('presentation_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='presentation name')),
                ('civil_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='civil name')),
                ('social_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='social name')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='last name')),
                ('campus', models.CharField(blank=True, max_length=255, null=True, verbose_name='campus')),
                ('campus_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='campus code')),
                ('department', models.CharField(blank=True, max_length=255, null=True, verbose_name='department')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('carrer', models.CharField(blank=True, max_length=255, null=True, verbose_name='carrer')),
                ('job', models.CharField(blank=True, max_length=255, null=True, verbose_name='job')),
                ('polo', models.CharField(blank=True, default='unknown', max_length=255, null=True, verbose_name='polo')),
                ('polo_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='polo code')),
                ('course', models.CharField(blank=True, max_length=255, null=True, verbose_name='course')),
                ('course_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='course code')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name='personal mail')),
                ('enterprise_email', models.CharField(blank=True, max_length=250, null=True, verbose_name='enterprise email')),
                ('academic_email', models.CharField(blank=True, max_length=250, null=True, verbose_name='academic email')),
                ('scholar_email', models.CharField(blank=True, max_length=250, null=True, verbose_name='scholar email')),
                ('eduroam', models.CharField(blank=True, max_length=250, null=True, verbose_name='eduroam')),
                ('first_access', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_access', models.DateTimeField(auto_now=True, verbose_name='last access')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='deleted at')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(blank=True, null=True, verbose_name='changed at')),
                ('password_set_at', models.DateTimeField(blank=True, null=True, verbose_name='password set at')),
                ('last_access_at', models.DateTimeField(blank=True, null=True, verbose_name='last ad access')),
                ('member_of', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000, verbose_name='member_of'), blank=True, null=True, size=None)),
                ('photo_url', models.CharField(blank=True, max_length=250, null=True, verbose_name='photo')),
                ('biografy', models.TextField(blank=True, null=True, verbose_name='biografy')),
                ('is_biografy_public', models.TextField(blank=True, null=True, verbose_name='show to all')),
                ('valid_photo', models.FileField(blank=True, null=True, upload_to='', verbose_name='valid photo')),
                ('pending_photo', models.FileField(blank=True, null=True, upload_to='', verbose_name='pending photo')),
                ('photo_solicitation_at', models.DateTimeField(blank=True, null=True, verbose_name='photo_solicitation_at')),
                ('photo_approved_at', models.DateTimeField(blank=True, null=True, verbose_name='photo_approved at')),
                ('photo_approved_by', models.CharField(blank=True, max_length=250, null=True, verbose_name='photo_approved by')),
                ('font_size', models.SmallIntegerField(blank=True, null=True, verbose_name='font size')),
                ('theme_skin', models.CharField(blank=True, choices=[('ava_ead_default', 'AVA-EaD padrão'), ('ava_ead_alternative', 'AVA-EaD alternativo'), ('suap_ead_default', 'SUAP-EaD padrão'), ('suap_ead_alternative', 'SUAP-EaD alternativo'), ('highcontrast', 'Alto contraste'), ('dark', 'Dark'), ('contrast', 'Contraste'), ('golden', 'Dourado'), ('purple', 'Púrpura'), ('navy', 'Marinha'), ('coral', 'Coral')], max_length=250, null=True, verbose_name='theme skin')),
                ('legends', models.NullBooleanField(verbose_name='legends')),
                ('sign_language', models.NullBooleanField(verbose_name='sign language')),
                ('screen_reader', models.NullBooleanField(verbose_name='screen reader')),
                ('is_special_needs_public', models.NullBooleanField(verbose_name='show to all')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('client_id', models.CharField(max_length=150, verbose_name='client_id')),
                ('secret', models.CharField(max_length=150, verbose_name='client_secret')),
                ('logo', models.FileField(blank=True, null=True, upload_to='', verbose_name='application_logo')),
                ('allowed_callback_urls', models.TextField(blank=True, null=True, verbose_name='allowed_callback_urls')),
                ('allowed_web_origins', models.TextField(blank=True, null=True, verbose_name='allowed_web_origins')),
                ('allowed_logout_urls', models.TextField(blank=True, null=True, verbose_name='allowed_logout_urls')),
                ('expiration', models.PositiveIntegerField(default=300, verbose_name='expiration_in_seconds')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='when_created')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'Aplicação',
                'verbose_name_plural': 'Aplicações',
            },
        ),
        migrations.CreateModel(
            name='SpecialNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('category', models.CharField(choices=[('Visão', 'Visão'), ('Audição', 'Audição'), ('Outras', 'Outras')], max_length=250, verbose_name='category')),
            ],
            options={
                'verbose_name': 'special need',
                'verbose_name_plural': 'special needs',
            },
        ),
        migrations.CreateModel(
            name='TransactionToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashcode', models.TextField(verbose_name='hash')),
                ('state', models.TextField(verbose_name='state')),
                ('redirect_uri', models.TextField(verbose_name='redirect_uri')),
                ('referer', models.TextField(blank=True, null=True, verbose_name='referer')),
                ('expire_at', models.DateTimeField(verbose_name='expireAt')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='id.Application', verbose_name='application')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Token de transação',
                'verbose_name_plural': 'Tokens de transações',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='special_needs',
            field=models.ManyToManyField(to='id.SpecialNeed', verbose_name='special needs'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
