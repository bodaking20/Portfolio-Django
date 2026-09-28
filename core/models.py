from django.db import models

# 1. نموذج السكريبتات
class Script(models.Model):
    title = models.CharField(max_length=200, verbose_name="اسم الاسكربت")
    image = models.ImageField(upload_to='scripts/', verbose_name="صورة الاسكربت")
    description = models.TextField(verbose_name="تفاصيل الاسكربت")
    price = models.CharField(max_length=100, verbose_name="أسعار الاشتراك")

    def __str__(self):
        return self.title

# 2. نموذج المواقع (أعمالك السابقة)
class Website(models.Model):
    title = models.CharField(max_length=200, verbose_name="اسم الموقع")
    image = models.ImageField(upload_to='websites/', verbose_name="صورة الموقع")
    description = models.TextField(verbose_name="تفاصيل الموقع")
    preview_link = models.URLField(verbose_name="رابط معاينة الموقع", blank=True, null=True)

    def __str__(self):
        return self.title

# 3. نموذج طلبات السكريبتات
class ScriptOrder(models.Model):
    STATUS_CHOICES = (
        ('جديد', 'طلب جديد'),
        ('جاري التواصل', 'جاري التواصل'),
        ('تم التسليم', 'تم التسليم'),
    )
    script = models.ForeignKey(Script, on_delete=models.CASCADE, verbose_name="الاسكربت المطلوب")
    contact_info = models.CharField(max_length=255, verbose_name="رقم الموبايل أو لينك فيسبوك")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='جديد', verbose_name="حالة الطلب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    def __str__(self):
        return f"طلب {self.script.title} - {self.contact_info}"

# 4. نموذج طلبات المواقع (الويب سايت)
class WebsiteOrder(models.Model):
    TYPE_CHOICES = (
        ('ويب سايت كامل', 'ويب سايت كامل'),
        ('لاندنج بيدج', 'لاندنج بيدج'),
    )
    STATUS_CHOICES = (
        ('جديد', 'طلب جديد'),
        ('جاري التواصل', 'جاري التواصل'),
        ('تم التسليم', 'تم التسليم'),
    )
    website_type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="نوع الموقع")
    requested_pages = models.TextField(verbose_name="الصفحات المطلوبة (لو ويب سايت كامل)", blank=True, null=True)
    contact_info = models.CharField(max_length=255, verbose_name="رقم الموبايل أو لينك فيسبوك")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='جديد', verbose_name="حالة الطلب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    def __str__(self):
        return f"طلب {self.website_type} - {self.contact_info}"

