from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.common.utils.admin import GeneralAdminModel

from .models import (AddressModel, CityModel, CountryModel, StateModel,
                     UserModel, UserPersonalInformationModel)


@admin.register(UserModel)
class UserModelAdmin(UserAdmin, GeneralAdminModel):

    search_fields = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
    )

    list_display = (
        'get_full_name',
        'username',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        "user_type",
        'get_groups',
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "user_type"
    )

    list_display_links = (
        'get_full_name',
        'username',
        'email',
    )

    ordering = (
        'default_order',
        'created',
        'last_name',
        'first_name',
        'email',
        'username',
    )

    readonly_fields = (
        'created',
        'updated',
        'last_login'
    )

    fieldsets = (
        (
            _('User Information'), {
                'fields': (
                    'username',
                    'password',
                    'user_type',
                )
            }
        ),
        (
            _('Personal Information'), {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                )
            }
        ),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (
            _('Dates'), {
                'fields': (
                    'last_login',
                    'created',
                    'updated'
                ),
                'classes': (
                    'collapse',
                )
            }
        ),
        (
            _('Priority'), {
                'fields': (
                    'default_order',
                ),
                'classes': (
                    'collapse',
                )
            }
        )
    )

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_groups.short_description = _('Groups')

    get_full_name.short_description = _('Names')


@admin.register(CountryModel)
class CountryModelAdmin(GeneralAdminModel):
    search_fields = (
        'country_name',
        'country_code'
    )

    list_display = (
        'country_name',
        'country_code'
    )

    ordering = (
        'country_name',
    )

    list_filter = (
        'country_name',
    )

    readonly_fields = (
        'created',
        'updated',
    )


@admin.register(StateModel)
class StateModelAdmin(GeneralAdminModel):
    search_fields = (
        'state_name',
        'country__country_name'
    )

    list_display = (
        'state_name',
        'country'
    )

    ordering = (
        'state_name',
        'country'
    )

    list_filter = (
        'country',
    )

    readonly_fields = (
        'created',
        'updated',
    )


@admin.register(CityModel)
class CityModelAdmin(GeneralAdminModel):
    search_fields = (
        'city_name',
        'state__state_name',
        'state__country__country_name'
    )

    list_display = (
        'city_name',
        'state',
        'get_country'
    )

    ordering = (
        'city_name',
        'state__state_name'
    )

    list_filter = (
        'state',
        'state__country'
    )

    readonly_fields = (
        'created',
        'updated',
    )

    def get_country(self, obj):
        return obj.state.country.country_name

    get_country.short_description = 'Country'


@admin.register(AddressModel)
class AddressModelAdmin(GeneralAdminModel):
    search_fields = (
        'country__country_name',
        'state__state_name',
        'city__city_name',
        'address_line_1',
        'postal_code'
    )

    list_display = (
        'country',
        'state',
        'city',
        'address_line_1',
        'address_line_2',
        'postal_code'
    )

    ordering = (
        'country',
        'state',
        'city',
        'address_line_1'
    )

    list_filter = (
        'country',
        'is_active'
    )

    readonly_fields = (
        'created',
        'updated',
    )

    fieldsets = (
        (None, {
            'fields': (
                'country',
                'state',
                'city',
                'address_line_1',
                'address_line_2',
                'postal_code'
            )
        }),
    )


@admin.register(UserPersonalInformationModel)
class UserPersonalInformationModelAdmin(GeneralAdminModel):
    search_fields = (
        'id',
        'user__first_name',
        'user__last_name',
        'user__email',
        'passport_id',
        'citizenship_country',
    )

    list_display = (
        'user',
        'birth_date',
        'gender',
        'citizenship_country',
        'passport_id',
        'date_of_issue',
        'date_of_expiry'
    )

    ordering = (
        'user__first_name',
        'user__last_name',
        'birth_date'
    )

    list_filter = (
        'gender',
        'citizenship_country'
    )

    readonly_fields = (
        'user',
    )

    fieldsets = (
        (None, {
            'fields': (
                'user',
                'birth_date',
                'gender',
                'citizenship_country'
            )
        }),
        ('Passport Information', {
            'fields': (
                'passport_id',
                'date_of_issue',
                'issuing_authority',
                'date_of_expiry',
                'passport_image',
                'signature'
            )
        }),
        ('Contact Information', {
            'fields': (
                'addresses',
                'phone_number_code',
                'phone_number'
            )
        }),
    )

    filter_horizontal = (
        'addresses',
    )
