import pickle
import pprint

def modifyFrame(key):
    result = 'unknown'
    if not key.isdecimal() :
        ignoreList = ['','-',' ']
        if key in ignoreList:
            result = 'DontHave'
            # it means that the fighter does Not have this move.
        else :
            try :
                floatKey = float(key)
                q,mod = divmod(floatKey, 1)
                if q == floatKey and mod == 0:
                    print(key,'->',str(int(floatKey)))
                    result = str(int(floatKey))  # integer
                else:
                    result = key  # float. maybe it means that tool(sheet2list) has any glitches.
            except ValueError:
                result = 'ToBeUpdated'
                # maybe it means that data source is on comments or has some lines.
                # so if we update tools, then frame data will be available.
    else:
        result = key # integer
    return result

print("generate SheetProperties")
with open("list_SheetProperties.pickle", mode='rb') as f:
    data = pickle.load(f)

dict_of_dict={}
for value in data:
    dict_of_dict.update(value)

print(dict_of_dict)
with open("dict_SheetProperties.pickle", mode='wb') as f:
    pickle.dump(dict_of_dict,f)


print("generate ShieldLag")
#list_ShieldLagGround
#load pickle
with open("list_ShieldLag.pickle", mode='rb') as f:
    data = pickle.load(f)


FIGHTER_NAME_IGNORE="DLC"

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
    _move["弱3"]           =modifyFrame(elem[13])
    _move["百列〆"]        =modifyFrame(elem[17])
    _move["ダッシュ攻撃"]   =modifyFrame(elem[21])
    _move["横強"]          =modifyFrame(elem[25])
    _move["上強"]          =modifyFrame(elem[29])
    _move["下強"]          =modifyFrame(elem[33])
    _move["横スマッシュ"]   =modifyFrame(elem[37])
    _move["上スマッシュ"]   =modifyFrame(elem[41])
    _move["下スマッシュ"]   =modifyFrame(elem[45])
    _tmp_ShieldsLag["ShieldsLag"] = _move

    ShieldsLag[_tmp_ShieldsLag["fighter"]]=_tmp_ShieldsLag

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
    _move["通常空中攻撃"]   =modifyFrame(elem[8])
    _move["前空中攻撃"]     =modifyFrame(elem[15])
    _move["後空中攻撃"]     =modifyFrame(elem[22])
    _move["上空中攻撃"]     =modifyFrame(elem[29])
    _move["下空中攻撃"]     =modifyFrame(elem[36])
    _tmp_ShieldsLag["ShieldsLag"] = _move

    if _tmp_ShieldsLag["fighter"] in ShieldsLag:
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
    _move['空N']            ={'forward' : modifyFrame(elem[12])}
    _move['空前']             ={'forward' : modifyFrame(elem[13])}
    _move['空後']             ={'forward' : modifyFrame(elem[14])}
    _move['空上']             ={'forward' : modifyFrame(elem[15])}
    _move['空下']            ={'forward' : modifyFrame(elem[16])}
    _move['つかみ']          ={'forward' : modifyFrame(elem[17])}
    _move['上スマ']           ={'forward' : modifyFrame(elem[18])}
    _move['上B']             ={'forward' : modifyFrame(elem[19])}
    _move['弱']			    ={'forward' : modifyFrame(elem[20])}
    _move['DA']		    	={'forward' : modifyFrame(elem[21])}
    _move['横強']			={'forward' : modifyFrame(elem[22])}
    _move['上強']			={'forward' : modifyFrame(elem[23])}
    _move['下強']			={'forward' : modifyFrame(elem[24])}
    _move['横スマ']			={'forward' : modifyFrame(elem[25])}
    _move['下スマ']			={'forward' : modifyFrame(elem[26])}

    _tmp['OosStartup'] = _move
    OutOfSheildStartup[_tmp["fighter"]]=_tmp

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
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空N'].update({'back' : modifyFrame(elem[12])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空前'].update({'back' : modifyFrame(elem[13])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空後'].update({'back' : modifyFrame(elem[14])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空上'].update({'back' : modifyFrame(elem[15])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['空下'].update({'back' : modifyFrame(elem[16])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['つかみ'].update({'back' : modifyFrame(elem[17])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['上スマ'].update({'back' : modifyFrame(elem[18])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['上B'].update({'back' : modifyFrame(elem[19])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['弱'].update({'back' : modifyFrame(elem[20])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['DA'].update({'back' : modifyFrame(elem[21])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['横強'].update({'back' : modifyFrame(elem[22])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['上強'].update({'back' : modifyFrame(elem[23])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['下強'].update({'back' : modifyFrame(elem[24])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['横スマ'].update({'back' : modifyFrame(elem[25])})
        OutOfSheildStartup[_tmp["fighter"]]['OosStartup']['下スマ'].update({'back' : modifyFrame(elem[26])})
    else:
        _move={}
        _move['空N']             ={'back' : modifyFrame(elem[12])}
        _move['空前']            ={'back' : modifyFrame(elem[13])}
        _move['空後']            ={'back' : modifyFrame(elem[14])}
        _move['空上']            ={'back' : modifyFrame(elem[15])}
        _move['空下']            ={'back' : modifyFrame(elem[16])}
        _move['つかみ']          ={'back' : modifyFrame(elem[17])}
        _move['上スマ']          ={'back' : modifyFrame(elem[18])}
        _move['上B']             ={'back' : modifyFrame(elem[19])}
        _move['弱']			     ={'back' : modifyFrame(elem[20])}
        _move['DA']		    	 ={'back' : modifyFrame(elem[21])}
        _move['横強']			 ={'back' : modifyFrame(elem[22])}
        _move['上強']			 ={'back' : modifyFrame(elem[23])}
        _move['下強']			 ={'back' : modifyFrame(elem[24])}
        _move['横スマ']			 ={'back' : modifyFrame(elem[25])}
        _move['下スマ']			 ={'back' : modifyFrame(elem[26])}
        _tmp['OosStartup']       = _move

        OutOfSheildStartup[_tmp["fighter"]]=_tmp

with open("dict_OutOfShieldStartup.pickle", mode='wb') as f:
    pickle.dump(OutOfSheildStartup,f)

#-------------------------------------------
# CharacterList
#-------------------------------------------
print("\ngenerate CharacterList")

CharacterList={}
for elem in OutOfSheildStartup.values():
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

with open("dict_CharacterList.pickle", mode='wb') as f:
    pickle.dump(CharacterList,f)

