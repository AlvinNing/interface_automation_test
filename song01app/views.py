from django.shortcuts import render
from django.http import HttpResponse
from song01app.num_count import _out_log

# Create your views here.
def upload_file(request):
    if request.method == "POST":
        File = request.FILES.get("files", None)
        if File is None:
            return HttpResponse("请选择需要上传的monkey日志文件")
        else:
            with open("./song01app/monkey_log_file/%s" % File.name, 'wb+') as  f:
                for chunk in File.chunks():
                    f.write(chunk)
            return render(request, "song01app/upload_file.html", {"data": _out_log(request).all()})
    else:
        return render(request, "song01app/upload_file.html")

