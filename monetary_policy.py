# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:17:41 2018

@author: pportocarrero
"""
# CODE TO SET THE DEFAULT WORKING DIRECTORY

import pandas as pd

import os

import pickle

os.chdir('D:\pportocarrero@mef.gob.pe\Investor Relations Office\Projects\monetary_policy')

#D:\pportocarrero@mef.gob.pe\Investor Relations Office\Projects\monetary_policy
#/Users/Pedro/Desktop/monetary_policy

cwd = os.getcwd()

######################## IMPORT DATASETS

#### LOADS EXCEL FILES AND PUTS THEM IN PANDAS 

inflation_fl = 'inflation_db.xlsx'

expectations_fl = 'expectations_db.xlsx'

interest_rate_fl = 'interest_rate_db.xlsx'

year_fl = 'year.xlsx'

inflation_db = pd.ExcelFile(inflation_fl)

expectations_db = pd.ExcelFile(expectations_fl)

interest_rate_db = pd.ExcelFile(interest_rate_fl)

year_db = pd.ExcelFile(year_fl)

#### LOADS DATAFRAMES AND SAVES THEM AS PICKLES

inflation_df = inflation_db.parse('Hoja1')

inflation_df.to_pickle('inflation_df.pickle')

expectations_df = expectations_db.parse('Hoja1')

expectations_df.to_pickle('expectations_df.pickle')

interest_rate_df = interest_rate_db.parse('Hoja1')

interest_rate_df.to_pickle('interest_rate_df.pickle')

year_df = year_db.parse('Hoja1')

year_df.to_pickle('year_df.pickle')

#### LOAD PICKLES DATASETS AND DELETES DEPRECATED FILES

inflation_data = pd.read_pickle('inflation_df.pickle')

expectations_data = pd.read_pickle('expectations_df.pickle')

interest_rate_data = pd.read_pickle('interest_rate_df.pickle')

year_data = pd.read_pickle('year_df.pickle')

del inflation_df

del inflation_fl

del expectations_df

del expectations_fl

del interest_rate_df

del interest_rate_fl

del year_df

del year_fl

######################## NEW DATA ON LAST ROW OF DATAFRAMES

# NEW DATA ON EXPECTATIONS
expectations_data.loc[len(expectations_data)] = ['Jan', 'January', '01', '18', 2018, 58.5, 70.7, 50, 2.23, 'nan', 2.4, 2.5]

expectations_data.to_pickle('expectations_df.pickle')

# NEW DATA ON INFLATION
inflation_data.loc[len(inflation_data)] = ['Jan', 'January', '01', '18', 2018, 0.127417107488597, 1.2531883694175, 0.127417107488597, -0.129632120477368, 1.97121356769657]

inflation_data.to_pickle('inflation_df.pickle')

# NEW DATA ON INTEREST RATES
interest_rate_data.loc[len(interest_rate_data)] = ['Jan', 'January', '01', '18', 2018, 3.00, 2, 3, 1]

interest_rate_data.to_pickle('interest_rate_df.pickle')

# NEW DATA ON YEAR

year_data.loc[len(year_data)] = ['Jan ''18']

######################## LOAD DATA

import pandas as pd

import os

import pickle

os.chdir('D:\pportocarrero@mef.gob.pe\Investor Relations Office\Projects\monetary_policy')

inflation_data = pd.read_pickle('inflation_df.pickle')

expectations_data = pd.read_pickle('expectations_df.pickle')

interest_rate_data = pd.read_pickle('interest_rate_df.pickle')

######################## 
######################## SAVE THE LATEST DATA (t = 0 and t = - 1)
######################## 

#### LATEST INFLATION

# THE MONTH
last_month_col = inflation_data.loc[: , 'month_lab_shrt']
last_month = last_month_col.tail(1)
last_month_t1 = last_month_col[-2:-1]

# INFLATION MONTHLY CHANGE
last_inf_m_col = inflation_data.loc[: , 'inflation_mth']
last_inf_m = last_inf_m_col.tail(1)
last_inf_m_t1 = last_month_col[-2:-1]

# INFLATION YOY
last_inf_yoy_col = inflation_data.loc[: , 'inflation_yoy']
last_inf_yoy = last_inf_yoy_col.tail(1)
last_inf_yoy_t1 = last_inf_yoy_col[-2:-1]

# INFLATION YTD
last_inf_ytd_col = inflation_data.loc[: , 'inflation_ytd']
last_inf_ytd = last_inf_ytd_col.tail(1)
last_inf_ytd_t1 = last_inf_ytd_col[-2:-1]

# INFLATION EXCLUDING FOOD AND ENERGY MONTHLY CHANGE
last_cinf_m_col = inflation_data.loc[: , 'core_inf_mth']
last_cinf_m = last_cinf_m_col.tail(1)
last_cinf_m_t1 = last_cinf_m_col[-2:-1]

# INFLATION EXCLUDING FOOD AND ENERGY YOY
last_cinf_yoy_col = inflation_data.loc[: , 'core_inf_yoy']
last_cinf_yoy = last_cinf_yoy_col.tail(1)
last_cinf_yoy_t1 = last_cinf_yoy_col[-2:-1]

#### LATEST EXPECTATIONS DATA

# EXPECTATIONS FOR 3 MONTHS AHEAD
last_3m_col = expectations_data.loc[: , '3m_ahead']
last_3m = last_3m_col.tail(1)
last_3m_t1 = last_3m_col[-2:-1]

# EXPECTATIONS FOR 12 MONTHS AHEAD
last_12m_col = expectations_data.loc[: , '12m_ahead']
last_12m = last_12m_col.tail(1)
last_12m_t1 = last_12m_col[-2:-1]

# INFLATION EXPECTATIONS FOR 12 MONTHS
last_12m_ex_col = expectations_data.loc[: , '12m_inf_exp']
last_12m_ex = last_12m_ex_col.tail(1)
last_12_ex_t1 = last_12m_ex_col[-2:-1]

# INFLATION EXPECTATIONS FOR 2018
last_2018_ie_col = expectations_data.loc[: , 'exp_inf_2018']
last_2018_ie = last_2018_ie_col.tail(1)
last_2018_ie_t1 = last_2018_ie_col[-2:-1]

# INFLATION EXPECTATIONS FOR 2019
last_2019_ie_col = expectations_data.loc[: , 'exp_inf_2019']
last_2019_ie = last_2019_ie_col.tail(1)
last_2019_ie_t1 = last_2019_ie_col[-2:-1]

#### LATEST INTEREST RATE DATA
last_interest_rate_col = interest_rate_data.loc[: , 'rate']
last_interest_rate = last_interest_rate_col.tail(1)
last_interest_rate_t1 = last_interest_rate_col[-2:-1]

######################## DATA FOR CHARTS

import matplotlib.pyplot as plt

# INTEREST RATE GRAPH
yr_lng_col = year_data.loc[: , 'yr_lng']

yr_lng = year_data[120:]

interest_rate_gph_rg = last_interest_rate_col[120:] # Data to plot since Jan 2010

plt.plot(interest_rate_gph_rg)
#plt.axis(yr_shrt_col)
plt.xlabel('Year')
plt.ylabel('%')

plt.plot(last_interest_rate_col)
