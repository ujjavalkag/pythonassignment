ds={
        'office':{
                    'medical':[{'room-number':'100','use':'reception','sq-ft':'50','price':'75'},
                               {'room-number':'101','use':'waiting','sq-ft':'250','price':'75'},
                               {'room-number':'102','use':'examination','sq-ft':'125','price':'150'},
                               {'room-number':'103','use':'examination','sq-ft':'125','price':'150'},
                               {'room-number':'104','use':'office','sq-ft':'150','price':'100'}],
                    'parking':{'location':'premium','style':'covered','price':'750'}
                               
    
        }
    }
d='parking'
for x in ds:
    if d in ds[x]:
        for s in ds[x][d]:
            print(ds[x][d][s])
            '''
for x in ds:
    if 'medical' in ds[x]:
        for i in range(len(ds[x]['medical'])):
            print(ds[x]['medical'][i])
                  
d=input('madical or parking:')
v=input('enter key values:')
g=input('enter old value:')
j=input('enter new value:')
for x in ds:
    if d in ds[x]:
        if ds[x][d][v]==g:
            ds[x][d][v]=j            
'''        
    
