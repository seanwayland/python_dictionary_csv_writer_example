
##3 sample data 
### nested list with list for each row of income data 
#data = [['bob', '23', 'NJ'],['bob','34', 'NJ'],['sean','25', 'NY']]



import csv
states_dict = {}
canditates_dict = {}
with open('sample_data.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for r in datareader:
        print(r)
        if r[2] not in states_dict:
            # create a key with a value of zero 
            states_dict[r[2]] = 0
            print("state not a key")
            print(states_dict)
        
        # add the row votes to the totoal for that state 
        states_dict.update({r[2]: states_dict.get(r[2]) + int(r[1])})
        print("state updated after this row ")
        print(states_dict)

print("final output dictionary ")
print(states_dict)



