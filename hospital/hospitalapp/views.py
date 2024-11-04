from django.shortcuts import render
from django.http import HttpResponseRedirect
from hospitalapp import dbconnection
import easygui
from django.core.files.storage import FileSystemStorage
from datetime import date
def index(request):
    return render(request,'base/index.html')
def login(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        sql="select * from logtb where username='"+a1+"' and password='"+a2+"'"
        data=dbconnection.selectone(sql)
        if data:
            if data[3]=='admin':
                return HttpResponseRedirect('adminindex')
            elif data[3]=='hr':
                request.session['HRUSERNAME']=a1
                return HttpResponseRedirect('hrindex')
            elif data[3]=='medicalsupredent':
                request.session['medicalusername']=a1
                if data[4]=='1':
                    request.session['medicalsuperusername']=a1
                    return HttpResponseRedirect('medicalsupredentprofile')
                elif data[4]=='0':
                    easygui.msgbox("request pending")
            elif data[3]=='doctor':
                if data[4]=='1':
                    request.session['doctorusername']=a1
                    return HttpResponseRedirect('doctorprofile')
                elif data[4]=='0':
                        easygui.msgbox("request pending")
            elif data[3]=='receptionist':
                if data[4]=='1':
                        request.session['receptionusername']=a1 
                        return HttpResponseRedirect('receptionprofile')   
                elif data[4]=='0':
                        easygui.msgbox("request pending")    
            elif data[3]=='pharmacist':
                
                if data[4]=='1':
                        request.session['pharmacyusername']=a1
                 
                 
                        return HttpResponseRedirect('pharmacyprofile')
                elif data[4]=='0':
                 easygui.msgbox("request pending")
            elif data[3]=='patient':
                request.session['patientusername']=a1
                return HttpResponseRedirect('patientprofile')
            
            
                
                    
                    
                


        else:
            easygui.msgbox("invalied username or password")

    return render(request,'base/login.html')
def adminindex(request):
    return render(request,'admin/adminindex.html')
def managedepartment(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        sql="select 8 from managedeptb where managedepartment='"+a1+"'"
        data=dbconnection.selectone(sql)
        if data:
            easygui.msgbox("already exist")
        else:

            sql="insert into managedeptb (managedepartment)values('"+a1+"')"
            dbconnection.insert(sql)
            easygui.msgbox("department added succesfully")
    sql="select * from managedeptb"
    data=dbconnection.selectall(sql)
    return render(request,'admin/managedepartment.html',{'p':data})
def delete(request):
    a1=request.GET.get('id')
    sql="delete from managedeptb where id='"+a1+"'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('managedepartment')
def managehr(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.FILES['c']
        fs=FileSystemStorage()
        fs.save('hospitalapp/static/user/'+a3.name,a3)
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        a7=request.POST.get('g')
        sql="select * from managehrtb where username='"+a6+"'"
        data=dbconnection.selectone(sql)
        if data:
            
            easygui.msgbox("already exist")
        else:
            sql="insert into managehrtb (name,address,photo,number,email,username,password)values('"+a1+"','"+a2+"','"+a3.name+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"')"
            dbconnection.insert(sql)
            
            sql="insert into logtb(username,password,type,status)values('"+a6+"','"+a7+"','hr','1')"
            dbconnection.insert(sql)
            easygui.msgbox("profile added succesfully")
    sql="select * from managehrtb"
    data=dbconnection.selectall(sql)
    return render(request,'admin/managehr.html',{'p':data})

        

            
    
def deletehr(request):
    
    a1=request.GET.get('deleteid')
    sql="delete from managehrtb where username='"+a1+"'"
    dbconnection.insert(sql)
    sql="delete from logtb where username='"+a1+"' and type='hr'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('managehr')
def edithr(request):
    a7=request.GET.get('editid')
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.POST.get('c')
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        sql="update managehrtb set name='"+a1+"', address='"+a2+"', number='"+a3+"', email='"+a4+"',username='"+a5+"',password='"+a6+"' where username='"+a7+"'"
        dbconnection.insert(sql)
        sql="update logtb set username='"+a5+"',password='"+a6+"' where username='"+a7+"' and type='hr'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfully")
        return HttpResponseRedirect('managehr')
    sql="select * from managehrtb where username='"+a7+"'"
    data=dbconnection.selectone(sql)
    return render(request,'admin/edithr.html',{'p':data})
def hrindex(request):
    return render(request,'hr/hrindex.html')
def managemedicalsupredent(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.FILES['c']
        fs=FileSystemStorage()
        fs.save('hospitalapp/static/upload/'+a3.name,a3)
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        a7=request.POST.get('g')
        a8=request.POST.get('h')
        a9=request.POST.get('i')
        a10=request.POST.get('j')
        
        sql="select * from managemedical where username='"+a6+"'"
        data=dbconnection.selectone(sql)
        if data:
            easygui.msgbox("already exist")
        else:
            
            sql="insert into managemedical(name,address,photo,number,email,username,password,age,qualification,experience)values('"+a1+"','"+a2+"','"+a3.name+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"','"+a8+"','"+a9+"','"+a10+"')"
            dbconnection.insert(sql)
            sql="insert into logtb(username,password,type,status)values('"+a6+"','"+a7+"','medicalsupredent','0')"
            dbconnection.insert(sql)
            easygui.msgbox(" medical-superintendent added succesfully")
    sql="select * from managemedical"
    data=dbconnection.selectall(sql)
    return render(request,'hr/managemedicalsupredent.html',{'p':data})
def deletemedical(request):
    a1=request.GET.get('id')
    sql="delete from managemedical where username='"+a1+"'"
    dbconnection.insert(sql)
    sql="delete from logtb where username='"+a1+"' and type='medicalsupredent'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('managemedicalsupredent')
def editmedical(request):
    b2=request.GET.get('id')
    if request.method=="POST":
        
        a2=request.POST.get('a')
        a3=request.POST.get('b')
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        a7=request.POST.get('g')
        a8=request.POST.get('h')
        a9=request.POST.get('i')
        a10=request.POST.get('j')
        sql="update managemedical set name='"+a2+"',address='"+a3+"',number='"+a4+"',email='"+a5+"',username='"+a6+"',password='"+a7+"',age='"+a8+"',qualification='"+a9+"',experience='"+a10+"' where username='"+b2+"'"
        dbconnection.insert(sql)
        sql="update logtb set username='"+a6+"',password='"+a7+"' where username='"+b2+"' and type='medicalsupredent'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfully")
        return HttpResponseRedirect('managemedicalsupredent')
    sql="select * from managemedical where username='"+b2+"'"
    data=dbconnection.selectone(sql)
    return render(request,'hr/editmedical.html',{'p':data})
def managedoctor(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.FILES['c']
        fs=FileSystemStorage()
        fs.save('hospitalapp/static/upload/'+a3.name,a3)
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        a7=request.POST.get('g')
        a8=request.POST.get('h')
        a9=request.POST.get('i')
        a10=request.POST.get('j')
        a11=request.POST.get('k')
        a12=request.POST.get('l')
        a13=request.POST.get('m')
        a14=request.POST.get('n')
        sql="select * from managedoctortb where username='"+a6+"'"
        data=dbconnection.selectone(sql)
        if data:
            easygui.msgbox("already exist")
        else:
            sql="insert into managedoctortb(name,address,photo,number,email,username,password,age,qualification,experience,speciality,typesof,biography,department)values('"+a1+"','"+a2+"','"+a3.name+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"','"+a8+"','"+a9+"','"+a10+"','"+a11+"','"+a12+"','"+a13+"','"+a14+"')"
            dbconnection.insert(sql)
            sql="insert into logtb(username,password,type,status)values('"+a6+"','"+a7+"','doctor','0')"
            dbconnection.insert(sql)
            easygui.msgbox("profile added succesfully")
    sql="select * from managedoctortb"
    data=dbconnection.selectall(sql)
    sql="select * from managedeptb"
    depdata=dbconnection.selectall(sql)
    return render(request,'hr/managedoctor.html',{'p':data,'m':depdata})
def deletedoctor(request):
    id=request.GET.get('id')
    sql="delete from managedoctortb where username='"+id+"'"
    dbconnection.insert(sql)
    sql="delete from logtb where username='"+id+"' and type='doctor'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('managedoctor')
def editdoctor(request):
    id=request.GET.get('id')
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.POST.get('d')
        a4=request.POST.get('e')
        a5=request.POST.get('f')
        a6=request.POST.get('g')
        a7=request.POST.get('h')
        a8=request.POST.get('i')
        a9=request.POST.get('j')
        a10=request.POST.get('k')
        a11=request.POST.get('l')
        a12=request.POST.get('m')
        sql="update managedoctortb set name='"+a1+"', address='"+a2+"',  number='"+a3+"', email='"+a4+"', username='"+a5+"', password='"+a6+"', age='"+a7+"', qualification='"+a8+"', experience='"+a9+"', speciality='"+a10+"', typesof='"+a11+"', biography='"+a12+"' where username='"+id+"'"
        dbconnection.insert(sql)
        sql="update logtb set username='"+a5+"',password='"+a6+"' where username='"+id+"' and type='doctor'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfully")
        return HttpResponseRedirect('managedoctor')
    sql="select * from managedoctortb where username='"+id+"'"
    data=dbconnection.selectone(sql)
    return render(request,'hr/editdoctor.html',{'p':data})
def managepharmacy(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.FILES['c']
        fs=FileSystemStorage()
        fs.save('hospitalapp/static/upload/'+a3.name,a3)
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        a7=request.POST.get('g')
        a8=request.POST.get('h')
        a9=request.POST.get('i')
        a10=request.POST.get('j')
        a11=request.POST.get('k')
        sql="select * from managepharmacytb where username='"+a6+"'"
        data=dbconnection.selectone(sql)
        if data:
            easygui.msgbox("already exist")
        else:
            sql="insert into managepharmacytb(name,address,photo,number,email,username,password,age,qualification,experience,biography)values('"+a1+"','"+a2+"','"+a3.name+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"','"+a8+"','"+a9+"','"+a10+"','"+a11+"')"
            dbconnection.insert(sql)
            sql="insert into logtb(username,password,type,status)values('"+a6+"','"+a7+"','pharmacist','0')"
            dbconnection.insert(sql)
            easygui.msgbox("profile added succesfully")
    sql="select * from managepharmacytb"
    data=dbconnection.selectall(sql)
    return render(request,'hr/managepharmacy.html',{'p':data})
def deletepharmacy(request):
    id=request.GET.get('id')
    sql="delete from managepharmacytb where username='"+id+"'"
    dbconnection.insert(sql)
    sql="delete from logtb where username='"+id+"' and type='pharmacist'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('managepharmacy')
def editpharmacy(request):
    id=request.GET.get('id')
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.POST.get('d')
        a4=request.POST.get('e')
        a5=request.POST.get('f')
        a6=request.POST.get('g')
        a7=request.POST.get('h')
        a8=request.POST.get('i')
        a9=request.POST.get('j')
        a10=request.POST.get('k')
        sql="update managepharmacytb set name='"+a1+"',address='"+a2+"',number='"+a3+"',email='"+a4+"',username='"+a5+"',password='"+a6+"',age='"+a7+"',qualification='"+a8+"',experience='"+a9+"',biography='"+a10+"' where username='"+id+"'"
        dbconnection.insert(sql)
        sql="update logtb set username='"+a5+"',password='"+a6+"' where username='"+id+"' and type='pharmacist'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfully")
        return HttpResponseRedirect('managepharmacy')
    sql="select * from managepharmacytb where username='"+id+"'"
    data=dbconnection.selectone(sql)
    return render(request,'hr/editpharmacy.html',{'p':data})   
def managereception(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.FILES['c']
        fs=FileSystemStorage()
        fs.save('hospitalapp/static/upload/'+a3.name,a3)
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        a7=request.POST.get('g')
        a8=request.POST.get('h')
        a9=request.POST.get('i')
        a10=request.POST.get('j')
        a11=request.POST.get('k')
        sql="select * from managereceptiontb where username='"+a6+"'"
        data=dbconnection.selectone(sql)
        if data:
            easygui.msgbox("already exist")
        else:
            sql="insert into managereceptiontb(name,address,photo,number,email,username,password,age,qualification,experience,biography)values('"+a1+"','"+a2+"','"+a3.name+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"','"+a8+"','"+a9+"','"+a10+"','"+a11+"')"
            dbconnection.insert(sql)
            sql="insert into logtb(username,password,type,status)values('"+a6+"','"+a7+"','receptionist','0')"
            dbconnection.insert(sql)
            easygui.msgbox("profile added succesfully")
    sql="select * from managereceptiontb"
    data=dbconnection.selectall(sql)
    return render(request,'hr/managereception.html',{'p':data})
def deletereception(request):
    id=request.GET.get('id')
    sql="delete from managereceptiontb where username='"+id+"'"
    dbconnection.insert(sql)
    sql="delete from logtb where username='"+id+"' and type='receptionist'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('managereception')
def editreception(request):
    id=request.GET.get('id')
    ids=request.GET.get('id')
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.POST.get('d')
        a4=request.POST.get('e')
        a5=request.POST.get('f')
        a6=request.POST.get('g')
        a7=request.POST.get('h')
        a8=request.POST.get('i')
        a9=request.POST.get('j')
        a10=request.POST.get('k')
        sql="update managereceptiontb set  name='"+a1+"', address='"+a2+"', number='"+a3+"', email='"+a4+"', username='"+a5+"', password='"+a6+"', age='"+a7+"', qualification='"+a8+"', experience='"+a9+"', biography='"+a10+"' where username='"+id+"'"
        dbconnection.insert(sql)
        sql="update logtb set username='"+a5+"',password='"+a6+"' where username='"+id+"'and type='receptionist'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfully")
        return HttpResponseRedirect('managereception')
    sql="select * from managereceptiontb where username='"+id+"'"
    data=dbconnection.selectone(sql)
    return render(request,'hr/editreception.html',{'p':data}) 
def approval (request):
    sql="select managemedical.id,managemedical.name,managemedical.address,managemedical.photo,managemedical.number,managemedical.email,managemedical.username,managemedical.password,managemedical.age,managemedical.qualification,managemedical.experience FROM managemedical INNER JOIN logtb ON managemedical.username=logtb.username where logtb.status='0'and type='medicalsupredent';"
    data=dbconnection.selectall(sql)

    return render(request,'admin/approval.html',{'p':data})
def medicalapproval(request):
    id=request.GET.get('id')
    sql="update logtb set status='1' where username='"+id+"' and type='medicalsupredent'"
    dbconnection.insert(sql)
    easygui.msgbox("approved succesfully")
    return HttpResponseRedirect('approval')
def doctorapproval(request):
    sql="select managedoctortb.id,managedoctortb.name,managedoctortb.address,managedoctortb.photo,managedoctortb.number,managedoctortb.email,managedoctortb.username,managedoctortb.password,managedoctortb.age,managedoctortb.qualification,managedoctortb.experience,managedoctortb.speciality,managedoctortb.typesof,managedoctortb.biography FROM managedoctortb INNER JOIN logtb ON managedoctortb.username=logtb.username where logtb.status='0' and type='doctor';"
    
    data=dbconnection.selectall(sql)
    return render(request,'admin/doctorapproval.html',{'p':data})
def doctorapprovalu(request):
    id=request.GET.get('id')
    sql="update logtb set status='1' where username='"+id+"' and type='doctor'"
    dbconnection.insert(sql)
    easygui.msgbox("approved succesfully")
    return HttpResponseRedirect('doctorapproval')
def pharmacyapproval(request):
    sql="select managepharmacytb.id,managepharmacytb.name,managepharmacytb.address,managepharmacytb.photo,managepharmacytb.number,managepharmacytb.email,managepharmacytb.username,managepharmacytb.password,managepharmacytb.age,managepharmacytb.qualification,managepharmacytb.experience,managepharmacytb.biography FROM managepharmacytb INNER JOIN logtb ON managepharmacytb.username=logtb.username where logtb.status='0' and type='pharmacist';"
    data=dbconnection.selectall(sql)
    return render(request,'admin/pharmacyapproval.html',{'p':data})
def pharmacyapprovalu(request):
    id=request.GET.get('id')
    sql="update logtb set status='1' where username='"+id+"' and type='pharmacist'"
    dbconnection.insert(sql)
    easygui.msgbox("approved succesfully")
    return HttpResponseRedirect('pharmacyapproval')
def receptionapproval(request):
    sql="select managereceptiontb.id,managereceptiontb.name,managereceptiontb.address,managereceptiontb.photo,managereceptiontb.number,managereceptiontb.email,managereceptiontb.username,managereceptiontb.password,managereceptiontb.age,managereceptiontb.qualification,managereceptiontb.experience,managereceptiontb.biography FROM managereceptiontb INNER JOIN logtb ON managereceptiontb.username=logtb.username where logtb.status='0' and type='receptionist';"
    data=dbconnection.selectall(sql)
    return render(request,'admin/receptionapproval.html',{'p':data})
def receptionapprovalu(request):
    id=request.GET.get('id')
    sql="update logtb set  status='1' where username='"+id+"' and type='receptionist'"
    dbconnection.insert(sql)
    easygui.msgbox("approved succesfully")
    return HttpResponseRedirect('receptionapproval')
def medicalsupredentprofile(request):
    return render(request,'medicalsupredent/medicalsupredentprofile.html')
def doctorprofile(request):
    return render(request,'doctor/doctorprofile.html')
def receptionprofile(request):
    return render(request,'reception/receptionprofile.html')
def pharmacyprofile(request):
    return render(request,'pharmacy/pharmacyprofile.html')
    
def managepatient(request):
    if request.method=="POST":
        a9=request.session['receptionusername']
        a1=request.POST.get('a')
        a2=request.POST.get('b')
       
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        a6=request.POST.get('f')
        a7=request.POST.get('g')
        a8=request.POST.get('h')
        a10=date.today()
       
        sql="select * from managepatienttb where username='"+a6+"'"
        data=dbconnection.selectone(sql)
        if data:
            easygui.msgbox("already exist")
        else:
            sql="insert into managepatienttb (name,address,number,email,username,password,age,receptionusername,date)values('"+a1+"','"+a2+"','"+a4+"','"+a5+"','"+a6+"','"+a7+"','"+a8+"','"+a9+"','"+str(a10)+"')"
            dbconnection.insert(sql)
            sql="insert into logtb (username,password,type,status)values('"+a6+"','"+a7+"','patient','0')"
            dbconnection.insert(sql)
            easygui.msgbox("registered succesfully")
    
    return render(request,'reception/managepatient.html')
def deletepatient(request):
    id=request.GET.get('id')
    date=request.GET.get('dt')







    sql="delete from managepatienttb where username='"+id+"'"
    dbconnection.insert(sql)
    sql="delete from logtb where username='"+id+"' and type='patient'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('managepatientdisplay?a='+date)
def editpatient(request):
    id=request.GET.get('id')
    date=request.GET.get('dt')
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.POST.get('d')
        a4=request.POST.get('e')
        a5=request.POST.get('f')
        a6=request.POST.get('g')
        a7=request.POST.get('h')
       
        sql="update managepatienttb set name='"+a1+"',address='"+a2+"',number='"+a3+"',email='"+a4+"',username='"+a5+"',password='"+a6+"',age='"+a7+"' where username='"+id+"'"
        dbconnection.insert(sql)
        sql="update logtb set username='"+a5+"',password='"+a6+"' where username='"+id+"' and type='patient'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfully")
        return HttpResponseRedirect('managepatientdisplay?a='+date)
    sql="select * from managepatienttb where username='"+id+"'"
    data=dbconnection.selectone(sql)
    return render(request,'reception/editpatient.html',{'p':data})
def patientobservation(request):
    a6=request.GET.get('id')
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.POST.get('c')
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        sql="insert into patientobservationtb (height,weight,bp,temperature,observation,patientusername)values('"+a1+"','"+a2+"','"+a3+"','"+a4+"','"+a5+"','"+a6+"')"
        dbconnection.insert(sql)
        easygui.msgbox("added succesfully")
    sql="select * from patientobservationtb where patientusername='"+a6+"'"
    data=dbconnection.selectall(sql)
    return render(request,'reception/patientobservation.html',{'p':data})
def deletepatientobservation(request):
    id=request.GET.get('id')
    sql="delete from patientobservationtb where id='"+id+"'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted succesfully")
    return HttpResponseRedirect('patientobservation')
