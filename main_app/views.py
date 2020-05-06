"""Importing models """
from main_app.models import ErrorReport
from main_app.models import Topic, Subtopic, MultipleChoice

"""Import the forms"""
#from main_app.forms import QuestionCustomizeForm
#from main_app.forms import MultipleChoiceForm

"""Import the class-based-view login required
Import the function-based-view login required"""
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

"""Import the reverse and reverse_lazy functions"""
from django.urls import reverse, reverse_lazy

"""Importi the render, get_object_or_404, and redirect"""
from django.shortcuts import render, get_object_or_404, redirect

"""Import timezone function"""
from django.utils import timezone





"""PROJECT SPECIFIC"""
import random
from electronics.power_electronics_engine import *
from main_app.question_manager import topics_keys, subtopics_keys, questions_by_subtopic, questions_by_topic
import requests as requests_library
from email_management.email_sender import send_email
from email_management.email_sender_2 import SendMessage
import yagmail

def landing(request):
    return render(request, 'main_app/landing.html')

def question_detail(request):
    #receive the topic type

    #pull a question scaffold from the database or alternative for now
    #pull a question from a hard coded database

    #generate the question dynamically
    question_instance = fewson_2_1()
    #push the question into the template
    context = {
        'question':question_instance.question,
        'answer':question_instance.answer,
        'solution':question_instance.latex_solution,
        'available':False,
    }

    return render(request, 'main_app/question_detail.html', context)

def question_customize(request):
    subtopic_found = False
    if request.method == "POST":
        for subtopic in subtopics_keys:
            if request.POST['subtopic'] == str(subtopic):
                print('Form submission debug')
                print(request.POST)
                print(request.POST['subtopic'])
                subtopic_found = subtopic


        if subtopic_found == False:
            #this code runs if the default combobx value was not changed
            #topics = topics_keys
            subtopics = subtopics_keys

            context = {
                #'topics':topics,
                'subtopics':subtopics,
            }
            return render(request, 'main_app/question_customize.html', context)

        #retrieve the proper set of questions
        question_pool = questions_by_subtopic[subtopic_found]
        question_instance = random.choice(question_pool)()

        #try if the question contains an image, and send it if there is

        #check if user is enrolled
        if request.user.is_authenticated:
            try:
                context = {
                    'available': True,
                    'question':question_instance.question,
                    'answer':question_instance.answer,
                    'solution':question_instance.latex_solution,
                    'subtopic_reroll':subtopic_found,
                    'image':question_instance.image,
                }
            except:
                context = {
                    'available': True,
                    'question':question_instance.question,
                    'answer':question_instance.answer,
                    'solution':question_instance.latex_solution,
                    'subtopic_reroll':subtopic_found,
                }
        else:
            #if the student is not enrolled
                try:
                    context = {
                        'available': True,
                        'question':question_instance.question,
                        'answer':question_instance.answer,
                        'solution':'\\text{Enrollment is required to view solution.}',
                        'subtopic_reroll':subtopic_found,
                        'image':question_instance.image,
                    }
                except:
                    context = {
                        'available': True,
                        'question':question_instance.question,
                        'answer':question_instance.answer,
                        'solution':'\\text{Enrollment is required to view solution.}',
                        'subtopic_reroll':subtopic_found,
                    }

        #return the questions to the template_name


        return render(request, 'main_app/question_detail.html', context)
    else:


        #topics = topics_keys
        subtopics = subtopics_keys

        context = {
            'subtopics':subtopics,
        }
        return render(request, 'main_app/question_customize.html', context)

def question_customize_reroll(request):
    if request.method == "POST":
        for subtopic in subtopics_keys:
            if request.POST['reroll'] == str(subtopic):
                print('Form submission debug')
                print(request.POST)
                print(request.POST['reroll'])
                subtopic_found = subtopic

        #retrieve the proper set of questions
        question_pool = questions_by_subtopic[subtopic_found]
        question_instance = random.choice(question_pool)()

        #try if the question contains an image, and send it if there is

        #check if user is enrolled
        if request.user.is_authenticated:
            try:
                context = {
                    'available': True,
                    'question':question_instance.question,
                    'answer':question_instance.answer,
                    'solution':question_instance.latex_solution,
                    'subtopic_reroll':subtopic_found,
                    'image':question_instance.image,
                }
            except:
                context = {
                    'available': True,
                    'question':question_instance.question,
                    'answer':question_instance.answer,
                    'solution':question_instance.latex_solution,
                    'subtopic_reroll':subtopic_found,
                }
        else:
            #if the student is not enrolled
                try:
                    context = {
                        'available': True,
                        'question':question_instance.question,
                        'answer':question_instance.answer,
                        'solution':'\\text{Enrollment is required to view solution.}',
                        'subtopic_reroll':subtopic_found,
                        'image':question_instance.image,
                    }
                except:
                    context = {
                        'available': True,
                        'question':question_instance.question,
                        'answer':question_instance.answer,
                        'solution':'\\text{Enrollment is required to view solution.}',
                        'subtopic_reroll':subtopic_found,
                    }

        #return the questions to the template_name


        return render(request, 'main_app/question_detail.html', context)
    else:


        #topics = topics_keys
        subtopics = subtopics_keys

        context = {
            #'topics':topics,
            'subtopics':subtopics,
        }
        return render(request, 'main_app/question_customize.html', context)

