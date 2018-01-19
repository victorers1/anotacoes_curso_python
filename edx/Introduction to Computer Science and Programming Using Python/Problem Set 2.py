# Problema 1
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Configurando variáveis
minimumMonthlyPayment = 0  # Só defini para que se torne global e possa ser usada nos Problems 2 e 3
unpaidBalance = balance  # unpaidBalance é o que falta pagar, no início, tudo
monthlyPayment = annualInterestRate / 12  # Juros mensal, só muda na primeira iteração

for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance  # Calculo o mínimo que posso pagar e pago esse mês
    unpaidBalance = balance - minimumMonthlyPayment  # Calculo quanto falta pagar
    # Atualiza o valor que estou devendo
    balance = unpaidBalance + monthlyPayment * unpaidBalance  # Na primeiroa iteração não altera 'balance'

    # print('%i - Balance: %.3f; mimPay: %.3f; unpaid: %.3f; inter: %.3f' %(i, balance,minimumMonthlyPayment,unpaidBalance, monthlyPaymentRate*unpaidBalance))
print("Remaining Balance: {}".format(round(balance, 2)))

# Problema 2
balance = 4773
annualInterestRate = 0.2
# Configurando variáveis
minimumMonthlyPayment = 0  # Valor o pagamento mínimo mensal para pagar todaa dívida
monthlyInterestRate = annualInterestRate/12  # Juros mensal = Juros Anual / 12
BFC = balance  # 'Balance For Calculation', pois o valor em 'balance' será usado mais tarde (linha 37)

while True:
    for j in range(12):
        # Pago o valor mínimo estimado
        unpaidBalance = BFC - minimumMonthlyPayment  # minimumMonthlyPayment aqui não é só 2% da dívida, é um valor fixo que será calculado
        # Atualiza a quatia devida
        BFC = unpaidBalance + monthlyInterestRate * unpaidBalance

    if BFC > 0:
        minimumMonthlyPayment += 10 # O valor mínimo das parcelas mensais será múltiplo de 10
        BFC = balance  # Redefine a variável usada para o cálculo da mensalidade mínima
    else:
        break
print('Lowest Payment: {}'.format(minimumMonthlyPayment))

#Problem 3
balance = 999999
annualInterestRate = 0.18
# Configurando variáveis
monthlyInterestRate = annualInterestRate / 12
BFC = balance  # 'Balance For Calculation', pois é necessário guardar o valor de 'balance'
LowerBound = BFC/12  # Valor mínimo estimado
UpperBound = (BFC*(1+monthlyInterestRate)**12)/12  # Valor máximo estimado
monthlyPayment = (LowerBound+UpperBound)/2  # Primeiro valor testado

while True:
    for k in range(12):
        # Pago o valor mínimo estimado
        unpaidBalance = BFC - monthlyPayment  # minimumMonthlyPayment aqui não é só 2% da dívida, é um valor fixo que será calculado
        # Atualiza a quatia devida
        BFC = unpaidBalance + monthlyInterestRate * unpaidBalance

    if abs(BFC) > 0.1:
        if BFC > 0:  # Não pagou toda dívida
            LowerBound = monthlyPayment
        else:  # Pagou mais do que devia
            UpperBound = monthlyPayment
        # Redefine as variável necessárias
        BFC = balance
        monthlyPayment = monthlyPayment = (LowerBound+UpperBound)/2
    else:
        break

print('Lowest Payment: {}' .format(round(monthlyPayment, 2)))

