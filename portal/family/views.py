from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
# Create your views here.

@login_required(login_url='/login')
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def logout(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    django_logout(request)
    return render(
        request,
        'app/logout.html',
        {
            'title':'Logged Out',
            'year':datetime.now().year,
        }
    )