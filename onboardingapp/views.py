from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import date
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings
from django.utils.crypto import get_random_string

from onboardingapp.models import LaunchRegistrants, ReferralRecords

# Create your views here.

def HomePage(request):    
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        referrer = request.POST['referercode']
        referralcode = get_random_string(length=10)
        # ReferralCode = 'substudent' + '-' +  get_random_string(length=10)
                    
        
        if not request.POST['fullname']:
            messages.success(request, 'Registration Failed: Enter Your Company Name')
            return redirect('HomePage')

        if not request.POST['email']:
            messages.success(request, 'Registration Failed: Enter Your Company Email Address')
            return redirect('HomePage')
        
        if not request.POST['phonenumber']:
            messages.success(request, 'Registration Failed: Enter Your Company Phone Number')
            return redirect('HomePage')

        checkFullName = LaunchRegistrants.objects.filter(fullname=fullname)
        checkEmail = LaunchRegistrants.objects.filter(email=email)
        checkUserEmail = User.objects.filter(email=email)
        checkPhonenumber = LaunchRegistrants.objects.filter(phonenumber=phonenumber)
        if checkEmail:
            messages.error(request, 'Sorry, Email address has already been registered')
            return redirect('HomePage')

        elif checkPhonenumber:
            messages.error(request, 'Sorry, Phone number has already been registered')
            return redirect('HomePage')
    
        elif checkUserEmail:
            messages.error(request, 'Sorry, email address has already been registered')
            return redirect('HomePage')
    
        else:
            form = LaunchRegistrants(fullname=fullname, email=email, phonenumber=phonenumber, referralcode=referralcode, referercode = referrer)
            user = User.objects.create_user(username=email, email=email, password=referralcode, first_name=fullname, last_name=phonenumber)
            createReferralProfile = ReferralRecords(fullname = fullname,email = email,  numberOfReferrals = 0)
            referralURL = f'https://nysc.limestone.ng/register/{referralcode}'
            login(request, user)
            createReferralProfile.save()
            form.save()
            user.save()
            authUser = authenticate(request, username=email, password=referralcode)
            
            if authUser is not None:
                notificationEmail(request, email, fullname, referralcode, referralURL)
                # try:
                #     notificationEmail(request, email, fullname)
                # except:
                #     print('Registration mail was not sent successfully')
                messages.success(request, 'Regitration was successful and login successful, Check your inbox for more information')
                return redirect('Dashboard')
            else:
                messages.success(request, 'Regitration was successful. Check your inbox for more information')
                return redirect('HomePage')
    return render(request, 'onboardingapp/home.html')


def RegisterPage(request):
    return render(request, 'onboardingapp/register.html')


@login_required(login_url='HomePage')
def Dashboard(request):
    if LaunchRegistrants.objects.filter(email = request.user.email):
        getUser = LaunchRegistrants.objects.get(email = request.user.email)
        getfullname = getUser.fullname
        getReferralCode = getUser.referralcode
        getReferrerCode = getUser.referercode
        getDateRegistered = getUser.created_at
        # get referrer details
        if getReferrerCode:
            if LaunchRegistrants.objects.filter(referralcode = getReferrerCode).values_list('fullname', flat=True):
                getReferrerDetails = LaunchRegistrants.objects.filter(referralcode = getReferrerCode)
                getReferrerFullName = getReferrerDetails.values_list('fullname', flat=True)[0]
            else:
                getReferrerFullName = 'None'
        else:
            getReferrerFullName = ''
        context = {'getfullname':getfullname, 'getReferralCode':getReferralCode, 
                'getReferrerCode':getReferrerCode, 'getDateRegistered':getDateRegistered, 
                'getReferrerFullName':getReferrerFullName}
    else:
        return redirect('HomePage')
    return render(request, 'onboardingapp/dashboard.html', context)


def notificationEmail(request, to_email, fullname, referralcode, referralURL):
    recipient_list = [to_email, 'isaact@lightsonheights.com']

    context = {'fullname':fullname, 'email':to_email, 'referralcode':referralcode, 'referralURL':referralURL}
    html_message = render_to_string("emails/signupnotification.html", context=context)
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject = "You successfully registered for the Limestone 2.0 Launch.", 
        body = plain_message,
        from_email = 'limestoneapp1@gmail.com',
        to= recipient_list
        )

    message.attach_alternative(html_message, "text/html")
    message.send()

    if message:
        print('Sent a login notification email')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly')



