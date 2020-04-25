# This project uses data obtained from the NYTimes and the Census. Data from the
NYTimes contains cumulative numbers of Coronavirus cases and related deaths
beginning January 21, 2020. I pull race and sex Census data from the ACS 5-year
survey as of 2018. Using this data to understand reports of Coronavirus and related
deaths affecting people of color, specifically African Americans, at higher rates
than it does white people. For this instance we use California.

# Initial script
1. Import the following modules; requests, pandas, numpy, and csv.
2. Have python read the csv file 'census-variables.csv' containing the desired
census variables. Assign it the name var_info
3. Set another variable to the 'variable' column of var_info with the .to_list()
method applied to the end
4. Add 'NAME' to the list of variables by setting var_list to ['NAME']+var_name
5. Concatenate the variables to a string
6. Set the api call to api = 'https://api.census.gov/data/2018/acs/acs5', the for
clause for all the counties (use 'county:*'), the in clause to '06' for California,
and the key to your own Census API key
7. Create a new dictionary containing the following: 'get':var_string,
'for':for_clause, 'in':in_clause, 'key':key_value
8. Set response to the value of calling requests.get() with the api and dictionary
arguments
9. Set rows to response.json()
10. Set variable name colnames to the first row of rows and datarows
11. Convert the data into a usable Pandas data frame, setting the columns to
colnames and data to datarows as the arguments.
12. Set the index of the dataframe to the column 'NAME'
13. Write the data to a csv file.
