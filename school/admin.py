from django.contrib import admin
from .models import Result, Profile, VerificationToken # Import Profile and VerificationToken
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

# Inline for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Unregister the default User and Group models
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,) # Add Profile inline

    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_active', 'is_staff', 'date_joined', 'last_login',
        'get_age', 'get_gender', 'is_verified_by_email' # Custom fields
    )
    list_filter = (
        'is_active', 'is_staff', 'is_superuser', 'groups',
        'profile__gender' # Filter by gender from profile
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login', 'is_verified_by_email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Verification', {'fields': ('is_verified_by_email',)}), # Custom fieldset
    )

    # Custom methods for list_display
    def get_age(self, obj):
        return obj.profile.age if hasattr(obj, 'profile') else None
    get_age.short_description = 'Age'

    def get_gender(self, obj):
        return obj.profile.get_gender_display() if hasattr(obj, 'profile') else None
    get_gender.short_description = 'Gender'

    def is_verified_by_email(self, obj):
        return obj.is_active # Assuming is_active means verified by email
    is_verified_by_email.boolean = True
    is_verified_by_email.short_description = 'Email Verified'

@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Result) # Keep Result registration
admin.site.register(VerificationToken) # Register VerificationToken