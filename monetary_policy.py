#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:39:43 2018

@author: Pedro
"""

import pandas as pd

import os

import pickle

os.chdir('/Users/Pedro/Desktop/monetary_policy')

cwd = os.getcwd()

#### LOADS EXCEL FILES AND PUTS THEM IN PANDAS 

inflation_fl = 'inflation_db.xlsx'

expectations_fl = 'expectations_db.xlsx'

interest_rate_fl = 'interest_rate_db.xlsx'

inflation_db = pd.ExcelFile(inflation_fl)

expectations_db = pd.ExcelFile(expectations_fl)

interest_rate_db = pd.ExcelFile(interest_rate_fl)

### LOADS DATAFRAMES AND SAVES THEM AS PICKLES

inflation_df = inflation_db.parse('Hoja1')

inflation_df.to_pickle('inflation_df.pickle')

expectations_df = expectations_db.parse('Hoja1')

expectations_df.to_pickle('expectations_df.pickle')

interest_rate_df = interest_rate_db.parse('Hoja1')

interest_rate_df.to_pickle('interest_rate_df.pickle')

## LOAD PICKLES DATASETS AND DELETES DEPRECATED FILES

inflation_data = pd.read_pickle('inflation_df.pickle')

expectations_data = pd.read_pickle('expectations_df.pickle')

interest_rate_data = pd.read_pickle('interest_rate_df.pickle')

del inflation_df

del inflation_fl

del expectations_df

del expectations_fl

del interest_rate_df

del interest_rate_fl