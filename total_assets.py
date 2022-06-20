import pandas as pd

pd.options.display.max_colwidth = 20
pd.options.display.max_rows = 4

df = pd.read_feather("s3://aq-dl/FinancialStatements/base.feather")

df.query('doc_tp == "DFP"', inplace=True)
df.drop(columns=["doc_tp", "doc_arq", "doc_ref", "doc_id"], inplace=True)
df.reset_index(drop=True, inplace=True)

df.query('dem_tp == "CON" or conta_id == "9.01.03"', inplace=True)
# Remover coluna que não será mais usada no backtesting
df.drop(columns=["dem_tp"], inplace=True)
df.reset_index(drop=True, inplace=True)

df.query("per_ref == 0", inplace=True)
# Remover coluna que não será mais usada no backtesting
df.drop(columns=["per_ref"], inplace=True)
df.reset_index(drop=True, inplace=True)

contas = ["1", "1.01.01", "1.01.02", "2.01.04", "2.02.01", "2.03", "3.05", "9.01.03"]
df.query("conta_id == @contas", inplace=True)
df.reset_index(drop=True, inplace=True)

procurar = "bco |banco|crédito|mercantil|seguradora|seguro|PPLA PARTICIPATIONS"
df.query("~cia_nome.str.contains(@procurar, case=False)", inplace=True)
df.reset_index(drop=True, inplace=True)

df.drop(columns=["conta_fixa"], inplace=True)
df.reset_index(drop=True, inplace=True)
df.drop(columns=["conta_desc"], inplace=True)

colunas_index = df.columns[:-1].to_list()
df = df.set_index(colunas_index).sort_index()

df = df.unstack(level="conta_id", fill_value=0)
df.columns = df.columns.droplevel(0)

df.reset_index(inplace=True)
df.columns.name = None

df["total_assets"] = df["1"]
df["total_cash"] = df["1.01.01"] + df["1.01.02"]
df["total_debt"] = df["2.01.04"] + df["2.02.01"]
df["net_debt"] = df["total_debt"] - df["total_cash"]
df.rename(
    columns={"2.03": "equity", "3.05": "ebit", "9.01.03": "shares_outstanding"},
    inplace=True,
)
df["invested_capital"] = df["equity"] + df["net_debt"]
df["roic"] = df["ebit"] / df["invested_capital"]
df.drop(columns=["1", "1.01.01", "1.01.02", "2.01.04", "2.02.01"], inplace=True)

df.query("equity > 0", inplace=True)

df.query("total_cash > 0", inplace=True)
df.query("ebit >= 0.001", inplace=True)
df.query("roic >= 0", inplace=True)

colunas = df.columns[:6].to_list() + [
    "total_assets",
    "shares_outstanding",
    "net_debt",
    "ebit",
    "roic",
]
df = df[colunas].copy()

df.query("shares_outstanding != 0", inplace=True)
df.to_csv("4_total_assets.csv", index=False)
