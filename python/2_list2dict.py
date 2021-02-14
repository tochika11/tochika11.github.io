import pickle
import pprint

print("generate ShieldLag")
#list_ShieldLagGround
#load pickle
with open("list_ShieldLag.pickle", mode='rb') as f:
    data = pickle.load(f)

#print(data)

FIGHTER_NAME_IGNORE="DLC"

#list2dict
ShieldsLag={}
for idx,elem in enumerate(data):
    if idx==0:
        continue
    if idx==1:
        continue

    _tmp_ShieldsLag={}
    _tmp_ShieldsLag["No."]           =elem[0]
    _tmp_ShieldsLag["fighter"]       =elem[1]

    if FIGHTER_NAME_IGNORE in _tmp_ShieldsLag["fighter"]:
        continue

    _move={}
    _move["弱3"]           =elem[13]
    _move["百列〆"]        =elem[17]
    _move["ダッシュ攻撃"]   =elem[21]
    _move["横強"]          =elem[25]
    _move["上強"]          =elem[29]
    _move["下強"]          =elem[32]
    _move["横スマッシュ"]   =elem[37]
    _move["上スマッシュ"]   =elem[41]
    _move["下スマッシュ"]   =elem[45]
    _tmp_ShieldsLag["ShieldsLag"] = _move

    ShieldsLag[_tmp_ShieldsLag["fighter"]]=_tmp_ShieldsLag

#print(ShieldsLag["1"])
#print(ShieldsLag["21'"])
#print(ShieldsLag)

#list_ShieldLagGround
#load pickle
with open("list_ShieldLagAerial.pickle", mode='rb') as f:
    data = pickle.load(f)

ShieldsLagGroudFighterName_KeyIsAerial = {
    'サムス': {'FighterName':{'Ground': 'サムス・ダークサムス'}},
    'ピーチ': {'FighterName':{'Ground': 'ピーチ・デイジー'}},
    'ピット': {'FighterName':{'Ground': 'ピット・ブラックピット'}},
    'シモン': {'FighterName':{'Ground': 'シモン・リヒター'}},
}

#list2dict
for idx,elem in enumerate(data):
    if idx==0:
        continue
    if idx==1:
        continue

    _tmp_ShieldsLag={}
    _tmp_ShieldsLag["No."]           =elem[0]
    _tmp_ShieldsLag["fighter"]       =elem[1]

    if FIGHTER_NAME_IGNORE in _tmp_ShieldsLag["fighter"]:
        continue

    _move={}
    _move["通常空中攻撃"]   =elem[8]
    _move["前空中攻撃"]     =elem[15]
    _move["後空中攻撃"]     =elem[22]
    _move["上空中攻撃"]     =elem[29]
    _move["下空中攻撃"]     =elem[36]
    _tmp_ShieldsLag["ShieldsLag"] = _move

#    print(_tmp_ShieldsLag["No."])
    if _tmp_ShieldsLag["fighter"] in ShieldsLag:
#        print("append",_tmp_ShieldsLag)
#        print("to", ShieldsLag[_tmp_ShieldsLag["fighter"]])
#        ShieldsLag[_tmp_ShieldsLag["fighter"]].update(_tmp_ShieldsLag)
        ShieldsLag[_tmp_ShieldsLag["fighter"]]["ShieldsLag"].update(_tmp_ShieldsLag["ShieldsLag"])
    else:
        if _tmp_ShieldsLag["fighter"] in ShieldsLagGroudFighterName_KeyIsAerial:
            print("unmatch fighter name. append areal ShieldsLag.")
            GroundFighterName = ShieldsLagGroudFighterName_KeyIsAerial[_tmp_ShieldsLag["fighter"]]['FighterName']['Ground']
            print(_tmp_ShieldsLag["fighter"], '->', GroundFighterName)

            ShieldsLag[GroundFighterName]["ShieldsLag"].update(_tmp_ShieldsLag["ShieldsLag"])
        else:
            print("new key",_tmp_ShieldsLag["fighter"], _tmp_ShieldsLag)
            ShieldsLag[_tmp_ShieldsLag["fighter"]]=_tmp_ShieldsLag

#print(ShieldsLag)

with open("dict_ShieldsLag.pickle", mode='wb') as f:
    pickle.dump(ShieldsLag,f)


#-------------------------------------------
# dict_OutOfShieldStartup
#-------------------------------------------
print("\ngenerate OutOfShieldStartup")
#load pickle
with open("list_OutOfSheildStartupForward.pickle", mode='rb') as f:
    data = pickle.load(f)

#list2dict
OutOfSheildStartup={}
for idx,elem in enumerate(data):
    if idx==0:
        continue
    if idx==1:
        continue

    _tmp={}
    _tmp["No."]           =elem[0]
    _tmp["fighter"]       =elem[1]

    if _tmp["No."] == "":
        continue
    if _tmp["fighter"] == "":
        continue

    _move={}
    _move['空N']            ={'forward' : elem[12]}
    _move['空前']             ={'forward' : elem[13]}
    _move['空後']             ={'forward' : elem[14]}
    _move['空上']             ={'forward' : elem[15]}
    _move['空下']            ={'forward' : elem[16]}
    _move['つかみ']          ={'forward' : elem[17]}
    _move['上スマ']           ={'forward' : elem[18]}
    _move['上B']             ={'forward' : elem[19]}
    _move['弱']			    ={'forward' : elem[20]}
    _move['DA']		    	={'forward' : elem[21]}
    _move['横強']			={'forward' : elem[22]}
    _move['上強']			={'forward' : elem[23]}
    _move['下強']			={'forward' : elem[24]}
    _move['横スマ']			={'forward' : elem[25]}
    _move['下スマ']			={'forward' : elem[26]}

    _tmp['OosStartup'] = _move
