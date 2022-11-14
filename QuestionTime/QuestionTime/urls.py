"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from core.views import IndexTemplateView
from users.forms import CustomUserForm

#https://django-registration.readthedocs.io/en/3.3/
#(per la verifica a due passaggi)https://django-registration.readthedocs.io/en/3.3/custom-user.html
#https://django-registration.readthedocs.io/en/3.3/one-step-workflow.html
from django_registration.backends.one_step.views import RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),

    #url per la registrazione (tramite form personalizzato) via browser
    path("accounts/register/", 
          RegistrationView.as_view(
                            form_class=CustomUserForm,
                            success_url="/",
                                ), name="django_registration_register"),

    #altri url del package django_registration
    path("accounts/", 
          include("django_registration.backends.one_step.urls")),

    #login tramite interfaccia browser standard
    path("accounts/", 
          include("django.contrib.auth.urls")),

    path("api/",
          include("users.api.urls")),

    path("api/",
          include("questions.api.urls")),

    #login tramite browsble api (rest_framework)
    path("api-auth/",
          include("rest_framework.urls")),

    #login tramite rest(dj-rest-auth)
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),

    #registrazione tramite rest(dj-rest-auth)
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    re_path(r"^.*$",
            IndexTemplateView.as_view(),
            name="entry-point")
]
