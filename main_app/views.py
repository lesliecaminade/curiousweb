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

#questionbank related imports
import random
from electronics.power_electronics_engine import *
from main_app.question_manager import topics_keys, subtopics_keys, questions_by_subtopic, questions_by_topic

#http related imports
import requests as requests_library

#email related imports
from email_management.email_sender import send_email
from email_management.email_sender_2 import SendMessage
import yagmail
"""function definitions"""

def list_this_model(model, attr, **kwargs):
    """this function returns a list of all the instance parameter of a model in the database
    model - the model the will be listed
    attr - the particular attribute to be listed"""

    output_list = []
    for object in model.objects.all():
        output_list.append(getattr(object, attr))
    return output_list


"""Views"""
def landing(request):
    #page the the user sees when going to the page for the first time.
    return render(request, 'main_app/landing.html')

"""I think this part of the code is not used anymore."""
# def question_detail(request):
#     question_instance = fewson_2_1()
#     #push the question into the template
#     context = {
#         'question':question_instance.question,
#         'answer':question_instance.answer,
#         'solution':question_instance.latex_solution,
#         'available':False,
#     }
#
#     return render(request, 'main_app/question_detail.html', context)

def question_customize(request):

    subtopic_found = False #this is a flag which sets if the subtopic selected was found or not

    if request.method == "POST":
        for subtopic in subtopics_keys:
            if request.POST['subtopic'] == str(subtopic):
                subtopic_found = subtopic

        if subtopic_found == False: #if the default combobx value was not changed
            subtopics = subtopics_keys

            context = {
                'subtopics':subtopics,
            }
            return render(request, 'main_app/question_customize.html', context) #the same page is returned again and the subtopics list is also returned along with it

        question_pool = questions_by_subtopic[subtopic_found] #retrieve all the questions from that particular subtopic
        question_instance = random.choice(question_pool)() #select one random question class and initialize it

        #check if user is enrolled
        if request.user.is_authenticated: #if the user is logged in (whether staff or student)
            try: #this try -except statement catches whether the question_instance contains an image or not
                context = {
                    'available': True, #this is a flag for if the question is available or not
                    'question':question_instance.question, #the question content
                    'answer':question_instance.answer, #the answer content
                    'solution':question_instance.latex_solution, #the solution content, formatted using latex
                    'subtopic_reroll':subtopic_found, #this is a hiddent input that contains the subtopic selection, and is used to select the same subtopic again when the user hits the next button
                    'image':question_instance.image, #the image object for the questions, some questions contain images,

                }
            except:
                context = {
                    'available': True,
                    'question':question_instance.question,
                    'answer':question_instance.answer,
                    'solution':question_instance.latex_solution,
                    'subtopic_reroll':subtopic_found,
                }
        else: #if the student is not enrolled
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

        return render(request, 'main_app/question_detail.html', context) #return the page that contains the randomly selected question from the engine
    else: #if the method is GET
        subtopics = subtopics_keys
        context = {
            'subtopics':subtopics,
        }
        return render(request, 'main_app/question_customize.html', context) #return the page with a dropdown with the list of all subtopics

"""I think the question_customize_reroll view is the exact same code as the question_customize view, so as of
writing, I am modifying the urls.py file to point the url mapping to the question_customize view instead of this
question_customize_reroll view."""

# def question_customize_reroll(request):
#     if request.method == "POST":
#         for subtopic in subtopics_keys:
#             if request.POST['reroll'] == str(subtopic):
#                 print('Form submission debug')
#                 print(request.POST)
#                 print(request.POST['reroll'])
#                 subtopic_found = subtopic
#
#         question_pool = questions_by_subtopic[subtopic_found]
#         question_instance = random.choice(question_pool)()
#         if request.user.is_authenticated:
#             try:
#                 context = {
#                     'available': True,
#                     'question':question_instance.question,
#                     'answer':question_instance.answer,
#                     'solution':question_instance.latex_solution,
#                     'subtopic_reroll':subtopic_found,
#                     'image':question_instance.image,
#                 }
#             except:
#                 context = {
#                     'available': True,
#                     'question':question_instance.question,
#                     'answer':question_instance.answer,
#                     'solution':question_instance.latex_solution,
#                     'subtopic_reroll':subtopic_found,
#                 }
#         else:
#                 try:
#                     context = {
#                         'available': True,
#                         'question':question_instance.question,
#                         'answer':question_instance.answer,
#                         'solution':'\\text{Enrollment is required to view solution.}',
#                         'subtopic_reroll':subtopic_found,
#                         'image':question_instance.image,
#                     }
#                 except:
#                     context = {
#                         'available': True,
#                         'question':question_instance.question,
#                         'answer':question_instance.answer,
#                         'solution':'\\text{Enrollment is required to view solution.}',
#                         'subtopic_reroll':subtopic_found,
#                     }
#         return render(request, 'main_app/question_detail.html', context)
#     else:
#         subtopics = subtopics_keys
#         context = {
#             'subtopics':subtopics,
#         }
#         return render(request, 'main_app/question_customize.html', context)

