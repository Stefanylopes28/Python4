import requests

def gerar_usuario():
    url = 'https://randomuser.me/api/'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição

        dados = response.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("\n=== Perfil Gerado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")

def main():
    gerar_usuario()

if __name__ == "__main__":
    main()
