import sys
import pickle
class info:
    def __init__(self):
        name=''
        phone=''
        email=''
    def set_name(self,name):
        self.name=name
    def set_phone(self,phone):
        self.phone=phone
    def set_email(self,email):
        self.email=email
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email
    def __str__(self):
        return f' {self.get_name()} {self.get_phone()} {self.get_email()}'
fs=open('rtk.txt','rb')
ds=pickle.load(fs)
ds=dict(ds)
while(1):
    print('1.info\n2.show\n3.file\n4.del\n5.search\n6.update\n7.exit')
    nt=int(input('enter your choice:'))
    if nt==1:
        f=info()
        x=input('enter name:')
        y=input('enter phone:')
        z=input('enter email:')
        f.set_name(x)
        f.set_phone(y)
        f.set_email(z)
        ds['name'].append(f.get_name())
        ds['contact'].append(f.get_phone())
        ds['email'].append(f.get_email())
    elif nt==2:
        print(ds)
    elif nt==3:
        print('file\n1.new/overwride\n2.show')
        ch=int(input('enter your choice:'))
        fn=input('enter file name with extension:')
        if ch==1:
            fs=open(fn,'wb')
            pickle.dump(ds,fs)
            fs.close()
        elif ch==2:
           fs=open(fn,'rb')
           st=pickle.load(fs)
           fs.close()
           print(st)
        else:
           print('invalid selection:')
    elif nt==4:
        dn=input('enter phone:')
        idn=0
        if 'contact' in ds:
            if len(ds['contact'])==0:
                print('empty first inser data')
            else:    
                for h in range(len(ds['contact'])):
                    if ds['contact'][h]==dn:
                        idn=h
                        break
                for xq in ds:
                    del (ds[xq][idn])
    elif nt==5:
        dn=input('enter phone:')
        idn=0
        if 'contact' in ds:
            if len(ds['contact'])!=0:
                for h in range(len(ds['contact'])):
                    if ds['contact'][h]==dn:
                        idn=h
                        break
                for xq in ds:
                    print(ds[xq][idn])
            else:
                print('empty list')
    elif nt==6:
        sn=input('enter key to update:')
        dn=input('enter new value to update:')
        cn=input('enter old contact number to check:')
        idn=0
        if sn in ds:
            for i in range(len(ds[sn])):
                if ds['contact'][i]==cn:
                    idn=i
                    break
        ds[sn][idn]=dn
    else:
        fs.close()
        fs=open('rtk.txt','wb')
        pickle.dump(ds,fs)
        fs.close()
        sys.exit(str(nt))

