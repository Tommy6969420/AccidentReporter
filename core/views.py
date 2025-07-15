from django.shortcuts import render
from.models import AccidentReport
# Create your views here.
def index(request):
    if request.method == 'POST':
        datetime = request.POST.get('datetime')
        report= request.POST.get('report')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        urgency = request.POST.get('urgency')
        try:
            AccidentReport.objects.create(
            datetime=request.POST.get('datetime'),
            report=report,
            latitude=latitude,
            longitude=longitude,
            urgency=urgency
        )
            
        except Exception as e:
            print(f"Error creating AccidentReport: {e}")
            return render(request, 'core/index.html', {'error': 'Failed to create report.'})
        context =  {
            'report': report,
            'latitude': latitude,
            'longitude': longitude,
            'urgency': urgency,
            
        }
        return render(request, 'core/index.html',context)

    return render(request, 'core/index.html')
def reports(request):
    reports = AccidentReport.objects.all().order_by('-datetime')

    context = {
        'reports': reports

    }
    return render(request, 'core/reports.html', context)