# Filter accounts and indicators that will be used for selecting stocks for
# the Magic Formula

import pandas as pd


def filter_data(max_cols=7, max_rows=5, max_width=10):
    """Função para filtrar os dados"""

    # Somente dados auditados serão usados -> (DFP)
    pd.options.display.max_colwidth = max_width
    pd.options.display.max_columns = max_cols
    pd.options.display.max_rows = max_rows

    df = pd.read_feather("s3://aq-dl/FinancialStatements/base.feather")

    df.query('doc_tp == "DFP"', inplace=True)
    # Remover colunas que não serão usadas no backtesting:
    df.drop(columns=["doc_tp", "doc_arq", "doc_ref", "doc_ver", "doc_id"], inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Iremos simular somente com dados consolidados (CON)
    # Conta "9.01.03" -> "Total de Ações (Capital Integralizado)" em balanço IND
    df.query('dem_tp == "CON" or conta_id == "9.01.03"', inplace=True)
    # Remover coluna que não será mais usada no backtesting
    df.drop(columns=["dem_tp"], inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Descartar períodos que não são o corrente -> per_ref == 0
    df.query("per_ref == 0", inplace=True)
    # Remover coluna que não será mais usada no backtesting
    df.drop(columns=["per_ref"], inplace=True)
    df.reset_index(drop=True, inplace=True)

    contas = ["1.01.01", "1.01.02", "2.01.04", "2.02.01", "2.03", "3.05", "9.01.03"]
    df.query("conta_id == @contas", inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Verificar se as contas selecionadas são fixas
    # Todas as empresas que contém contas não fixas nas contas selecionadas são IFs
    df.query("conta_fixa == 0").cia_nome.unique()
    # Buscar demais bancos e demais IFs
    procurar = "bco |banco|crédito|mercantil|seguradora|seguro|PPLA PARTICIPATIONS"
    # Remover essas empresas do dataframe
    df.query("~cia_nome.str.contains(@procurar, case=False)", inplace=True)
    df.reset_index(drop=True, inplace=True)
    # Remover a coluna conta fixa da base, pois não será mais usada
    df.drop(columns=["conta_fixa"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    # Remover a descrição do código contábil para a operação futura de unstack
    df.drop(columns=["conta_desc"], inplace=True)

    return df


df = filter_data()
df
