IP = int(input("Insira o primeiro octeto do IP: "))
classe='nenhum'

if(IP>=0 and IP<=127):
    classe ='A'
elif(IP>127 and IP<=191):
    classe ='B'
elif(IP>191 and IP<=223):
    classe ='C'
elif(IP>223 and IP<=239):
    classe ='D'
elif(IP>239):
    classe ='E'

print("A classe do IP é " + classe)