from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request, tvno = 0):
    tv_list = [
        {'name': '東森', 'tvcode':'RaIJ767Bj_M'},
        {'name': '民視', 'tvcode': 'XxJKnDLYZz4'},
        {'name': '華視', 'tvcode': 'TL8mmew3jb8'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())
def engtv(request, tvno = 0):
    tv_list = [
        {'name': 'SkyNews', 'tvcode': '9Auq9mYxFEE'},
        {'name': 'Euro News', 'tvcode': 'jgGOQF_14wI'},
        {'name': 'DW News', 'tvcode': 'NvqKZHpKs-g'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    return render(request, 'engtv.html', locals())
    