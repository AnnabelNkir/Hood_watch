from django.db.models.query import Prefetch
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignupForm,ProfileForm,NeighbourForm,BusinessForm,PostForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Business,Neighbour,Profile, Post



@login_required(login_url='/accounts/login/')
def index(request):
    hood = Neighbour.objects.all()
    return render(request,'index.html',{"hood":hood})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile=Profile(user=user)
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Confirm your neighbourhood residence.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('<h3 style ="text-align:center;"> We have sent a link to your email, please follow the link to complete the registration. </h3>')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('<h4> Thank you for your email confirmation. To login to your account, <a href="/accounts/login">Click here .</a> </h4>')
    else:
        return HttpResponse('<h1 style = "color:red;"> Activation link is invalid! </h1>')

def profile(request):
    profile = Profile.objects.filter(user=request.user)
    current_user = request.user
    neighbour = Neighbour.objects.filter(user=current_user)
    biz = Business.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form =ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if image_form.is_valid:
            image_form.save()
        else:
            image_form = ProfileForm()
            return render(request, 'profile.html', {"image_form": image_form,"biz":biz,"profile":profile,"neighbour":neighbour,"pr":Prefetch})
    return render(request, 'profile.html', {"image_form": image_form,"biz":biz,"profile":profile,"neighbour":neighbour})

def create(request):
    area = Neighbour.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
        return redirect('/')

    else:
        form = NeighbourForm()
    return render(request, 'create.html', {"form": form,"area":area })

def hood(request,id):
    bizna = Business.objects.filter(neighbourhood_id=id)
    post_form = PostForm()
    hood = Neighbour.objects.get(pk=id)
    posts = Post.objects.filter(neighbourhood_id=id)
    # posts = hood.post.all()
    return render(request, 'hood.html', {"bizna": bizna, "hood": hood, "post_form": post_form ,"posts": posts })


def biz(request):
    # biz = Neighbour.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.user = current_user
            biz.save()
            print(biz)
        return redirect('/')

    else:
        form = BusinessForm()
    return render(request, 'biz.html', {"form": form })


def post(request):
    neighbourhood = request.user.profile.neighbourhood
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.neighbourhood = neighbourhood
            post.save()
            
        return redirect('hood', neighbourhood.id)

    else:
        post_form = PostForm()
    return render(request, 'hood.html', {"post_form": post_form })



def search_results(request):    
    if 'name' in request.POST:
        search_term = request.POST.get("name")
        searched_business = Business.objects.filter(name__icontains=search_term)
        print('searched_business')
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_business": searched_business})

    else:
        message = "Please search for a valid business"
        return render(request, 'search.html',{"message":message})



def profiles(request,id):
    profile = Profile.objects.get(user_id=id)
    biz=Business.objects.filter(user_id=id)
   
                       
    return render(request,'profiles.html',{"profile":profile,"biz":biz})