def editpatientobservation(request):
    id=request.GET.get('id')
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        a3=request.POST.get('c')
        a4=request.POST.get('d')
        a5=request.POST.get('e')
        sql="update patientobservationtb set height='"+a1+"',weight='"+a2+"',bp='"+a3+"',temperature='"+a4+"',observation='"+a5+"' where id='"+id+"'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfuly")
        return HttpResponseRedirect('patientobservation?id='+id)
    sql="select * from patientobservationtb where id='"+id+"'"
    data=dbconnection.selectone(sql)
    return render(request,'reception/editpatientobservation.html',{'p':data})
def patientconsultation(request):
    a2=request.GET.get('id')
    if request.method=="POST":
        a1=request.POST.get('a')
        return HttpResponseRedirect('patientconsultationdoctor?id='+a1+"&pid="+a2)
        # sql="insert into patientconsultationtb (department)values('"+a1+"')"
        # dbconnection.insert(sql)
        # easygui.msgbox("department added succesfully")
    sql="select * from managedeptb"
    data=dbconnection.selectall(sql)
    return render(request,'reception/patientconsultation.html',{'p':data})
def patientconsultationdoctor(request):
    a1=request.GET.get('id')
    a2=request.GET.get('pid')
    if request.method=="POST":
        a3=request.POST.get('a')
        a4=date.today()
        sql="insert into patientconsultationtb(name,department,doctor,date,status)values('"+a2+"','"+a1+"','"+a3+"','"+str(a4)+"','0')"
        dbconnection.insert(sql)
        easygui.msgbox("added succesfully")

    sql="select * from managedoctortb where department='"+a1+"'"
    data=dbconnection.selectall(sql)
    return render(request,'reception/patientconsultationdoctor.html',{'p':data})
