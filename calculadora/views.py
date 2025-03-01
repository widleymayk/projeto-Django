from django.shortcuts import render

# Vou criar a função para exibir a calculadora
def exibir_calculadora(request):
    resultado = None # variavel para armazenar o resultado

    if request.method == 'POST':
        try:
            
            # Realiza a coleta de número e operação

            numeroUm = float(request.POST.get('numero__um'))
            numeroDois = float(request.POST.get('numero__dois'))
            operacao = request.POST.get('operacao')

            # realiza a operação de acordo com a escolha do usuário

            if operacao == 'adicao':
                resultado = numeroUm + numeroDois
            elif operacao == 'subtracao':
                resultado = numeroUm - numeroDois
            elif operacao == 'multiplicacao':
                resultado = numeroUm * numeroDois
            elif operacao == 'divisao':
                if operacao < 0 :
                    resultado = 'Valor deve ser positivo'
                resultado = numeroUm / numeroDois
        # Exceção para impedir valores invalidos
        except(ValueError, ZeroDivisionError):
            resultado = "Valores invalidos"
    # Renderiza o HTML e envia o resultado
    return render(request, 'calculadora/index.html', {'resultado':resultado})    

