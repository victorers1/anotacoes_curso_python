def palindromo(str):
    s = str.lower()
    if(s == s[::-1]):
        print("É um palíndromo")
    else:
        print("Não é palíndromo")

pali = "Ana"
palindromo(pali)