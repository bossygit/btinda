from django import forms

class CourseForm(forms.Form):
  exp_nom = forms.CharField(label="Nom expéditeur",widget=forms.TextInput(attrs={'placeholder':'Nom expéditeur','class':'form-control'}))
  exp_tel = forms.CharField(max_length=10,label="Téléphone expéditeur",widget=forms.TextInput(attrs={'placeholder':'Téléphone expéditeur','class':'form-control'}))
  dest_nom = forms.CharField(max_length=100,label="Nom destinataire",widget=forms.TextInput(attrs={'placeholder':'Nom destinataire','class':'form-control'}))
  dest_tel = forms.CharField(max_length=10,label="Téléphone destinataire",widget=forms.TextInput(attrs={'placeholder':'Téléphone destinataire','class':'form-control'}))
  dest_adresse = forms.CharField(max_length=100,label="Adresse destination",widget=forms.TextInput(attrs={'placeholder':'Adresse\Reference','class':'form-control'}))
  desc_colis = forms.CharField(max_length=250,label="Description du service",widget=forms.Textarea(attrs={'placeholder':'Description du service','class':'form-control','rows':'2'}))