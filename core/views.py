from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        report= request.POST.get('report')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        context =  {
            'report': report,
            'latitude': latitude,
            'longitude': longitude
        }
        return render(request, 'core/index.html',context)

    return render(request, 'core/index.html')