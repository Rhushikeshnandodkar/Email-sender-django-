from django.shortcuts import render
from .models import *
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
        print("label is .................", label)
        label_id = LableModel.objects.get(lable_name=label)
        sector_id = SectorModel.objects.get(sector_name=sector)
        group_id = GroupModel.objects.get(group_name=group)
        all_subs = SubscribersModel.objects.filter(label=label_id, group=group_id, sector=sector_id)
    return render(request, "filter-data.html", {'all_subs': all_subs})