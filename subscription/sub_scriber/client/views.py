from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from writer.models import Article

from . models import Subscription

from account.models import CustomUser

from . paypal import *

@login_required(login_url='my-login')
def client_dashboard(request):

    try:
        subDetails = Subscription.objects.get(user=request.user)
        subscription_plan = subDetails.subscription_plan
        context = {'SubPlan': subscription_plan}     
        return render(request, 'client/client-dashboard.html', context)
    except:
        subscription_plan = "None"
        context = {'SubPlan': subscription_plan}
        return render(request, 'client/client-dashboard.html', context)

@login_required(login_url='my-login')
def browse_articles(request):

    try:
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
    except:
        return render(request, 'client/subscription-locked.html')
    
    current_subscription_plan = subDetails.subscription_plan

    if current_subscription_plan == 'Standard':
        articles = Article.objects.all().filter(is_premium=False)
    elif current_subscription_plan == 'Premium':
        articles = Article.objects.all()

    context = {'AllClientArticles': articles}
    return render(request, 'client/browse-articles.html', context)

@login_required(login_url='my-login')
def subscription_locked(request):
    
    return render(request, 'client/subscription-locked.html')

@login_required(login_url='my-login')
def subscription_plans(request):

    return render(request, 'client/subscription-plans.html')

@login_required(login_url='my-login')
def account_management(request):

    try:
        subDetails = Subscription.objects.get(user=request.user)
        subscription_id = subDetails.paypal_subscription_id
        context = {'SubscriptionID': subscription_id}
        return render(request, 'client/account-management-client.html', context)
    except:
        return render(request, 'client/account-management-client.html')

@login_required(login_url='my-login')
def create_subscription(request, subID, plan):

    custom_user = CustomUser.objects.get(email=request.user)

    firstName = custom_user.first_name
    lastName = custom_user.last_name

    fullName = firstName + " " + lastName

    selected_sub_plan = plan
    paypalID = subID

    if selected_sub_plan == "Standard":
        sub_cost = "4.99"
    elif selected_sub_plan == "Premium":
        sub_cost = "9.99"

    subscription = Subscription.objects.create(
    subscriber_name = fullName,
    subscription_plan = selected_sub_plan,
    subscription_cost = sub_cost,
    paypal_subscription_id = paypalID,
    is_active = True,
    user = request.user)

    context = {'SubscriptionPlan': selected_sub_plan}
    return render(request, 'client/create-subscription.html', context)
    
@login_required(login_url='my-login')
def delete_subscription(request, subID):

    # Delete subscription from PayPal
    access_token = get_access_token()
    cancel_subscription_paypal(access_token, subID)

    # Delete a subscription from Django (application side)
    subscription = Subscription.objects.get(user=request.user, paypal_subscription_id=subID)
    subscription.delete()

    return render(request, 'client/delete-subscription.html')

@login_required(login_url='my-login')
def update_subscription(request, subID):
    
    access_token = get_access_token()
    approve_link = update_subscription_paypal(access_token,subID)
    if approve_link:
        return redirect(approve_link)
    else:
        return HttpResponse("Unable to comply, approval link missing")

@login_required(login_url='my-login')
def paypal_update_sub_confirmed(request):

    try:
        sub_details = Subscription.objects.get(user=request.user)
        subID = sub_details.paypal_subscription_id
        context = {'SubscriptionID': subID}
        return render(request, 'client/paypal-update-sub-confirmed.html', context)
    except:
        return render(request, 'client/paypal-update-sub-confirmed.html')
    
@login_required(login_url='my-login')
def django_update_sub_confirmed(request, subID):

    access_token = get_access_token()
    current_plan_id = get_current_subscription(access_token, subID)

    if current_plan_id == 'P-2RU37377SR376025BM35NZGQ':
        new_plan_name = 'Standard'
        new_cost = "4.99"
        Subscription.objects.filter(paypal_subscription_id=subID).update(subscription_plan=new_plan_name, subscription_cost=new_cost)
    elif current_plan_id == ' P-4HF936665H352344KM35OBIY':
        new_plan_name = 'Premium'
        new_cost = "9.99"
        Subscription.objects.filter(paypal_subscription_id=subID).update(subscription_plan=new_plan_name, subscription_cost=new_cost)

    return render(request, 'client/django-update-sub-confirmed.html')
    