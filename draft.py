#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:47:24 2020

@author: jenniferraichel
"""
#Import modules needed for setup
import csv
import numpy as np
import requests
import pandas as pd

#use a list of census variables desired called census-variables.csv from file
var_info = pd.read_csv('census-variables.csv')
#convert pandas series to a list
var_name = var_info['variable'].to_list()
#add NAME for clarity
var_list = ['NAME']+ var_name
#concatenate to a string
var_string = ','.join(var_list)

#OPTIONAL FOR IF YOU HAVE 2/3 VARIABLES which variable to use from ACS DEMOGRAPHIC AND HOUSING ESTIMATES 2018 5 year
##var_name = 'B01001_001E,B01001_002E,B01001_026E,B02001_001E,B02001_002E,B02001_003E,B02001_004E,B02001_005E,B02001_006E,B02001_007E,B02001_008E,B02001_009E,B02001_010E'
##var_list = 'NAME,' + var_name

api = 'https://api.census.gov/data/2018/acs/acs5'

#want data for all counties
for_clause = 'county:*'

#fips code for california
in_clause = 'state:06'

#api key
key_value = "af10e96213e12ad345f07e631862efd83ad3f365"

##FOR OPTIONAL USE var_list
#create a dictionary to hold results of census data
cd = {'get':var_string, 'for':for_clause, 'in':in_clause, 'key':key_value}

response = requests.get(api, cd)

#if statement test to see if it went right
if response.status_code == 200:
    print('Successful Request')
else:
    print(response.status_code)
    print(response.text)
    assert False
    #assert statement
    
rows = response.json()

colnames = rows[0]
datarows = rows[1:]

results = pd.DataFrame(columns = colnames, data = datarows)

results['fips'] = results['state'] + results['county']
results.set_index('fips', inplace=True)

results.to_csv("census-CA.csv")