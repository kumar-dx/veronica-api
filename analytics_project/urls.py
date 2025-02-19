"""
URL configuration for analytics_project project.

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
from django.contrib import admin
from django.urls import path
from analytics_app.views import track_visitors, list_records, home, store_unique_visitors

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/analytics/visitors/', track_visitors, name='track-visitors'),
    path('api/v1/analytics/records/', list_records, name='list-records'),
    path('api/v1/analytics/stores/metrics/', store_unique_visitors, name='store-metrics'),
]
