from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from app1.models import logintable,usertable,personaltable,educationtable,medicaltable,accounttable,goaltable
from django.contrib.auth import logout
from datetime import datetime
# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]

        x = logintable(Name=a, Email=b, Type="User")
        x.save()
        q = usertable(Loginid=x,Name=a, Email=b,Type="User")
        q.save()
        return redirect('success')
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]

        q = logintable.objects.filter(Name=a).first()

        if q and q.Email == b and q.Type == "User":
            x = usertable.objects.get(Name=a)

            if x.Email == b:
                request.session["member_id"] = x.id
                return render(request, "profile.html", {"name": x, "email": b})
        else:
            return redirect('invalid')

    return render(request, "login.html")

 #personal

def personal(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]

        k = personaltable(Name=a, lastname=b, dob=c, age=d, address=e, Email=f, number=g)
        k.save()
        return redirect('submit')

    return render(request, "personalform.html")

def personaldata(request):

    x = usertable.objects.get(id=request.session["member_id"])
    print(x.Name)
    c=personaltable.objects.filter(Name=x.Name)

    if request.method=="POST":
        c.Name = request.POST["name1"]
        c.lastname = request.POST["name2"]
        c.dob = request.POST["name3"]
        c.age = request.POST["name4"]
        c.address = request.POST["name5"]
        c.Email = request.POST["name6"]
        c.number = request.POST["name7"]
        c.save()

    return render(request, "data_personal.html",{"personalkey":c})

def delete(request,id1):
    c=personaltable.objects.get(id=id1)
    c.delete()
    return redirect('deleted')



def personaledit(request,id2):
    c = get_object_or_404(personaltable, id=id2)

    if request.method == "POST":
        try:
            # Assign values from the form to the model fields
            c.Name = request.POST.get("name1", "").strip()
            c.lastname = request.POST.get("name2", "").strip()
            dob = request.POST.get("name3", "")
            c.dob = datetime.strptime(dob, '%Y-%m-%d').date()  # Convert to date object
            c.age = int(request.POST.get("name4", "0"))
            c.address = request.POST.get("name5", "").strip()
            c.Email = request.POST.get("name6", "").strip()
            c.number = request.POST.get("name7", "").strip()
            c.save()
            return redirect('update')
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    return render(request,"personaledit.html", {'key1':c})

#education

def education(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]
        h = request.POST["name8"]
        i = request.POST["name9"]
        j = request.POST["name10"]
        k = request.POST["name11"]
        l = educationtable(Name=a, sslc_school=b, sslc_year=c, sslc_percentage=d, plus_two_school=e, plus_two_year=f, plus_two_percentage=g, degree_college=h, degree_course=i, degree_year=j, degree_percentage=k)
        l.save()
        return redirect('submit')

    return render(request,"educationform.html")

def educationdata(request):
    x = usertable.objects.get(id=request.session["member_id"])
    print(x.Name)
    c = educationtable.objects.filter(Name=x.Name)

    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.sslc_school=request.POST["name2"]
        c.sslc_year=request.POST["name3"]
        c.sslc_percentage=request.POST["name4"]
        c.plus_two_school=request.POST["name5"]
        c.plus_two_year=request.POST["name6"]
        c.plus_two_percentage=request.POST["name7"]
        c.degree_college=request.POST["name8"]
        c.degree_course=request.POST["name9"]
        c.degree_year=request.POST["name10"]
        c.degree_percentage=request.POST["name11"]
        c.save()

    return render(request, "educationdata.html", {"educationkey": c})

def educationedit(request,id3):
    c = educationtable.objects.get(id=id3)
    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.sslc_school = request.POST["name2"]
        c.sslc_year = request.POST["name3"]
        c.sslc_percentage = request.POST["name4"]
        c.plus_two_school = request.POST["name5"]
        c.plus_two_year = request.POST["name6"]
        c.plus_two_percentage = request.POST["name7"]
        c.degree_college = request.POST["name8"]
        c.degree_course = request.POST["name9"]
        c.degree_year = request.POST["name10"]
        c.degree_percentage = request.POST["name11"]
        c.save()
        return redirect('update')
    return render(request,"educationedit.html", {'key3':c})

def edudelete(request,id8):
    c=educationtable.objects.get(id=id8)
    c.delete()
    return redirect('deleted')

# Medical

