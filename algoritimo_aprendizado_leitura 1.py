import random

# Dicionário global de palavras: chaves são letras, valores são palavras que começam com essas letras
palavras = {
    'a': 'abacaxi',
    'b': 'bola',
    'c': 'cachorro',
    'd': 'dado',
    'e': 'elefante',
    'f': 'foca',
    'g': 'gato'
}

def ensinar_leitura():
    """
    Inicia um jogo interativo para ensinar leitura de palavras simples.
    O usuário é apresentado a uma série de palavras e deve identificar a letra inicial de cada uma.
    Para cada palavra, o usuário digita a letra que acredita ser a inicial. O programa informa se a resposta está correta ou não,
    e ao final incentiva o usuário a continuar praticando.
    Pré-requisitos:
        - Um dicionário global chamado 'palavras', onde as chaves são letras e os valores são palavras que começam com essas letras.
        - O módulo 'random' deve estar importado.
    Exemplo de uso:
        ensinar_leitura()
    """
    
    print("Bem-vindo ao jogo de aprendizado de leitura!")
    print("Vamos aprender algumas palavras simples.")

    letras = list(palavras.keys())
    random.shuffle(letras)

    for letra in letras:
        palavra = palavras[letra]
        print(f"Qual letra começa a palavra '{palavra}'?")
        resposta = input("Digite a letra correta: ").lower()
        
        if resposta == letra:
            print("Muito bem! Você acertou! 🎉")
        else:
            print(f"Quase! A resposta correta é '{letra}'. Vamos tentar outra!")

    print("Ótimo trabalho! Continue praticando e logo você estará lendo tudo!")

ensinar_leitura()
