import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def home(request):
    return render(request, "hello/home.html")

def about(request):
    driver = webdriver.Chrome()
    driver.get("https://autodocxsystem.by/")
    assert "Super Inform Soft" in driver.title
    logform = driver.find_element(By.ID, "LogForm")
    inputname = driver.find_element(By.ID, "name")
    submitbtn = driver.find_element(By.ID, "submit")
    inputname.send_keys("Chief Creator")
    submitbtn.click()

    driver.close()
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template("hello/all_members.html")
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))