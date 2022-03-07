from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
import requests
from .forms import MWForm
from django.shortcuts import redirect
from .mw_calculator import MWcalculator


def compounds_list(request):
    compounds = Compound.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'compounds/compounds_list.html', {'compounds': compounds})

def compound_detail(request, pk):
    compound = get_object_or_404(Compound, pk=pk)
    compound_InChIKey = compound.InChIKey
    pubchem_request = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/"+compound_InChIKey+"/synonyms/json").json()
    pubchem_request_synonym = pubchem_request['InformationList']['Information'][0]['Synonym']
    return render(request, 'compounds/compound_detail.html', {'compound': compound, 'request': pubchem_request_synonym})

def compound_data_list(request):
    compound_data = Compound_Data.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'compounds/compound_data_list.html', {'compound_data': compound_data})

def computed_mw(request):
    computed = Computed_Molecular_Weight.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'compounds/computed_mw.html', {'computed': computed})


def computed_mw_new(request):
    if request.method == "POST":
        form = MWForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.calculated_molecular_weight = str(MWcalculator(post.molecular_formula))
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('computed_mw')
    else:
        form = MWForm()
    return render(request, 'compounds/computed_mw_new.html', {'form': form})

