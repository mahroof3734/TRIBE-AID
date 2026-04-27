from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def log_out(request):
    request.session['lid'] = ''
    return HttpResponse('''<script>alert("Log out");window.location="/myapp/login/"</script>''')


def login(request):
    return render(request, 'login_index.html')


def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    l = Login.objects.filter(username=username, password=password)
    if l.exists():
        l2 = Login.objects.get(username=username, password=password)
        request.session['lid'] = l2.id
        if l2.type == 'admin':
            return HttpResponse('''<script>alert("login success");window.location="/myapp/admin_home/"</script>''')
        elif l2.type == 'districtofficer':
            return HttpResponse('''<script>alert("login success");window.location="/myapp/district_home/"</script>''')
        elif l2.type == 'councilor':
            return HttpResponse('''<script>alert("login success");window.location="/myapp/counciler_home/"</script>''')

        else:
            return HttpResponse('''<script>alert("invalid user");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("invalid username and password");window.location="/myapp/login/"</script>''')


def admin_home(request):
    if request.session['lid']=='':
        return redirect("/myapp/login/")
    else:
        return render(request, 'admin/admin_index.html')


def add_district(request):
    if request.session['lid']=='':
        return redirect("/myapp/login/")
    else:
        return render(request, 'admin/add_district_officer.html')


def add_district_post(request):
    if request.session['lid']=='':
        return redirect("/myapp/login/")
    else:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        phone = request.POST['textfield3']
        gender = request.POST['RadioGroup1']
        DOB = request.POST['textfield4']
        photo = request.FILES['textfield5']
        place = request.POST['textfield6']
        post = request.POST['textfield7']
        pin = request.POST['textfield8']
        district = request.POST['textfield9']
        workingdistrict = request.POST['textfield11']
        state = request.POST['textfield10']

        dt = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(dt, photo)
        path = fs.url(dt)

        import random

        l = Login()
        l.username = email
        l.password = random.randint(0000, 9999)
        l.type = 'districtofficer'
        l.save()

        a = District_officer()
        a.name = name
        a.email = email
        a.phone = phone
        a.gender = gender
        a.dob = DOB
        a.photo = path
        a.place = place
        a.post = post
        a.pin = pin
        a.district = district
        a.workingdistrict = workingdistrict
        a.state = state
        a.LOGIN = l
        a.save()

        return HttpResponse('''<script>alert("success");window.location="/myapp/admin_home/"</script>''')


def add_package(request):
    if request.session['lid'] == '':
         return redirect("/myapp/login/")
    else:
           return render(request, 'admin/add_package.html')


def add_package_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        name = request.POST['textfield']
        type = request.POST['select']
        description = request.POST['textfield3']
        amount = request.POST['textfield2']

        b = Package()
        b.name = name
        b.type = type
        b.description = description
        b.amount = amount
        b.save()

        return HttpResponse('''<script>alert("success");window.location="/myapp/admin_home/"</script>''')


