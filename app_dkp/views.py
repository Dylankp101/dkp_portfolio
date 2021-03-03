from django.shortcuts import render, redirect
def headpage(request):
    return render(request, "frontpage.html")