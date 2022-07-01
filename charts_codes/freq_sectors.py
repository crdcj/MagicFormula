"""This is a script to make some chart from the notebook 1_included_companies."""

import pandas as pd
import altair as alt

pd.options.display.max_colwidth = 20
pd.options.display.max_columns = 6
pd.options.display.max_rows = 6
CVM_PATH = "data/external/cad_cia_aberta.csv"
cols = [
    "DENOM_SOCIAL",
    "DT_REG",
    "DT_CANCEL",
    "SIT",
    "DT_INI_SIT",
    "CD_CVM",
    "SETOR_ATIV",
]

df = pd.read_csv(CVM_PATH, sep=";", encoding="iso-8859-1")[cols]
df = (
    df.sort_values("DT_INI_SIT", ignore_index=True)
    .dropna(subset="SETOR_ATIV")
    .drop_duplicates(subset="CD_CVM", keep="last", ignore_index=True)
    .sort_values("CD_CVM", ignore_index=True)
)
# len(df.SETOR_ATIV.unique())
# df.SETOR_ATIV.value_counts().sum()

# create a chart with the total sector frequency
chart_freq = (
    alt.Chart(df, width=1000, height=500)
    .mark_bar()
    .encode(
        alt.Y(
            "count(SETOR_ATIV):Q",
            # bin=True,
        ),
        alt.X(
            "SETOR_ATIV:N",
            axis=alt.Axis(title="Frequency"),
            sort="-y",
        ),
        alt.Color("SETOR_ATIV:N", legend=None),
        tooltip=["SETOR_ATIV:N", "count(SETOR_ATIV):Q"],
    )
)
df
chart_freq.save("../charts/chart_freq_total.html")

removed_sectors = [
    "Arrendamento Mercantil",
    "Bancos",
    "Bolsas de Valores/Mercadorias e Futuros",
    "Crédito Imobiliário",
    "Emp. Adm. Part. - Arrendamento Mercantil",
    "Emp. Adm. Part. - Bancos",
    "Emp. Adm. Part. - Crédito Imobiliário",
    "Emp. Adm. Part. - Energia Elétrica",
    "Emp. Adm. Part. - Intermediação Financeira",
    "Emp. Adm. Part. - Saneamento, Serv. Água e Gás",
    "Emp. Adm. Part. - Securitização de Recebíveis",
    "Emp. Adm. Part. - Seguradoras e Corretoras",
    "Emp. Adm. Part. - Sem Setor Principal",
    "Emp. Adm. Part.-Bolsas de Valores/Mercadorias e Futuros",
    "Emp. Adm. Participações",
    "Energia Elétrica",
    "Factoring",
    "Intermediação Financeira",
    "Saneamento, Serv. Água e Gás",
    "Securitização de Recebíveis",
    "Seguradoras e Corretoras",
    "Telecomunicações",
]

df_included = pd.read_csv("../data/included_companies.csv", sep="|")
df_included

# create a chart with just the included sectors frequency
chart_freq = (
    alt.Chart(df_included, width=800, height=250)
    .mark_bar()
    .encode(
        alt.Y(
            "count(SETOR_ATIV):Q",
            axis=alt.Axis(title="Frequency"),
            # bin=True,
        ),
        alt.X(
            "SETOR_ATIV:N",
            axis=alt.Axis(title="Sector"),
            sort="-y",
        ),
        alt.Color("SETOR_ATIV:N", legend=None),
        tooltip=["SETOR_ATIV:N", "count(SETOR_ATIV):Q"],
    )
)
df
chart_freq.save("../charts/chart_freq_included.html")

df_included
