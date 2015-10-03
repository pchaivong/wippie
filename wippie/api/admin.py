from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from .models import Holiday
from .models import TSUser


class TSUserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmed Password", widget=forms.PasswordInput)

    class Meta:
        model = TSUser
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = super(TSUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class TSUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = TSUser
        fields = ('email', 'password', 'date_of_birth', 'is_active',
                  'is_admin', 'avatar', 'first_name', 'last_name', 'nickname', 'mobile')

    def clean_password(self):
        return self.initial["password"]

class TSUserAdmin(UserAdmin):

    form = TSUserChangeForm
    add_form = TSUserCreationForm

    list_display = ('email', 'date_of_birth', 'is_admin', 'first_name', 'last_name', 'nickname',
                    'mobile', 'avatar')

    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'nickname', 'date_of_birth', 'mobile', 'avatar')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('date_of_birth',)
    filter_horizontal = ()


# Register new User model
admin.site.register(TSUser, TSUserAdmin)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(Holiday)
