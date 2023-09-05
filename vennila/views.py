from django.shortcuts import render

# Create your views here.
def index(request, use_json=False):
    if request.method == "GET":
        return render(request,"vennila/index.html", {})
    raise NotImplementedError()
