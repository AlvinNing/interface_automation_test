from django.shortcuts import render
from song02app import upload_file
from song02app import models, get_info

import datetime

def home(request):
    if request.method == 'POST':
        logics = upload_file.logic()
        logics.upload_file(request)
        path = get_info.get_info.get_file_path(request)
        case_list = logics.readExcel(path)
        logics.interfaceTest(case_list, path)
        res = models.result.objects.all()
        return render(request, "song02app/home.html", {"data": res})
    else:
        return render(request, "song02app/home.html")
    # logics = upload_file.logic()
    # logics.upload_file(request)
    # path = get_info.get_info.get_file_path(request)
    # case_list = logics.readExcel(path)
    # logics.interfaceTest(case_list, path)
    # res = models.result.objects.all()
    # return render(request, "song02app/home.html", {"data": res})