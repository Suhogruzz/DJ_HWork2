from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    content = []
    with open(BUS_STATION_CSV, encoding='utf-8', newline='') as stations:
        reader = csv.DictReader(stations, delimiter=",")
        for row in reader:
            add_content = ({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
            content.append(add_content)
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    page_content = paginator.page(page_number)
    context = {
         'bus_stations': page_content,
         'page': page,
    }
    return render(request, 'stations/index.html', context)

