from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import FileManagementForm
from .models import File_uploading
# Create your views here.
def file_upload(request):
    if request.method == 'POST':
        data = FileManagementForm(request.POST, request.FILES)

        if data.is_valid():
            data.save()
            return redirect('file_list')

    else:

     data = FileManagementForm()
     
    return render(request,'upload.html',{'form':data})

def file_list(request):
   files = File_uploading.objects.all()

   return render(request,'file_list.html',{'files':files})

def download_file(request,id):
   obj = File_uploading.objects.get(id=id)

   file_path = obj.file.path
   return FileResponse(open(file_path,'rb'),as_attachment=True)