def patientconsultationappointment(request):
    a1=request.session['doctorusername']
    sql="select * from patientconsultationtb where doctor='"+a1+"' and status='0'"
    data=dbconnection.selectall(sql)
    return render(request,'doctor/patientconsultationappointment.html',{'p':data})
def patientobservationview(request):
    a2=request.GET.get('idd')
    a1=request.GET.get('id')
    sql="select * from patientobservationtb where patientusername='"+a1+"'"
    data=dbconnection.selectone(sql)
    return render(request,'doctor/patientobservationview.html',{'p':data,'m':a2})
def addmedicine(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        a2=request.POST.get('b')
        sql="select * from addmedicinetb where medicine='"+a2+"'"
        data=dbconnection.selectone(sql)
        if data:
            easygui.msgbox("medicine already existed")
        else:

            sql="insert into addmedicinetb (category,medicine)values('"+a1+"','"+a2+"')"
            dbconnection.insert(sql)
            easygui.msgbox("added succesfully")
    sql="select * from addmedicinetb"
    data=dbconnection.selectall(sql)
        
    return render(request,'pharmacy/addmedicine.html',{'p':data})    
def addstock(request):
    if request.method=="POST":
        a1=request.POST.get('a')
        return HttpResponseRedirect('addstockr?id='+a1)
    return render(request,'pharmacy/addstock.html')
def addstockr(request):
    a2=request.session['pharmacyusername']
    a1=request.GET.get('id')
    a6=date.today()
    if request.method=="POST":
        a3=request.POST.get('a')
        a4=request.POST.get('b')
        a5=request.POST.get('c')
        sql="insert into stockdtb (category,medicine,date,pharmacyusername,quantity,price)values('"+a1+"','"+a3+"','"+str(a6)+"','"+a2+"','"+a4+"','"+a5+"')"
        dbconnection.insert(sql)
        sql="select * from stockqtb where medicine='"+a3+"'"
        data=dbconnection.selectone(sql)
        if data:
            sql="update stockqtb set quantity='"+a4+"' where medicine='"+a3+"'"
            dbconnection.insert(sql)
        else:
            sql="insert into stockqtb (category,medicine,quantity,price)values('"+a1+"','"+a3+"','"+a4+"','"+a5+"')"
            dbconnection.insert(sql)
        easygui.msgbox("stock added successfully")
    sql="select * from addmedicinetb where category='"+a1+"'"
    data=dbconnection.selectall(sql)
    sql="select * from stockdtb"
    fdata=dbconnection.selectall(sql)
    return render(request,'pharmacy/addstockr.html',{'p':data,'f':fdata})
def prescription(request):
    a2=request.GET.get('id')
    a3=request.GET.get('idd')
    
    if request.method=="POST":
        a1=request.POST.get('a')
        return HttpResponseRedirect('prescriptiont?id='+a1+"&pid="+a2+"&idd="+a3)
    return render(request,'doctor/prescription.html')
def prescriptiont(request):
    a8=request.GET.get('idd')
    a7=date.today()
    a6=request.session['doctorusername']
    a2=request.GET.get('pid')
    a1=request.GET.get('id')
    
    if request.method=="POST":
        a3=request.POST.get('b')
        a4=request.POST.get('c')
        a5=request.POST.get('d')
        sql="select * from stockqtb where medicine='"+a3+"'"
        data=dbconnection.selectone(sql)
        if data[3]>a4:

       
                    sql="insert into doctorprescriptiontb (category,medicine,quantity,time,patientusername,doctorusername,date)values('"+a1+"','"+a3+"','"+a4+"','"+a5+"','"+a2+"','"+a6+"','"+str(a7)+"')"
                    dbconnection.insert(sql)
        else:
            easygui.msgbox("out of stock")
    sql="select * from stockqtb where category='"+a1+"' AND quantity>2"
    data=dbconnection.selectall(sql)
    sql="select * from doctorprescriptiontb where patientusername='"+a2+"' and date='"+str(a7)+"' and doctorusername='"+a6+"'"
    fdata=dbconnection.selectall(sql)
    return render(request,'doctor/prescriptiont.html',{'p':data,'m':fdata,'m1':a8})
def prescriptiontt(request):
    a1=request.GET.get('id')
    sql="update patientconsultationtb set status='1' where id='"+a1+"'"
    dbconnection.insert(sql)
    easygui.msgbox("finished")
    return HttpResponseRedirect('patientconsultationappointment')
def addmedicinedelete(request):
    a1=request.GET.get('id')
    sql="delete  from addmedicinetb where id='"+a1+"'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted")
    return HttpResponseRedirect('addmedicine')
