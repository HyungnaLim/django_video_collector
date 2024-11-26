from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError

def home(request):
    app_name = 'Cute Animal Video Collection'
    return render(request, 'video_collector/home.html', {'app_name': app_name})

def add(request):
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                # messages.info(request, 'New video saved!')
                return redirect('video_list')
            except ValidationError:
                messages.warning(request, 'Invalid Youtube URL')
            except IntegrityError:  # for duplicate video
                messages.warning(request, 'You already added this video')

        # if video is not saved
        messages.warning(request, 'Please check the data entered.')
        return render(request, 'video_collection/add.html', {'new_video_form':new_video_form})

    new_video_form = VideoForm
    return render(request, 'video_collector/add.html', {'new_video_form':new_video_form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_collector/video_list.html', {'videos':videos})