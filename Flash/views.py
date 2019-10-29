from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@ login_required
def index_views(request):
    user = request.user
    return render(request, "Flash/index.html", {"user": user})