def addmedicineedit(request):
    a1=request.GET.get('id')
    if request.method=="POST":
        a2=request.POST.get('a')
        a3=request.POST.get('b')
        sql="update addmedicinetb set category='"+a2+"',medicine='"+a3+"' where id='"+a1+"'"
        dbconnection.insert(sql)
        easygui.msgbox("updated succesfully")
        return HttpResponseRedirect('addmedicine')
    sql="select * from addmedicinetb where id='"+a1+"'"
    data=dbconnection.selectone(sql)
    return render(request,'pharmacy/addmedicineedit.html',{'p':data})
def stockdelete(request):
    a1=request.GET.get('id')
    a2=request.GET.get('idd')
    
    a3=request.GET.get('cat')
    sql="delete from stockdtb where id='"+a1+"'"
    dbconnection.insert(sql)
    sql="delete from stockqtb where medicine='"+a2+"'"
    dbconnection.insert(sql)
    easygui.msgbox("deleted")
    return HttpResponseRedirect('addstockr?id='+a3)
def pharmacybilling(request):
    # if request.method=="POST":
    #     a1=request.POST.get('a')
    #     a2=date.today()
    #     sql=" select * FROM doctorprescriptiontb where patientusername='"+a1+"'  and date ='"+str(a2)+"'"
    #     data=dbconnection.selectall(sql)
    #     return render(request,'pharmacy/pharmacybilling.html',{'p':data}) 
    return render(request,'pharmacy/pharmacybilling.html') 
