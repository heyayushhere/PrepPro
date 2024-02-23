from django.shortcuts import render

# Create your views here.
# learning/views.py
from django.shortcuts import render
from django.http import JsonResponse
import openai


from .roadmappy import generate_dynamic_roadmap_data
from .roadmapdsa import generate_dynamic_roadmapdsa_data


def home_view(request):
    return render(request, 'learning/index.html')
def visual(request):
    return render(request, 'learning/visual.html')
def linkedlist(request):
    return render(request, 'learning/linkedlist.html')
def hashmap(request):
    return render(request, 'learning/hashmap.html')
def sorting(request):
    return render(request, 'learning/sorting.html')
def hashing(request):
    return render(request, 'learning/hashing.html')
def trees(request):
    return render(request, 'learning/trees.html')
def recursive(request):
    return render(request, 'learning/recursive.html')

def bubblesort(request):
    return render(request, 'learning/sorting/bubblesort.html') 

def selectionsort(request):
    return render(request, 'learning/sorting/selectionsort.html') 

def mergesort(request):
    return render(request, 'learning/sorting/mergesort.html') 

def insertionsort(request):
    return render(request, 'learning/sorting/insertionsort.html') 
# Set your OpenAI API key

def generate_dynamic_response(node_id):
    openai.api_key = ''
# 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
    prompt = f"Generate large content of around 300 words for node {node_id} in Python learning roadmap:"
    
    # Use the OpenAI GPT model to generate content
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=500
    )
    
    return response['choices'][0]['text']

def generate_dynamic_responsec(node_id):
    prompt = f"Generate content for node {node_id} in C learning roadmap:"

    # Use the OpenAI GPT model to generate content
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=300
    )

    return response['choices'][0]['text']

def generate_dynamic_responsejava(node_id):
    prompt = f"Generate content for node {node_id} in java learning roadmap:"

    # Use the OpenAI GPT model to generate content
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=300
    )

    return response['choices'][0]['text']

def generate_dynamic_responsedsa(node_id):
    prompt = f"Generate content for node {node_id} in dsa learning roadmap:"

    # Use the OpenAI GPT model to generate content
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=300
    )

    return response['choices'][0]['text']

def generate_dynamic_responsedp(node_id):
    prompt = f"Generate content for node {node_id} in dp learning roadmap:"

    # Use the OpenAI GPT model to generate content
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=300
    )

    return response['choices'][0]['text']

def generate_dynamic_responsecpp(node_id):
    prompt = f"Generate content for node {node_id} in cpp learning roadmap:"

    # Use the OpenAI GPT model to generate content
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=300
    )

    return response['choices'][0]['text']

def roadmap(request):
    roadmap_data = generate_dynamic_roadmap_data()
    length = len(roadmap_data['nodes'])
    print(length)
    return render(request, 'learning/roadmaps/roadmappy.html', {'roadmap_data': roadmap_data,'length':length})

def roadmapdsa(request):
    roadmap_data = generate_dynamic_roadmapdsa_data()
    return render(request, 'learning/roadmaps/roadmapdsa.html', {'roadmap_data': roadmap_data})
def roadmapdp(request):
    roadmap_data = generate_dynamic_roadmapdp_data()
    return render(request, 'learning/roadmaps/roadmapdp.html', {'roadmap_data': roadmap_data})
def roadmapcpp(request):
    roadmap_data = generate_dynamic_roadmapcpp_data()
    return render(request, 'learning/roadmaps/roadmapcpp.html', {'roadmap_data': roadmap_data})

def roadmaps(request):
    return render(request, 'learning/roadmaps.html')


def get_response(request, node_id):
    response_text = generate_dynamic_response(node_id)
    return JsonResponse({'response': response_text})

def get_responsedsa(request, node_id):
    response_text = generate_dynamic_responsedsa(node_id)
    return JsonResponse({'response': response_text})







# GENERATION OF 

from django.http import JsonResponse
from googleapiclient.discovery import build

# Set your API key and Custom Search Engine ID
API_KEY = ''
CSE_ID = ''

def get_search_results(query):
    service = build('customsearch', 'v1', developerKey=API_KEY)
    result = service.cse().list(q=query, cx=CSE_ID).execute()
    print(result.get('items', []))
    return result.get('items', [])

def generate_links(request, query):
    search_results = get_search_results(query)
    links = [result['link'] for result in search_results]
    links7_list = links[:7] 
    print(links7_list)
    return JsonResponse({'links': links7_list})


from django.http import JsonResponse
import requests

def generate_and_display_videos(request, node_id):

    api_key = 'AIzaSyCsoDWSJfR0YORcSiw8LtTtB97D0E_NZZ4'

        # Fetch data from the YouTube API
    api_url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={node_id}&key={api_key}'
    response = requests.get(api_url)
    data = response.json()

        # Extract video details
    videos = []
    for item in data.get('items', []):
        video_id = item.get('id', {}).get('videoId') or item.get('id', {}).get('playlistId')
        if video_id:
            video_title = item.get('snippet', {}).get('title')
            videos.append({'id': video_id, 'title': video_title})
    return JsonResponse({'videos': videos})

        
