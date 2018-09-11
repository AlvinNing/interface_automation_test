class get_info():

    def get_tester_name(request):
        if request.method == "POST":
            testers = request.POST.get("peoples", None)
        return testers

    def get_file_path(request):
        if request.method == "POST":
            File = request.FILES.get("files", None)
            file_path = './song02app/testFile/%s' % File.name
        return file_path

    def get_file_name(request):
        if request.method == "POST":
            filename = request.POST.get("files", None)
        return filename