def bill(request):
    a1=request.GET.get('a')
    a2=date.today()
    sql=" select * FROM doctorprescriptiontb where patientusername='"+a1+"'  and date ='"+str(a2)+"'"
    data=dbconnection.selectall(sql)
    sql="SELECT *,pharmacybillingaddtb.quantity*stockqtb.price FROM `pharmacybillingaddtb` inner join stockqtb on pharmacybillingaddtb.medicine=stockqtb.medicine where patientusername='"+a1+"' and date='"+str(a2)+"' and status='0'"

    fdata=dbconnection.selectall(sql)
    sql="SELECT sum(pharmacybillingaddtb.quantity*stockqtb.price) FROM `pharmacybillingaddtb` inner join stockqtb on pharmacybillingaddtb.medicine=stockqtb.medicine where patientusername='"+a1+"' and date='"+str(a2)+"'"
    sdata=dbconnection.selectone(sql)
    return render(request,'pharmacy/pharmacybilling.html',{'p':data,'m':fdata,'s':sdata}) 
    
def patientprofile(request):
    return render(request,'patient/patientprofile.html')
def consultationp(request):
    a1=request.session['patientusername']
    sql="select DISTINCT date from doctorprescriptiontb where patientusername='"+a1+"'"
    data=dbconnection.selectall(sql)
    return render(request,'patient/consultationp.html',{'p':data})