def allocate_package(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        e = Package.objects.all()
        return render(request, 'admin/allocate_package.html', {'data': e})


def allocate_package_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        district = request.POST['select']
        package = request.POST['select2']
        alloted_amount = request.POST['textfield']

        f = Allocate_package()
        f.district = district
        f.date = datetime.now().today()
        f.alloted_amount = alloted_amount
        f.PACKAGE_id = package
        f.save()
        return HttpResponse('''<script>alert("success");window.location="/myapp/admin_home/"</script>''')


def edit_district(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        data = District_officer.objects.get(id=id)
        return render(request, 'admin/edit district officer.html', {'data': data})


def edit_district_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        phone = request.POST['textfield3']
        gender = request.POST['RadioGroup1']
        DOB = request.POST['textfield4']
        place = request.POST['textfield6']
        post = request.POST['textfield7']
        pin = request.POST['textfield8']
        district = request.POST['textfield9']
        workingdistrict = request.POST['textfield11']
        state = request.POST['textfield10']
        id = request.POST['id']
        a = District_officer.objects.get(id=id)
        if 'photo' in request.FILES:
            photo = request.FILES['textfield5']
            dt = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs = FileSystemStorage()
            fs.save(dt, photo)
            path = fs.url(dt)
            a.photo = path

        a.name = name
        a.email = email
        a.phone = phone
        a.gender = gender
        a.dob = DOB
        a.place = place
        a.post = post
        a.pin = pin
        a.district = district
        a.workingdistrict = workingdistrict
        a.state = state
        a.save()

        return HttpResponse('''<script>alert("success");window.location="/myapp/admin_home/"</script>''')


def edit_allocated(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        data = Allocate_package.objects.get(id=id)
        data2 = Package.objects.all
        return render(request, 'admin/edit_allocated_package.html', {'data': data, 'data2': data2})


def edit_allocated_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        district = request.POST['select']
        package = request.POST['select2']
        alloted_amount = request.POST['textfield']
        id = request.POST['id']

        f = Allocate_package.objects.get(id=id)
        f.district = district
        f.date = datetime.now().today()
        f.alloted_amount = alloted_amount
        f.PACKAGE_id = package
        f.save()
        return HttpResponse('''<script>alert("success");window.location="/myapp/admin_home/"</script>''')


def edit_package(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
      data = Package.objects.get(id=id)
    return render(request, 'admin/edit_package.html', {'data': data})


def edit_package_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
            name = request.POST['textfield']
            type = request.POST['select']
            description = request.POST['textfield2']
            amount = request.POST['textfield3']
            id = request.POST['id']

            b = Package.objects.get(id=id)
            b.name = name
            b.type = type
            b.description = description
            b.amount = amount
            b.save()

            return HttpResponse('''<script>alert("success");window.location="/myapp/admin_home/"</script>''')


def view_district(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        c = District_officer.objects.all()
        return render(request, 'admin/view district officer.html', {'data': c})


def view_district_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        search = request.POST['textfield']
        return


def view_allocated(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        a = Allocate_package.objects.all()
        return render(request, 'admin/view_allocated_package.html', {'data': a})


def view_allocated_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        search = request.POST['textfield']
        return render(request, 'admin/view_allocated_package.html')


def view_package(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
            d = Package.objects.all()
            return render(request, 'admin/view_package.html', {'data': d})


def view_package_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
          search = request.POST['textfield']
          return


def delete_district_officer(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        District_officer.objects.get(id=id).delete()
        return HttpResponse('''<script>alert("deleted");window.location="/myapp/admin_home/"</script>''')


def delete_package(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        Package.objects.get(id=id).delete()
        return HttpResponse('''<script>alert("deleted");window.location="/myapp/admin_home/"</script>''')


def delete_allocated_package(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        Allocate_package.objects.get(id=id).delete()
        return HttpResponse('''<script>alert("deleted");window.location="/myapp/admin_home/"</script>''')



##################district off ############

def add_councilor(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, "district_officer/add_councilor.html")


def add_councilor_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        DOB = request.POST['textfield3']
        phone = request.POST['textfield4']
        email = request.POST['textfield5']
        photo = request.FILES['fileField']
        place = request.POST['textfield6']
        post = request.POST['textfield7']
        district = request.POST['textfield9']
        state = request.POST['textfield10']

        dt = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(dt, photo)
        path = fs.url(dt)

        import random

        l = Login()
        l.username = email
        l.password = random.randint(0000, 9999)
        l.type = 'councilor'
        l.save()

        obj = Councilors()
        obj.name = name
        obj.email = email
        obj.phone = phone
        obj.photo = path
        obj.gender = gender
        obj.dob = DOB
        obj.place = place
        obj.district = district
        obj.post = post
        obj.state = state
        obj.LOGIN = l
        obj.save()
        return HttpResponse('''<script>alert("added successfully");window.location="/myapp/add_councilor/"</script>''')


def edit_councilor(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        data = Councilors.objects.get(id=id)
        return render(request, "district_officer/edit_councilor.html", {"data": data})


def edit_councilor_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        DOB = request.POST['textfield3']
        phone = request.POST['textfield4']
        email = request.POST['textfield5']
        place = request.POST['textfield6']
        post = request.POST['textfield7']
        district = request.POST['textfield9']
        state = request.POST['textfield10']
        id = request.POST['id']

        obj = Councilors.objects.get(id=id)

        if 'fileField' in request.FILES:
            photo = request.FILES['fileField']
            if photo != '':
                dt = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
                fs = FileSystemStorage()
                fs.save(dt, photo)
                path = fs.url(dt)
                obj.photo = path
                obj.save()

        obj.name = name
        obj.email = email
        obj.phone = phone
        obj.gender = gender
        obj.dob = DOB
        obj.place = place
        obj.district = district
        obj.post = post
        obj.state = state
        obj.save()
        return HttpResponse('''<script>alert("edited successfully");window.location="/myapp/view_councilors/"</script>''')


def profile_view(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        data = District_officer.objects.get(LOGIN=request.session['lid'])
        return render(request, "district_officer/profile_view.html", {'data': data})


def tribe_related_problem(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        a = Tribal_related_problem.objects.all()
        return render(request, "district_officer/tribe_related_problem.html", {"data": a})


def tribe_related_problem_POST(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        search = request.POst['textfield']
        a = Tribal_related_problem.objects.filter(title__icontains=search)
        return render(request, "district_officer/tribe_related_problem.html", {"data": a})


def district_view_allocated_package(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, "district_officer/view_allocated_package.html")


def view_allocated_package_POST(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        search = request.POST['textfield']
        a = Tribal_related_problem.objects.filter(title__icontains=search)
        return render(request, "district_officer/view_allocated_package.html")


def view_councilors(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        data = Councilors.objects.all()
        return render(request, "district_officer/view_councilors.html", {'data': data})


def view_councilors_POST(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        search = request.POST['textfield']
        a = Councilors.objects.filter(name__icontains=search)
        return render(request, "district_officer/view_councilors.html", {'data': a})


def district_home(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, "district_officer/district_officer_index.html")


def delete_councilor(request, id):
    Councilors.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location="/myapp/view_councilors/"</script>''')


#############     COUNCILLOR     ################################




def add_coordinater(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, "councilor/add_coordinater.html")


def add_coordinater_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        name = request.POST['textfield']
        photo = request.FILES['fileField']
        email = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        dob = request.POST['textfield4']
        phone = request.POST['textfield5']
        place = request.POST['textfield6']
        post = request.POST['textfield7']
        district = request.POST['textfield8']
        state = request.POST['textfield9']

        dt = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(dt, photo)
        path = fs.url(dt)

        import random

        l = Login()
        l.username = email
        l.password = random.randint(0000, 9999)
        l.type = 'Coordinater'
        l.save()

        obj = Coordinater()
        obj.name = name
        obj.email = email
        obj.phone = phone
        obj.photo = path
        obj.gender = gender
        obj.dob = dob
        obj.place = place
        obj.district = district
        obj.post = post
        obj.state = state
        obj.LOGIN = l
        obj.save()
        return HttpResponse('''<script>alert("added successfully");window.location="/myapp/add_councilor/"</script>''')



def counciler_home(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, "councilor/councilor_index.html")


def edit_coordinater(request, id):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        a = Coordinater.objects.get(id=id)
        return render(request, "councilor/edit_coordinater.html", {"data": a})


def edit_coordinater_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        dob = request.POST['textfield4']
        phone = request.POST['textfield5']
        place = request.POST['textfield6']
        post = request.POST['textfield7']
        district = request.POST['textfield8']
        state = request.POST['textfield9']
        id = request.POST['id']

        obj = Coordinater.objects.get(id=id)

        if 'fileField' in request.FILES:
            photo = request.FILES['fileField']
            if photo != '':
                dt = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
                fs = FileSystemStorage()
                fs.save(dt, photo)
                path = fs.url(dt)
                obj.photo = path
                obj.save()

        obj.name = name
        obj.email = email
        obj.phone = phone
        obj.gender = gender
        obj.dob = dob
        obj.place = place
        obj.district = district
        obj.post = post
        obj.state = state
        obj.save()
        return HttpResponse('''<script>alert("edited successfully");window.location="/myapp/view_coordinator/"</script>''')


def delete_coordinater(request, id):
    Coordinater.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location="/myapp/view_coordinater/"</script>''')


def counciler_view_profile(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        a = Councilors.objects.get(LOGIN_id=request.session['lid'])
        return render(request, 'councilor/view profile.html', {"data": a})


def view_request(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        a = Request_entry_service.objects.all()
        return render(request, 'councilor/view request.html', {"data": a})


def view_request_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        from_date = request.POST['textfield']
        to_date = request.POST['textfield']
        return render(request, 'councilor/view request.html')


def view_service_for_allocated_tribe(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, 'councilor/view service for allocated tribe.html')


def view_service_for_allocated_tribe_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, 'councilor/view service for allocated tribe.html')


def councilor_view_tribes(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        a = Tribes.objects.all()
        return render(request, 'councilor/view tribes.html', {"data": a})


def councilor_view_tribes_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:

        search=request.POST['textfield']
        a = Tribes.objects.filter(name__icontains=search)
        return render(request, 'councilor/view tribes.html', {"data": a})


def view_coordinator(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        obj = Coordinater.objects.all()
        return render(request, 'councilor/view_coordinator.html', {"data": obj})


def view_coordinator_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, 'councilor/view_coordinator.html')


def view_report(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        a=Tribal_related_problem.objects.all()
        return render(request, 'councilor/view_report.html', {"data": a})


def view_report_post(request):
    if request.session['lid'] == '':
        return redirect("/myapp/login/")
    else:
        return render(request, 'councilor/view_report.html')


########################   FLUTTER              ######################


def flutt_login(request):
    username = request.POST['username']
    password = request.POST['password']
    l = Login.objects.filter(username=username, password=password)
    if l.exists():
        l2 = Login.objects.get(username=username, password=password)
        lid = l2.id
        if l2.type == 'Coordinater':
            return JsonResponse({"status": "ok", "lid": str(lid)})
        else:
            return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "ok"})


def flutt_view_profile(request):
    lid = request.POST['lid']
    a = Coordinater.objects.get(LOGIN_id=lid)
    return JsonResponse({"status": "ok",
                         "name": a.name,
                         "email": a.email,
                         "photo": a.photo,
                         "phone": a.phone,
                         "gender": a.gender,
                         "dob": a.dob,
                         "place": a.place,
                         "district": a.district,
                         "post": a.post,
                         "state": a.state,
                         })


def flutt_add_tribal_families(request):
    name = request.POST['name']
    culture = request.POST['culture']
    population_size = request.POST['population_size']
    language = request.POST['language']
    location = request.POST['location']
    traditional_occupation_on_jobs = request.POST['traditional_occupation_on_jobs']
    caste_and_religion = request.POST['caste_and_religion']
    lid = request.POST['lid']

    a = Tribes()
    a.name = name
    a.culture = culture
    a.population_size = population_size
    a.language = language
    a.location = location
    a.traditional_occupation_on_jobs = traditional_occupation_on_jobs
    a.caste_and_religion = caste_and_religion
    a.save()
    return JsonResponse({"status": "ok"})


def flutt_edit_tribal_families(request):
    name = request.POST['name']
    culture = request.POST['culture']
    population_size = request.POST['population_size']
    language = request.POST['language']
    location = request.POST['location']
    traditional_occupation_on_jobs = request.POST['traditional_occupation_on_jobs']
    caste_and_religion = request.POST['caste_and_religion']

    a = Tribes()
    a.name = name
    a.culture = culture
    a.population_size = population_size
    a.language = language
    a.location = location
    a.traditional_occupation_on_jobs = traditional_occupation_on_jobs
    a.caste_and_religion = caste_and_religion
    a.save()
    return JsonResponse({"status": "ok"})


def flutt_view_tribal_families(request):
    lid = request.POST['lid']
    a = Tribes.objects.get(TRIBE__LOGIN_id=lid)
    l = []
    for i in a:
        l.append({"id": i.id,
                  "name": i.name,
                  "culture": i.culture,
                  "population_size": i.population_size,
                  "language": i.language,
                  "location": i.location,
                  "traditional_occupation_on_jobs": i.traditional_occupation_on_jobs,
                  "caste_and_religion": i.caste_and_religion,
                  })
    return JsonResponse({"status": "ok"})


def flutt_add_family_members(request):
    member_name = request.POST['member_name']
    dob = request.POST['dob']
    relation = request.POST['relation']
    gender = request.POST['gender']
    lid = request.POST['lid']

    a = Tribal_member()
    a.member_name = member_name
    a.dob = dob
    a.relation = relation
    a.gender = gender
    a.TRIBE = Tribes.objects.get(LOGIN_id=lid)
    a.save()

    return JsonResponse({"status": "ok"})


def flutt_edit_family_members(request):
    member_name = request.POST['member_name']
    dob = request.POST['dob']
    relation = request.POST['relation']
    gender = request.POST['gender']
    lid = request.POST['lid']

    a = Tribal_member()
    a.member_name = member_name
    a.dob = dob
    a.relation = relation
    a.gender = gender
    a.TRIBE = Tribes.objects.get(LOGIN_id=lid)
    a.save()

    return JsonResponse({"status": "ok"})


def flutt_view_family_members(request):
    lid = request.POST['lid']
    a = Tribal_member.objects.get(TRIBE__LOGIN_id=lid)
    l = []
    for i in a:
        l.append({"id": i.id,
                  "member_name": i.member_name,
                  "dob": i.dob,
                  "relation": i.relation,
                  "gender": i.gender,
                  })
    return JsonResponse({"status": "ok"})


def flutt_report_problem(request):
    title = request.POST['title']
    problem = request.POST['problem']
    photo = request.POST['photo']
    date = request.POST['date']
    status = request.POST['status']
    tid = request.POST['tid']

    a = Tribal_related_problem()
    a.title=title
    a.problem=problem
    a.photo=photo
    a.date=date
    a.status=status
    a.TRIBE = Tribes.objects.get(LOGIN_id=tid)
    a.save()

    return JsonResponse({"status": "ok"})


def flutt_supply_the_package(request):
    name=request.POST['name']
    description=request.POST['description']
    unit=request.POST['unit']
    tid=request.POST['tid']
    cid=request.POST['cid']

    a=Food_and_medical_supply()
    a.name=name
    a.description=description
    a.unit=unit
    a.TRIBE_id = tid
    a.COORDINATER_id=cid
    a.save()
    return JsonResponse({"status": "ok"})


def flutt_add_notification(request):
    description=request.POST['description']
    lid=request.POST['lid']

    a = Notification()
    a.description=description
    a.date=datetime.now()
    a.COORDINATER=Coordinater.objects.get(LOGIN_id=lid)
    a.save()
    return JsonResponse({"status": "ok"})


def flutt_request_entry_for_service(request):
    service_name=request.POST['service_name']
    lid=request.POST['lid']
    tid=request.POST['tid']

    a=Request_entry_service()
    a.service_name=service_name
    a.date=datetime.now()
    a.status='pending'
    a.TRIBE_id=tid
    a.COORDINATER=Coordinater.objects.get(LOGIN_id=lid)
    a.save()

    return JsonResponse({"status": "ok"})


def flutt_service_entry_with_tribes_identity_card_verification(request):

    return JsonResponse({"status": "ok"})
def flutt_change_password(request):
    current_password=request.POST['current_password']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    lid=request.POST['lid']
    a=Login.objects.filter(id=lid,password=current_password)
    if a.exists():
        Login.objects.get(id=lid,password=current_password)
        if new_password==confirm_password:
            Login.objects.filter(id=lid).update(password=new_password)
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status": "no"})