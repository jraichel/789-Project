# This project uses data obtained from the NYTimes and the Census. Data from the NYTimes contains cumulative numbers of Coronavirus cases and related deaths beginning January 21, 2020. I pull race and sex Census data from the ACS 5-year survey as of 2018. Using this data to understand reports of Coronavirus and related deaths affecting people of color, specifically African Americans, at higher rates than it does white people.
For this instance we use California. Download NYTimes Covid data https://github.com/nytimes/covid-19-data

# Initial script to acquire and organize Census data
1. Import the following modules; requests, pandas, numpy, and csv.
2. Have python read the csv file 'census-variables.csv' containing the desired census variables. Assign it the name var_info
3. Set another variable to the 'variable' column of var_info with the .to_list() method applied to the end
4. Add 'NAME' to the list of variables by setting var_list to ['NAME']+var_name
5. Concatenate the variables to a string
6. Set the api call to api = 'https://api.census.gov/data/2018/acs/acs5', the for clause for all the counties (use 'county:star'), the in clause to '06' for California, and the key to your own Census API key
7. Create a new dictionary containing the following: 'get':var_string, 'for':for_clause, 'in':in_clause, 'key':key_value
8. Set response to the value of calling requests.get() with the api and dictionary arguments
9. Set rows to response.json()
10. Set variable name colnames to the first row of rows and datarows
11. Convert the data into a usable Pandas data frame, setting the columns to colnames and data to datarows as the arguments.
12. Set the index of the dataframe to the column 'NAME'
13. Write the data to a csv file.

# Analysis script
1. Import csv and pandas modules
2. Run the line pd.set_option('display.max_rows', None) so pandas does not limit the data
3. Make 'census-variables.csv' into a pandas dataframe including the index column 'variable'
4. Set var_group to the 'table' column of var_info
5. Read the census data csv ex 'census-CA.csv', use the argument index_col='NAME' to set the index to the column of county names
6. Set group_by_table to the result of applying the .groupby() method to the read file using the arguments var_group, axis='columns', and sort=False.
7. Aggregate using the .sum() method
8. Now you can compute percentages ratios for comparison

# Mapping in QGIS
1. Grab the 2018 US county shapefile from https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html
2. add the layer in QGIS
3. Filter layer to only California counties, code '06'
4. Export the layer as a gpkg
5. Add county name labels and turn on the text buffer around the name.
6. Add the csv files from the original script and 'us-counties.csv' from the NYTimes covid-19 dataset
7. Join the two csv layers on 'fips'
8. Construct a heat map based on cases or deaths
9. Add pie chart displaying ratio of white to African American race data
