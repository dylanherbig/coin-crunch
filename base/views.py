# Create your views here.

from curses.ascii import HT
from email.mime import base
from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile

# from rest_framework.response import Response
import requests
import json 


# Create your views here.

base_url = "https://api-sandbox.circle.com/v1/"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer QVBJX0tFWTo1OTliODk4YTUxYTlhYmRiNjgwYjdiNWRkN2I0ZmY2MDo0ODljNWYxZTUwNDE4ZjE3ZThlNmI5M2MyZjNmMjIwMA",
}

def index(request):

    url = base_url + "ping"
    response = requests.request("GET", url, headers=headers)

    return HttpResponse(response)

def configuration(request):
    url = base_url + "configuration"
    response = requests.request("GET", url, headers=headers)

    return HttpResponse(response)

def balances(request):
    url = base_url + "businessAccount/balances"
    response = requests.request("GET", url, headers=headers)

    return HttpResponse(response)

def getUserWallet(request):
    profile = Profile.objects.get(user=request.user)
    url = base_url + "wallets/" + str(profile.walletId)

    response = requests.request("GET", url, headers=headers)

    return HttpResponse(response.text)

def createBlockchainAddress(request):
    profile = Profile.objects.get(user=request.user)

    url = base_url + "wallets/" + str(profile.walletId) + "/addresses"
    headers["Content-Type"] = "application/json"

    payload = {
        "idempotencyKey": profile.id,
        "currency": "USD",
        "chain": "ETH"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    dict = json.loads(response.text)

    profile.blockChainAddress = dict['data']['address']

    profile.save()

    return HttpResponse(response.text)

def createTransfer(request):
    profile = Profile.objects.get(user=request.user)

    url = base_url + "transfers"
    headers["Content-Type"] = "application/json"


    payload = {
        "source": {
            "type": "wallet",
            "id": profile.walletId
        },
        "destination": {
            "type": "wallet",
            "id": "12345"
        },
        "amount": {
            "amount": "3.14",
            "currency": "USD"
        },
        "idempotencyKey": profile.id
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return HttpResponse(response.text)    

def createWallet(request):
    url = base_url + "wallets/"
    headers["Content-Type"] = "application/json"

    profile = Profile.objects.get(user=request.user)

    payload = {
        "description": "Treasury Wallet",
        "idempotencyKey": profile.id,
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    dict = json.loads(response.text)

    profile.walletId = dict['data']['walletId']
    profile.entityId = dict['data']['entityId']

    profile.save()
    
    return HttpResponse(response.text)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiZGhwMnJwZSIsImEiOiJjbDI0enpvbnowMHc2M2JvNTdkZnMxNjViIn0.jMXoAk9xqZfs_-4U_bQpDg'
    return render(request, 'mapPage.html', 
                  { 'mapbox_access_token': mapbox_access_token })