"""this report_error view can be revised instead of saving a database file, it should send an email
similar to how the request for enrollment"""

def report_error(request):
    if request.method =="POST": #if the method is POST
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

    else: #if the method is GET
        return render(request, 'main_app/report_error.html') #return the report error page

def login_view(request):
    if request.method == "POST": # if method is POST
        username = request.POST['username'] #get username field
        password = request.POST['password'] #get the passwor field
        user = authenticate(request, username=username, password=password) #instantiate a user from the built-in django user authentication

        if user is not None: #if the user credentials are valid
            login(request, user) #login function
            return render(request, 'main_app/landing.html',{'message':'Login Successful.'}) #return to the landing page with a message indicating a successful login
        else: #if the user credentials are invalid
            return render(request, 'main_app/landing.html',{'danger': 'Login Failed.'}) #return to the login page with a message indicating a failed login


    else: #if method is GET
        return render(request, 'main_app/login.html') #return the login page

def logout_view(request):
    logout(request)
    return render(request, 'main_app/landing.html', {'message': 'Logout Successful.'})

def enroll(request):
    if request.method == "POST": # if method is POST

        """These are all information related to setting up the google recaptcha,
        for more information, see https://www.google.com/recaptcha/admin/site/351143989"""
        recaptcha = request.POST['g-recaptcha-response']
        recaptcha_data = {
            'secret': '6Lc1CO4UAAAAACs9XqPf35SGvdtP-0QmDM0n0K6V',
            'response': recaptcha,
        }
        google_captcha_response = requests_library.post('https://www.google.com/recaptcha/api/siteverify', recaptcha_data)

        if 'true' in google_captcha_response.text: #if the google recaptch confirms a valid human
            """yagmail is a library to manage google smtp in a more simpler manner,
            for more information, visit https://github.com/kootenpv/yagmail"""

            yag = yagmail.SMTP('cortexsilicon','jnzbhrbqcsavnlhu') #input the email username and app password
            contents = [f"""Name: {request.POST['first_name']}, {request.POST['last_name']},
School: {request.POST['school_name']},
Year Graduated: {request.POST['year_graduated']},
Phone Number: {request.POST['phone_number']},
Facebook: {request.POST['facebook_username']}"""] #this is the content of the email to be sent to the admin, pertaining to enrollment details
            yag.send('lesliecaminade@gmail.com', 'New Enrollment', contents) #send the email
            return render(request, 'main_app/landing.html', {'message': 'Enrollment has been requested, keep your lines open so we can contact you.'}) #return to the landing page with a message of a successful enrollment
        else:
            return render(request, 'main_app/landing.html', {'danger': 'Recaptcha failed. If you are really a human, please try again.'}) #return to the landing page with a message of a failed enrollment request due to a failed recaptcha

    else:# if method is GET
        return render(request, 'main_app/enrollment.html') #return the enrollment request page

