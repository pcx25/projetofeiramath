import streamlit as st
import requests
from datetime import datetime


def obter_cotacao_dolar():
    # Obter a data atual no formato esperado pela API
    data_atual = datetime.now().strftime("%m-%d-%Y")

    # URL da API do Banco Central
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_atual}'&$top=100&$format=json"

    try:
        # Requisição à API
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacoes = dados.get("value", [])

        if cotacoes:
            compra = cotacoes[0]['cotacaoCompra']
            venda = cotacoes[0]['cotacaoVenda']
            return compra, venda
        else:
            return None, None
    except requests.exceptions.RequestException as erro:
        return None, None


def app():
    st.title("Cotação do Dólar")
    st.write("Bem-vindo ao visualizador de cotação do dólar em tempo real!")

    compra, venda = obter_cotacao_dolar()

    if compra is not None and venda is not None:
        st.write(f"Cotação do dólar de {datetime.now().strftime('%d/%m/%Y')}:")
        st.write(f"Compra: R$ {compra}")
        st.write(f"Venda: R$ {venda}")
    else:
        st.write("Não foi possível obter a cotação do dólar no momento.")


if __name__ == "__main__":
    app()
