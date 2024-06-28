from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Count
from django.contrib import messages
from django import template
import base64

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from .models import embvideo
@csrf_exempt
def homePage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        send_mail(name,message,'settings.EMAIL_HOST_USER',[email],fail_silently=False)
        print("okk")
    hidden_posts = Posts.objects.filter(Trending=1).order_by('-created_at')[:4] 
    pics = Posts.objects.filter(Trending=0).order_by('-created_at')[:12]  #slide images
    links = embvideo.objects.all()
    picts=Posts.objects.filter(Trending=0)
    categories = set(pic.category for pic in picts)

    # categories = (set(Posts.objects.values_list('category__category', flat=True)))  # Create a set of unique category names
    
    pictures = UploadedFile.objects.all().order_by('-id')[:8]
    videos = videofile.objects.all().order_by('-id')[:1]
    
    return render(request, 'app/index-2.html', {"categories": categories, "pics": pics, 'pictures': pictures, 'videos': videos, 'hidden_posts': hidden_posts,'links':links})


def categoryview(request,category):
    pics = Posts.objects.filter(Trending=0)
    categories = set(pic.category for pic in pics)
    hidden_posts=Posts.objects.filter(Trending=1).order_by('-created_at')[:4]
    if(Category.objects.filter(category=category,status=0)):
        post=Posts.objects.filter(category__category=category).order_by('-created_at')
        # category__postTitle= Category.objects.filter(category=category).first()
        return render(request,'categoryfiles/index.html',{'post':post,'category__category':category,'hidden_posts':hidden_posts,'categories':categories})
    else:
        messages.warning(request,"no such file")
        return redirect('index')   

from django.shortcuts import render, get_object_or_404
from .models import Posts

def single_post_details(request, post_id):
    pics = Posts.objects.filter(Trending=0)
    categories = set(pic.category for pic in pics)
    post = get_object_or_404(Posts, id=post_id)
    hidden_posts=Posts.objects.filter(Trending=1).order_by('-created_at')[:4]
    pictures = UploadedFile.objects.all().order_by('-id')[:8]
    
    trending=Posts.objects.filter(SinglePageTrending=1).order_by('-created_at')[:4]
    return render(request, "categoryfiles/singlepost_details.html", {'post': post,'categories':categories,'hidden_posts':hidden_posts,'pictures':pictures,'trending':trending})



def post_details(request, category, post_slug):
    # Filter posts and get unique categories
    pics = Posts.objects.filter(Trending=0)
    categories = set(pic.category for pic in pics)
    trending=Posts.objects.filter(SinglePageTrending=1).order_by('-created_at')[:4]
    # Retrieve hidden posts
    hidden_posts = Posts.objects.filter(Trending=1).order_by('-created_at')[:4]
    pictures = UploadedFile.objects.all().order_by('-id')[:8] 
    # Retrieve the post based on category and slug, filtering by status
    post = Posts.objects.filter(category__category=category, id=post_slug, Trending=0).first()

    # Check if post exists and status allows display
    if post:
        # Context dictionary with post details and potentially ads
        context = {
            'post': post,
            'adsimage': UploadedFile.objects.all(),
            'adsvideo': videofile.objects.all(),
            'hidden_posts': hidden_posts,
            'categories': categories,
            'pictures':pictures,
            'trending':trending
        }
        # Render the view_details1.html template with post details
        return render(request, "categoryfiles/view_details1.html", context)
    else:
        # If the post does not exist, redirect to singleimage view
        return redirect('singleimage', category=category, post_slug=post_slug)

def singleimage(request, category, post_slug):
    pics = Posts.objects.filter(Trending=0)
    categories = set(pic.category for pic in pics)
    hidden_posts = Posts.objects.filter(Trending=1).order_by('-created_at')[:4]
    # Retrieve the post
    post = get_object_or_404(Posts, category__category=category, id=post_slug, Trending=1)
    pictures = UploadedFile.objects.all().order_by('-id')[:8]
    trending=Posts.objects.filter(SinglePageTrending=1).order_by('-created_at')[:4]
    # Render the singleimage.html template with the post details
    return render(request, "categoryfiles/singleimage.html", {'post': post,'categories':categories,'hidden_posts':hidden_posts,'pictures':pictures,'trending':trending})



from django.contrib import messages
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                request.session['registration_successful'] = True
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'app/register.html')

