from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from myapp.models import Image

# Create your views here.


def home(request):
    images = Image.objects.all()
    li = list(images)
    image_list = []
    l1,l2,l3 = [], [], []
    for i in li:
        if len(l1) == len(l2) and len(l1) == len(l3):
            l1.append(i)
        elif len(l1) > len(l2) and len(l2) == len(l3):
            l2.append(i)
        elif len(l1) == len(l2) and len(l2) > len(l3):
            l3.append(i)
    image_list.append(l1)
    image_list.append(l2)
    image_list.append(l3)
    print(image_list)
    context = {"images_list": image_list}
    return render(request, "home.html", context)


def image(request, id):
    if request.method == "GET":
        img = Image.objects.get(id=id)
        context = {"name": img.name, "url": img.url, "id":id}
        return render(request, "image.html", context)
    elif request.method == "POST" and 'save_images' in request.POST:
        img = Image.objects.get(id=id)
        img.name = request.POST["name"]
        img.url = request.POST["url"]
        img.save()
        return redirect("home")
    return redirect("home")


def delete_image(request, id):
    img = Image.objects.get(id=id)
    img.delete()
    return redirect("home")


def add_images(request):
    if request.method == "GET":
        template = loader.get_template("add_images.html")
        return HttpResponse(template.render())
    elif request.method == "POST":
        img = Image(name=request.POST["name"],
                    url=request.POST["url"])
        img.save()
        return redirect("home")
    return redirect("home")