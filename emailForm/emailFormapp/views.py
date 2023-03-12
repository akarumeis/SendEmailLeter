from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

# Створюєм функцію представлення


def create_leter(request):
    # Створюємо словник
    context = {}
    # Якщо запрос є "POST"
    if request.method == 'POST':
        # Беремо повідомлення з запиту
        message = request.POST.get('message')
        # Беремо адресу з запиту
        email = request.POST.get('email')
        # Беремо ім'я з запиту
        name = request.POST.get('name')
        # Формуємо повідомлення
        message = f"Ім'я: {name}\nПовідомлення: {message}\nПошта: {email}"
        # Якщо немає помилок
        try:
            # Надсилаємо повідомлення на пошту
            send_mail('Тема', message, 'settings.EMAIL_HOST_USER', [email])
            # send_mail(subject - тема, message - повідомлення, from_email - з якої електронної пошти, recipient_list - список пошт одержувачів) - ці пареметри є обов'язковими!
        # Якщо виник вийняток
        except BadHeaderError:
            # Додаємо помилку
            context['error'] = 'Знайдено некоректний заголовок'
    # Повертаємо сформовану сторінку
    return render(request, 'index.html', context)