@csrf_exempt  
def Login(request):
    if request.method == 'POST':#IF THE CONDITION IS TRUE IT SHOULD ENTER INTO THE IF CONDITION
       username = request.POST['username'] 
       password = request.POST['password']  

       user = auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request, user)
           print('login is successfully')
           return redirect('dash_board')
       else:
           print('invalid credentials')
           return redirect('login')
    else:
        return render(request,'app/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print("logged out successfully")
        return redirect('login')    
        
          



 


# =========================================================


def m(request):
        return render(request,"app/category.html")

def m1(request):
    pics = Posts.objects.filter(Trending=0)
    categories = set(pic.category for pic in pics)
   
    return render(request, "app/contact.html", {'categories':categories})



# def m2(request):
#         return render(request,"app/index.html")


def about(request):
    pics = Posts.objects.filter(Trending=0)
    categories = set(pic.category for pic in pics)
   
    return render(request, "app/about.html", {'categories':categories})

# ========================================================
@csrf_exempt
@login_required
def addcategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('addcat') 
        else:
            messages.error(request, 'error,please provide the correct details!')

    categories = Category.objects.all()  # Fetch all categories from the database
    context = {"form": form, "categories": categories}
    
    return render(request, 'main/add_category.html',context)


@login_required
def dashBoard(request):
    categorycount = Category.objects.count()
    subcategorycount = SubCategory.objects.count()
    postcount = Posts.objects.count()
    

    context = {'categorycount': categorycount, 'subcategorycount': subcategorycount, 'postcount': postcount}

    return render(request,'main/dashboard.html',context)



        


@login_required
def managecategory(request):
    eachproduct = Category.objects.all()
    show_popup = request.GET.get('showPopup', 'false').lower() == 'true'
    data = {
        'eachproduct' : eachproduct,'show_popup':show_popup
    }
    
    return render(request,'main/managecategory.html',data)
#update ===================
@login_required
@csrf_exempt
def Updatecategory(request,pk):
    eachproduct =Category.objects.get(id=pk)

    form = CategoryForm(instance=eachproduct)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=eachproduct)
        if form.is_valid():
            form.save()
            messages.success(request,"update successfully")
            return redirect('managecategory')
            
    context ={
        "form": form
    }
    
    return render(request,'main/updatecategory.html',context)

# Deleting the record from the database from the table, base on the primary key or unique key


@login_required


def deletecategory(request, pk):
    try:
        eachproduct = Category.objects.get(id=pk)
        eachproduct.delete() # 1=Deleted
      
    except Category.DoesNotExist:
        messages.error(request, "Category does not exist or already deleted")
    return redirect('deletesuccess')



def showcategory(request):
      return render(request,'main/showcategory.html')

# =====   *subcategory*  ===================================
@csrf_exempt
@login_required
def addsubcategory(request):
      form=SubCategoryForm()

      if request.method=='POST':
            form=SubCategoryForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"subcategory successfully added  ")
                return redirect('addsubcategory')
      categories = SubCategory.objects.all()  # Fetch all categories from the database
      context = {"form": form, "categories": categories}

      return render(request, 'main/add_subcategory.html',context)
@login_required
def managesubcategory(request):
    eachproduct = SubCategory.objects.all()
    data = {
        'eachproduct' : eachproduct
    }
    
    return render(request,'main/manage_subcategory.html',data)
#update ===================
@login_required
@csrf_exempt
def Updatesubcategory(request,pk):
    eachproduct =SubCategory.objects.get(id=pk)

    form = SubCategoryForm(instance=eachproduct)
    if request.method == "POST":
        form = SubCategoryForm(request.POST, request.FILES, instance=eachproduct)
        if form.is_valid():
            form.save()
            messages.success(request,"updatesubcategory successfully")
         
            return redirect('managesubcategory')
    context ={
        "form": form
    }
    
    return render(request,'main/updatesubcategory.html',context)


# Deleting the record from the database from the table, base on the primary key or unique key
@login_required
def deletesubcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    messages.success(request, "Deleted successfully")
    return redirect('deletesuccess')

#=====================POST==============================

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
@csrf_exempt

@login_required
def addpost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post added successfully!')
            return redirect('addpost')
        else:
            messages.error(request, 'Error adding post. Please correct the errors.')

    categories = Posts.objects.all()  # Fetch all categories from the database
    context = {"form": form, "categories": categories}
    
    return render(request, 'main/add_post.html', context)

@login_required
def managepost(request):
    eachproduct = Posts.objects.all()
    show_popup = request.GET.get('showPopup', 'false').lower() == 'true'
    data = {
        'eachproduct' : eachproduct,'show_popup':show_popup
    
    }
    
    return render(request,'main/manage_post.html',data)


