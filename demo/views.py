import random
from typing import List

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from demo.models import Car, Person, Order


def hello_view(request):

    context = {
        'test': 5,
        'data': [1, 5, 8],
        'val': "Hi! I'm here"
    }

    return render(request, 'demo.html', context)

    # name = request.GET.get("name")
    # age = int(request.GET.get("age", 20))
    # print(age)
    return HttpResponse(f'Hello, {name}')


def sum(request, a, b):
    result = a + b
    return HttpResponse(f'Sum = {result}')


CONTENT = [str(i) for i in range(10000)]


def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)


def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']),
        model=random.choice(['M1', 'M2', 'M3', 'M4', 'M5', 'M6']),
        color=random.choice(['White', 'Black', 'Blue', 'Green', 'Orange'])
    )
    car.save()
    return HttpResponse(f'Все получилось! Новая машина: {car.brand}, {car.model}')


def list_car(request):
    car_objects = Car.objects.all()
    # car_objects = Car.objects.filter(brand='B1')
    # car_objects = Car.objects.filter(brand__contains='2')
    # car_objects = Car.objects.filter(brand__startswith='B')
    cars = [f'{c.id}: {c.brand}, {c.model}: {c.color}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        # Person(name='P', car=car).save()
        Person.objects.create(name='P', car=car)
    return HttpResponse('Всё получилось!!!')


def list_person(request):
    person_objects = Person.objects.all()
    people = []
    for p in person_objects:
        people.append(f'{p.name}: {p.car.brand}, {p.car.model}, {p.car.color}')
    return HttpResponse('<br>'.join(people))


def list_orders(request):
    # orders = Order.objects.all
    orders = Order.objects.filter(positions__product__price__gte=500)
    context = {'orders': orders}
    return render(request, 'orders.html', context)

