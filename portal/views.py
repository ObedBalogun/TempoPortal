from django.shortcuts import render, get_object_or_404
from .models import VisitRequests,Visitor,Staff
from .forms import VisitorsForm
import secrets
from sendgrid.helpers.mail import Email,Content,Mail
import sendgrid
from django.utils.translation import ugettext as _
from django.contrib import messages

# Create your views here.
def formpage(request):
    if request.method =="POST":
        req = VisitRequests.objects.all().order_by('-timestamp')
        token=secrets.token_urlsafe(20)     
        visitor_name = request.POST.get("visitor_name")
        staff_id = request.POST.get('staff')
        time=request.POST.get('time_in')
        visit_type = request.POST.get("visit_type")
        comment = request.POST.get("comment")
        staff = Staff.objects.get(id=staff_id)
        staff_email = staff.staff_email
        visitor = Visitor.objects.create(visitor_name=visitor_name)
        visit_request = VisitRequests.objects.create(staff=staff, visitor=visitor, comment=comment, token=token,
                                                     status=None,timestamo=time,visit_type=visit_type)

        link = "http://192.168.1.179/portal/approval/" + staff_id + "/" + token
        visit_content = 'You have a waiting visitor' + '\n' + 'Name:' + visitor_name + '\n' + 'Purpose Of Visit:' + visit_type + '\n' + 'Additional Comment:' + comment + '\n' + link
        from_email = Email("Tempo_security@tempong.com")
        to_email = Email(staff_email)
        subject = visitor_name
        content = Content("text/plain", visit_content)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.headers)
        if response.status_code == 200:
            messages.add_message(request, messages.SUCCESS, _('Mail sent'))
        elif response.status_code == 202:
            messages.add_message(request, messages.SUCCESS, _('Mail sent for processing'))
        else:
            messages.add_message(request, messages.ERROR, _('Mail not sent'))
        return render(request, 'portal/all_requests.html', {'requests': req,})
    else:
        form = VisitorsForm()
        context = {'form': form}
        return render(request, 'portal/formpage.html', context)

def approval(request,staff_id,token):
    staff = Staff.Objects.get(id=staff_id)
    if request.method == 'POST':
        if request.POST.get('request_action') == '1':
            visit_requests = VisitRequests.objects.get(token=token)
            visit_requests.status = True
            visit_requests.save()
            requests = VisitRequests.objects.filter(staff=staff).order_by('-timestamp')
            context = {
                'requests': requests,
                'staff': staff,
            }
            return render(request, 'portal/staff_requests.html', context)

        elif request.POST.get('request_action') == '2':
            visit_requests=Visitor.objects.get(token=token)
            visit_requests.status = False
            visit_requests.save()
            requests = VisitRequests.objects.filter(staff=staff).order_by('-timestamp')
            context = {
                'requests': requests,
                'staff': staff,
            }
            return render(request, 'portal/staff_requests.html', context)
    requests=VisitRequests.objects.filter(token=token)
    context={
        'requests':requests,
        'staff': staff,
    }
    return render(request, 'portal/staff_requests.html',context)

def all_requests(request):
    requests = VisitRequests.objects.all().order_by('-timestamp')
    context = {
        'requests':requests
    }
    return render(request, 'portal/all_requests.html', context)

def requests(request,staff_id):
    staff=get_object_or_404(Staff, id=staff_id)
    visitors=Visitor.objects.all()

    requests = VisitRequests.objects.filter(staff=staff)
    context = {
        'staff': staff,
        'requests': requests,
        'visitors':visitors
    }
    return render(request, 'portal/requests.html',context)

