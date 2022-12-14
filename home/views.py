from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.forms import SearchForm,RegisterForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile, FAQ
from Policlinic.models import AppointmentForm,Randevu,Policlinic,Category,Images,Comment,CommentForm,Doctors

def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Policlinic.objects.all().order_by('?')[:4]
    category=Category.objects.all()
    policlinicdata=Policlinic.objects.all().order_by('?')[:3]
    doctordata=Doctors.objects.all().order_by('?')[:3]
    context={'page':'home','setting':setting, 'category':category, 'sliderdata':sliderdata, 'policlinicdata':policlinicdata,'doctordata':doctordata}
    return render(request,'index.html',context)

def hakkimizda(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting , 'page':'hakkimizda'}
    return render(request,'hakkimizda.html',context)

def iletisim(request):
    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarıyla iletildi. Teşekkürler!")
            return HttpResponseRedirect('iletisim')
    
    setting=Setting.objects.get(pk=1)
    form=ContactFormu()
    context={'setting':setting , 'form':form}
    return render(request,'iletisim.html',context)

def kategori(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    context={'setting':setting ,'category':category,'page':'kategori'}
    return render(request,'kategori.html',context)

def kategori_policlinics(request,id,slug):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    policlinics=Policlinic.objects.filter(category_id=id)
    context={'setting':setting ,'policlinics':policlinics, 'category':category, 'slug':slug}
    return render(request,'klinikler.html',context)

def policlinic_details(request,id,slug):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    images=Images.objects.filter(policlinic_id=id)
    policlinic=Policlinic.objects.filter(pk=id)
    comments=Comment.objects.filter(policlinic_id=id,status='True')
    context={'setting':setting ,'policlinic':policlinic, 'category':category, 'images':images,'comments':comments, 'slug':slug}
    return render(request,'policlinic_details.html',context)

@login_required(login_url='/login')
def addcomment(request,id):
    if request.method=='POST':
        url=request.META.get('HTTP_REFERER')
        form=CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user
            data=Comment()
            data.user_id=current_user.id
            data.policlinic_id=id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.rate=form.cleaned_data['rate']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Yorumunuz başarıyla gönderildi. Teşekkürler, Sağlıcakla Kalın!")
            return HttpResponseRedirect(url)
    messages.warning(request,"oOoPs! Yorumunuz gönderilemedi! Lütfen kontrol ediniz.")
    return HttpResponseRedirect(url)

def policlinic_search(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            setting=Setting.objects.get(pk=1)
            category=Category.objects.all()
            query=form.cleaned_data['query']
            policlinics=Policlinic.objects.filter(title__icontains=query)
            context={'policlinics':policlinics,'setting':setting,'category':category}
            return render(request,'policlinic_search.html',context)
    return HttpResponseRedirect('/')

def doctors(request):
    setting=Setting.objects.get(pk=1)
    doctors=Doctors.objects.all()
    context={'setting':setting ,'doctors':doctors}
    return render(request,'doktorlar.html',context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Hatası! Kullanıcı adı veya şifre yanlış.")
            return HttpResponseRedirect('/login/')
    return render(request,'login.html',context)

def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/')
    form=RegisterForm()
    setting=Setting.objects.get(pk=1)
    context={'form':form,'setting':setting}
    return render(request,'register.html',context)

def faq(request):
    setting=Setting.objects.get(pk=1)
    faq=FAQ.objects.all()
    context={'setting':setting ,'faq':faq}
    return render(request,'faq.html',context)

def randevu(request):
    setting=Setting.objects.get(pk=1)
    policlinic=Policlinic.objects.all()
    doctor=Doctors.objects.all()
    context={'setting':setting ,'doctor':doctor,'policlinic':policlinic}
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            current_user=request.user
            data=Randevu()
            data.user_id=current_user.id
            data.policlinic=form.cleaned_data['policlinic']
            data.doctor=form.cleaned_data['doctor']
            data.email=form.cleaned_data['email']
            data.phone=form.cleaned_data['phone']
            data.date=form.cleaned_data['date']
            data.time=form.cleaned_data['time']
            data.payment=form.cleaned_data['payment']
            data.insurance=form.cleaned_data['insurance']
            data.note=form.cleaned_data['note']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            return render(request,'randevu.html',context)
    return render(request,'randevu.html',context)

def profile(request):
    current_user=request.user
    user=UserProfile.objects.get(user_id=current_user.id)
    setting=Setting.objects.get(pk=1)
    context={'setting':setting ,'user':user}
    return render(request,'profile.html',context)
