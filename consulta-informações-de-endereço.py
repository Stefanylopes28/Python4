import requests  # O import deve estar no topo

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()

        dados = response.json()

        if 'erro' in dados:
            print("CEP não encontrado. Verifique se o número está correto.")
            return

        logradouro = dados.get('logradouro', 'Não disponível')
        bairro = dados.get('bairro', 'Não disponível')
        cidade = dados.get('localidade', 'Não disponível')
        estado = dados.get('uf', 'Não disponível')

        print("\n=== Endereço Consultado ===")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")

def main():
    cep = input("Digite o CEP (somente números): ").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Deve conter exatamente 8 números.")
        return

    consultar_cep(cep)

if __name__ == "__main__":
    main()
