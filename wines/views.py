# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def check_new_entry(request):
    if request.method == 'GET':
        return render(request, 'upload_new_winedata.html')
    # elif request.method == 'POST':
    #     winery = request.POST.get('winery')
    #     country = request.POST.get('country')
    #     province = request.POST.get('province')
    #     region1 = request.POST.get('region1')
    #     region2 = request.POST.get('region2')
    #     variety = request.POST.get('variety')
    #     price = request.POST.get('price')
    #     points = request.POST.get('point')
    #     description = request.POST.get('description')
    #     designation = request.POST.get('designation')
    #     db.wines.insert({'winery' : winery, 'country' : country , 'province' : province, 'region1' : region1, 'region2' : region2, 'variety': variety, 'price' : price, 'point' : point , 'description' : description, 'designation' : designation})


