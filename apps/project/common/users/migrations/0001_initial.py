# Generated by Django 4.2.7 on 2024-12-06 06:24

import apps.project.common.users.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import encrypted_model_fields.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='names')),
                ('last_name', models.CharField(max_length=150, verbose_name='surnames')),
                ('email', encrypted_model_fields.fields.EncryptedEmailField(verbose_name='email address')),
                ('user_type', models.CharField(choices=[('H', 'Holder'), ('R', 'Representative'), ('B', 'Buyer'), ('I', 'Intermediary')], default='H', max_length=2, verbose_name='User')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'apps_users_user',
                'unique_together': {('username', 'email')},
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('address_line_1', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Address Line 1')),
                ('address_line_2', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True, verbose_name='Address Line 2 (Optional)')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal/Zip Code')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'apps_users_address',
            },
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('country_name', models.CharField(max_length=100, unique=True, verbose_name='Country Name')),
                ('country_code', models.CharField(max_length=5, unique=True, verbose_name='Country Code')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'apps_users_country',
            },
        ),
        migrations.CreateModel(
            name='UserPersonalInformationModel',
            fields=[
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('birth_date', encrypted_model_fields.fields.EncryptedDateField(default=apps.project.common.users.models.UserPersonalInformationModel.default_birth_date, validators=[apps.project.common.users.models.UserPersonalInformationModel.validate_birth_date], verbose_name='Birth Date')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Gender')),
                ('citizenship_country', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Citizenship')),
                ('passport_id', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Passport Identification')),
                ('date_of_issue', models.DateField(default=django.utils.timezone.now, verbose_name='Date of Issue')),
                ('issuing_authority', models.CharField(max_length=100, verbose_name='Issuing Authority')),
                ('date_of_expiry', models.DateField(default=apps.project.common.users.models.UserPersonalInformationModel.default_date_of_expiry, verbose_name='Date of Expiry')),
                ('phone_number_code', models.CharField(max_length=5, verbose_name='Phone Number Code')),
                ('phone_number', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Phone Number')),
                ('passport_image', models.ImageField(upload_to=apps.project.common.users.models.UserPersonalInformationModel.passport_directory_path, verbose_name='Passport Image')),
                ('signature', models.ImageField(upload_to=apps.project.common.users.models.UserPersonalInformationModel.signature_directory_path, verbose_name='Beneficiary signature')),
                ('addresses', models.ManyToManyField(blank=True, related_name='personal_information', to='users.addressmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_information', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Personal Information',
                'verbose_name_plural': 'User Personal Information',
                'db_table': 'apps_users_userpersonalpnformation',
            },
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('state_name', models.CharField(max_length=100, verbose_name='State Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_state_country', to='users.countrymodel')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
                'db_table': 'apps_users_state',
                'unique_together': {('state_name', 'country')},
            },
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('city_name', models.CharField(max_length=100, verbose_name='City Name')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_city_state', to='users.statemodel')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'apps_users_city',
                'unique_together': {('city_name', 'state')},
            },
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_address_city', to='users.citymodel'),
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_address_country', to='users.countrymodel'),
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_address_state', to='users.statemodel'),
        ),
    ]
