# from schoolsystem.trainer.models import Trainer
from .models import Trainer
from django.shortcuts import redirect, render
from .forms import TrainerRegistrationForms



def register_trainer(request):
    form=TrainerRegistrationForms()
    return render(request,"register_trainer.html",{"form":form})

def register_trainer(request):
    if request.method=="POST":
        form=TrainerRegistrationForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
                print(form.errors)
    else:
        form=TrainerRegistrationForms()
    return render(request,"register_trainer.html",{"form":form})

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})


def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})

def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForms(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
    else:
            form=TrainerRegistrationForms(instance=trainer)
    return render(request,"edit_trainer.html",{"form":form})
def delete_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    trainer.delete()
    return redirect(trainer_list)


