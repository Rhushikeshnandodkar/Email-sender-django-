from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail , EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    label = LableModel.objects.all()
    sector = SectorModel.objects.all()
    group = GroupModel.objects.all()
    all_subs = SubscribersModel.objects.all()
    return render(request, "index.html", {'all_subs': all_subs, 'label': label, 'sector': sector, 'group': group})

def filter(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        sector = request.POST.get('sector')
        group = request.POST.get('group')
        try:
            label_id = LableModel.objects.get(lable_name=label)
            sector_id = SectorModel.objects.get(sector_name=sector)
            group_id = GroupModel.objects.get(group_name=group)
            all_subs = SubscribersModel.objects.filter(label=label_id, group=group_id, sector=sector_id)
        except:
            return redirect("/notfound")
    return render(request, "filter-data.html", {'all_subs': all_subs})

def notfound(request):
    return render(request, "notfound.html")

def campaign(request):
    campaigns = CampaignsModel.objects.all()
    return render(request, "campaign.html", {'campaigns': campaigns})

def campdetails(request, pk):
    camp_object = CampaignsModel.objects.get(id=pk)
    print(camp_object.template)
    label_id = LableModel.objects.get(lable_name=camp_object.label)
    sector_id = SectorModel.objects.get(sector_name=camp_object.sector)
    group_id = GroupModel.objects.get(group_name=camp_object.group)
    camp_users = SubscribersModel.objects.filter(label=label_id, group=group_id, sector=sector_id)
    return render(request, "campaigndetails.html", {'all_subs': camp_users, 'campaign': camp_object})

def thanks(request):
    return render(request, "thanks.html")
def sendemail(request, pk):
    if request.method == "POST":
        camp_object = CampaignsModel.objects.get(id=pk)
        label_id = LableModel.objects.get(lable_name=camp_object.label)
        sector_id = SectorModel.objects.get(sector_name=camp_object.sector)
        group_id = GroupModel.objects.get(group_name=camp_object.group)
        camp_users = SubscribersModel.objects.filter(label=label_id, group=group_id, sector=sector_id)      
        print(camp_object.template)
        email_list = []
        for i in camp_users:
            email_list.append(i.email)
        msg_html = render_to_string(f'../{camp_object.template}', {'camp_object': camp_object})
        print(msg_html)
        send_mail(
            "cad & cart",
            msg_html,
            "consulthub@gmail.com",
            email_list,
            html_message=msg_html,
            fail_silently=False
        )     
        return redirect("thanks")
    return render(request, "index.html")
