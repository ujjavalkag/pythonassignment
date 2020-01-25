import sys
import pickle
def medical_val(d,ds):
    r=input('which room values you want to change:')
    f=input('enter key to change:')
    y=input('enter previous value:')
    j=input('enter new value:')
    for x in ds:
        if d in ds[x]:
                for i in range(len(ds[x][d])):
                    for c in ds[x][d][i]:
                        if ds[x][d][i][f]==y  and ds[x][d][i]['room-number']==r:
                            ds[x][d][i][f]=j
    d_show(d,ds)
    
def parking_val(d,ds):
    v=input('enter key values:')
    g=input('enter old value:')
    j=input('enter new value:')
    for x in ds:
        if d in ds[x]:
            if ds[x][d][v]==g:
                ds[x][d][v]=j
    s_show(d,ds)            

def s_show(d,ds):
    for x in ds:
        if d in ds[x]:
            for s in ds[x][d]:
                print(d,ds[x][d][s])

def d_show(d,ds):
    for x in ds:
        if d in ds[x]:
            for i in range(len(ds[x][d])):
                print(ds[x][d][i])
    
def main(ds):
    while(1):
        print('1.change attributes:\n2.addvalues:\n3.delvalues:\n4.add data to file defaut any value to exit:')
        ch=int(input('enter choice:'))
        if ch==1:
            call(ds)
        elif ch==2:
            addval(ds)
        elif ch==3:
            delval(ds)
        elif ch==4:
            file(ds)
        else:
            sys.exit(str(ch))
def file(ds):
    print('1.overwride/new file,2.read')
    nu=int(input('enter your choice:'))
    fn=input('enter file name with extension:')
    if nu==1:
        fs=open(fn,'wb')
        pickle.dump(ds,fs)
        fs.close()
    elif nu==2:
        fs=open(fn,'rb')
        dsd=pickle.load(fs)
        fs.close()
        print(dsd)
    
    
def call(ds):
    #q=input('list_dict or s_dict')
    d=input('enter which key attributes you want to change/medical/parking:')
    if d=='medical':
        medical_val(d,ds)
    else:
        parking_val(d,ds)

def addval(ds):
    w=input('newroom or newatt')
    p=input('enter location to enter value/medical/parking etc:')
    if w=='newroom' and p=='medical':
        rm=input('enter room number:')
        us=input('enter use:')
        ar=input('enter area:')
        pr=input('enter price:')
        (ds['office']['medical']).append({'room-number':rm,'use':us,'sq-ft':ar,'price':pr})
        d_show(p,ds)     
    elif w=='newatt' and p=='medical':
        rmn=input('enter room key to add attribute:')
        nat=input('enter new attributes:')
        nval=input('enter new attribute value:')
        for jh in range(len(ds['office']['medical'])):
            if ds['office']['medical'][jh]['room-number']==rmn:
                ds['office']['medical'][jh][nat]=nval
        d_show(p,ds)     
    else:
        nat=input('enter new attributes:')
        nval=input('enter new attribute value:')
        ds['office']['parking'][nat]=nval
        s_show(p,ds)
def delval(ds):
    w=input('delroom or delatt')
    p=input('enter location to enter value/medical/parking etc:')
    if w=='delroom' and p=='medical':
        rm=input('enter room number:')
        for dk in range(len(ds['office']['medical'])):
            if ds['office']['medical'][dk]['room-number']==rm:
                          (ds['office']['medical']).pop(dk)
                          break
        d_show(p,ds)     
    elif w=='delatt' and p=='medical':
        rmn=input('enter room key to delet attribute:')
        nat=input('enter attributes:')
        for jh in range(len(ds['office']['medical'])):
            if ds['office']['medical'][jh]['room-number']==rmn:
                del (ds['office']['medical'][jh][nat])
                break
        d_show(p,ds)     
    else:
        nat=input('enter new attributes:')
        del(ds['office']['parking'][nat])
        s_show(p,ds)
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

main(ds)
