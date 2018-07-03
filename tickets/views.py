from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Sales
from django.utils import timezone
from datetime import datetime
from .uuid_create import dict_to_uuid
from .qr_create import create_qrcode
from .email_send import send_email

# Create your views here.


def index(request):
    return HttpResponse("Hello to the intial page for danjo'd version of the ticketing app.")


@login_required
def form_user(request):
    return render(request, 'form_sale.html', {'details': ''})

@login_required
def store_mail(request):
    if request.method == 'POST':
        name = request.POST['name']
        reg_no = request.POST['reg_no']
        mail_id = request.POST['mail_id']
        mobile_no = request.POST['phone']
        college = request.POST['college']
        pay_mode = request.POST['pay_mode']
        location_sale = request.POST['location']
        sale_type = request.POST['type']
        pch_name = str(request.user.first_name) + ' ' + str(request.user.last_name)
        date = timezone.now()
        customer = {
                     'name': name,
                     'reg_no': reg_no,
                     'mail_id': mail_id,
                     'mobile_no': mobile_no,
                     'college': college,
                     'pay_mode': pay_mode,
                     'location_sale': location_sale,
                     'sale_type': sale_type,
                     'pch_name': pch_name,
                     'date': date}
        uuid = dict_to_uuid(customer)
        sale_instance = Sales.objects.create(
                                              name=name,
                                              reg_no=reg_no,
                                              mail_id=mail_id,
                                              mobile_no=mobile_no,
                                              college=college,
                                              pay_mode=pay_mode,
                                              location_sale=location_sale,
                                              sale_type=sale_type,
                                              pch_name=pch_name,
                                              unique_id=uuid,
                                              time=date
                                            )
        create_qrcode(uuid)
        send_email(mail_id, uuid)
        return render(request, 'form_sale.html', {'mail_id': 'Email successfully sent to ' + str(mail_id)})


