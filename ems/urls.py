from django.contrib import admin
from django.urls import path, include
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🌐 HOME PAGE (must be first)
    path('', views.dashboard),

    # 🌐 WEB APP ROUTES
    path('', include('employees.urls')),

    # 🔌 API ROUTES
    path('api/', include('employees.api_urls')),
]