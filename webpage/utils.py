from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_approval_email(user_email, pet_name):
    subject = 'Adoption Approved'
    text_content = f'Congratulations! Your adoption request for {pet_name} has been approved.'
    html_content = f'''
    <html>
        <body>
            <div style="text-align: center;">
                <img src="static/onlyLOGO.jpg" alt="Tailwagger Adoption Center" style="max-width: 200px; margin-bottom: 20px;">
            </div>
            <h1>Congratulations!</h1>
            <p>Your adoption request for <strong>{pet_name}</strong> has been approved.</p>
            <p>Thank you for choosing to adopt a pet. We hope you have a wonderful time with your new companion.</p>
            <p>Come and get your new friend at our shelter!</p>
            <p>Best regards,<br>The Pet Adopt Team</p>
        </body>
    </html>
    '''
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_pickup_email(user_email, pet_name):
    subject = 'Thank You for Picking Up Your Pet'
    text_content = f'Thank you for picking up {pet_name} from our shelter. We hope you have a wonderful time with your new companion.'
    html_content = f'''
    <html>
        <body>
            <div style="text-align: center;">
                <img src="https://example.com/path/to/your/logo.png" alt="Tailwagger Adoption Center" style="max-width: 200px; margin-bottom: 20px;">
            </div>
            <h1>Thank You!</h1>
            <p>Thank you for picking up <strong>{pet_name}</strong> from our shelter. We hope you have a wonderful time with your new companion.</p>
            <p>If you have any questions or need any assistance, please do not hesitate to contact us.</p>
            <p>Best regards,<br>The Tailwagger Adoption Center Team</p>
        </body>
    </html>
    '''
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_rejection_email(user_email, pet_name):
    subject = 'Adoption Request Rejected'
    text_content = f'We regret to inform you that your adoption request for {pet_name} has been rejected.'
    html_content = f'''
    <html>
        <body>
            <div style="text-align: center;">
                <img src="https://example.com/path/to/your/logo.png" alt="Tailwagger Adoption Center" style="max-width: 200px; margin-bottom: 20px;">
            </div>
            <h1>Adoption Request Rejected</h1>
            <p>We regret to inform you that your adoption request for <strong>{pet_name}</strong> has been rejected.</p>
            <p>If you have any questions or need any assistance, please do not hesitate to contact us.</p>
            <p>Best regards,<br>The Tailwagger Adoption Center Team</p>
        </body>
    </html>
    '''
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()