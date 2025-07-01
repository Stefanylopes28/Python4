import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()

        dados = response.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada. Verifique se o código está correto.")
            return

        cotacao = dados[chave]

        valor_atual = cotacao.get('bid', 'Não disponível')
        valor_maximo = cotacao.get('high', 'Não disponível')
        valor_minimo = cotacao.get('low', 'Não disponível')
        data_hora = cotacao.get('create_date', 'Não disponível')

        print(f"\n=== Cotação {moeda}/BRL ===")
        print(f"Valor Atual: R$ {valor_atual}")
        print(f"Valor Máximo: R$ {valor_maximo}")
        print(f"Valor Mínimo: R$ {valor_minimo}")
        print(f"Última Atualização: {data_hora}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a cotação: {e}")

def main():
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()

    if not moeda.isalpha() or len(moeda) != 3:
        print("Código inválido. Informe um código de moeda com 3 letras (ex: USD).")
        return

    consultar_cotacao(moeda)

if __name__ == "__main__":
    main()
