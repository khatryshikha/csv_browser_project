# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from database import db
import csv
import time
# Create your views here.

def check_new_entry(request):
    if request.method == 'GET':
        return render(request, 'upload_new_winedata.html')
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
        db.test.insert(data)
        return render(request, 'index.html')