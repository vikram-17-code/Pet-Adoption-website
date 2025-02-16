from django.shortcuts import render,redirect,get_object_or_404
from .models import pet, breed, Profile 
from .models import adoption as Adoption
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm,ChangePasswordForm, UpdateUserInfo ,AddPetForm ,UpdatePetForm ,BreedRecommendationForm ,AdoptionForm,SearchForm ,ReportForm ,AddBreedForm
from django import forms
from django.contrib.auth.decorators import permission_required,login_required, user_passes_test
from django.views.decorators.cache import cache_control
from django.utils import timezone
from datetime import timedelta
import matplotlib 
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.db.models import Count
import urllib.parse

matplotlib.use('Agg')

# Create your views here.

def home(request):
    pets =pet.objects.all()
    if request.user.is_authenticated:
        adoptions = Adoption.objects.filter(customer=request.user)
        if any(adoption.approval and not adoption.status for adoption in adoptions):
            messages.success(request, "One or more of your adoption requests have been approved!")
    return render(request, "home.html",{"pets":pets,})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def About(request):
   return render(request,"About.html",{})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):

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

        return render(request,"login.html",{})
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
    logout(request)
    messages.success(request,"you are logged out!")
    return redirect("home")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
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
            return redirect("home")
        else:
            messages.success(request,"Error!,Please try again!")
            return redirect("register")

    return render(request,"register.html",{"form":form,})

def Pet_detail(request,pk):
    Pet = pet.objects.get(id=pk)
    return render(request, "petPage.html",{"Pet":Pet,})

def breed_detail(request,bre):
    bre=bre.replace('-',' ')
    try:
        Breed_category = breed.objects.get(name=bre)
        Pet = pet.objects.filter(breed=Breed_category)
        return render(request, "breed.html",{"Pet":Pet ,"breed":Breed_category})
    except:
        messages.success(request,"Error")
        return redirect("home")
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    return render(request, "user/profile.html",{"profile":profile})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_user(request):
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
            return render(request,"user/update_user.html",{"user_form":user_form,})
    else:
        messages.success(request,"you must be logged in")
        return redirect("home")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_password(request):
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
            return render(request,"user/change_password.html",{"form":form,})
    else:
        messages.success(request,"you must be logged in..")
        return redirect ("home")
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def user_info(request):
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
            return render(request,"user/user_info.html",{"form":form,})
    else:
        messages.success(request,"you must be logged in")
        return redirect("home")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staff_login(request):
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
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_pet(request):
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
    return render(request, 'staff/add_pet.html', {'form': form,"Breed":Breed})
    

@user_passes_test(lambda u: u.is_staff) 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def manage_pets(request):
    pets = pet.objects.all()
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        pet_to_delete = pet.objects.get(id=pet_id)
        pet_to_delete.delete()
        messages.success(request, "Pet deleted successfully!")
        return redirect('manage_pets')
    return render(request, "staff/manage_pets.html", {"pets": pets,})


