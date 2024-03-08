"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.urls import re_path, include
from app.forms import BootstrapAuthenticationForm
from app.views import home, contact, about
from django.contrib.auth import views as auth_views  # Import the auth views
from django.contrib.auth.views import LogoutView
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    re_path(r'^$', home, name='home'),
    re_path(r'^contact$', contact, name='contact'),
    re_path(r'^about', about, name='about'),
    #re_path(r'^login/$',
        #'django.contrib.auth.views.login',
        #{
            #'template_name': 'app/login.html',
            #'authentication_form': BootstrapAuthenticationForm,
           # 'extra_context':
            #{
                #'title':'Log in',
                #'year':datetime.now().year,
           # }
       # },
        #name='login'),
# Your URL pattern definition
    re_path(
        r'^login/$',
        auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=BootstrapAuthenticationForm, extra_context={'title': 'Log in', 'year': datetime.now().year}),
        name='login'
    ),
    #re_path(r'^logout$',
        #'django.contrib.auth.views.logout',
        #{
            #'next_page': '/',
        #},
       # name='logout'),
    # Your URL pattern definition
    re_path(
        r'^logout/$',
        LogoutView.as_view(next_page='/'),  # Using LogoutView directly as a callable
        name='logout'
    ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