def create_multiple_choice_question(request):
    if request.user.is_staff: #if the user is a staff (teacher)
        if request.method == "POST": #if the method is POST
            """the variables being setup below pertain to the question structure
            the try-except statement are catching whether the question creator has inserted
            images or not. """
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

            topic = request.POST['topic']
            subtopic = request.POST['subtopic']

            #create the multiple_choice_question instance
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

            try: #attempt to save the question
                multiple_choice_question.save() #save the question to the database
                topics = list_this_model(Topic, 'name') #create a list of all topics
                subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
                context = {
                    'topics': topics,
                    'subtopics': subtopics, #the list of all subtopics
                    'previous_topic': topic, #variables keeping track of the selected option previously
                    'previous_subtopic' : subtopic, #variables keeping track of the selected option previously
                    'message': 'Question successfully saved.'
                }
            except:
                subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
                topics = list_this_model(Topic, 'name') #create a list of all topics
                context = {
                    'topics': topics,
                    'subtopics': subtopics,
                    'previous_topic': topic,
                    'previous_subtopic' : subtopic,
                    'danger': 'Question saving failed.'
                }

            return render(request, 'main_app/create_multiple_choice_question.html', context) #return the page to create the new question again
        else: #if method is GET
            topics = list_this_model(Topic, 'name') #create a list of all topics
            subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
            context = {
                'topics': topics,
                'subtopics': subtopics,
                'previous_topic': None,
                'previous_subtopic' : None,
            }
            return render(request, 'main_app/create_multiple_choice_question.html', context) #return to page to create a question



    elif request.user.is_authenticated: #IF THE user is logged in but is not a  staff
        return render(request, 'main_app/landing.html', {'danger': 'Staff Login Required'}) #return the page with a message that a staff account is required
    else: #if the user is really not logged in
        return render(request, 'main_app/login.html', {'danger': 'Staff Login Required'}) ##return the page with a message that a staff account is required

def multiple_choice_question_customize(request):
    if request.method == "POST": #if the method is POST
        topics = list_this_model(Topic, 'name') #create a list of all topics
        subtopic = request.POST['subtopic'] #subtopic field content from the HTML form
        subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
        if subtopic == "Select a topic": #the 'Select a topic' is the default value in the dropdown, and this is checking if the dropdown was not changed
            context = {
                'subtopics': subtopics,
                'message': 'Please select a topic.',
            }
            return render(request, 'main_app/multiple_choice_customize.html', context) #return the page with the message that you have not selected a topic

        all_questions_on_that_topic = MultipleChoice.objects.filter(subtopic = subtopic) #this is a QueryDict of all the MultipleChoice instances that satisfy the filter

        try: #and if the all_questions_on_that_topic contains something
            one_question = random.choice(all_questions_on_that_topic) #pick one question instance
        except: #and if the all_questions_on_that_topic is empty

            """redundant line"""
            # subtopics = []
            #
            # for object in Subtopic.objects.all():
            #     subtopics.append(getattr(object, 'name'))
            context = {
                'topics': topics,
                'subtopics': subtopics,
                'message': 'The selected topic contains no available questions for now.',
            }
            return render(request, 'main_app/multiple_choice_customize.html', context) #return a page with the message that the subtopic is empty

        """ This section contains a html code generator on presenting the choices and corresponding images,
            The choices and the images are bound together in a list containing HTML codes,
        then shuffled to effectively shuffle the questions,
        and then iterated in a for loop on the template tags.
            The series of if- statements is just checking if an image is present, and tries not to add
        unnecessary HTML code if not needed."""

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

        random.shuffle(choices_html_code) #shuffle the choices list, note that in the HTML template tags, the for loop there does not shuffle.

        context = {
            'question': one_question.question,
            'image': one_question.image,
            'correct': one_question.correct,
            'wrong_1': one_question.wrong_1,
            'wrong_2': one_question.wrong_2,
            'wrong_3': one_question.wrong_3,
            'solution': one_question.solution,
            'subtopic': subtopic, #this is so that the subtopic selected is saved for the NEXT button, the user would not select the topic again
            'choices_html_code': choices_html_code,
            'available': True, #flag
            'pk': one_question.pk, #this is the question primary key, and is used for identifying the question, especially for cases when the
            #user is of staff level and wants to edit or delete the question. buttons are present on the page.
        }
        return render(request, 'main_app/multiple_choice_detail.html', context) #return the page containing the question.

    else: #if the method is GET
        topics = list_this_model(Topic, 'name') #create a list of all topics
        subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
        context = {
            'topics': topics,
            'subtopics': subtopics,
        }
        return render(request, 'main_app/multiple_choice_customize.html', context) #return a page to allow the user to select a topic.

