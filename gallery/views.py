from django.shortcuts import render
from django.http  import HttpResponse
from . models import Image,Location,Category

# Create your views here.
def welcome(request):
    
    image=Image.objects.all()
    return render(request,'index.html',{'image':image})

def search_results(request):
    # print("searched_images")
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        print("searched_images")
        message = f"{search_term}"

        return render(request, 'all-apps/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-apps/search.html',{"message":message})

def display_image(request,image_id):
    try:
        image=Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"welcome.html", {"image":image}) 

def display_category(request):
    
        category=Category.objects.all()
        image=Image.objects.all()
       
    
        return render(request,'all-apps/category.html',{'category':category, 'image':image}) 
            