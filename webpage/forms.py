from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm ,SetPasswordForm
from django import forms
from .models import Profile ,pet ,adoption ,breed 
from django.core.validators import MinLengthValidator


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}),required=False)
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first_name'}),required=False)
    last_name = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last_name'}),required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}),required=False)
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first_name'}),required=False)
    last_name = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last_name'}),required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

class ChangePasswordForm(SetPasswordForm):
    old_password = forms.CharField( label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}) ) 
    
    def clean_old_password(self): 
        old_password = self.cleaned_data.get("old_password") 
        if not self.user.check_password(old_password): 
            raise forms.ValidationError("Old password is incorrect.") 
        return old_password
        

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'] = self.fields.pop('old_password') 
        self.fields = {key: self.fields[key] for key in ['old_password', 'new_password1', 'new_password2']}

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

    
class UpdateUserInfo(forms.ModelForm):
    
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}),required=False)
    address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}),required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'city'}),required=False)
    state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'state'}),required=False)
    zipcode =forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'zipcode'}),required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'country'}),required=False)

    class Meta:
        model = Profile
        fields = ("phone","address","city","state","zipcode","country")



class AddPetForm(forms.ModelForm):
    class Meta:
        model = pet
        fields = ['name', 'age', 'breed', 'gender', 'description', 'size',
                   'vaccinations', 'spayed_neutered', 'medical_conditions', 'image']


class UpdatePetForm(forms.ModelForm):
    class Meta:
        model = pet
        fields = ['name', 'age', 'breed', 'gender', 'description', 'size', 
                  'vaccinations', 'spayed_neutered', 'medical_conditions', 'image', 'is_adopted']


class BreedRecommendationForm(forms.Form):
    activity_level_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    size_choices = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]
    activity_level = forms.ChoiceField(choices=activity_level_choices, label="Activity Level", widget=forms.RadioSelect)
    size = forms.ChoiceField(choices=size_choices, label="Preferred Size", widget=forms.RadioSelect)
    good_with_kids = forms.BooleanField(required=False, label="Good with Kids")
    Guard_dog = forms.BooleanField(required=False, label="Guard dog")
    athletic = forms.BooleanField(required=False, label="athletic")
    low_shedding = forms.BooleanField(required=False, label="Low Shedding")
    first_time_owner = forms.BooleanField(required=False, label="Suitable for First-Time Owner")

    class Meta:
        model = breed
        field = ['activity_level', 'size', 'Guard_dog', 'athletic', 'good_with_kids', 'low_shedding', 'first_time_owner']

class AdoptionForm(forms.ModelForm):
    pet_name = forms.CharField(label="Pet Name", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})) 
    user_name  = forms.CharField(label="Name", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    phone = forms.CharField(label="Phone", max_length=15, required=True, validators=[MinLengthValidator(10)], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    city = forms.CharField(label="City", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}))
    state = forms.CharField(label="State", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}))
    zipcode = forms.CharField(label="Zipcode", max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode'}))
    declaration = forms.BooleanField(label="Declaration", required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
        
    class Meta:
        model = adoption
        fields = ['user_name', 'pet', 'pet_name',  'phone', 'address','city','state','zipcode','declaration']
        widgets = { 'pet': forms.HiddenInput(),
                'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
                'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
                'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
                'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}),
                'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode'}),
                'declaration': forms.CheckboxInput(attrs={'class': 'form-check-input',}),}
        
    def __init__(self, *args, **kwargs):
        super(AdoptionForm, self).__init__(*args, **kwargs)
        self.fields['declaration'].label = 'I hereby declare that the information provided is true and correct to the best of my knowledge and belief. And I will be fully responsible for this animal and take good care of it.'

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search for pets...'}))
    age = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    size = forms.ChoiceField(choices=[('', 'Select Size'),('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], required=False)
    breed = forms.ModelChoiceField(queryset=breed.objects.all(), required=False, empty_label="Select Breed")
    gender = forms.ChoiceField(choices=[('', 'Select Gender'), ('male', 'Male'), ('female', 'Female')], required=False)


class ReportForm(forms.Form):
    breed = forms.ModelChoiceField(queryset=breed.objects.all(), required=False, empty_label="Select Breed")
    date_range = forms.ChoiceField(choices=[
        ('today', 'Today'),
        ('last_week', 'Last Week'),
        ('last_month', 'Last Month'),
        ('last_year', 'Last Year'),

    ], required=True, label="Date Range")


class AddBreedForm(forms.ModelForm):
    class Meta:
        model = breed
        fields = ['name', 'activity_level', 'good_with_kids', 'Guard_dog', 'athletic', 'size', 'low_shedding', 'first_time_owner','image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Breed Name'}),
            'activity_level': forms.Select(),
            'good_with_kids': forms.CheckboxInput(),
            'Guard_dog': forms.CheckboxInput(),
            'athletic': forms.CheckboxInput(),
            'size': forms.Select(),
            'low_shedding': forms.CheckboxInput(),
            'first_time_owner': forms.CheckboxInput(),
            'image': forms.ClearableFileInput()
        }