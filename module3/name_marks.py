x=input('enter credentials').split(',')
t='{} obtain {} marks out of 460 in theory and {} marks out of 40 in practical and successfully passes the exam with {}% in aggregate.many congratulations to {}'
sum1=int(x[1])+int(x[2])+int(x[3])+int(x[4])+int(x[5])
psum=int(x[6])+int(x[7])+int(x[8])
ps=(sum1/500)*100
print(t.format(x[0],sum1,psum,ps,x[0]))
