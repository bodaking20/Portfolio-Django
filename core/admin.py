from django.contrib import admin
from .models import Script, Website, ScriptOrder, WebsiteOrder

# إعدادات ظهور جدول السكريبتات
@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

# إعدادات ظهور جدول المواقع
@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_link')

# إعدادات ظهور جدول طلبات السكريبتات
@admin.register(ScriptOrder)
class ScriptOrderAdmin(admin.ModelAdmin):
    list_display = ('script', 'contact_info', 'status', 'created_at')
    list_filter = ('script', 'status') # دي عشان تقدر تفلتر الطلبات على حسب الاسكربت زي ما طلبت
    search_fields = ('contact_info',)

# إعدادات ظهور جدول طلبات المواقع
@admin.register(WebsiteOrder)
class WebsiteOrderAdmin(admin.ModelAdmin):
    list_display = ('website_type', 'contact_info', 'status', 'created_at')
    list_filter = ('website_type', 'status')
    search_fields = ('contact_info',)

