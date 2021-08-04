from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'memo', 'created', 'update')
    search_fields = ('id', 'first_name','last_name')
    ordering = ('-update', '-created')
    list_filter = ('first_name', 'last_name', 'created', 'update')

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite

class BlogAdminSite(AdminSite):
    site_header = 'マイページ'
    site_title = 'マイページ'
    index_title = 'ホーム'
    site_url = None
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


mypage_site = BlogAdminSite(name="mypage")
mypage_site.register(models.Post)
