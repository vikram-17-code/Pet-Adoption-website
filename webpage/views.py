from django.shortcuts import render,redirect,get_object_or_404
from .models import pet, breed, Profile 
from .models import adoption as Adoption
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UpdateUserInfo ,AddPetForm ,UpdatePetForm ,BreedRecommendationForm ,AdoptionForm ,PaymentForm
from django import forms
from django.contrib.auth.decorators import permission_required,login_required, user_passes_test


# Create your views here.
def home(request):
    #for dropdown menw
    Breed =breed.objects.all()
    pets =pet.objects.all()
    return render(request, "home.html",{"pets":pets,"Breed":Breed})

def About(request):
    #for dropdown menw
    Breed =breed.objects.all()
    return render(request,"About.html",{"Breed":Breed})

def login_user(request):
    #for dropdown menw
    Breed =breed.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_staff: 
                messages.success(request,"Error!,Please try again!")
                return redirect('login') 
            else: 
                login(request, user) 
                messages.success(request, "You are logged in!") 
                return redirect("home")
                
        else:
            messages.success(request,"Error!,Please try again!")
            return redirect("login")
    else:

        return render(request,"login.html",{"Breed":Breed})

def logout_user(request):
    logout(request)
    messages.success(request,"you are logged out!")
    return redirect("home")

def register(request):
    #for dropdown menw
    Breed =breed.objects.all()
    form = SignUpForm()
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]

            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"You are successfully registered!!")
            redirect("home")
        else:
            messages.success(request,"Error!,Please try again!")
            redirect("register")

    return render(request,"register.html",{"form":form,"Breed":Breed})

def Pet_detail(request,pk):
    #for dropdown menw
    Breed =breed.objects.all()

    
    Pet = pet.objects.get(id=pk)
    return render(request, "petPage.html",{"Pet":Pet,"Breed":Breed})

def breed_detail(request,bre):

    #for dropdown menw
    Breed =breed.objects.all()

    bre=bre.replace('-',' ')

    try:
        Breed_category = breed.objects.get(name=bre)
        Pet = pet.objects.filter(breed=Breed_category)
        return render(request, "breed.html",{"Pet":Pet ,"breed":Breed_category,"Breed":Breed})
    except:
        messages.success(request,"Error")
        return redirect("home")

def profile(request):
    #for dropdown menw
    Breed =breed.objects.all()
    profile = get_object_or_404(Profile, user=request.user)
    
    return render(request, "profile.html",{"Breed":Breed,"profile":profile})


def update_user(request):
    #for dropdown menw
    Breed =breed.objects.all()
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None,instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request,"user data is updated")
            if current_user.is_staff:
                return redirect("staff_home")
            else:
                return redirect("home")
        else:
            return render(request,"update_user.html",{"user_form":user_form,"Breed":Breed})
    else:
        messages.success(request,"you must be logged in")
        return redirect("home")


def change_password(request):
    #for dropdown menw
    Breed =breed.objects.all()
    if request.user.is_authenticated:
        current_user=request.user
        
        if request.method == "POST":
            form = ChangePasswordForm(current_user,data=request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "your password has been chanage...")
                return redirect("login")
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                    return redirect("change_password")
        else:
            form=ChangePasswordForm(current_user)
            return render(request,"change_password.html",{"form":form,"Breed":Breed})
    else:
        messages.success(request,"you must be logged in..")
        return redirect ("home")
    
def user_info(request):
    #for dropdown menw
    Breed =breed.objects.all()
    if request.user.is_authenticated:
        current_user=Profile.objects.get(user__id=request.user.id)
        form = UpdateUserInfo(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request,"user info is updated")
            if current_user.is_staff:
                return redirect("staff_home")
            else:
                return redirect("home")
        else:
            return render(request,"user_info.html",{"form":form,"Breed":Breed})
    else:
        messages.success(request,"you must be logged in")
        return redirect("home")


def breed_category(request):
    #for dropdown menw
    Breed =breed.objects.all()
    
    return render(request, "breed_category.html",{"Breed":Breed})



def staff_login(request):
    #for dropdown menw
    Breed =breed.objects.all()
     
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password) 
        if user is not None and user.is_staff: 
            login(request, user) 
            messages.success(request, 'Welcome, Staff Member!') 
            return redirect('staff_home') 
        else: 
            messages.error(request, 'Invalid credentials or not a staff member.') 
            return redirect('staff_login') 
    return render(request, 'staff_login.html')



@permission_required('webpage.can_add_pet', raise_exception=True)
def add_pet(request):
    #for dropdown menw
    Breed =breed.objects.all()
    
    if request.method == 'POST':
        form = AddPetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet added successfully!')
            return redirect('manage_pets')
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AddPetForm()
    return render(request, 'add_pet.html', {'form': form,"Breed":Breed})
    

