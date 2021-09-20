from django.contrib import admin
from users.models import NewUser


@admin.display(description='first name')
def upper_case_name(obj):
    return ("%s" % (obj.first_name[0].upper() + obj.first_name[1:].lower()))


@admin.register(NewUser)
class CustomUserAdmin(admin.ModelAdmin):

    model = NewUser

    empty_value_display = 'unknown'

    list_display = [
        'email',
        upper_case_name,
        'joined_date',
        'is_superuser',
        'is_active',
    ]

    list_filter = [
        'joined_date',
    ]

    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'phone_number')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('joined_date', 'is_active')
        })
    )

    