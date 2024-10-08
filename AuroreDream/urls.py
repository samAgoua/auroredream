"""
URL configuration for AuroreDream project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import ProfileView
from django.conf.urls.static import static
from Event.urls import urlpatterns as event_urls
from ContentSharing.urls import urlpatterns as contentsharing_urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('admin/', admin.site.urls),
    path('base/', TemplateView.as_view(template_name='layout/base.html')),
    
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", ProfileView.as_view()),
    path("evenement/", include(event_urls)),
    path("contentsharing/", include(contentsharing_urls)),
    path("unicorn/", include("django_unicorn.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
