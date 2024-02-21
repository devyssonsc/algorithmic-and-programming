Ext=["zero", "um", "dois", "três", "quatro","cinco","seis","sete","oito","nove"]
F=[0, 0, 0, 0, 0, 0,0,0,0,0]
print("Texto? ")
nums= input()
while nums == "":
    print("Texto? ")
    nums = input()
ords="0123456789"
qts=0
novonum=""
for i in range(len(nums)):
    onde=ords.find(nums[i])
    if onde >=0:
        novonum=novonum+Ext[onde]
        F[onde]=F[onde]+1
        qts=qts+1
    else:
        novonum = novonum + nums[i]
print("*******************************************")
print("Inicial:", nums)
print("Por Extenso:", novonum)
print("Foram efetuadas as seguintes",qts, "transformações:")
for i in range(10):
    if F[i] > 0:
        print(ords[i],"para", Ext[i], F[i])