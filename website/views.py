from django.shortcuts import render
from django.http import HttpResponse
from .models import Member,AppRole,OrgRole,Center,Region
from .filters import MemberFilter
from .utils import *
from django.db.models import Q
from django.core.cache import cache
import logging
from .auth import *
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

#this new code for authenticate user using
#OOTB user authentication data model
def home(request):

    try:
        print("request.user.is_authenticated--- ", request.user.is_authenticated)
        if request.user.is_authenticated:
            return render(request,'home.html', {})
        if request.method == 'POST':
            if request.POST.keys() >= {'emailaddress'}:
                emailaddress = request.POST['emailaddress']
                context = generateAuthCode(request, emailaddress)
                return render(request, 'auth.html', context)
            elif request.POST.keys() >= { 'authcode', 'email' }:
                emailaddress = request.POST['email']
                context = authenticateUser(request, emailaddress)
                if context == True:
                    setupAppPermissions(request, emailaddress)
                    return render(request,'home.html',{})
                else:
                    return render(request, 'auth.html', context)
    except Exception as err:
        print(f'Unexpected {err} from home(), {type(err)}')
        raise
    return render(request,'auth.html',{})

#To import file - Admin Use
def importFile(request):
    return render(request, 'import-page.html',{})

#To export file - Admin Use
def exportFile(request):
    return render(request, 'export-page.html',{})

# #Show All Cards of Region Officers
# def show_regions(request):
#     return render(request, 'show-region.html',{})


#Get all regional officers
def getAllRegionalOfficers(request):
    allRegionalOfficers = Member.objects.filter(approle__name='Regional Officer')
    logging.debug('allRegionalOfficers:1 ' + str(allRegionalOfficers))
    filterMembers = MemberFilter(request.GET, queryset=allRegionalOfficers)
    allRegionalOfficers = filterMembers.qs
    logging.debug('allRegionalOfficers:2 ' + str(allRegionalOfficers))

    page_obj = Paginator(allRegionalOfficers, 12)
    page = request.GET.get('page')
    allRegionalOfficers = page_obj.get_page(page)

    return render(request,'regional-officers-page.html',{'allRegionalOfficers':allRegionalOfficers,'filterMembers':filterMembers})

#Get all national officers
def getAllNationalOfficers(request):
    allNationalOfficers = Member.objects.filter(approle__name='National Officer')
    logging.debug('allNationalOfficers: ' + str(allNationalOfficers))
    filterMembers = MemberFilter(request.GET, queryset=allNationalOfficers)
    allNationalOfficers = filterMembers.qs

    page_obj = Paginator(allNationalOfficers, 12)
    page = request.GET.get('page')
    allNationalOfficers = page_obj.get_page(page)

    return render(request, 'national-officers-page.html', {'allNationalOfficers': allNationalOfficers, 'filterMembers' : filterMembers})

#Get all center officers
def getAllCenterOfficers(request):
    allCenterOfficers = Member.objects.filter(approle__name='Center Officer')
    logging.debug('allCenterOfficers: ' + str(allCenterOfficers))
    filterMembers = MemberFilter(request.GET, queryset=allCenterOfficers)
    allCenterOfficers = filterMembers.qs

    page_obj = Paginator(allCenterOfficers, 12)
    page = request.GET.get('page')
    allCenterOfficers = page_obj.get_page(page)

    return render(request, 'center-officers-page.html', {'allCenterOfficers':  allCenterOfficers,'filterMembers' : filterMembers})

#Get regional officers for specific region
def getRegionOfficers(request, regionId):
    regionOfficers = Member.objects.filter(approle__name='Regional Officer', region_id=regionId)
    logging.debug('regionOfficers: ' + str(regionOfficers))
    return render(request, 'display-region.html', {'regionOfficers': regionOfficers})


#Get center officers for specific center
def getCenterOfficers(request, centerId):
    centerOfficers = Member.objects.filter(approle__name='Center Officer', center_id=centerId)
    logging.debug('centerOfficers: ' + str(centerOfficers))
    return render(request, 'display-center.html', {'centerOfficers': centerOfficers})

#Get all centers of a region
def getRegionalCenters(request, regionId):
    centersByRegionId = Center.objects.filter(region_id=regionId)
    logging.debug('centersByRegionId: ' + str(centersByRegionId))

# Search By Member-Names
def search_members(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            searched =  request.POST['searched']

            members = Member.objects.filter(
                Q(first_name__contains=searched)
                | Q(last_name__contains=searched)
                | Q(region__name__contains=searched)
                | Q(orgrole__name__contains=searched)
                | Q(approle__name__contains=searched)).distinct()
            # role_info = MemberInfo.objects.filter(Q(roleDesc__description__icontains =searched))
            # Asset.objects.filter( project__name__contains="Foo" )
            # members = MemberInfo.objects.filter(firstName__contains=searched)
            logging.debug('members: ' + str(members))
            return render(request, 'search-members.html', {'searched':searched, 'members': members})
        else:
            return render(request, 'search-members.html', {})
    else:
        return render(request,'auth.html',{})

def uploadFile(request):

    csv_file = None
    message = "All are up to date"
    importType = None
    if request.method == "POST":
        importType = request.POST.get('importType')
        try:
            csv_file = request.FILES['file']
        except Exception as ex:
            message = str(ex)
            return render(request, 'import-page.html', {"message" : "upload failed. check your input file."})
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            message = 'Please upload a CSV file'
            return render(request, 'import-page.html', {"message" : message})
        else:
            loadeddata = ""
            loadeddata = uploadCSVFile(csv_file, importType)
            #print(loadeddata, "loadeddata")
            if len(loadeddata) == 0:
                return render(request, 'import-page.html', {"message" : message})
            else:
                return render(request, 'import-page.html', {"loadeddata": loadeddata})
    else:
        return render(request, 'import-page.html',{})
