# interview/urls.py
from django.urls import path
from .views import ask_question,submit_answer
urlpatterns = [
    path('ask/', ask_question, name='ask_question'),
    path('submit/', submit_answer, name='submit_answer'),
    # path('get_answer_overview/', get_answer_overview, name='get_answer_overview'),
 ]
