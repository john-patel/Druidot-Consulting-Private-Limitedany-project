from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from PIL import Image
import pytesseract
from datetime import datetime, timezone
import time
import os
from django.http import HttpResponse
from django.contrib import messages



def myFunc(request):
    return render(request,'index.html')


# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             image = form.cleaned_data['image']
#             scheduled_time = form.cleaned_data['scheduled_time']
#             print(scheduled_time)
#             extracted_text = extract_text_from_image(image)  # Extract text using Pytesseract

            

#             form = ImageUploadForm()
#             return render(request, 'upload.html', {'success': 'File uploaded successfully', 'extracted_text': extracted_text})
#             # return redirect('upload',{'success' : 'File uploaded succesfully'})  # Redirect to a success page
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload.html', {'form': form})

# def extract_text_from_image(image):
#     # Open the image using Pillow
#     image_pil = Image.open(image)   
#     pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
#     # Apply OCR using Pytesseract
#     extracted_text = pytesseract.image_to_string(image_pil)
#     # print(extracted_text)
#     if '\n' in extracted_text:
#         extracted_text = extracted_text.replace('\n','<br>')
#         print(extracted_text)
#     else : 
#         print('i am else code')
#     return extracted_text

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = form.cleaned_data['image']
            scheduled_time = form.cleaned_data['scheduled_time']
            if scheduled_time == None :
                pass
            else :
                time_schudeler(scheduled_time)
            
            extracted_text = extract_text_from_image(image)  # Extract text using Pytesseract

            form = ImageUploadForm()
            # Generate and download the text file
            response = HttpResponse(content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="extracted_text.txt"'
            response.write(extracted_text)
            # Display success message on the page
            messages.success(request, 'File uploaded successfully!')
            
            return response
        

            # return render(request, 'upload.html', {'success': 'File uploaded successfully', 'extracted_text': extracted_text})
            # return redirect('upload',{'success' : 'File uploaded successfully'})  # Redirect to a success page
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def extract_text_from_image(image):
    # Open the image using Pillow
    image_pil = Image.open(image)   
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    # Apply OCR using Pytesseract
    extracted_text = pytesseract.image_to_string(image_pil)
    # print(extracted_text)
    # if '\n' in extracted_text:
    #     extracted_text = extracted_text.replace('\n','<br>')
    #     print(extracted_text)
    # else : 
    #     print('i am else code')
    return extracted_text

def time_schudeler(scheduled_time):
    # Get the current time
    current_time = datetime.now(timezone.utc)

    # Calculate the time difference between current time and scheduled time
    time_difference = scheduled_time - current_time

    # Convert the time difference to seconds
    time_difference_seconds = time_difference.total_seconds()

    if time_difference_seconds > 0:
        # Sleep for the remaining time until the scheduled time
        time.sleep(time_difference_seconds)

