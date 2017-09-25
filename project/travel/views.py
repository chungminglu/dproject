from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from datetime import datetime
from travel.models import site , gthoteltime , gtsitactivity, gtsiteapparel,gtsiteother,gtsiterestaurant, gtsiteshop
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    Site = site.objects.get(ID='s7')
    HotelTime = gthoteltime.objects.all()
    Activity = gtsitactivity.objects.all()
    Apparel = gtsiteapparel.objects.all()
    OtherSite = gtsiteother.objects.all()
    Restaurant = gtsiterestaurant.objects.all()
    Shop = gtsiteshop.objects.all()
    return render(request, "testmap.html", locals())