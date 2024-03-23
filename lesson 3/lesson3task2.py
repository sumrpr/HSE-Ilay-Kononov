import json
import re
inndict = {}
def emailfinder(m):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return(re.findall(pattern, m))
rows = []
traders = open('1000_efrsb_messages.json', 'r')
traderslist = json.load(traders)
for m in traderslist:
    inn = m['publisher_inn']
    emails = emailfinder(m['msg_text'])
    if inn and emails:
        inndict[inn] = emails
jsonfile = open("emails.json", "w")  
json.dump(inndict, jsonfile, indent = 6)