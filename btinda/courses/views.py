from django.shortcuts import render
from .forms import CourseForm
from .models import Course


# Create your views here.

def course(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = CourseForm(request.POST or None)

    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        enom = form.cleaned_data['exp_nom']
        etel = form.cleaned_data['exp_tel']
        dnom = form.cleaned_data['dest_nom']
        dtel = form.cleaned_data['dest_tel']
        dadresse = form.cleaned_data['dest_adresse']
        dcolis = form.cleaned_data['desc_colis']
        
        Course.objects.create(exp_nom = enom,exp_tel = etel,dest_nom = dnom,dest_tel =dtel,dest_adresse = dadresse,dest_colis = dcolis)
        
        message = 'Votre course a été enregistrée'
        
        


    
    return render(request, 'front-page.html', locals())

        
    