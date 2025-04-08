import string

def preprocesar_texto(texto, n=2):
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    palabras = texto.split()
    ngramas = [" ".join(palabras[i:i+n]) for i in range(len(palabras)-n+1)]
    return ngramas

def hash_personalizado(ngram):
    valor_hash = 0
    for char in ngram:
        valor_hash = (valor_hash * 31 + ord(char)) % (10**9 + 7)
    return valor_hash