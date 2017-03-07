from django.http import HttpResponse
from .models import Project

def index(request):
    all_projects = Project.objects.all()
    html = ''
    for oneProject in all_projects:
        url = '/dashboard/' + str(Project.id) + '/'
        html += '<a href="' + url + '">' + Project.ProjName + '</a><br>'
    return HttpResponse(html)

def userDashboard(request, userid):
    return HttpResponse("<h2>Projects of user: " + str(userid) + "</h2>")
