# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:17:41 2018

@author: pportocarrero
"""
# CODE TO SET THE DEFAULT WORKING DIRECTORY

import pandas as pd

import os

import pickle

os.chdir('/Users/Pedro/Desktop/monetary_policy')

#D:\pportocarrero@mef.gob.pe\Investor Relations Office\Projects\monetary_policy
#/Users/Pedro/Desktop/monetary_policy

cwd = os.getcwd()


#### LOADS EXCEL FILES AND PUTS THEM IN PANDAS 

inflation_fl = 'inflation_db.xlsx'

expectations_fl = 'expectations_db.xlsx'

interest_rate_fl = 'interest_rate_db.xlsx'

inflation_db = pd.ExcelFile(inflation_fl)

expectations_db = pd.ExcelFile(expectations_fl)

interest_rate_db = pd.ExcelFile(interest_rate_fl)


#### LOADS DATAFRAMES AND SAVES THEM AS PICKLES

inflation_df = inflation_db.parse('Hoja1')

inflation_df.to_pickle('inflation_df.pickle')

expectations_df = expectations_db.parse('Hoja1')

expectations_df.to_pickle('expectations_df.pickle')

interest_rate_df = interest_rate_db.parse('Hoja1')

interest_rate_df.to_pickle('interest_rate_df.pickle')

#### LOAD PICKLES DATASETS AND DELETES DEPRECATED FILES

inflation_data = pd.read_pickle('inflation_df.pickle')

expectations_data = pd.read_pickle('expectations_df.pickle')

interest_rate_data = pd.read_pickle('interest_rate_df.pickle')

del inflation_df

del inflation_fl

del expectations_df

del expectations_fl

del interest_rate_df

del interest_rate_fl

#### NEW DATA ON LAST ROW OF DATAFRAMES

expectations_data.loc[len(expectations_data)] = ['Jan', 'January', '01', '18', 2018, 58.5, 70.7, 50, 2.23, 'nan', 2.4, 2.5]

expectations_data.to_pickle('expectations_df.pickle')

inflation_data.loc[len(inflation_data)] = ['Jan', 'January', '01', '18', 2018, 0.127417107488597, 1.2531883694175, 0.127417107488597, -0.129632120477368, 1.97121356769657]

inflation_data.to_pickle('inflation_df.pickle')

interest_rate_data.loc[len(interest_rate_data)] = ['Jan', 'January', '01', '18', 2018, 3.00, 2, 3, 1]

interest_rate_data.to_pickle('interest_rate_df.pickle')

#### LOAD DATA

inflation_data = pd.read_pickle('inflation_df.pickle')

expectations_data = pd.read_pickle('expectations_df.pickle')

interest_rate_data = pd.read_pickle('interest_rate_df.pickle')
