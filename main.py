import xmltodict,json

f = open('xml.xml')
text=f.read()
f.close()
o = xmltodict.parse(text)
text=json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
f = open('json.json','w')
f.write(text)
f.close()
print(text)