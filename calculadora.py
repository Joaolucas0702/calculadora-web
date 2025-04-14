class CalculadoraDespesasImoveis:
    def __init__(self):
        self.tabela_registros = []  # Placeholder para tabela futura, se necessário

    def calcular_goiania_trindade_canedo(self, valor_imovel, valor_financiado, tipo_financiamento, cidade, seguro, primeiro_imovel=True):
        """Calcula despesas para Goiânia, Trindade ou Senador Canedo
        Args:
            seguro: Valor do seguro (deve ser verificado na simulação)
        """
        entrada = valor_imovel - valor_financiado

        # Lavratura do contrato
        if tipo_financiamento == "SBPE":
            lavratura = (valor_financiado * 0.01) + 842
        else:
            lavratura = (valor_financiado * 0.01) + (valor_financiado * 0.015)

        # ITBI
        itbi = valor_imovel * 0.005  # 0,5% exemplo
        itbi_total = itbi if primeiro_imovel else valor_imovel * 0.01

        # Registro (valor fixo de exemplo)
        total_registros = 3000.0

        total_despesas = itbi_total + lavratura + total_registros + seguro

        return {
            "Entrada": entrada,
            "ITBI": itbi_total,
            "Lavratura": lavratura,
            "Registro": total_registros,
            "Seguro (conferir na simulação)": seguro,
            "Total Despesas": total_despesas
        }

    def calcular_aparecida(self, valor_imovel, valor_financiado, tipo_financiamento, renda_bruta, seguro, primeiro_imovel=True):
        """Calcula despesas para Aparecida de Goiânia
        Args:
            seguro: Valor do seguro (deve ser verificado na simulação)
        """
        entrada = valor_imovel - valor_financiado

        # Lavratura
        if tipo_financiamento == "SBPE":
            lavratura = (valor_financiado * 0.01) + 842
        else:
            lavratura = (valor_financiado * 0.01) + (valor_financiado * 0.015)

        # ITBI
        itbi = valor_imovel * 0.005
        itbi_total = itbi if primeiro_imovel else valor_imovel * 0.01

        # Registro
        total_registros = 2800.0

        total_despesas = itbi_total + lavratura + total_registros + seguro

        return {
            "Entrada": entrada,
            "ITBI": itbi_total,
            "Lavratura": lavratura,
            "Registro": total_registros,
            "Seguro (conferir na simulação)": seguro,
            "Total Despesas": total_despesas
        }
