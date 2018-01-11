h = int(input("Bote as horas: "))
m = int(input("Bote os minutos: "))
s = int(input("Bote os segundos: "))

tempo = s + m*60 + h*60*60

print("Tempo total em segundos:", tempo)
