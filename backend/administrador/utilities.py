from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Newsletter, ContentNewsLetter




def news_letter_create(request, content):
    news = ContentNewsLetter.objects.create(content=content)
    news.save()
    return news


def send_news(news):
    from_email = settings.EMAIL_HOST_USER

    for subs in Newsletter.objects.all():
        to_email = subs

        subject = 'News Letter'
        text_content = 'Updates'
        html_content = render_to_string('admin/send_news.html', {'news':news})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()