def multiple_choice_question_list(request):
    if request.method == "POST" and request.user.is_staff: #if method is POST  and the user is a staff LOL

        subtopic = request.POST['subtopic'] #subtopic field from the HTML
        all_questions_on_that_topic = MultipleChoice.objects.filter(subtopic = subtopic) #QueryDict of all the MultipleChoice objects satisfying the filter
        context = {
            'available': True, #flag
            'all_questions': all_questions_on_that_topic, #this are all the questions
            'subtopic': subtopic,
        }
        return render(request, 'main_app/multiple_choice_question_list.html', context) #return the page with a list of all the question within that subtopic

    elif request.method == "GET" and request.user.is_staff: #if method is GET and user is staff
        topics = list_this_model(Topic, 'name') #create a list of all topics
        subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
        context = {
            'available': True,
            'topics': topics,
            'subtopics': subtopics,
        }
        return render(request, 'main_app/multiple_choice_question_list_select.html', context) #return the page with a list of all subtopics
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
            'choices_html_code': choices_html_code,
            'available': True, #flag
            'pk': one_question.pk, #this is the question primary key, and is used for identifying the question, especially for cases when the
            #user is of staff level and wants to edit or delete the question. buttons are present on the page.
            'disable_next': True, #flag to make the next button disappear
        }
        return render(request, 'main_app/multiple_choice_detail.html', context) #return the question without the next button
    else: #if the user is not a staff
        return render(request, 'main_app/landing.html', {'danger':'Admin account is required to allow targeted question lookup.'}) #return to the landing page with a message that says only admin accounts are allowed to target questions

def multiple_choice_question_delete(request, pk):
    if request.user.is_staff: #if the user is a staff
        one_question = MultipleChoice.objects.get(pk = pk) #one question that will be deleted
        one_question.delete() #actually delete the question
        topics = list_this_model(Topic, 'name') #create a list of all topics
        subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
        context = {
            'message': 'Question successfully deleted.',
            'topics': topics,
            'subtopics': subtopics,
        }
        return render(request, 'main_app/multiple_choice_question_list_select.html', context) #return the page saying that deletion is sucessful
    else: # if user is not a staff
        topics = list_this_model(Topic, 'name') #create a list of all topics
        subtopics = list_this_model(Subtopic, 'name') #create a list of all subtopics
        context = {
            'danger': 'Admin account is required to delete questions.',
            'topics': topics,
            'subtopics': subtopics,
        }
        return render(request, 'main_app/multiple_choice_question_list_select.html', context) #return a page that says deletion is not allowed

def change_password(request):
    if request.user.is_authenticated and request.method == "POST": #if user is logged in and the method is POST
        password = request.POST['password'] #html password field
        confirm_password = request.POST['confirm_password'] #html confirm_password field
        if password == confirm_password: #if the passwords match
            request.user.set_password(password) #actually set the new password
            request.user.save() #save the user to the database
            return render(request, 'main_app/landing.html', {'message':'Password change successful.'}) #return to the page saying that the password change is succcessful
        else: #if the passwords do not match
            return render(request, 'main_app/change_password.html', {'danger': 'Passwords did not match, try again.'}) #return the same page again saying that the passwords do not match and the user should try again
    elif request.method =="GET" and request.user.is_authenticated: #if user is logged in and method is GET
        return render(request, 'main_app/change_password.html') #return the page
    else: #if user is not logged in
        return render(request, 'main_app/landing.html', {'danger':'Login is first required.'}) #return to the landing page saying log in is required

def load_subtopics(request):
    topic = request.GET.get('topic') #get the topic value passed in by the ajax call in the javascript in the json file
    previous_topic = request.GET.get('previous_topic') #get the previous topic value passed in by the ajax call in the javascripp
    previous_subtopic = request.GET.get('previous_subtopic') #get the previous topic value passed in by the ajax call in the javascript
    subtopics = Subtopic.objects.filter(topic = topic).order_by('name') #get all the subtopics under the topic


    #populate a list with the strings containing the list of all the subtopics
    subtopics_list = []
    for subtopic in subtopics:
        subtopics_list.append(subtopic.name)
    context = {
        'subtopics': subtopics_list,
        'previous_topic': previous_topic,
        'previous_subtopic': previous_subtopic,
    }
    return render(request, 'main_app/ajax/load_subtopics_dropdown.html', context) #pass the page snippet along with the list of the subtopics
