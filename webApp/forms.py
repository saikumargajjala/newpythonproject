from django import forms

from ckeditor.widgets import CKEditorWidget
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude=['created_at']
        fields = ['category','categoryDescription','status','created_at']

        widgets ={
            'category': forms.TextInput(attrs ={'class':'form-control ','style': 'margin-bottom: 50px;'}),
            # 'images': forms.FileInput(attrs ={'class':'form-control ','style': 'margin-bottom: 10px;'}),
            'categoryDescription': forms.Textarea(attrs ={'class' : 'form-control','style': 'margin-bottom: 10px;'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-bottom: 10px;'}),
            'created_at': forms.FileInput(attrs ={'class':'form-control ','style': 'margin-bottom: 10px;'}),
            
            
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category','subcategory','subcategoryDescription']

        widgets ={
            'category': forms.Select(attrs = {'class' :'form-control','style': 'margin-bottom: 50px;'}),
            'subcategory' : forms.TextInput(attrs ={'class':'form-control','style': 'margin-bottom: 40px;'}),
            'subcategoryDescription': forms.Textarea(attrs ={'class' :'form-control','style': 'margin-bottom: 40px;'}),
            
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['postTitle', 'category', 'subcategory', 'image', 'SinglePageTrending', 'Trending', 'postdetails']
        widgets = {
            'postTitle': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 30px;'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 30px;'}),
            'subcategory': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 30px;'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 30px;'}),
            'SinglePageTrending': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-bottom: 30px;'}),
            'Trending': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-bottom: 30px;'}),
            'postdetails': CKEditorWidget(attrs={'class': 'form-control', 'style': 'margin-bottom: 100px;'})
        }



        label_attrs = {
            'postdetails': {'style': 'margin-top:500px;'}  # Adjust the style as needed
        }
class UploadedFileForm(forms.ModelForm):
    class Meta:
        model= UploadedFile
        fields= ["Image"]

        widgets ={  
            'Image': forms.FileInput(attrs ={'class' : 'form-control'}),
            
        }

class videoFileForm(forms.ModelForm):
    class Meta:
        model= videofile
        fields= ["video"]

        widgets ={  
            
            'video': forms.FileInput(attrs ={'class':'form-control'}),
        }
        
# from embed_video.fields import EmbedVideoField

# class embForm(forms.ModelForm):
#     class Meta:
#         model= embvideo
#         fields= ['id',"title",'link','description']
#         widgets={
#       'title': forms.TextInput(attrs={'class': 'form-control'}),
#         'link': forms.TextInput(attrs={'class': 'form-control'}),
#         'description': forms.Textarea(attrs={'class': 'form-control'}),}