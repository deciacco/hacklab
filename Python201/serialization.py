import pickle

hackers = {"neug": 1, "geohot": 100, "neo": 1000}

for key, value in hackers.items():
	print(key, value)
print ("-"*50)

serialized = pickle.dumps(hackers)
print(serialized)

print ("-"*50)

hackers_v2 = pickle.loads(serialized)

for key, value in hackers_v2.items():
	print(key, value)

print ("-"*50)

# save serialized object to file
#with open("hackers.pickle", "wb") as hndl:
#	pickle.dump(hackers, hndl)

# read serialized object from file
with open("hackers.pickle", "rb") as hndl:
	hackers_v3 = pickle.load(hndl)
print(hackers_v3)