def RegisterReferredUser(request, code):    
    getReferrerDetails = LaunchRegistrants.objects.filter(referralcode = code)
    if getReferrerDetails:
        if request.method == 'POST':
            fullname = request.POST['fullname']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            referrer = code
            referralcode = get_random_string(length=10)
            # ReferralCode = 'substudent' + '-' +  get_random_string(length=10)
                        
            
            if not request.POST['fullname']:
                messages.success(request, 'Registration Failed: Enter Your Company Name')
                return redirect('RegisterReferredUser')

            if not request.POST['email']:
                messages.success(request, 'Registration Failed: Enter Your Company Email Address')
                return redirect('RegisterReferredUser')
            
            if not request.POST['phonenumber']:
                messages.success(request, 'Registration Failed: Enter Your Company Phone Number')
                return redirect('RegisterReferredUser')

            checkFullName = LaunchRegistrants.objects.filter(fullname=fullname)
            checkEmail = LaunchRegistrants.objects.filter(email=email)
            checkUserEmail = User.objects.filter(email=email)
            checkPhonenumber = LaunchRegistrants.objects.filter(phonenumber=phonenumber)
            if checkEmail:
                messages.error(request, 'Sorry, Email address has already been registered')
                return redirect('RegisterReferredUser')

            elif checkPhonenumber:
                messages.error(request, 'Sorry, Phone number has already been registered')
                return redirect('RegisterReferredUser')
        
            elif checkUserEmail:
                messages.error(request, 'Sorry, email address has already been registered')
                return redirect('RegisterReferredUser')
        
            else:
                form = LaunchRegistrants(fullname=fullname, email=email, phonenumber=phonenumber, referralcode=referralcode, referercode = referrer)
                user = User.objects.create_user(username=email, email=email, password=referralcode, first_name=fullname, last_name=phonenumber)
                createReferralProfile = ReferralRecords(fullname = fullname,email = email,  numberOfReferrals = 0)
                referralURL = f'https://nysc.limestone.ng/register/{referralcode}'
                login(request, user)
                form.save()
                user.save()
                createReferralProfile.save()
                authUser = authenticate(request, username=email, password=referralcode)
                
                if authUser is not None:
                    # notificationEmail(request, email, fullname)
                    try:
                        notificationEmail(request, email, fullname, referralcode, referralURL)
                    except:
                        print('Registration mail was not sent successfully')
                    messages.success(request, 'Regitration was successful, kindly check your inbox for more information')
                    return redirect('Dashboard')
                else:
                    messages.success(request, 'Regitration was successful. Kindly check your inbox for more information')
                    return redirect('RegisterReferredUser')
    
    else:
        return redirect('HomePage')
    
    return render(request, 'onboardingapp/registerreferreduser.html')



def ReferralTable(request):
    UpdateAllReferrals(request)
    getAllRegistrantsReferralData = ReferralRecords.objects.all()
    getAllRegistrantsCount = LaunchRegistrants.objects.all().count()
    context = {'getAllRegistrantsReferralData':getAllRegistrantsReferralData, 'getAllRegistrantsCount':getAllRegistrantsCount}
    return render(request, 'onboardingapp/viewreferraltable.html', context)
    


def UpdateAllReferrals(request):
    try:        
        getAllRegistrants = LaunchRegistrants.objects.all()
        for registrant in getAllRegistrants:
            # if registrant.referralcode:
            getRegistrantReferrerCode = registrant.referralcode
            print(registrant.email)
            getAllRegistrantReferralsCount = LaunchRegistrants.objects.filter(referercode = getRegistrantReferrerCode).count()
            print(getAllRegistrantReferralsCount)
            getReferrer = LaunchRegistrants.objects.get(referralcode = getRegistrantReferrerCode)
            ReferralRecords.objects.filter(email = getReferrer.email).delete()
            form = ReferralRecords(fullname = getReferrer.fullname,email = getReferrer.email,  numberOfReferrals = getAllRegistrantReferralsCount)
            form.save()
        return redirect('ReferralTable')
    except:
        return redirect('ReferralTable')
        

# ReferralRecords