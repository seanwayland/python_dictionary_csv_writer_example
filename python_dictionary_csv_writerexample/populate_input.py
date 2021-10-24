##3 sample data 
### nested list with list for each row of income data 
data = [['23', 'bob', 'NJ'],['34','bob', 'NJ'],['25','sean', 'NY']]
### data format : votes, candidate, county 

### initialize a results dictionary 
### it has 2 keys . counties and canditates and a value as a dictionary to store each set of results

results_dict = { "counties_dict" : {}, "candidates_dict" : {} } 

### loop through the data to process 

for row in data:
    # populate counties_dict 
    # if the county of the data is not in the counties dict add it as a key 
    county = row[2]
    if county not in results_dict["counties_dict"]:
        # create a key with the name of the county and a value zero 
        results_dict["counties_dict"][county] = 0
    ## add the votes to the current county 
    results_dict["counties_dict"][county] = results_dict["counties_dict"][county] + int(row[0])


    # populate canditates_dict 

    candidates = row[1]
    if candidates not in results_dict["candidates_dict"]:
        # create a key with the name of the county and a value zero 
        results_dict["candidates_dict"][candidates] = 0
    ## add the votes to the current county 
    results_dict["candidates_dict"][candidates] = results_dict["candidates_dict"][candidates] + int(row[0])

print(results_dict)

results = results_dict 

totalcountyvotes = sum(results['counties_dict'].values())
print("total county votes")
print(totalcountyvotes)

for k, v in results['counties_dict'].items():
    print("votes per county")
    print(k, v)
    print("percent voters per county")
    print(k, v/totalcountyvotes * 100)

print("winning county is ")
print(max(results['counties_dict'], key=results['counties_dict'].get))










