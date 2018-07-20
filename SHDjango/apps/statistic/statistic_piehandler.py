from django.shortcuts import render


def PieHandler(request):
    return render(request, "pie.html")