#    print(_tmp)
    OutOfSheildStartup[_tmp["fighter"]]=_tmp

# print("Oos move forward")
# print(OutOfSheildStartup)
# print(OutOfSheildStartup['1'])

#load pickle
with open("list_OutOfSheildStartupBack.pickle", mode='rb') as f:
    data = pickle.load(f)

#list2dict
for idx,elem in enumerate(data):
    if idx==0:
        continue
    if idx==1:
        continue

    _tmp={}
    _tmp["No."]           =elem[0]
    _tmp["fighter"]       =elem[1]
    if _tmp["No."] == "":
        continue
    if _tmp["fighter"] == "":
        continue

    if _tmp["fighter"] in OutOfSheildStartup:
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空N'].update({'back' : elem[12]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空前'].update({'back' : elem[13]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空後'].update({'back' : elem[14]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空上'].update({'back' : elem[15]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空下'].update({'back' : elem[16]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['つかみ'].update({'back' : elem[17]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['上スマ'].update({'back' : elem[18]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['上B'].update({'back' : elem[19]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['弱'].update({'back' : elem[20]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['DA'].update({'back' : elem[21]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['横強'].update({'back' : elem[22]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['上強'].update({'back' : elem[23]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['下強'].update({'back' : elem[24]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['横スマ'].update({'back' : elem[25]})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['下スマ'].update({'back' : elem[26]})
    else:
        _move={}
        _move['空N']             ={'back' : elem[12]}
        _move['空前']            ={'back' : elem[13]}
        _move['空後']            ={'back' : elem[14]}
        _move['空上']            ={'back' : elem[15]}
        _move['空下']            ={'back' : elem[16]}
        _move['つかみ']          ={'back' : elem[17]}
        _move['上スマ']          ={'back' : elem[18]}
        _move['上B']             ={'back' : elem[19]}
        _move['弱']			     ={'back' : elem[20]}
        _move['DA']		    	 ={'back' : elem[21]}
        _move['横強']			 ={'back' : elem[22]}
        _move['上強']			 ={'back' : elem[23]}
        _move['下強']			 ={'back' : elem[24]}
        _move['横スマ']			 ={'back' : elem[25]}
        _move['下スマ']			 ={'back' : elem[26]}
        _tmp['OosStartup']       = _move

        # print('append new fighter. ', _tmp)
        OutOfSheildStartup[_tmp["fighter"]]=_tmp

# print("Oos move all")
# print(OutOfSheildStartup)
#print(OutOfSheildStartup['1'])

with open("dict_OutOfShieldStartup.pickle", mode='wb') as f:
    pickle.dump(OutOfSheildStartup,f)

#-------------------------------------------
# CharacterList
#-------------------------------------------
print("\ngenerate CharacterList")

CharacterList={}
# print("OutOfSheildStartup")
for elem in OutOfSheildStartup.values():
    # print(elem)
    if elem["fighter"] == "":
        continue

    _tmp={}
    _tmp["fighter"]     =elem["fighter"]
    _tmp["No."]         =elem["No."]
    _tmp["property"]    ={"OutOfSheildStartup": True}
    if _tmp["fighter"] in CharacterList:
        print("error. conflict in OutOfSheildStartup", CharacterList[_tmp["fighter"]], elem)
    else:
        CharacterList[_tmp["fighter"]] = _tmp

# print("ShieldsLag")
for elem in ShieldsLag.values():
    if elem["fighter"] == "":
        continue

    _tmp={}
    _tmp["fighter"]     =elem["fighter"]
    _tmp["No."]         =elem["No."]
    if _tmp["fighter"] in CharacterList:
        if CharacterList[_tmp["fighter"]]["No."] != elem["No."]:
            print("warning. mismatch No. OutOfSheildStartup vs ShieldLag")
            print("fighter ", _tmp["fighter"])
            print("OutOfSheildStartup ", _tmp["No."])
            print("ShieldsLag ", elem["No."])
        CharacterList[_tmp["fighter"]]["property"].update({"ShieldsLag": True})
    else:
        _tmp["property"]    ={"ShieldsLag": True}

        CharacterList[_tmp["fighter"]] = _tmp
        # print("append new fighter name from ShieldsLag", _tmp)

#-------------------------------
# check property
#-------------------------------
for elem in CharacterList.values():
    if 'ShieldsLag' not in elem['property']:
        elem['property'].update({"ShieldsLag": False})
        print('ShieldsLag is not defined.', elem['fighter'], elem['No.'])
    if 'OutOfSheildStartup' not in elem['property']:
        elem['property'].update({"OutOfSheildStartup": False})
        print('OutOfSheildStartup is not defined.', elem['fighter'], elem['No.'])

# print(CharacterList)

with open("dict_CharacterList.pickle", mode='wb') as f:
    pickle.dump(CharacterList,f)

