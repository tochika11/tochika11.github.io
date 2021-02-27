import pickle
import json

MoveList={}
# -------------------------------------
# ShieldsLag
# -------------------------------------
with open("dict_ShieldsLag.pickle", mode='rb') as f:
    data = pickle.load(f)

print("dict_ShieldsLag")
for fighter in data.values():
    # print(fighter["fighter"], fighter)
    for move,frame in fighter["ShieldsLag"].items():
        # print(move,frame)
        moveProp = {"move": move , "type":"ShieldsLag"}
        # print(MoveList)
        if frame in MoveList :
            if fighter["fighter"] in MoveList[frame] :
                MoveList[frame][fighter["fighter"]]["move"].append(moveProp)
            else :
                MoveList[frame][fighter["fighter"]] = {"move" : [moveProp]}
        else :
            MoveList[frame] = {'fighter':fighter["fighter"], "move" : [moveProp]}

# -------------------------------------
# OutOfShieldStartup
# -------------------------------------
with open("dict_OutOfShieldStartup.pickle", mode='rb') as f:
    data = pickle.load(f)

print("dict_OutOfShieldStartup")
for fighter in data.values():
    # print(fighter["fighter"], fighter)
    for key,value in fighter["OosStartup"].items():
        move = key
        frame = value["back"]
        # print(move,frame)
        moveProp = {"move": move , "type":"OosStartup" + "back"}
        # print(MoveList)
        if frame in MoveList :
            if fighter["fighter"] in MoveList[frame] :
                MoveList[frame][fighter["fighter"]]["move"].append(moveProp)
            else :
                MoveList[frame][fighter["fighter"]] = {"move" : [moveProp]}
        else :
            MoveList[frame] = {'fighter':fighter["fighter"], "move" : [moveProp]}

# -------------------------------------
# CharacterList
# -------------------------------------
with open("dict_CharacterList.pickle", mode='rb') as f:
    data = pickle.load(f)

print("dict_CharacterList")

def dispInvalidFrame(key, value):

    delimiter = '-------------\n'
    print(delimiter)
    ignoreList = ['DontHave']
    if key in ignoreList :
        print(key,type(key)," is ignored")
        return
    
    warningList = ['ToBeUpdated']
    if key in warningList :
        print(key,type(key)," is in warning", value)
        return

    print(key,type(key)," is not int", value)
    return 

# check not int
for key, value in MoveList.items():
    if not key.isdecimal() :
        try :
            floatKey = float(key)
            q,mod = divmod(floatKey, 1)
            if q == floatKey and mod == 0:
                print(floatKey, '->', int(floatKey))
                floatKey = int(floatKey)
            if type(floatKey) is not int:
                dispInvalidFrame(floatKey, value)
        except ValueError:
            print('ValueError')
            dispInvalidFrame(key, value)
