from django.shortcuts import render
# from .models import Project

# Create your views here.
def projects(request):
    projectsList = [{'id':1,
                     'title':'Online-Kino',
                     'description':'Ein Kino mit der umfassendsten Filmbibliothek.'},
                    {'id':2,
                     'title':'Plattform mit IT-Kursen',
                     'description':'Kurse zu Front-End, Back-End und mobiler Entwicklung.'},
                    {'id':3,
                     'title':'Recruiting-Portal',
                     'description':'Stellenangebote für hochkarätige Fachkräfte.'},
    ]
    return render(request, 'projects/projects.html', {'projects':projectsList})

def project(request):
    return render(request, 'projects/single-project.html')