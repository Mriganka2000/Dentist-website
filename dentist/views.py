from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        send_mail(
            message_name,
            'Thanks for choosing us. We will contract to you soon',
            message_email,
            [message_email],
        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def service(request):
    return render(request, 'service.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blogDetail(request):
    return render(request, 'blog-details.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        appointment = "Thanks for choosing us. You have booked the scheldule at " + \
            your_scheldule + " on date " + your_date

        send_mail(
            your_name,
            appointment,
            your_email,
            [your_email],
        )

        return render(request, 'appointment.html', {
            'your_scheldule': your_scheldule,
            'your_name': your_name,
            'your_email': your_email,
            'your_phone': your_phone,
            'your_date': your_date,
        }
        )

    else:
        return render(request, 'index.html', {})
