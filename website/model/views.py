from django.http import HttpResponse
from .models import ComponentGroup
from .models import Component
from .models import ThreatCatalogue
from .models import Threat
from .models import CountermeasureCatalogue
from .models import Countermeasure
from .models import Responsible
from .models import ResponsibleInit
from .models import ResponsibleImpl
from .models import Checking
from .models import Role
from .models import LifecyclePhase


# Create your views here.

# connect to the database is here

def index(request):
    return HttpResponse("<h1>this will be default model")

def componentDetail(request):
    #connect to db and get Component data
    all_componentGroups = ComponentGroup.objects.all()
    html = ''
    for componentGroup in all_componentall_componentGroups:
        url = '/BSI/' + str(componentGroup.id) + '/'
        html += '<a href="#"' + url + '">' + componentGroup.name +'</a><br>'
    return HttpResponse(html)

def componentDetail(request):
    #connect to db and get Component data
    all_component = Component.objects.all()
    html = ''
    for component in all_component:
        url = '/BSI/' + str(component.id) + '/'
        html += '<a href="#"' + url + '">' +component.name +'</a><br>'
    return HttpResponse(html)

def threatCatalogueDetail(request):
    #connect to db and get ThreatCatalogue data
    all_threatCatalogues = ThreatCatalogue.objects.all()
    html = ''
    for threatCatalogue in all_threatCatalogues:
        url = '/BSI/' + str(threatCatalogue.id) + '/'
        html += '<a href="#"' + url + '">' +threatCatalogue.name +'</a><br>'
    return HttpResponse(html)

def threatDetail(request):
    #connect to db and get Threat data
    all_threats = Threat.objects.all()
    html = ''
    for threat in all_threats:
        url = '/BSI/' + str(threat.id) + '/'
        html += '<a href="#"' + url + '">' +threat.name +'</a><br>'
    return HttpResponse(html)

def CountermeasureCatalogueDetail(request):
    #connect to db and get CountermeasureCatalogue data
    all_countermeasureCatalogues = CountermeasureCatalogue.objects.all()
    html = ''
    for countermeasureCatalogue in all_countermeasureCatalogues:
        url = '/BSI/' + str(countermeasureCatalogue.id) + '/'
        html += '<a href="#"' + url + '">' + countermeasureCatalogue.name +'</a><br>'
    return HttpResponse(html)

def responsibleDetail(request):
    #connect to db and get Responsible data
    all_Responsiblities = Responsible.objects.all()
    html = ''
    for responsiblity in all_Responsiblities:
        url = '/BSI/' + str(responsiblity.role) + '/'
        html += '<a href="#"' + url + '">' + responsiblity.countermeasure +'</a><br>'
    return HttpResponse(html)

def checkingDetail(request):
    #connect to db and get Checking data
    all_checkings = Checking.objects.all()
    html = ''
    for cheking in all_checkings:
        url = '/BSI/' + str(cheking.description) + '/'
        html += '<a href="#"' + url + '">' + cheking.countermeasure +'</a><br>'
    return HttpResponse(html)

def role(request):
    #connect to db and get role data
    all_roles = Role.objects.all()
    html = ''
    for role in  all_roles:
        url = '/BSI/' + str(role.name) + '/'
        html += '<a href="#"' + url + '">' + role.description +'</a><br>'
    return HttpResponse(html)

def lifecyclePhase(request):
    #connect to db and get Responsible data
    all_lifeCyclePhases = lifecyclePhase.objects.all()
    html = ''
    for lifeCyclephase in  all_lifeCyclePhases:
        url = '/BSI/' + str(lifeCyclephase.id) + '/'
        html += '<a href="#"' + url + '">' + lifeCyclephase.name + '</a><br>'
    return HttpResponse(html)
