import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pickle
import datetime

#authorize
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

json_key = "smash-sandbox-9aeb91a4ca12.json"
sheet_key = '1bdAEBAn1WlWcsJrJaCDrmIk97nHnj9yZy0TouFpmkiA' # original
# sheet_key = '1eKF4JTeOnn42Xz9PfxTnxvVr3ITmpykx2pFPd658HLU' # copied
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
gc = gspread.authorize(credentials)


#sheet access
#access by key
workbook = gc.open_by_key(sheet_key)

propertiesList = []
propertiesList.append({"title" : workbook.title})
propertiesList.append({"url" : workbook.url})
propertiesList.append({"id" : workbook.id})
_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
propertiesList.append({"datetime" : _datetime})

with open("list_SheetProperties.pickle", mode='wb') as f:
    pickle.dump(propertiesList,f)

#sheet ガード硬直差(地上攻撃)
worksheet = workbook.worksheet("ガード硬直差(地上攻撃)")
list_of_lists = worksheet.get_all_values()

#print all records:対象データは辞書用のキー情報が不足しているため使用できない。
with open("list_ShieldLagGround.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)

#sheet ガード硬直差(空中攻撃)
worksheet = workbook.worksheet("ガード硬直差(空中攻撃)")
list_of_lists = worksheet.get_all_values()

with open("list_ShieldLagAerial.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)


#sheet ガード硬直後最速行動(前)
worksheet = workbook.worksheet("ガード硬直後最速行動(前)")
list_of_lists = worksheet.get_all_values()

with open("list_OutOfSheildStartupForward.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)

#sheet ガード硬直後最速行動(後)
worksheet = workbook.worksheet("ガード硬直後最速行動(後)")
list_of_lists = worksheet.get_all_values()

with open("list_OutOfSheildStartupBack.pickle", mode='wb') as f:
    pickle.dump(list_of_lists,f)
