import csv, urllib
from urllib import parse

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    stations_list = []
    with open('data-398-2018-08-30.csv', 'r', encoding='cp1251') as datafile:
        reader = csv.DictReader(datafile)
        for station in reader:
            stations_list.append({
                'Name': station['Name'],
                'Street': station['Street'],
                'District': station['District']})

    stations_url = reverse(bus_stations) + '?'
    paginator = Paginator(stations_list, 10)
    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if stations.has_previous():
        prev_page = stations.previous_page_number()
    if stations.has_next():
        next_page = stations.next_page_number()

    return render(request, 'index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': stations_url + urllib.parse.urlencode({'page': prev_page}),
        'next_page_url': stations_url + urllib.parse.urlencode({'page': next_page}),
    })

