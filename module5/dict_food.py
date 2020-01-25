food={
    'fruits':{
        'apple':{
        'major_producer':'india',
        'protien_val':1.5,
        'fat'       :0.5,
        'carbo'    :2.4
        },
        'banana':{
        'major_producer':'us',
        'protien_val':2.5,
        'fat'       :0.7,
        'carbo'    :2.0
        }
        }
    }
maxv=0
foodt=''
for x in food:
    for y in food[x]:
        if food[x][y]['protien_val']>maxv:
            foodt=y
            maxv=food[x][y]['protien_val']
print(foodt,maxv)            
            
