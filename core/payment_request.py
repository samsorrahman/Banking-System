from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal
from core.models import Notification, Transaction
from decimal import Decimal

@login_required
def SearchUsersRequest(request):
    account = Account.objects.all() ## all the account in my db
    query = request.POST.get("account_number") ## <input name="account_number">

    if query:
        account = account.filter(
            Q(account_number=query)|
            Q(account_id=query)

        ).distinct()
    
    context = {
        "account": account,
        "query": query,
    }
    return render(request, "payment_request/search-users.html", context)