def report_error(request):
    if request.method =="POST":
        email = request.POST['email']
        description = request.POST['description']
        image = request.POST['image']


        recaptcha = request.POST['g-recaptcha-response']
        recaptcha_data = {
            'secret': '6Lc1CO4UAAAAACs9XqPf35SGvdtP-0QmDM0n0K6V',
            'response': recaptcha,
        }

        google_captcha_response = requests_library.post('https://www.google.com/recaptcha/api/siteverify', recaptcha_data)
        if 'true' in google_captcha_response.text:
            #create and save the object
            error_report = ErrorReport.objects.create(email = email, description = description, image = image)
            error_report.save()
        return render(request, 'main_app/landing.html')
    else:
        return render(request, 'main_app/report_error.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'main_app/landing.html',{'message':'Login Successful.'})
        else:
            return render(request, 'main_app/landing.html',{'danger': 'Login Failed.'})
    else:
        return render(request, 'main_app/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'main_app/landing.html', {'message': 'Logout Successful.'})

def enroll(request):
    if request.method == "POST":
        recaptcha = request.POST['g-recaptcha-response']
        recaptcha_data = {
            'secret': '6Lc1CO4UAAAAACs9XqPf35SGvdtP-0QmDM0n0K6V',
            'response': recaptcha,
        }

        google_captcha_response = requests_library.post('https://www.google.com/recaptcha/api/siteverify', recaptcha_data)
        if 'true' in google_captcha_response.text:
            #create and save the object
            #send_email(f"""{request.POST['first_name']}, {request.POST['last_name']}, {request.POST['school_name']}, {request.POST['year_graduated']}, {request.POST['phone_number']}, {request.POST['facebook_username']}""")
            #SendMessage(sender, to, subject, msgHtml, msgPlain, '/path/to/file.pdf')
            #SendMessage('cortexsilicon@gmail.com', 'lesliecaminade@gmail.com', 'New Enrollment', , f"""{request.POST['first_name']}, {request.POST['last_name']}, {request.POST['school_name']}, {request.POST['year_graduated']}, {request.POST['phone_number']}, {request.POST['facebook_username']}""")
            yag = yagmail.SMTP('cortexsilicon','232653F8746C73C0DA302C73608B2511846BE1D2')
            contents = [f"""{request.POST['first_name']}, {request.POST['last_name']}, {request.POST['school_name']}, {request.POST['year_graduated']}, {request.POST['phone_number']}, {request.POST['facebook_username']}"""]
            yag.send('lesliecaminade@gmail.com', 'New Enrollment', contents)
            return render(request, 'main_app/landing.html', {'message': 'Enrollment has been requested, keep your lines open so we can contact you.'})
        else:
            return render(request, 'main_app/report_error.html')


    else:
        return render(request, 'main_app/enrollment.html')

def create_multiple_choice_question(request):
    if request.user.is_staff:
        if request.method == "POST":
            question = request.POST['question']
            correct = request.POST['correct']
            wrong_1 = request.POST['wrong_1']
            wrong_2 = request.POST['wrong_2']
            wrong_3 = request.POST['wrong_3']

            try:
                image = request.POST['image']
            except:
                image = None

            try:
                correct_image = request.POST['correct_image']
            except:
                correct_image = None

            try:
                wrong_image_1 = request.POST['wrong_image_1']
            except:
                wrong_image_1 = None

            try:
                wrong_image_2 = request.POST['wrong_image_2']
            except:
                wrong_image_2 = None

            try:
                wrong_image_3 = request.POST['wrong_image_3']
            except:
                wrong_image_3 = None

            try:
                solution = request.POST['solution']
            except:
                solution = None

            subtopic = request.POST['subtopic']

            multiple_choice_question = MultipleChoice.objects.create(
                author = request.user.username,
                question = question,
                correct = correct,
                wrong_1 = wrong_1,
                wrong_2 = wrong_2,
                wrong_3 = wrong_3,
                image = image,
                correct_image = correct_image,
                wrong_image_1 = wrong_image_1,
                wrong_image_2 = wrong_image_2,
                wrong_image_3 = wrong_image_3,
                solution = solution,
                subtopic = Subtopic.objects.filter(name=subtopic)[0]
            )

            try:
                multiple_choice_question.save()

                subtopics = []
                for object in Subtopic.objects.all():
                    subtopics.append(getattr(object, 'name'))

                context = {
                    'subtopics': subtopics,
                    'previous_subtopic' : subtopic,
                    'message': 'Question successfully saved.'
                }
            except:
                context = {
                    'subtopics': subtopics,
                    'previous_subtopic' : subtopic,
                    'danger': 'Question saving failed.'
                }

            return render(request, 'main_app/create_multiple_choice_question.html', context)
        else:
            subtopics = []

            for object in Subtopic.objects.all():
                subtopics.append(getattr(object, 'name'))

            context = {
                'subtopics': subtopics,
            }
            return render(request, 'main_app/create_multiple_choice_question.html', context)

    elif request.user.is_authenticated:
        return render(request, 'main_app/landing.html', {'danger': 'Staff Login Required'})
    else:
        return render(request, 'main_app/login.html', {'danger': 'Staff Login Required'})

def multiple_choice_question_customize(request):

    if request.method == "POST":
        subtopic = request.POST['subtopic']

        subtopics = []

        for object in Subtopic.objects.all():
            subtopics.append(getattr(object, 'name'))

        if subtopic == "Select a topic":
            context = {
                'subtopics': subtopics,
                'message': 'Please select a topic.',
            }

            return render(request, 'main_app/multiple_choice_customize.html', context)




        all_questions_on_that_topic = MultipleChoice.objects.filter(subtopic = subtopic)

        try:
            one_question = random.choice(all_questions_on_that_topic)
        except:
            subtopics = []

            for object in Subtopic.objects.all():
                subtopics.append(getattr(object, 'name'))

            context = {
                'subtopics': subtopics,
                'message': 'Please select a topic.',
            }

            return render(request, 'main_app/multiple_choice_customize.html', context)

        if one_question.correct_image:
            correct_image_html_code = f"""
<div class="container">
<img src= " {one_question.correct_image.url} " class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            correct_image_html_code = ''

        if one_question.wrong_image_1:
            wrong_image_1_html_code = f"""
<div class="container">
<img src= " {one_question.wrong_image_1.url} " class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            wrong_image_1_html_code = ""

        if one_question.wrong_image_1:
            wrong_image_2_html_code = f"""
<div class="container">
<img src= " {one_question.wrong_image_2.url} " class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            wrong_image_2_html_code = ""

        if one_question.wrong_image_1:
            wrong_image_3_html_code = f"""
<div class="container">
<img src= " {one_question.wrong_image_2.url} "" class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            wrong_image_3_html_code = ""

        choices_html_code = [
f"""<button type="button" class="btn btn-outline-primary correct_choice my-1 btn-block">{one_question.correct}</button>
<div class="container">
</div> {correct_image_html_code}""",
f"""<button type="button" class="btn btn-outline-primary wrong_choice my-1 btn-block">{one_question.wrong_1}</button>
<div class="container">
</div> {wrong_image_1_html_code}""",
f"""<button type="button" class="btn btn-outline-primary wrong_choice my-1 btn-block">{one_question.wrong_2}</button>
<div class="container">
</div> {wrong_image_2_html_code}""",
f"""<button type="button" class="btn btn-outline-primary wrong_choice my-1 btn-block">{one_question.wrong_3}</button>
<div class="container">
</div> {wrong_image_3_html_code}""",
        ]

        random.shuffle(choices_html_code)

        context = {
            'question': one_question.question,
            'image': one_question.image,
            'correct': one_question.correct,
            'wrong_1': one_question.wrong_1,
            'wrong_2': one_question.wrong_2,
            'wrong_3': one_question.wrong_3,
            'solution': one_question.solution,
            'subtopic': subtopic,
            'choices_html_code': choices_html_code,
            'available': True,
            'pk': one_question.pk,
        }

        return render(request, 'main_app/multiple_choice_detail.html', context)


    else:
        subtopics = []

        for object in Subtopic.objects.all():
            subtopics.append(getattr(object, 'name'))

        context = {
            'subtopics': subtopics,
            'message': 'Please select a topic.'
        }

        return render(request, 'main_app/multiple_choice_customize.html', context)

def multiple_choice_question_list(request):
    if request.method == "POST" and request.user.is_staff:

        subtopic = request.POST['subtopic']
        all_questions_on_that_topic = MultipleChoice.objects.filter(subtopic = subtopic)

        context = {
            'available': True,
            'all_questions': all_questions_on_that_topic,
            'subtopic': subtopic,
        }
        return render(request, 'main_app/multiple_choice_question_list.html', context)

    elif request.method == "GET" and request.user.is_staff:

        subtopics = []
        for object in Subtopic.objects.all():
            subtopics.append(getattr(object, 'name'))

        context = {
            'available': True,
            'subtopics': subtopics,
        }

        return render(request, 'main_app/multiple_choice_question_list_select.html', context)
    else:
        return render(request, 'main_app/landing.html', {'danger':'Admin account is required to allow question listing.'})

def multiple_choice_question_specific(request, pk):
    if request.user.is_staff:
        one_question = MultipleChoice.objects.get(pk = pk)

        if one_question.correct_image:
            correct_image_html_code = f"""
<div class="container">
<img src= " {one_question.correct_image.url} " class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            correct_image_html_code = ''

        if one_question.wrong_image_1:
            wrong_image_1_html_code = f"""
<div class="container">
<img src= " {one_question.wrong_image_1.url} " class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            wrong_image_1_html_code = ""

        if one_question.wrong_image_1:
            wrong_image_2_html_code = f"""
<div class="container">
<img src= " {one_question.wrong_image_2.url} " class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            wrong_image_2_html_code = ""

        if one_question.wrong_image_1:
            wrong_image_3_html_code = f"""
<div class="container">
<img src= " {one_question.wrong_image_2.url} "" class="col-lg-6 col-md-12 mx-auto rounded d-block" alt="Question image">
</div>
<hr class="my-4">"""
        else:
            wrong_image_3_html_code = ""

        choices_html_code = [
f"""<button type="button" class="btn btn-outline-primary correct_choice my-1 btn-block">{one_question.correct}</button>
<div class="container">
</div> {correct_image_html_code}""",
f"""<button type="button" class="btn btn-outline-primary wrong_choice my-1 btn-block">{one_question.wrong_1}</button>
<div class="container">
</div> {wrong_image_1_html_code}""",
f"""<button type="button" class="btn btn-outline-primary wrong_choice my-1 btn-block">{one_question.wrong_2}</button>
<div class="container">
</div> {wrong_image_2_html_code}""",
f"""<button type="button" class="btn btn-outline-primary wrong_choice my-1 btn-block">{one_question.wrong_3}</button>
<div class="container">
</div> {wrong_image_3_html_code}""",
        ]

        context = {
            'question': one_question.question,
            'image': one_question.image,
            'correct': one_question.correct,
            'wrong_1': one_question.wrong_1,
            'wrong_2': one_question.wrong_2,
            'wrong_3': one_question.wrong_3,
            'solution': one_question.solution,
            'subtopic': one_question.subtopic,
            'choices_html_code': choices_html_code,
            'available': True,
            'pk': one_question.pk,
        }
        return render(request, 'main_app/multiple_choice_detail.html', context)
    else:
        return render(request, 'main_app/landing.html', {'danger':'Admin account is required to allow targeted question lookup.'})

def multiple_choice_question_delete(request, pk):
    if request.user.is_staff:
        one_question = MultipleChoice.objects.get(pk = pk)
        one_question.delete()

        subtopics = []
        for object in Subtopic.objects.all():
            subtopics.append(getattr(object, 'name'))
        context = {
            'message': 'Question successfully deleted.',
            'subtopics': subtopics,
        }

        return render(request, 'main_app/multiple_choice_question_list_select.html', context)
    else:
        subtopics = []
        for object in Subtopic.objects.all():
            subtopics.append(getattr(object, 'name'))
        context = {
            'danger': 'Admin account is required to delete questions.',
            'subtopics': subtopics,
        }
        return render(request, 'main_app/multiple_choice_question_list_select.html', context)

def change_password(request):
    if request.user.is_authenticated and request.method == "POST":

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            request.user.set_password(password)
            request.user.save()
            return render(request, 'main_app/landing.html', {'message':'Password change successful.'})
        else:
            return render(request, 'main_app/change_password.html', {'danger': 'Passwords did not match, try again.'})
    elif request.method =="GET" and request.user.is_authenticated:
        return render(request, 'main_app/change_password.html')
    else:
        return render(request, 'main_app/landing.html', {'danger':'Login is first required.'})
