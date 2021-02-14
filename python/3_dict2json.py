import pickle
import json

# -------------------------------------
# ShieldsLag
# -------------------------------------
with open("dict_ShieldsLag.pickle", mode='rb') as f:
    data = pickle.load(f)

#print(data)

sd = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2)
# print(sd)

with open("ShieldsLag.json", mode='w') as f:
    json.dump(data, f, sort_keys=True, ensure_ascii=False, indent=2)

# -------------------------------------
# OutOfShieldStartup
# -------------------------------------
with open("dict_OutOfShieldStartup.pickle", mode='rb') as f:
    data = pickle.load(f)

#print(data)

sd = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2)
# print(sd)

with open("OutOfShieldStartup.json", mode='w') as f:
    json.dump(data, f, sort_keys=True, ensure_ascii=False, indent=2)
