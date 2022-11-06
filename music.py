N=int(input ('enter the amount of rows: '))
M=int(input ('enter the amount of columns: '))
row=[]
column=[]
for d in range(0,N):
    for b in range(0,M):
        row.append(int(input('enter a number: '))) 
    column.append(row)
    row=[]

def finder(r,c):
    
    if r<N:
        if int(row[r+1])%int(row[r])==0 or int(row[r])%int(row[r+1])==0 :
            r-=1
        else:
            r=r
        finder(r,c)
        
    elif r>0:
        if int(row[r+1])%int(row[r])==0 or int(row[r])%int(row[r+1])==0 :
            r+=1
        else:
            r=r
        finder(r,c)
    
    
    elif c<M:
        if int(column[c-1])%int(column[c])==0 or int(column[c])%int(column[c-1])==0 :
            c-=1
        else:
            c=c
        finder(r,c)
        
    elif c>0:
        if int(column[c+1])%int(column[c])==0 or int(column[c])%column(c+1==0) :
            c+=1
        else:
            c=c
        finder(r,c)
    elif r>N and c>M:
        if int(column[c+1])%int(column[c])==0 or int(column[c])%int(column[c+1])==0 and int(row[r+1])%int(row[r])==0 or int(row[r])%int(row[r+1])==0 :
            c+=1
            r+=1
        else:
            c=c
            r=r
        finder(r,c)
    elif r>N and c>0:
        if int(column[c+1])%int(column[c])==0 or int(column[c])%int(column[c+1])==0 and int(row[r-1])%int(row[r])==0 or int(row[r])%int(row[r-1])==0 :
            c+=1
            r-=1
        else:
            c=c
            r=r
        finder(r,c)
    elif r>0 and c>M:
        if int(column[c-1])%int(column[c])==0 or int(column[c])%int(column[c-1])==0 and int(row[r+1])%int(row[r])==0 or int(row[r])%int(row[r+1])==0 :
            c-=1
            r+=1
        else:
            c=c
            r=r
        finder(r,c)
    if r==N and c==M:
        print ('yes')
    else:
        print ('no')
        
finder(1,1)
        
    
        
    
    
    

    