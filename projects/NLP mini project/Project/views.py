from django.shortcuts import render
from dbn_neuralnet import *
# Create your views here.
def index(request):
    if request.method == "POST":
        return render(request, 'search/index.html', {'data': 'wow'})
    else:
        return render(request, 'search/index.html')

def find(request):
    print("aagaya message!!")
    print(request.POST)
    data = dict()
    data['text'] = request.POST['text']
    data['method'] = request.POST['method']
    if data['method'] == 'DBN_neuralnet':
        acc_tf_dbn,f_mes_tf_dbn = test_with_unigram_tf_dbn()
        acc_tfidf_dbn,f_mes_tfidf_dbn = test_with_unigram_tfidf_dbn()
    
    data['acc_tf']= acc_tf_dbn
    data['acc_tfidf']= acc_tfidf_dbn
    data['f_mes_tf_dbn']= f_mes_tf_dbn
    data['f_mes_tfidf_dbn']= f_mes_tfidf_dbn


    return render(request, 'search/searchresult.html', data)