def complaintp(request):
    a1=request.session['patientusername']
    a2=date.today()
    if request.method=="POST":
        a3=request.POST.get('a')
        sql="insert into patientcomplainttb (complaint,date,patientusername)values('"+a3+"','"+str(a2)+"','"+a1+"')"
        dbconnection.insert(sql)
        easygui.msgbox("added succesfully")
    sql="select * from patientcomplainttb where patientusername='"+a1+"'"
    data=dbconnection.selectall(sql)    
    return render(request,'patient/complaintp.html',{'p':data})
def consultationf(request):
    a1=request.GET.get('id')
    a2=request.session['patientusername']
    sql="select * from doctorprescriptiontb inner join managedoctortb on doctorprescriptiontb.doctorusername=managedoctortb.username where patientusername='"+a2+"' and date='"+str(a1)+"'"
    data=dbconnection.selectall(sql)
    
    return render(request,'patient/consultationf.html',{'p':data})
def addpharmacy(request):
    a4=request.session['pharmacyusername']
    a1=request.GET.get('id')
    a2=request.GET.get('med')
    a3=date.today()
    a5=request.GET.get('pid')
    a6=request.GET.get('qid')
    sql="insert into pharmacybillingaddtb (prescriptionid,pharmacyusername,medicine,date,patientusername,quantity,status,billno)values('"+a1+"','"+a4+"','"+a2+"','"+str(a3)+"','"+a5+"','"+a6+"','0','0')"
    dbconnection.insert(sql)
    easygui.msgbox("added")
    sql="update stockqtb set quantity=quantity-'"+a6+"' where medicine='"+a2+"'"
    dbconnection.insert(sql)
    
    return HttpResponseRedirect('bill?a='+a5)
