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
        
f=info()
f.set_name('uk')
f.set_phone('876653679')
f.set_email('ghhjj@dfgf.klk')
fs=open('rtk.txt','wb')
pickle.dump(f,fs)
fs.close()
fs=open('rtk.txt','rb')
sa=info()
sa=pickle.load(fs)
fs.close()
print(sa.__str__())
