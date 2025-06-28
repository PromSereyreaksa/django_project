from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
import os
import json
from .models import Profile
from google.auth.transport import requests as grequests
from django.contrib.auth import logout
import uuid
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .supabase_client import SUPABASE_URL, supabase
from .forms import ProfileForm
from io import BytesIO
from PIL import Image

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title':'index'})

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to access this page.")
        return redirect('login')
    return render(request, 'home.html', {'title':'home'})

### register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            phone_no = form.cleaned_data.get('phone_no')
            ### mail system
            htmly = get_template('Email.html')
            d = {'username': username}
            subject, from_emial, to = 'Welcome to my website' , 'prumsereyreaksa@gmail.com' , email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_emial, [to])
            #EmailMultiAlternatives is used when you want to send both plain text and HTML versions of an email.
            #Because not all email clients (apps) support HTML!
            #If the email client supports HTML → it shows the HTML version (text/html)
            #If not → it falls back to the plain text version
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'register'})

def Login(request):
    if request.method == 'POST':
        ## can also use aut form
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #will return a user object if the credentials are valid, otherwise None
        if user is not None:
            #so if it returns a user object, we can log the user in
            form = login(request,user) #to make sure they are who they say they are
            messages.success(request, f'Welcome {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'Login'})

@csrf_exempt
def auth_receiver(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        token = data.get('credential')
        if not token:
            return JsonResponse({'error': 'Missing credential'}, status=400)

        try:
            idinfo = id_token.verify_oauth2_token(
                token,
                grequests.Request(),
                "1055977422174-v2f3tvqhtbh5lmtta7ukhd3m1m9qehr8.apps.googleusercontent.com"
            )

            email = idinfo['email']
            full_name = idinfo.get('name', '')
            first_name = full_name.split(' ')[0]
            last_name = ' '.join(full_name.split(' ')[1:]) or ''
            sub = idinfo['sub']
            username = f'google_{sub}'

            # Create or get user
            user, created = User.objects.get_or_create(username=username, defaults={
                'email': email,
                'first_name': first_name,
                'last_name': last_name
            })
            # Create profile if doesn't exist
            Profile.objects.get_or_create(user=user)
            # Log in
            login(request, user)
            return JsonResponse({'status': 'logged_in', 'redirect': '/home'})
        except ValueError:
            return JsonResponse({'error': 'Invalid token'}, status=400)

    return JsonResponse({'error': 'POST required'}, status=405)

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index')
    
@login_required
def profile_views(request):
    profile = request.user.profile
    if request.method == 'POST' and 'avatar' in request.FILES:
        avatar_file = request.FILES['avatar']

        # Open image with Pillow
        image = Image.open(avatar_file)

        # Resize the image (example: max width or height 300px, maintaining aspect ratio)
        max_size = (300, 300)
        image.thumbnail(max_size)

        # Save resized image to bytes buffer
        buffer = BytesIO()
        image_format = image.format or 'PNG'  # Use original format or PNG fallback
        image.save(buffer, format=image_format)
        buffer.seek(0)

        # Create filename
        filename = f"avatars/{uuid.uuid4().hex}.{image_format.lower()}"

        # Upload resized image bytes to Supabase
        res = supabase.storage.from_('avatar').upload(filename, buffer.read())

        # Check upload result
        if hasattr(res, 'error') and res.error:
            print("Upload error:", res.error)
        else:
            public_url = f"{SUPABASE_URL}/storage/v1/object/public/avatar/{filename}"
            profile.avatar = public_url
            profile.save()
            return redirect('profile')

    return render(request, 'profile_av.html', {'profile': profile})