def patientcomplaint(request):
    sql="select * FROM patientcomplainttb INNER JOIN managepatienttb on patientcomplainttb.patientusername=managepatienttb.username;"
    data=dbconnection.selectall(sql)
    return render(request,'admin/patientcomplaint.html',{'p':data})
def stock(request):
    sql="select * from stockqtb"
    data=dbconnection.selectall(sql)
    return render(request,'admin/stock.html',{'p':data})
def stockcollection(request):
    sql="select * from stockdtb"
    data=dbconnection.selectall(sql)
    return render(request,'admin/stockcollection.html',{'p':data})
def patientdate(request):
    sql="select  DISTINCT date  from doctorprescriptiontb"
    data=dbconnection.selectall(sql)
    return render(request,'admin/patientdate.html',{'p':data})
def patientdatee(request):
    a1=request.GET.get('date')
    sql="SELECT * FROM `doctorprescriptiontb` inner JOIN managepatienttb on doctorprescriptiontb.patientusername=managepatienttb.username INNER JOIN managedoctortb ON doctorprescriptiontb.doctorusername=managedoctortb.username WHERE doctorprescriptiontb.date='"+str(a1)+"'"
    data=dbconnection.selectall(sql)
    return render(request,'admin/patientdatee.html',{'p':data})
def billing(request):
    sql="select * from pharmacyfinishtb"
    data=dbconnection.selectall(sql)
    
   
    return render(request,'admin/billing.html',{'p':data})