def medical(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]
        h = request.POST["name8"]
        i = request.POST["name9"]
        j = medicaltable(Name=a, age=b, height=c, weight=d, blood_group=e, gender=f, allergies=g, emergency_contact=h, medications=i)
        j.save()
        return redirect('submit')

    return render(request,"medicalform.html")

def medicaldata(request):
    x = usertable.objects.get(id=request.session["member_id"])
    print(x.Name)
    c = medicaltable.objects.filter(Name=x.Name)

    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.age = request.POST["name2"]
        c.height = request.POST["name3"]
        c.weight = request.POST["name4"]
        c.blood_group = request.POST["name5"]
        c.gender = request.POST["name6"]
        c.allergies = request.POST["name7"]
        c.emergency_contact = request.POST["name8"]
        c.medications = request.POST["name9"]
        c.save()

    return render(request, "medicaldata.html", {"medicalkey": c})

def medicaledit(request,id100):
    c = medicaltable.objects.get(id=id100)
    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.age = request.POST["name2"]
        c.height = request.POST["name3"]
        c.weight = request.POST["name4"]
        c.blood_group = request.POST["name5"]
        c.gender = request.POST["name6"]
        c.allergies = request.POST["name7"]
        c.emergency_contact = request.POST["name8"]
        c.medications = request.POST["name9"]
        c.save()
        return redirect('update')
    return render(request,"medicaledit.html", {'key30':c})

def meddelete(request,id99):
    c=medicaltable.objects.get(id=id99)
    c.delete()
    return redirect('deleted')

#finance

def account(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = accounttable(Name=a, bank_name=b, account_number=c, ifsc_code=d, account_type=e, annual_income=f)
        g.save()
        return redirect('submit')

    return render(request,"financeform.html")

def accountdata(request):
    x = usertable.objects.get(id=request.session["member_id"])
    print(x.Name)
    c = accounttable.objects.filter(Name=x.Name)

    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.bank_name = request.POST["name2"]
        c.account_number = request.POST["name3"]
        c.ifsc_code = request.POST["name4"]
        c.account_type = request.POST["name5"]
        c.annual_income = request.POST["name6"]
        c.save()

    return render(request, "financedata.html", {"accountkey": c})

def accountedit(request,id20):
    c = accounttable.objects.get(id=id20)
    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.bank_name = request.POST["name2"]
        c.account_number = request.POST["name3"]
        c.ifsc_code = request.POST["name4"]
        c.account_type = request.POST["name5"]
        c.annual_income = request.POST["name6"]
        c.save()
        return redirect('update')
    return render(request,"financeedit.html", {'key20':c})

def acdelete(request,id25):
    c=accounttable.objects.get(id=id25)
    c.delete()
    return redirect('deleted')

def goal(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = goaltable(Name=a, shortTermGoals=b, longTermGoals=c, dreamDestinations=d, bucketListItems=e)
        f.save()
        return redirect('submit')
    return render(request,"goalform.html")

def goaldata(request):
    x = usertable.objects.get(id=request.session["member_id"])
    print(x.Name)
    c = goaltable.objects.filter(Name=x.Name)

    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.shortTermGoals = request.POST["name2"]
        c.longTermGoals = request.POST["name3"]
        c.dreamDestinations = request.POST["name4"]
        c.bucketListItems = request.POST["name5"]
        c.save()

    return render(request, "goaldata.html", {"goalkey": c})

def goaledit(request,id22):
    c = goaltable.objects.get(id=id22)
    if request.method == "POST":
        c.Name = request.POST["name1"]
        c.shortTermGoals = request.POST["name2"]
        c.longTermGoals= request.POST["name3"]
        c.dreamDestinations = request.POST["name4"]
        c.bucketListItems = request.POST["name5"]
        c.save()
        return redirect('update')
    return render(request,"goaledit.html", {'key22':c})

def goaldelete(request,id12):
    c=goaltable.objects.get(id=id12)
    c.delete()
    return redirect('deleted')



def user_logout(request):
    logout(request)
    return redirect('home')


def success(request):
    return render(request, "success.html")

def invalid(request):
    return render(request,"invalid.html")

def update(request):
    return render(request,"update.html")

def submit(request):
    return render(request,"submit.html")

def deleted(request):
    return render(request,"delete.html")

def profile(request):
    return render(request,"profile.html")
