# learning/urls.py
from django.urls import path
from .views import home_view ,roadmaps,roadmap
from .views import get_response ,roadmapdsa,get_responsedsa
from .views import generate_and_display_videos,generate_links

urlpatterns = [
    path('py/', roadmap, name='roadmap'),
    path('dsa/', roadmapdsa, name='roadmapdsa'),
    path('get_response/<str:node_id>/', get_response, name='get_response'   ),
    path('get_responsedsa/<str:node_id>/', get_responsedsa, name='get_responsedsa'),
    path('', home_view, name='home_view'),
    path('roadmaps/', roadmaps , name='roadmaps'),
    path('generate_links/<str:query>/', generate_links, name='generate_links'),
    path('generate_videos/<str:node_id>/', generate_and_display_videos, name='generate_videos'),


]

