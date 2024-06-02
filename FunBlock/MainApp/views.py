import os
import zipfile
import io
from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.shortcuts import redirect

# from .models import Tile

# Create your views here.


def home(request):
    return render(request, "home.html")


def download_file(request):
    file_path = "path_to_folder/FunBlock/FunBlockInstaller.exe"
    response = FileResponse(
        open(file_path, "rb"), content_type="application/octet-stream"
    )
    response["Content-Disposition"] = 'attachment; filename="FunBlockInstaller.exe"'
    return response


def dynmap_view(request):
    return redirect(
        "http://54.38.236.174:9804/?worldname=FunWorld&mapname=surface&zoom=1&x=-994&y=64&z=-1958"
    )


def download_mods(request):
    # Create a BytesIO object for storing the zip file in memory
    in_memory = io.BytesIO()

    # Create a ZipFile object
    zip = zipfile.ZipFile(in_memory, "w")

    # List of all files to be downloaded
    files = [
        "path_to_folder/FunBlock/mods/curse_mods_list.json",
        "path_to_folder/FunBlock/mods/soccermod-0.1-1.20.1.jar",
        "path_to_folder/FunBlock/mods/version.txt",
    ]

    # Add each file to the zip file
    for file in files:
        zip.write(file, arcname=os.path.basename(file))

    # Close the ZipFile object
    zip.close()

    # Move the cursor of the BytesIO object to the beginning
    in_memory.seek(0)

    # Create a FileResponse object with the BytesIO object and the appropriate headers
    response = FileResponse(in_memory, as_attachment=True, filename="mods.zip")
    response["Content-Type"] = "application/zip"

    return response


def download_launcher(request):
    # Get a list of all files in the /update directory
    files = os.listdir("path_to_folder/FunBlock/update")

    # Find the .exe file
    for file in files:
        if file.endswith(".exe"):
            exe_file = file
            break
    else:
        return HttpResponse("No .exe file found", status=404)

    # Create a FileResponse object with the .exe file and the appropriate headers
    file_path = os.path.join(
        "path_to_folder/FunBlock/update",
        exe_file,
    )
    response = FileResponse(
        open(file_path, "rb"), as_attachment=True, filename=exe_file
    )
    response["Content-Type"] = "application/octet-stream"

    return response
