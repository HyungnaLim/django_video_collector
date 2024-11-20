from django.shortcuts import render

def home(request):
    app_name = 'Cute Animal Video Collection'
    return render(request, 'video_collector/home.html', {'app_name': app_name})
