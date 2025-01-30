from django.shortcuts import render, redirect

def carrinho(request):
    return render(request, 'carrinho.html')

def adicionar_carrinho(request, id_carrinho):
    if request.method == "POST" and id_carrinho:
        dados = request.POST.dict()
        tamanho = dados.get('tamanho')
        id_cor = dados.get('cor')
        print(tamanho)
        print(id_cor)
        return redirect('loja')
    else:
        return redirect('loja')
