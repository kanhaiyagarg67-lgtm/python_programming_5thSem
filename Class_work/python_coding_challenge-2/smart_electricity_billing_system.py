'''Problem 1: Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate the total units consumed.  
5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  '''


units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house)

# Convert dictionary items to list
dict_items = list(units.items())

# 2. Find highest-consuming house
highest_house = dict_items[0][0]
highest_units = dict_items[0][1]

for house, unit in units.items():
    if unit > highest_units:
        highest_units = unit
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest_units, "units )")

# 3. Find lowest-consuming house
lowest_house = dict_items[0][0]
lowest_units = dict_items[0][1]

for house, unit in units.items():
    if unit < lowest_units:
        lowest_units = unit
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, "(", lowest_units, "units )")

# 4. Calculate total units consumed
total_units = 0
for unit in units.values():
    total_units = total_units + unit

print("\nTotal Units Consumed:", total_units)

# 5. Create separate lists
low = []
medium = []
high = []

for house, unit in units.items():
    if unit < 200:
        low.append(house)
    elif unit <= 400:
        medium.append(house)
    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# 6. Count houses eligible for energy-saving campaign
campaign = 0
for unit in units.values():
    if unit > 300:
        campaign = campaign + 1

print("\nEligible for Energy-Saving Campaign:", campaign)

'''
Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5