@user_passes_test(lambda u: u.is_staff)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_pet(request, pk):
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
    return render(request, "staff/update_pet.html", {"form": form, "pet": Pet,})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def breed_recommendation(request):
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
            filters = {
                'activity_level': activity_level,
                'athletic': athletic,
                'Guard_dog': Guard_dog,
                'size': size,
                }
    
            if low_shedding:
                filters['low_shedding'] = low_shedding
    
            if first_time_owner:
                filters['first_time_owner'] = first_time_owner

            if good_with_kids:
                filters['good_with_kids'] = good_with_kids

            recommended_breeds = breed.objects.filter(**filters)

            return render(request, 'breed_recom_result.html', {'form': form, 'recommended_breeds': recommended_breeds, 'Breed': Breed}) 
    else:
        form = BreedRecommendationForm() 
    return render(request, 'breed_recom.html', {'form': form, 'Breed': Breed})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
        elif action == 'change_approval':
            if not adoption.approval:
                adoption.approval = True
                adoption.save()
                messages.success(request, "Adoption approval status changed successfully!")
        return redirect('manage_adoptions')
    
    return render(request, "staff/manage_adoptions.html", {"adoptions": adoptions})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_adopted_pets(request):
    adoptions = Adoption.objects.filter(customer=request.user)
    if any(adoption.approval and not adoption.status for adoption in adoptions):
        messages.success(request, "One or more of your adoption requests have been approved!")
    return render(request, "user/user_adopted_pets.html", {"adoptions": adoptions})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staff_home(request):
    return render(request, "staff/staff_home.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def search_pets(request):
    pets = pet.objects.all()
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        age = search_form.cleaned_data['age']
        size = search_form.cleaned_data['size']
        breed = search_form.cleaned_data['breed']
        gender = search_form.cleaned_data['gender']
        
        if query:
            pets = pets.filter(name__icontains=query)
        if age:
            pets = pets.filter(age__icontains=age)
        if size:
            pets = pets.filter(size=size)
        if breed:
            pets = pets.filter(breed=breed)
        if gender:
            pets = pets.filter(gender=gender)
    
    return render(request, "search_pets.html", {"pets": pets, "search_form": search_form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(lambda u: u.is_staff)
def generate_report(request):
    report_form = ReportForm(request.GET or None)
    adoptions = Adoption.objects.filter(status=True)
    report_data = None
    chart_data = None


    if report_form.is_valid():
        breed = report_form.cleaned_data['breed']
        date_range = report_form.cleaned_data['date_range']
        today = timezone.now().date()

        if date_range == 'today':
            start_date = today
        elif date_range == 'last_week':
            start_date = today - timedelta(days=7)
        elif date_range == 'last_month':
            start_date = today - timedelta(days=30)
        elif date_range == 'last_year':
            start_date = today - timedelta(days=365)

        if breed:
            adoptions = adoptions.filter(pet__breed=breed)

        adoptions = adoptions.filter(date__gte=start_date)

        report_data = {
            'total_adoptions': adoptions.count(),
            'adoptions': adoptions
        }

        if adoptions.exists():
            # Generate chart data
            chart_data = adoptions.values('pet__breed__name').annotate(count=Count('id'))

            # Clear the previous plot
            plt.clf()

            # Create a pie chart
            labels = [data['pet__breed__name'] for data in chart_data]
            sizes = [data['count'] for data in chart_data]
            colors = plt.cm.Paired(range(len(labels)))

            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')

            # Save the plot to a BytesIO object
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = 'data:image/png;base64,' + urllib.parse.quote(string)

            return render(request, "staff/generate_report.html", {"report_form": report_form, "report_data": report_data, "chart_data": uri})

    return render(request, "staff/generate_report.html", {"report_form": report_form, "report_data": report_data})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(lambda u: u.is_staff)
def add_breed(request):
    if request.method == 'POST':
        form = AddBreedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Breed added successfully!')
            return redirect('manage_breeds')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AddBreedForm()
    
    return render(request, 'staff/add_breed.html', {'form': form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(lambda u: u.is_staff)
def manage_breeds(request):
    breeds = breed.objects.all()
    return render(request, 'staff/manage_breeds.html', {'breeds': breeds,})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(lambda u: u.is_staff)
def update_breed(request, pk):
    breed_instance = get_object_or_404(breed, pk=pk)
    if request.method == 'POST':
        form = AddBreedForm(request.POST, instance=breed_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Breed updated successfully!')
            return redirect('manage_breeds')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AddBreedForm(instance=breed_instance)
    
    return render(request, 'staff/update_breed.html', {'form': form, 'breed': breed_instance})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(lambda u: u.is_staff)
def delete_breed(request, pk):
    breed = get_object_or_404(breed, pk=pk)
    if request.method == 'POST':
        breed.delete()
        messages.success(request, 'Breed deleted successfully!')
        return redirect('manage_breeds')
    return render(request, 'staff/manage_breeds.html')
