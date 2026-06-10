from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from . import views
from .views import add_employee
from .views import delete_employee
from .views import edit_employee
from .views import login_view
from .views import logout_view

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.employee_list),
    path('add/', add_employee),
    path('delete/<int:id>/', delete_employee),
    path('edit/<int:id>/', edit_employee),
    path('login/', login_view),
    path('logout/', logout_view),
]