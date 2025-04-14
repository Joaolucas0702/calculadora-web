import streamlit as st
from calculadora import CalculadoraDespesasImoveis
import pandas as pd
import io

def main():
    st.set_page_config(page_title="Calculadora de Despesas de Imóveis", layout="centered")

    st.title("🏠 Calculadora de Despesas de Imóveis")

    if "calculadora" not in st.session_state:
        st.session_state.calculadora = CalculadoraDespesasImoveis()

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

                texto_resultado = f"""
### 🏠 *CÁLCULO PARA COMPRA DE IMÓVEL COM FINANCIAMENTO*

#### 📄 *Dados do Imóvel e Financiamento*
- **Valor de Compra e Venda:** R$ {valor_imovel:,.2f}
- **Valor Financiado:** R$ {valor_financiado:,.2f}
- **Valor de Entrada:** R$ {resultados['Entrada']:,.2f}
- **Tipo de Financiamento:** {tipo_financiamento}

#### 💼 *Despesas Relacionadas à Compra do Imóvel*

1️⃣ **Caixa Econômica Federal – R$ {resultados['Lavratura']:,.2f}**  
Esse valor corresponde à lavratura do contrato de financiamento/escritura, avaliação do imóvel e relacionamento.

2️⃣ **ITBI – Prefeitura – R$ {resultados['ITBI']:,.2f}**  
O Imposto sobre Transmissão de Bens Imóveis (ITBI) pode ser cobrado separadamente sobre o valor do imóvel e sobre o valor financiado, dependendo da legislação municipal.

3️⃣ **Cartório de Registro de Imóveis – R$ {resultados['Registro']:,.2f}**  
Esse valor refere-se ao registro do contrato de financiamento, obrigatório para garantir a legalidade da compra e a segurança jurídica do comprador.

💼 **Seguro (verificar na simulação):** R$ {resultados['Seguro (conferir na simulação)']:,.2f}

---

#### ✅ *Total Geral das Despesas*
💰 **Aproximadamente R$ {resultados['Total Despesas']:,.2f}**

---

⚠️ *Aviso Importante:*  
A Suporte Soluções Imobiliárias não é responsável pelo cálculo oficial das despesas relacionadas à compra do imóvel. O presente levantamento tem caráter informativo e visa apenas auxiliar o cliente a entender os custos envolvidos na aquisição, com base em valores estimados.

Para obter informações precisas e realizar os pagamentos, recomenda-se entrar em contato com os órgãos responsáveis, como Prefeitura e o Cartório de Registro de Imóveis.
"""

                st.markdown(texto_resultado)

                buffer = io.StringIO()
                buffer.write(texto_resultado)
                st.download_button(
                    label="📥 Baixar cálculo em TXT",
                    data=buffer.getvalue(),
                    file_name="calculo_imovel.txt",
                    mime="text/plain"
                )

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

                texto_resultado = f"""
### 🏠 *CÁLCULO PARA COMPRA DE IMÓVEL COM FINANCIAMENTO*

#### 📄 *Dados do Imóvel e Financiamento*
- **Valor de Compra e Venda:** R$ {valor_imovel:,.2f}
- **Valor Financiado:** R$ {valor_financiado:,.2f}
- **Valor de Entrada:** R$ {resultados['Entrada']:,.2f}
- **Tipo de Financiamento:** {tipo_financiamento}

#### 💼 *Despesas Relacionadas à Compra do Imóvel*

1️⃣ **Caixa Econômica Federal – R$ {resultados['Lavratura']:,.2f}**  
Esse valor corresponde à lavratura do contrato de financiamento/escritura, avaliação do imóvel e relacionamento.

2️⃣ **ITBI – Prefeitura – R$ {resultados['ITBI']:,.2f}**  
O Imposto sobre Transmissão de Bens Imóveis (ITBI) pode ser cobrado separadamente sobre o valor do imóvel e sobre o valor financiado, dependendo da legislação municipal.

3️⃣ **Cartório de Registro de Imóveis – R$ {resultados['Registro']:,.2f}**  
Esse valor refere-se ao registro do contrato de financiamento, obrigatório para garantir a legalidade da compra e a segurança jurídica do comprador.

💼 **Seguro (verificar na simulação):** R$ {resultados['Seguro (conferir na simulação)']:,.2f}

---

#### ✅ *Total Geral das Despesas*
💰 **Aproximadamente R$ {resultados['Total Despesas']:,.2f}**

---

⚠️ *Aviso Importante:*  
A Suporte Soluções Imobiliárias não é responsável pelo cálculo oficial das despesas relacionadas à compra do imóvel. O presente levantamento tem caráter informativo e visa apenas auxiliar o cliente a entender os custos envolvidos na aquisição, com base em valores estimados.

Para obter informações precisas e realizar os pagamentos, recomenda-se entrar em contato com os órgãos responsáveis, como Prefeitura e o Cartório de Registro de Imóveis.
"""

                st.markdown(texto_resultado)

                buffer = io.StringIO()
                buffer.write(texto_resultado)
                st.download_button(
                    label="📥 Baixar cálculo em TXT",
                    data=buffer.getvalue(),
                    file_name="calculo_imovel_aparecida.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Erro no cálculo: {e}")

if __name__ == "__main__":
    main()
