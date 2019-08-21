from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from .forms import UserChangeForm, UserCreationForm
from .models import Troupe, TroupeLeader, Clown, Client

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name", "is_troupe_leader", "is_clown", "is_client", )}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_troupe_leader", "is_clown", "is_client", "is_superuser"]
    # search_fields = ["name"]

# @admin.register(User)
# class MyUserAdmin(AuthUserAdmin):
#   form = MyUserChangeForm
#   add_form = MyUserCreationForm
#   fieldsets = (("User Profile", {"fields": ("is_educator", "is_guardian", "is_learner",)}),) + AuthUserAdmin.fieldsets
#   list_display = ("username", "is_educator", "is_guardian", "is_learner", "is_superuser")


admin.site.register(Troupe)
admin.site.register(TroupeLeader)
admin.site.register(Clown)
admin.site.register(Client)
