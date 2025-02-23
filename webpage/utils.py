from django.core.mail import send_mail
from django.conf import settings

def send_approval_email(user_email, pet_name):
    subject = 'Adoption Approved'
    message = f'Congratulations! Your adoption request for {pet_name} has been approved.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)