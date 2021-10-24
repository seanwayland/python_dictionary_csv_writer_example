results = {'counties_dict': {'NJ': 57, 'NY': 25}, 'candidates_dict': {'bob': 57, 'sean': 25}}

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

