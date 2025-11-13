airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['RDU'] = }")
print(f"{airports.get('RDU') = }")

print(f"{airports.get('PHL') = }")
print(f"{airports.get('PHL', 'NOT FOUND') = }")
print(f"{airports.setdefault('PHL', 'Philadelphia') = }")

print(f"{'FOUND' if airports.get('PHL') else 'NOT FOUND'}")
print(f"{airports = }")
if 'PHL' in airports:
    print("FOUND")

airports['PHL'] = "City of Brotherly Love"
print(f"{airports = }")
print()

for key in airports.keys():
    print(key)
print()

for value in airports.values():
    print(value)
print()

for code, city in airports.items():
    print(code, city)
print()