import csv
arr = []
with open('data.csv', 'r') as f:
     reader = csv.reader(f)
     for row in reader:
         tempdict  = {}
         tempdict['shopId'] = row[0]
         tempdict['price'] = row[1]
         tempdict['name'] = row[2]
         arr.append(tempdict)
         tempdict  = {}

prod1 = []
prod2 = []
price = 10000000
id = ''
for a in arr :
    if(a['name'] == 'teddy_bear'):
        prod1.append(a)

   
for a in arr :
    if(a['name']=='baby_powder'):
        prod2.append(a)



for x in prod1:
    for y in prod2:
        if(x['shopId'] == y['shopId']):
            temp = float(x['price']) + float(y['price'])
            if(price > temp) :
                price = temp
                id = x['shopId']

print (id, price)
for a in arr :
    if(a['name'] == 'scissor'):
        prod1.append(a)

   
for a in arr :
    if(a['name']=='bath_towel'):
        prod2.append(a)


for x in prod1:
    for y in prod2:
        if(x['shopId'] == y['shopId']):
            temp = float(x['price']) + float(y['price'])
            if(price > temp) :
                price = temp
                id = x['shopId']

print (id, price)

