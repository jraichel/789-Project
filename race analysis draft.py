#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:08:56 2020

@author: jenniferraichel
"""

#Import modules needed for setup
import csv
import pandas as pd

#use variable name as csv file may change
csvname = 'census-CA.csv'

#don't let pandas suppress rows
pd.set_option('display.max_rows', None)

var_info = pd.read_csv('census-variables.csv', index_col='variable')

var_group = var_info['table']

print(var_group)

interest = pd.read_csv('census-CA.csv', index_col='NAME')

group_by_table = interest.groupby(var_group, axis='columns', sort=False)

by_table = group_by_table.sum()

tables = ['White', 'Black', 'American Indian or Alaska Native', 'Asian', 'Native Hawaiian', 'Other']

by_table['check'] = by_table[tables].sum(axis='columns')

print(by_table)

pct = by_table.div(by_table['Total Race'], axis='index')*100

print(pct['Black'])