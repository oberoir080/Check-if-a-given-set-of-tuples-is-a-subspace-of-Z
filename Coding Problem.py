elemts=[int(i) for i in input().split()]            #input of elements of W
tuple_list=[]
n=4

for i in range(0,len(elemts),n):
    tuple_list.append(tuple(elemts[i:i+n]))            #converts elements in "elemts" to tuples of 4


xoremptylst=[]                  #empty lists to check if W is a subspace of (Z/2Z)^4 under vector addition and scalar multiplication 
andemptylst=[]
andemptylst2=[]

for i in range(len(tuple_list)):                # this loop performs vector addition
    for j in range(i,len(tuple_list)):
        for k in range(0,4):
            xoremptylst.append(tuple_list[i][k]^tuple_list[j][k])
    
newxoremptylst=[]               # list to append elemts from "xoremptylst" and place them in tuples of 4. The loop below performs this function

for i in range(0,len(xoremptylst),n):           
    newxoremptylst.append(tuple(xoremptylst[i:i+n]))

for i in range(len(tuple_list)):                # this loop performs scalar multiplication
    for j in range(0,4):
        andemptylst.append(0&tuple_list[i][j])
        andemptylst2.append(1&tuple_list[i][j])

newandemptylst=[]               # list to append elemts from "andemptylst" and "andemptylst2" and place them in tuples of 4. The loop below performs this function

for i in range(0,len(andemptylst),n):
    newandemptylst.append(tuple(andemptylst[i:i+n]))
    newandemptylst.append(tuple(andemptylst2[i:i+n]))

flag=0                      

for i in newxoremptylst:
    if i not in tuple_list:
        flag=0
        print("False")
        break                   # even if 1 element is not in subspace it prints False
    else:
        flag=1

if flag==1:                     # if flag is 1 then only it checks if scalar multiplication is True/False
    for i in newandemptylst:
        if i not in tuple_list:
            print("False")
            break
    print("True")
            