#update ===================
# from django.urls import reverse
@csrf_exempt
@login_required
def Updatepost(request,pk):
    eachproduct =Posts.objects.get(id=pk)

    form = PostForm(instance=eachproduct)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=eachproduct)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Post added successfully!')
            return redirect('updatepost',pk=pk)
        else:
            messages.error(request, 'Error adding post. Please correct the errors.')
            
    context ={
        "form": form
    }
    
    return render(request,'main/updatepost.html',context)

# Deleting the record from the database from the table, base on the primary key or unique key
@login_required
def deletepost(request,pk):
    eachproduct =Posts.objects.get(id=pk)
    eachproduct.delete() # 1=Deleted
    
    return redirect('deletesuccess')

def deletesuccess(request):
    return render(request,'main/delete_post.html')


# ===============================upload===========
@csrf_exempt
@login_required
def addupload(request):
    form = UploadedFileForm()

    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"added succesfully")
            return redirect('addupload')

    categories = UploadedFile.objects.all()  # Fetch all categories from the database
    context = {"form": form, "categories": categories}
    
    return render(request, 'main/addupload.html', context)
@login_required
def manageupload(request):
    eachproduct = UploadedFile.objects.all()
    context = {
        'eachproduct' : eachproduct
    }
    
    return render(request,'main/manageupload.html',context)
@csrf_exempt
@login_required
def Updateupload(request,pk):
    eachproduct =UploadedFile.objects.get(id=pk)

    form = UploadedFileForm(instance=eachproduct)
    if request.method == "POST":
        form = UploadedFileForm(request.POST, request.FILES, instance=eachproduct)
        if form.is_valid():
            form.save()
            messages.success(request,"updated succesfully")
            return redirect('manageupload')
    context ={
        "form": form
    }
    
    return render(request,'main/updateupload.html',context)

# Deleting the record from the database from the table, base on the primary key or unique key
@login_required
def deleteupload(request,pk):
    eachproduct =UploadedFile.objects.get(id=pk)
    eachproduct.delete() # 1=Deleted
  

    return redirect('deletesuccess')

@csrf_exempt
@login_required
def addvideo(request):
    form = videoFileForm()

    if request.method == 'POST':
        form = videoFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"added succesfully")
            return redirect('addvideo')

    categories = videofile.objects.all()  # Fetch all categories from the database
    context = {"form": form, "categories": categories}
    
    return render(request, 'main/addvideo.html', context)
@login_required
def managevideo(request):
    eachproduct = videofile.objects.all()
    context = {
        'eachproduct' : eachproduct
    }
    
    return render(request,'main/managevideo.html',context)
@csrf_exempt
@login_required
def Updatevideo(request,pk):
    eachproduct =videofile.objects.get(id=pk)

    form = videoFileForm(instance=eachproduct)
    if request.method == "POST":
        form = videoFileForm(request.POST, request.FILES, instance=eachproduct)
        if form.is_valid():
            form.save()
            messages.success(request,"updated succesfully")
            return redirect('managevideo')
    context ={
        "form": form
    }
    
    return render(request,'main/updatevideo.html',context)

# Deleting the record from the database from the table, base on the primary key or unique key
@login_required
def deletevideo(request,pk):
    eachproduct = videofile.objects.get(id=pk)
    eachproduct.delete() # 1=Deleted
   

    return redirect('deletesuccess')
    
    
@csrf_exempt
@login_required
def addlink(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        evideo_url = request.POST.get('evideo')
        description = request.POST.get('description')
        if title and evideo_url and description:  
            embvideo.objects.create(title=title, link=evideo_url, description=description)
            messages.success(request,"added succesfully")
            return redirect('addlink')
    return render(request, 'main/addlink.html')
@login_required
@csrf_exempt
def Updatelink(request, pk):
    instance = get_object_or_404(embvideo, id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        evideo_url = request.POST.get('evideo')
        description = request.POST.get('description')
        if title and evideo_url and description:  
            instance.title = title
            instance.link = evideo_url
            instance.description = description
            instance.save()
            messages.success(request,"updated succesfully")
            return redirect('updatelink',pk=pk)
    return render(request, 'main/updatelink.html', {'instance': instance})
    
def deletelink(request, pk):
    instance = get_object_or_404(embvideo, id=pk)
    instance.delete()
  
    return redirect('deletesuccess')

@login_required
def managelink(request):
    instances = embvideo.objects.all()
    return render(request, 'main/managelink.html', {'instances': instances})

def change_password(request):
        if request.method=='POST':
                form= PasswordChangeForm(user=request.user,data=request.POST)
                if form.is_valid():
                        form.save()
                        update_session_auth_hash(request,form.user)
                        print("okkk")
                        return redirect('login')
        else:
                form=PasswordChangeForm(user=request.user)
                print("no")
        return render(request,'main/change_password.html',{'form':form})

