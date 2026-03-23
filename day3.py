'''sams=["hi","hello",23,11,2.3,True,]
sams[3]=0
print(sams,type(sams))
sams.append("uuu")

sams.insert(1,"banna")
print(sams)
sams.remove("uuu")
print(sams)'''

'''nums=[4,32,11,13,5,1,7,8,15,9,0,31,44]
nums.sort()
nums.reverse()
print(nums)
nums.pop()
print(nums)
print(nums.index(32))
nums.clear()
print(nums)'''
'''
num=[9,8,7,6,5,4,3,2,1,0]
num.sort()
print(num)
print(num[2:5])#prints the elements from index 2 to 5
print(num[:6])#prints the elemenss from 0 to 6 (excloding 6th)
print(num[6:])#prints the elements from 6 to end(exclding 6th)
print(num[:-1])#prints the elements from 0 to end but excliding the last element
print(num[:-2])#prints the elements from 0 to end but excliding the last two element
print(num[::2])#prints thr elements from 0 to end with the jump step of 2
print(num[::-2])#prints thr elements from end to 0 with the jump step of 2
'''
'''
num=[9,8,7,6,5,4,3,2,1,0]
num.sort()
num.remove(0)
for i,num in enumerate(num):
    print(i,num)
'''
'''
lit=[]
for i in range(10):
    lit.append(i**3)
print(lit)
'''
#list compresion 
nis=[i**2 for i in range(6)]
print(nis)

