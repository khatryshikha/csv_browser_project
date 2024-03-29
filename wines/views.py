# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import csv
import time
from tqdm import tqdm
from django.shortcuts import render
from django.conf import settings
from .database import dbs as db

# Create your views here.

def home(request):
    return render(request,'home_page.html')

def check_new_entry(request):
    if request.method == 'GET':
        count = db.test.find({}).count()
        if (count == 0):
            return render(request, 'upload_new_winedata.html')
        else:
            context = {
                'count' : count
            }
            return render(request, 'query.html',context)
    elif request.method == 'POST':
        files = request.FILES['datafile']
        with open(str(files),'rb') as fl:
            spamreader = csv.reader(files, delimiter=str(','))
            row_count = sum(1 for row in fl )
        count = 0
        data = []
        head_list = []
        iterator = tqdm(spamreader,total=row_count)
        for row in iterator:
            time.sleep(0.1)
            if ( count == 0 ):
                head_list = row
                count = count + 1
            else: 
                data.append(dict(zip(head_list, row)))
                count= count +1
        db.test.insert(data)
        context = { 
            'count':count-1
        }
        return render(request, 'query.html',context)

def filter_item(request):
    global item
    if request.method == 'POST' :
        search_field = request.POST.get('query')
        search_data = request.POST.get('Search')
        if len(str(search_data)) != 2 :
            search_data = search_data.title()
        else:
            search_data = search_data.upper()
        dbs =db.test
        if search_field == 'all' or search_data == '' :
            item = list(dbs.find({}))                                    
        else:
            item = list(dbs.find({ search_field : search_data }))
        if item == []:
            return render(request,'result_error.html')
        else:
            context = {
                'items':item,
                'field':search_field,
                'data' : search_data
            }
            return render(request, 'result.html',context)
    else :
        return render(request, 'result.html', {'items': item})

def clear_database(request):
    db.test.remove({})
    return render(request,'upload_new_winedata.html')

def details(request,id):
    detail = db.test.find_one({ 'id' : id })        # column name can be anything
    return render(request,'details.html',{'detail': detail})

