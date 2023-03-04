"""intro URL Configuration

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
from django.urls import path

from demo.views import hello_view, sum, pagi, create_car, list_car, create_person, list_person, list_orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('sum/<int:a>/<int:b>/', sum),
    path('pagi/', pagi),
    path('new_car/', create_car),
    path('cars/', list_car),
    path('new_person/', create_person),
    path('people/', list_person),
    path('orders/', list_orders)

]
