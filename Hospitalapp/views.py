from django.shortcuts import render
from .models import Homes,Branch,Gallery,Blog,Package
from .forms import HomesForm
# Create your views here.
def Home(request):
    homes=Homes.objects.all()
    if request.method=="POST": 
        names=request.POST.get('names','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        message=request.POST.get('message','')       
        enq=Homes(names=names,email=email,number=number,message=message)
        enq.save()
    return render(request,'index.html',{"homes":homes})





def about(request):

    return render(request,'about.html')


def test(request):
    return render(request,'test.html')

def package(request):
    pack=Package.objects.all()
    return render(request,'package.html',{"pack":pack})



def packages(request,id):
    packs=Package.objects.get(id=id)
    return render(request,'packages.html',{'packs':packs})





def blog(request):
    blogs=Blog.objects.all()
    return render(request,'blog.html',{"blogs":blogs})


def blogpage(request):
    blog=Blog.objects.all()
    return render(request,'blogpage.html',{"blog":blog})


def blogpage1(request):
    blog1=Blog.objects.all()
    return render(request,'blogpage1.html',{"blog1":blog1})





def gallery(request):
    gallerys=Gallery.objects.all()
    return render(request,'gallery.html',{'gallerys':gallerys})



def branches(request):
    branch=Branch.objects.all()
    return render(request,'branches.html',{"branch":branch})



def branchplace(request,id):
    branchs=Branch.objects.get(id=id)
    return render(request,'branchplace.html',{'branchs':branchs})



def contacts(request):
    return render(request,'contacts.html')



def appointment(request):
    return render(request,'appointment.html')