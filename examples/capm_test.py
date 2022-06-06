import sys
import os

# the following code is to replace the current path
# with the package's path   
current_path = os.getcwd()
current_path = current_path.replace('examples','Scripts')
sys.path.insert(0,current_path)
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from datetime import date

import capm

df_merc_vista = pd.read_csv('~/Documents/Github/AlgebraQuant/MagicFormula/data/df_vista_2012-2020.csv')
#df_merc_vista = df_merc_vista.drop(["preexe","especi"], axis=1)


df_acoes = df_merc_vista[df_merc_vista.especi.str.startswith('ON') |  df_merc_vista.especi.str.startswith('PN')].reset_index(drop=True)
df_acoes = df_acoes.drop(["especi","tpmerc","preexe","totneg","voltot","quatot"], axis=1)
