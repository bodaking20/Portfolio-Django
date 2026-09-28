from django.shortcuts import render, get_object_or_404, redirect
from .models import Script, Website, ScriptOrder, WebsiteOrder
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def scripts_list(request):
    scripts = Script.objects.all()
    return render(request, 'scripts_list.html', {'scripts': scripts})

def websites_list(request):
    websites = Website.objects.all()
    return render(request, 'websites_list.html', {'websites': websites})

def script_detail(request, id):
    script = get_object_or_404(Script, id=id)
    if request.method == 'POST':
        contact_info = request.POST.get('contact_info')
        ScriptOrder.objects.create(script=script, contact_info=contact_info)
        
        # إضافة رسالة التأكيد
        messages.success(request, 'تم استلام طلبك للاسكربت بنجاح! سنتواصل معك قريباً.')
        return redirect('home')
        
    return render(request, 'script_detail.html', {'script': script})

def website_detail(request, id):
    website = get_object_or_404(Website, id=id)
    if request.method == 'POST':
        website_type = request.POST.get('website_type')
        requested_pages = request.POST.get('requested_pages', '')
        contact_info = request.POST.get('contact_info')
        WebsiteOrder.objects.create(
            website_type=website_type, 
            requested_pages=requested_pages, 
            contact_info=contact_info
        )
        
        # إضافة رسالة التأكيد
        messages.success(request, 'تم استلام طلب الويب سايت بنجاح! سنتواصل معك قريباً.')
        return redirect('home')
        
    return render(request, 'website_detail.html', {'website': website})