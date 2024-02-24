# interview/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import InterviewQuestion
import openai

openai.api_key = ''

def generate_interview_question(role, topic, difficulty):
    prompt = f"Generate problems  {difficulty} 5 questions level interview question for a {role} on the topic of {topic}:"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=300
    )
    generated_question = response['choices'][0]['text']
    return generated_question


def ask_question(request):
    role_choices = InterviewQuestion.ROLE_CHOICES
    difficulty_choices = InterviewQuestion.DIFFICULTY_CHOICES
    topic_choices = InterviewQuestion.TOPIC_CHOICES  # Add this line

    if request.method == 'POST':
        role = request.POST.get('role', '')
        topic = request.POST.get('topic', '')
        difficulty = request.POST.get('difficulty', '')
        
        # Generated interview question using OpenAI
        generated_question = generate_interview_question(role, topic, difficulty)
        print(generated_question)
        # print(hints)
        s=""
        s=s+generated_question
        
        a=[]

        a=s.split('\n\n')
        
        a.pop(0)
        InterviewQuestion.objects.create(role=role, topic=topic, difficulty=difficulty, question=generated_question)
        questions = InterviewQuestion.objects.all()
        
        return render(request, 'interview/ask_question.html', {
            'role_choices': role_choices,
            'difficulty_choices': difficulty_choices,
            'generated_question':a,
            'topic_choices': topic_choices,  # Add this line
            'questions': questions,
        })

    return render(request, 'interview/ask_question.html', {'role_choices': role_choices, 'difficulty_choices': difficulty_choices, 'topic_choices': topic_choices})


def submit_answer(request):
    # Retrieve the generated question from the session
    generated_question = request.session.get('generated_question', None)

    if request.method == 'POST':
        form = InterviewQuestionForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer']
            InterviewQuestion.objects.create(question=generated_question, user_answer=user_answer, review_status=False)
            return redirect('submission_confirmation')
    else:
        form = InterviewQuestionForm()

    return render(request, 'interview/submit_answer.html', {
        'form': form,
        'generated_question': generated_question,
    })


