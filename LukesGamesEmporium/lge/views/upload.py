from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def uploadPage(request):
    return render(request, 'upload.html')