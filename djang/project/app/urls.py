from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('packages',views.packages,name='packages'),
    path('test',views.test,name='test'),
    path('gallery',views.gallery,name='gallery'),
    path('department',views.department,name='department'),
    path('contact',views.contact,name='contact'),
    path('branch',views.branch,name='branch'),
    path('appointment',views.appointment,name='appointment'),
    path('blog',views.blog,name='blog'),
    path('subblog',views.subblog,name='subblog'),
    path('subpackage',views.subpackage,name='subpackage'),


]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)