@user_passes_test(lambda u: u.is_staff) 
def manage_pets(request):
   
    
    pets = pet.objects.all()
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        pet_to_delete = pet.objects.get(id=pet_id)
        pet_to_delete.delete()
        messages.success(request, "Pet deleted successfully!")
        return redirect('manage_pets')
    return render(request, "manage_pets.html", {"pets": pets,})


@user_passes_test(lambda u: u.is_staff)
def update_pet(request, pk):
    #for dropdown menw
    
    try: 
        Pet = get_object_or_404(pet, pk=pk) 
    except Pet.DoesNotExist: 
        messages.error(request, "Pet not found.") 
        return redirect('manage_pets')
    if request.method == "POST":
        form = UpdatePetForm(request.POST, request.FILES, instance=Pet)
        if form.is_valid():
            form.save()
            messages.success(request, "Pet details updated successfully!")
            return redirect('petP', pk=Pet.pk)
    else:
        form = UpdatePetForm(instance=Pet)
    return render(request, "update_pet.html", {"form": form, "pet": Pet,})


def breed_recommendation(request):
    #For dropdown menu 
    Breed = breed.objects.all() 
    form = BreedRecommendationForm(request.POST) 

    if request.method == 'POST': 
        
        if form.is_valid(): 
            activity_level = form.cleaned_data['activity_level'] 
            good_with_kids = form.cleaned_data['good_with_kids']
            Guard_dog = form.cleaned_data['Guard_dog']
            athletic = form.cleaned_data['athletic'] 
            size = form.cleaned_data['size'] 
            low_shedding = form.cleaned_data['low_shedding'] 
            first_time_owner = form.cleaned_data['first_time_owner'] 
            
            # Filtering logic based on user inputs 
            recommended_breeds = breed.objects.filter( 
                activity_level=activity_level, 
                good_with_kids=good_with_kids,
                athletic=athletic,
                Guard_dog=Guard_dog,
                size=size, 
                low_shedding=low_shedding, 
                first_time_owner=first_time_owner ) 
            return render(request, 'breed_recom_result.html', {'form': form, 'recommended_breeds': recommended_breeds, 'Breed': Breed}) 
    else:
        form = BreedRecommendationForm() 
    return render(request, 'breed_recom.html', {'form': form, 'Breed': Breed})


def adopt_pet(request, pk):
    if request.user.is_authenticated:
        pet_instance = get_object_or_404(pet, pk=pk)
        user_profile = request.user.profile
        if pet_instance.is_adopted:
            messages.error(request, 'This pet has already been adopted.')
            return redirect('home')
        if request.method == 'POST':
            form = AdoptionForm(request.POST)
            if form.is_valid():
                adoption_instance = form.save(commit=False)
                adoption_instance.pet = pet_instance
                adoption_instance.customer = request.user
                adoption_instance.save()
                pet_instance.is_adopted = True
                pet_instance.save()
                messages.success(request, 'Adoption process completed successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = AdoptionForm(initial=
                {'user_name' : user_profile.user,
                'pet': pet_instance,
                'pet_name': pet_instance.name,
                'phone': user_profile.phone,  
                'address': user_profile.address, 
                'phone': user_profile.phone,
                'city': user_profile.city,
                'state': user_profile.state,
                'zipcode': user_profile.zipcode,})
        return render(request, 'adopt_pet.html', {'form': form, 'pet': pet_instance})
    else:
        messages.error(request, 'You must be logged in!')
        return redirect('home')

@user_passes_test(lambda u: u.is_staff)
def manage_adoptions(request):
    adoptions = Adoption.objects.all()
    if request.method == 'POST':
        adoption_id = request.POST.get('adoption_id')
        action = request.POST.get('action')
        adoption = get_object_or_404(Adoption, id=adoption_id)
        pet = adoption.pet
        if action == 'change_status':
            adoption.status = not adoption.status
            adoption.save()
            messages.success(request, "Adoption status changed successfully!")
        elif action == 'delete_adoption':
            pet.is_adopted = False
            pet.save()
            adoption.delete()
            messages.success(request, "Adoption deleted successfully!")
        return redirect('manage_adoptions')
    
    return render(request, "manage_adoptions.html", {"adoptions": adoptions})

@login_required
def user_adopted_pets(request):
    adoptions = Adoption.objects.filter(customer=request.user)
    return render(request, "user_adopted_pets.html", {"adoptions": adoptions})

def staff_home(request):
    return render(request, "staff_home.html")

@login_required
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            messages.success(request, 'Payment processed successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PaymentForm()
    
    return render(request, 'payment.html', {'form': form})