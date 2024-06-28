from django.db import models
import datetime
from ckeditor.fields import RichTextField
import os
from ckeditor_uploader.fields import RichTextUploadingField


def getFileName(request,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)

class Category(models.Model):
          category=models.CharField(max_length=300)
        #   images=models.ImageField(upload_to=getFileName,null=True,blank=True)
          categoryDescription=models.TextField()
          status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
          created_at=models.DateTimeField(auto_now_add=True)
 
          
          def __str__(self):
                  return self.category

class SubCategory(models.Model):
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        subcategory=models.CharField(max_length=300)
        subcategoryDescription=models.TextField()

        def __str__(self):
                return self.subcategory


class Posts(models.Model):
        postTitle=models.CharField(max_length=200,null=False,blank=False)
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
        created_at=models.DateTimeField(auto_now_add=True,blank=True)
        image=models.ImageField(upload_to=getFileName,null=True,blank=True)
        Trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
        SinglePageTrending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
        postdetails=RichTextUploadingField(blank=True,null=True)
      
       

        def __str__(self):
                return self.postTitle



class UploadedFile(models.Model):
        
        Image= models.ImageField(upload_to='uploads/',null=False,blank=False)
        

        def __str__(self):
           return str(self.Image)
    
class videofile(models.Model):
    video= models.FileField(upload_to='videos/', null=True)

    def __str__(self):
        return str(self.video) 
        
from embed_video.fields import EmbedVideoField
class embvideo(models.Model):
      title=models.CharField(max_length=400,null=True,blank=True)
      link= EmbedVideoField()
      description=models.TextField()
      def __str__(self):
        return str(self.link)
