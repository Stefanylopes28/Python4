import random
import string

def gerar_senha(tamanho):
    if tamanho < 1:
        return "O tamanho da senha deve ser no mínimo 1."

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Informe o tamanho desejado para a senha: "))
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
    except ValueError:
        print("Por favor, informe um número inteiro válido.")

if __name__ == "__main__":
    main()
