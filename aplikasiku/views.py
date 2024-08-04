import os
from django.http import HttpResponse
from django.shortcuts import render
import subprocess

def jalankan_streamlit(script_path):
    command = f"streamlit run {script_path}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output

def tampilkan_halaman_lingkaran(request):
    output = jalankan_streamlit("aplikasiku/lingkaran.py")
    return HttpResponse(output)

def tampilkan_halaman_batang(request):
    output = jalankan_streamlit("aplikasiku/batang.py")
    return HttpResponse(output)

def tampilkan_halaman_garis(request):
    output = jalankan_streamlit("aplikasiku/garis.py")
    return HttpResponse(output)

def halaman_utama(request):
    return render(request, 'halaman_utama.html')
