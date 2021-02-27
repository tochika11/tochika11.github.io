import pickle
import json
import os

OUTPUT_DIR='json/'
os.makedirs(OUTPUT_DIR, exist_ok=True)
# -------------------------------------
# SheetProperties
# -------------------------------------
with open("dict_SheetProperties.pickle", mode='rb') as f:
    data = pickle.load(f)

sd = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2)
with open(OUTPUT_DIR+"SheetProperties.json", mode='w') as f:
    json.dump(data, f, sort_keys=True, ensure_ascii=False, indent=2)


# -------------------------------------
# ShieldsLag
# -------------------------------------
with open("dict_ShieldsLag.pickle", mode='rb') as f:
    data = pickle.load(f)

sd = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2)
with open(OUTPUT_DIR+"ShieldsLag.json", mode='w') as f:
    json.dump(data, f, sort_keys=True, ensure_ascii=False, indent=2)

# -------------------------------------
# OutOfShieldStartup
# -------------------------------------
with open("dict_OutOfShieldStartup.pickle", mode='rb') as f:
    data = pickle.load(f)

sd = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2)
with open(OUTPUT_DIR+"OutOfShieldStartup.json", mode='w') as f:
    json.dump(data, f, sort_keys=True, ensure_ascii=False, indent=2)

# -------------------------------------
# CharacterList
# -------------------------------------
with open("dict_CharacterList.pickle", mode='rb') as f:
    data = pickle.load(f)

sd = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2)
with open(OUTPUT_DIR+"CharacterList.json", mode='w') as f:
    json.dump(data, f, sort_keys=True, ensure_ascii=False, indent=2)