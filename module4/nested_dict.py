dict1={
    1:{'fistname':'u',
       'middlename':'None'
        },
    2:{
        'age':21
        },

    3:{'sex':'male'
        }
    }
dict1[1]['lastname']='k'
del(dict1[1]['middlename'])
dict1[2]['bday']='31/02/0000'
dict1[3]['checked']='yassssssssss'
for x in dict1:
    for y in dict1[x]:
            print(y,dict1[x][y])
    print()    
