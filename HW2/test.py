num="0x10101010"
output=""
for i in range(2,10) :
    if(num[i]=="1") :
        output+="1"
    else :
        output+="0"

print(output)


temp_imm=hex(12412312312)
print(temp_imm)
print(temp_imm[:4])

arr="1000011101100101"

if (arr[1]=="0") :
    print("yes")

# rs=int(arr1[i][6:11],2)
# rt=int(arr1[i][11:16],2)
# if arr1[i][16]=="1" :
#     imm=int(arr1[i][16:],2)-1
#     bin_imm1=bin(imm)[2:]
#     bin_imm=bin_imm1.zfill(16)
#     arr3=[]
#     str1=""
#     for j in range (len(bin_imm)) :
#         if int(bin_imm[j])==1 :
#             arr3.extend([0])
#         else :
#             arr3.extend([1])
#     for j in range (len(arr3)) :
#         str1 += str(arr3[j])
#     output="-"+str(int(str1,2))
#     imm=int(output)


arr="0x00000010"
barr=bin(int(arr,0))
print(arr[-4:])


0b 1111 1111 1111 1111 1111 1111 1111 1111


0b 1000 0000 0000 0000 0000 0000 0000 0000
0b 1111 1111 1111 1111 1111 1111 1111 111