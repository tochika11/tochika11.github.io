import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pickle

#authorize
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

json_key = "smash-sandbox-9aeb91a4ca12.json"
sheet_name = "スマブラSP データいろいろ (Ver.9.0.0) "
sheet_key = '1eKF4JTeOnn42Xz9PfxTnxvVr3ITmpykx2pFPd658HLU'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
gc=gspread.authorize(credentials)


#sheet access

#access by name
#wks=gc.open(sheet_name)
#print(wks.id)

#access by key
workbook = gc.open_by_key(sheet_key)
print(workbook.title)
print(workbook.id)

#sheet ガード硬直差(地上攻撃)

worksheet = workbook.worksheet("ガード硬直差(地上攻撃)")

#print all value
list_of_lists = worksheet.get_all_values()
#print(list_of_lists)

#取得対象
#弱３、百列〆、ダッシュ攻撃、横強、上強、下強、横スマッシュ、上スマッシュ、下スマッシュ

#print all records:対象データは辞書用のキー情報が不足しているため使用できない。
#dict_of_dict = worksheet.get_all_records()
#print(dict_of_dict)

with open("list_ShieldLagGround.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)



#sheet ガード硬直差(空中攻撃)

worksheet = workbook.worksheet("ガード硬直差(空中攻撃)")

#print all value
list_of_lists = worksheet.get_all_values()
print(list_of_lists)

#取得対象
#弱３、百列〆、ダッシュ攻撃、横強、上強、下強、横スマッシュ、上スマッシュ、下スマッシュ

#print all records:対象データは辞書用のキー情報が不足しているため使用できない。
#dict_of_dict = worksheet.get_all_records()
#print(dict_of_dict)

with open("list_ShieldLagAerial.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)


#sheet ガード硬直後最速行動(前)
worksheet = workbook.worksheet("ガード硬直後最速行動(前)")

#print all value
list_of_lists = worksheet.get_all_values()
print(list_of_lists)

with open("list_OutOfSheildStartupForward.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)

#sheet ガード硬直後最速行動(後)
worksheet = workbook.worksheet("ガード硬直後最速行動(後)")

#print all value
list_of_lists = worksheet.get_all_values()
print(list_of_lists)

with open("list_OutOfSheildStartupBack.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)