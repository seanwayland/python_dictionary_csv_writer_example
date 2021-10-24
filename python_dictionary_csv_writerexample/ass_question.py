

import csv
results_dict = { "counties_dict" : {}, "candidates_dict" : {} } 
with open('sample_data.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        print(row)
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


print("results")
print(results_dict)

