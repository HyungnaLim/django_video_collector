from django.test import TestCase
from django.urls import reverse
from .models import Video
import re

class TestHomePage(TestCase):

    def test_app_title_message_shown_on_home_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, 'Cute Animal Video Collection')

class TestAddVideos(TestCase):
    
    def test_add_video(self):
        valid_video = {
            'name': 'cats and domino',
            'url': 'https://www.youtube.com/watch?v=7Nn7NZI_LN4',
            'notes': 'cats watching domino'
        }
        url = reverse('add_video')
        response = self.client.post(url, data=valid_video, follow=True)

        self.assertTemplateUsed('video_collection/video_list.html')
        self.assertContains(response, 'cats and domino')
        self.assertContains(response, 'https://www.youtube.com/watch?v=7Nn7NZI_LN4')
        # note: how can I check for url with & symbol? html will encode & as &amp; so simple assertion wouldn't work
        self.assertContains(response, 'cats watching domino')
        
        video_count = Video.objects.count()
        self.assertEqual(1, video_count)

class TestVideoList(TestCase):
    pass

class TestVideoSearch(TestCase):
    pass

class TestVideoModel(TestCase):
    pass