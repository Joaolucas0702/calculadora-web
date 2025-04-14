import streamlit as st
from calculadora import CalculadoraDespesasImoveis
import pandas as pd

def main():
    st.set_page_config(page_title="Calculadora de Despesas de Imóveis", layout="centered")

    st.title("🏠 Calculadora de Despesas de Imóveis")

    # Inicializa a calculadora se ainda não estiver na sessão
    if "calculadora" not in st.session_state:
        st.session_state.calculadora = CalculadoraDespesasImoveis()

    # Abas para diferentes cidades
    tab1, tab2 = st.tabs(["Goiânia/Trindade/Canedo", "Aparecida de Goiânia"])

    with tab1:
        st.header("Cálculo para Goiânia, Trindade ou Senador Canedo")

        col1, col2 = st.columns(2)
        with col1:
            valor_imovel = st.number_input("Valor do Imóvel (R$)", min_value=0.0, value=500000.0)
            valor_financiado = st.number_input("Valor Financiado (R$)", min_value=0.0, value=300000.0)
            seguro = st.number_input("Seguro (verificar na simulação)", min_value=0.0, value=220.0)
        
        with col2:
            tipo_financiamento = st.selectbox("Tipo de Financiamento", ["SBPE", "Outro"])
            cidade = st.selectbox("Cidade", ["Goiânia", "Trindade", "Senador Canedo"])
            primeiro_imovel = st.checkbox("Primeiro Imóvel/Financiamento?", value=True)

        if st.button("Calcular Despesas"):
            try:
                resultados = st.session_state.calculadora.calcular_goiania_trindade_canedo(
                    valor_imovel, valor_financiado, tipo_financiamento, cidade, seguro, primeiro_imovel
                )

                st.subheader("📋 Resultado do Cálculo")

                tabela = pd.DataFrame({
                    "Descrição": [
                        "Valor de Entrada",
                        "Lavratura do Contrato",
                        "Registro",
                        "ITBI",
                        "Seguro (verificar na simulação)"
                    ],
                    "Valor (R$)": [
                        resultados["Entrada"],
                        resultados["Lavratura"],
                        resultados["Registro"],
                        resultados["ITBI"],
                        resultados["Seguro (conferir na simulação)"]
                    ]
                })

                st.table(tabela)
                st.success(f"**Total Estimado de Despesas: R$ {resultados['Total Despesas']:.2f}**")

            except Exception as e:
                st.error(f"Erro no cálculo: {e}")

    with tab2:
        st.header("Cálculo para Aparecida de Goiânia")

        col1, col2 = st.columns(2)
        with col1:
            valor_imovel = st.number_input("Valor do Imóvel (R$)", min_value=0.0, value=500000.0, key="ap_valor_imovel")
            valor_financiado = st.number_input("Valor Financiado (R$)", min_value=0.0, value=300000.0, key="ap_valor_financiado")
            seguro = st.number_input("Seguro (verificar na simulação)", min_value=0.0, value=30.0, key="ap_seguro")

        with col2:
            tipo_financiamento = st.selectbox("Tipo de Financiamento", ["SBPE", "Outro"], key="ap_tipo_financiamento")
            renda_bruta = st.number_input("Renda Bruta (R$)", min_value=0.0, value=2000.0)
            primeiro_imovel = st.checkbox("Primeiro Imóvel/Financiamento?", value=True, key="ap_primeiro_imovel")

        if st.button("Calcular Despesas", key="ap_calcular"):
            try:
                resultados = st.session_state.calculadora.calcular_aparecida(
                    valor_imovel, valor_financiado, tipo_financiamento, renda_bruta, seguro, primeiro_imovel
                )

                st.subheader("📋 Resultado do Cálculo")

                tabela = pd.DataFrame({
                    "Descrição": [
                        "Valor de Entrada",
                        "Lavratura do Contrato",
                        "Registro",
                        "ITBI",
                        "Seguro (verificar na simulação)"
                    ],
                    "Valor (R$)": [
                        resultados["Entrada"],
                        resultados["Lavratura"],
                        resultados["Registro"],
                        resultados["ITBI"],
                        resultados["Seguro (conferir na simulação)"]
                    ]
                })

                st.table(tabela)
                st.success(f"**Total Estimado de Despesas: R$ {resultados['Total Despesas']:.2f}**")

            except Exception as e:
                st.error(f"Erro no cálculo: {e}")

if __name__ == "__main__":
    main()
