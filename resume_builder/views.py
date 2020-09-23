from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .utils import *
from django.views.generic import View
from django.template.loader import get_template


# Create your views here.


def resume_form(request):
    context = {}
    return render(request, 'resume_builder/resume_form.html', context)


def resume(request, pk):
    resume = Resume.objects.get(id=pk)
    context = {'resume': resume}
    return render(request, 'resume_builder/resume.html', context)


def download_pdf(request):
    # get the end user's resume
    device_id = uuid.UUID(request.COOKIES['device'])
    current_user = get_end_user(request.user, device_id)
    resume = Resume.objects.get_or_create(end_user=current_user)[
        0]  # remove the tuple
    template = get_template('pdf/resume_1.html')
    context = {
        'resume': resume
    }
    html = template.render(context)
    pdf = render_to_pdf('pdf/resume_1.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Resume.pdf"
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")
