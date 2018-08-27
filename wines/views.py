# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from database import db
import csv
import time
# Create your views here.

def check_new_entry(request):
    if request.method == 'GET':
        count = db.test.count({})
        if (count == 0):
            return render(request, 'upload_new_winedata.html')
        else:
            context = {
                'count' : count
            }
            return render(request, 'query.html',context)
    elif request.method == 'POST':
        files = request.FILES['datafile']
        spamreader = csv.reader(files, delimiter=str(','))
        count = 0
        data = []
        head_list = []
        for row in spamreader:
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
            item = list(dbs.find({}))                                     # find all items in db and put hen in a dict item ( problem )
        else:
            item = list(dbs.find({ search_field : search_data }))            # search for paricular items in db (problem)
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
        return render(request, 'result.html', {'items': item })

def clear_database(request):
    db.test.remove({})
    return render(request,'upload_new_winedata.html')

def details(request,id):
    detail = db.test.find_one({ 'id' : id })
    return render(request,'details.html',{'detail': detail})

def return_items(items):
    return items



