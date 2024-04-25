from django.utils import timezone
from django.shortcuts import redirect, render
from app.models import Blog, ContactFormLog, FrequentlyAskedQuestion, GeneralInfo, Service, Testimonial
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage



def home(request):
    generalInfo = GeneralInfo.objects.first()
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    question = FrequentlyAskedQuestion.objects.all()
    print(testimonial)
    context = {
        "services": services,
        "company_name" : getattr(generalInfo,"company_name", ""),
        "location" : getattr(generalInfo, "location", ""),
        "email" : getattr(generalInfo, "email",""),
        "phone": getattr(generalInfo, "phone", ""),
        "open_hours" : getattr(generalInfo,"open_hours", ""),
        "video_url" : getattr(generalInfo,"video_url", ""),
        "twitter_url" : getattr(generalInfo,"twitter_url", ""),
        "instagram_url" : getattr(generalInfo,"instagram_url", ""),
        "linkedin_url" : getattr(generalInfo,"linkedin_url", ""),
        "testimonials" : testimonial,
        "questions":question,
        "blogs":blogs,
    }
    return render(request, "index.html", context)


def blog(request):
    all_blogs = Blog.objects.all().order_by('-created_at')
    blogs_per_page = 3
    paginator = Paginator(all_blogs, blogs_per_page)
    page = request.GET.get("page")
        
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)# print(page)
    context = {
        'blogs':blogs
    }
    return render(request, "blog.html", context)


def blog_details(request, id):
    print(id)
    blog = get_object_or_404(Blog, pk=id)
    context = {
        "blog":blog
    }
    return render(request, "blog-details.html", context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }
        #message=f'{name} - {email} - {message}'
        is_success = False 
        is_error = False
        error_message =  ""
        
        html_content = render_to_string('email.html', context)
        try:
            send_mail(
            subject=subject,
            message=None,
            html_message=html_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            messages.error(request, "There is an error, cannot send message")
        else:
            is_success = True
            messages.success(request, "Your message has been sent successfully")
        
        ContactFormLog.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
            action_time = timezone.now(),
            is_success=is_success,
            is_error=is_error,
            error_message=error_message            
        )    
                
    return redirect('home')
