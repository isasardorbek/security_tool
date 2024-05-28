# scan/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .scanner import scan_code

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def scan_view(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        vulnerabilities = scan_code(code)
        return JsonResponse({'vulnerabilities': vulnerabilities})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