def billingt(request):
    a1=request.GET.get('bill')
    sql="SELECT *,pharmacybillingaddtb.quantity*stockqtb.price FROM `pharmacybillingaddtb` inner JOIN pharmacyfinishtb on pharmacybillingaddtb.billno=pharmacyfinishtb.billno inner join managepharmacytb on managepharmacytb.username=pharmacybillingaddtb.pharmacyusername inner join stockqtb on stockqtb.medicine=pharmacybillingaddtb.medicine WHERE pharmacybillingaddtb.billno='"+a1+"'"
    
    data=dbconnection.selectall(sql)
    return render(request,'admin/v_bill.html',{'p':data})
def finish(request):
    a1=request.GET.get('pid')
    a2=request.GET.get('amount')
    a4=request.session['pharmacyusername']
    a5=date.today()
    sql="SELECT * FROM `pharmacyfinishtb` order by id DESC LIMIT 1"
    data=dbconnection.selectone(sql)
    if data:
        billno=int(data[1])+1
    else:
        billno=100
    sql="insert  into pharmacyfinishtb (billno,date,patients,pharmacist,total)values('"+str(billno)+"','"+str(a5)+"','"+a1+"','"+a4+"','"+a2+"')" 
    dbconnection.insert(sql)
    sql="update pharmacybillingaddtb set billno='"+str(billno)+"', status='1' where patientusername='"+a1+"' and date='"+str(a5)+"'"
    dbconnection.insert(sql)
    easygui.msgbox("updated")
    return HttpResponseRedirect('bill?a='+a1)
def managepatientdisplay(request):
    # if request.method=="GET":
    a1=request.GET.get('a')
    if a1:
        sql="select * from managepatienttb where date='"+a1+"'"
        data=dbconnection.selectall(sql)
        return render(request,'reception/managepatientdisplay.html',{'p':data})
    return render(request,'reception/managepatientdisplay.html')
        
    
    
    
    
   


   
    
   
   
        
        
        
    
    
    
    
    

    


    
   
    
    
# Create your views here.
