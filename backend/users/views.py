from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q

from . forms import RegisterUserForm, UpdateProfileForm, BecomeVendorForm, SetPasswordForm, PasswordResetForm
from . models import User
from products.models import Product
from .tokens import account_activation_token
from orders.models import Order, OrderItem

def vendor_earnings(request):
    vendor = request.user
    products = vendor.products.all()
    orders = vendor.orders.all()
    for order in orders:
        order.vendor_amount = 0
        order.vendor_total = 0
        order.fully_paid = True
        for item in order.items.all():
            if item.vendor == request.user:
                if item.is_paid:
                    order.vendor_total += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request, 'users/earnings.html', {'vendor':vendor, 'products':products, 'orders':orders})

def my_profile(request):
    customer = request.user
    orders = customer.ordenes.all()
    # orderItems = orders.vendors.all()
    return render(request, 'users/my_profile.html', {'orders':orders})

def vendor_products(request):
    vendor = request.user
    products = vendor.products.all()
    return render(request, 'users/vendor_products.html', {'products':products})


def create_vendor(request):
    user = request.user
    form = BecomeVendorForm(instance=user)

    if request.method == 'POST':
        form = BecomeVendorForm(request.POST, instance=user)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.is_vendor = True
            vendor.save()
            return redirect('home')

    return render(request, 'users/create_vendor.html', {'form': form})
    


def update_profile(request):
    user = request.user
    form = UpdateProfileForm(instance=user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'users/update_profile.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'See you later!')
    return redirect('home')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)

        except:
            messages.success(request, 'User does not exist!')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome ' + user.username)
            return redirect('home')

        else:
            messages.success(request, 'Username or password does not match!')
    return render(request, 'users/login.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login_page')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('home')

def activate_email(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("users/activate.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def register_page(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_active = False
            user.save()
            activate_email(request, user, form.cleaned_data.get('email'))
            # login(request, user)
            # messages.success(request, 'Account created!')
            return redirect('home')
        else:
            messages.success(request, 'An error occurred during registation!')

    return render(request, 'users/register.html', {'form': form})

def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login_page')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'users/password_reset_confirm.html', {'form': form})

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = User.objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("users/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('home')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="users/password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'users/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("home")



def vendor_profile(request):
    return render(request, 'users/vendor_profile.html')

def become_vendor(request):
    return render(request, 'users/become_vendor.html')

