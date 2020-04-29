import binascii
import sys

arr1=[]
arr2=[]
arr3=[]
arr4=[]
lui_arr=[]
lui_num=0
temp_arr=[]
is_exit=0

R=["add", "addu", "and", "nor", "or", "slt", "sltu", "sub", "subu", "xor"]
Shift=["sll", "sllv", "sra", "srav", "srl", "srlv"]
I=["addi", "addiu", "andi", "lui", "ori", "slti", "sltiu", "xori"]

mips_code=""

registers=[
    "0x00000000", # $0
    "0x00000000", # $1
    "0x00000000", # $2
    "0x00000000", # $3
    "0x00000000", # $4
    "0x00000000", # $5
    "0x00000000", # $6
    "0x00000000", # $7
    "0x00000000", # $8
    "0x00000000", # $9
    "0x00000000", # $10
    "0x00000000", # $11
    "0x00000000", # $12
    "0x00000000", # $13
    "0x00000000", # $14
    "0x00000000", # $15
    "0x00000000", # $16
    "0x00000000", # $17
    "0x00000000", # $18
    "0x00000000", # $19
    "0x00000000", # $20
    "0x00000000", # $21
    "0x00000000", # $22
    "0x00000000", # $23
    "0x00000000", # $24
    "0x00000000", # $25
    "0x00000000", # $26
    "0x00000000", # $27
    "0x00000000", # $28
    "0x00000000", # $29
    "0x00000000", # $30
    "0x00000000", # $31
    "0x00000000" # pc register
]

instruction_memory="0x00000000"

def init() : # initiate registers array
    for i in range (33) :
        registers[i]="0x00000000"

def pc_reg() :
    registers[32]=hex(int(registers[32],0)+4)
    remain=10-len(registers[32])
    registers[32]=registers[32][:2]+remain*"0"+registers[32][2:]

def preprocess(reg_num) : # reg_num : rs, rt, rd etc
    # hex string to integer
    step1=registers[reg_num]
    step2=int(step1, 0)
    return step2

def bitwise_and(n1,n2) :
    t1=bin(int(registers[n1],0))
    t2=bin(int(registers[n2],0)) #### 
    remain1=34-len(t1)
    remain2=34-len(t2)
    t1=t1[:2]+remain1*"0"+t1[2:]
    t2=t2[:2]+remain2*"0"+t2[2:]
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=hex(int(output,0))
    remain=10-len(goal)
    goal=goal[:2]+remain*"0"+goal[2:]
    return goal

def bitwise_andi(n1,imm) :
    t1=bin(int(registers[n1],0))
    if (imm>=0) :
        t2=bin(imm)
    else :
        num=bin(-imm)
        remain=34-len(num)
        num=num[:2]+"0"*remain+num[2:] # zero extend
        temp=[]
        temp_str=""
        for i in range(2,34) :
            if (num[i]=="1") :
                temp.extend([0]) 
            elif (num[i]=="0") :
                temp.extend([1])
        for i in range(len(temp)) :
            temp_str+=str(temp[i])
        t2=bin(int(temp_str,2)+1)
    remain1=34-len(t1)
    remain2=34-len(t2)
    t1=t1[:2]+remain1*"0"+t1[2:] # zero extend
    t2=t2[:2]+remain2*"0"+t2[2:] # zero extend
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=hex(int(output,0))
    remain=10-len(goal)
    goal=goal[:2]+remain*"0"+goal[2:]
    return goal

def bitwise_nor(n1,n2) :
    t1=bin(int(registers[n1],0))
    t2=bin(int(registers[n2],0))
    remain1=34-len(t1)
    remain2=34-len(t2)
    t1=t1[:2]+remain1*"0"+t1[2:]
    t2=t2[:2]+remain2*"0"+t2[2:]
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="0" and t2[i]=="0") :
            output+="1"
        else :
            output+="0"
    goal=hex(int(output,0))
    remain=10-len(goal)
    goal=goal[:2]+remain*"0"+goal[2:]
    return goal

def bitwise_or(n1,n2) :
    t1=bin(int(registers[n1],0))
    t2=bin(int(registers[n2],0))
    remain1=34-len(t1)
    remain2=34-len(t2)
    t1=t1[:2]+remain1*"0"+t1[2:]
    t2=t2[:2]+remain2*"0"+t2[2:]
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" or t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=hex(int(output,0))
    remain=10-len(goal)
    goal=goal[:2]+remain*"0"+goal[2:]
    return goal

def bitwise_ori(n1,imm) :
    t1=bin(int(registers[n1],0))
    if (imm>=0) :
        t2=bin(imm)
    else :
        num=bin(-imm)
        remain=18-len(num)
        num=num[:2]+"0"*remain+num[2:] # zero extend
        temp=[]
        temp_str=""
        for i in range(2,18) :
            if (num[i]=="1") :
                temp.extend([0]) 
            elif (num[i]=="0") :
                temp.extend([1])
        for i in range(len(temp)) :
            temp_str+=str(temp[i])
        t2=bin(int(temp_str,2)+1)
    remain1=34-len(t1)
    remain2=34-len(t2)
    t1=t1[:2]+remain1*"0"+t1[2:] # zero extend
    t2=t2[:2]+remain2*"0"+t2[2:] # zero extend
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" or t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=hex(int(output,0))
    remain=10-len(goal)
    goal=goal[:2]+remain*"0"+goal[2:]
    return goal

def bitwise_xor(n1,n2) :
    t1=bin(int(registers[n1],0))
    t2=bin(int(registers[n2],0))
    remain1=34-len(t1)
    remain2=34-len(t2)
    t1=t1[:2]+remain1*"0"+t1[2:]
    t2=t2[:2]+remain2*"0"+t2[2:]
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="0") :
            output+="1"
        elif (t1[i]=="0" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=hex(int(output,0))
    remain=10-len(goal)
    goal=goal[:2]+remain*"0"+goal[2:]
    return goal

def bitwise_xori(n1,imm) :
    t1=bin(int(registers[n1],0))
    if (imm>=0) :
        t2=bin(imm)
    else :
        num=bin(-imm)
        remain=34-len(num)
        num=num[:2]+"0"*remain+num[2:] # zero extend
        temp=[]
        temp_str=""
        for i in range(2,34) :
            if (num[i]=="1") :
                temp.extend([0]) 
            elif (num[i]=="0") :
                temp.extend([1])
        for i in range(len(temp)) :
            temp_str+=str(temp[i])
        t2=bin(int(temp_str,2)+1)
    remain1=34-len(t1)
    remain2=34-len(t2)
    t1=t1[:2]+remain1*"0"+t1[2:] # zero extend
    t2=t2[:2]+remain2*"0"+t2[2:] # zero extend
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="0") :
            output+="1"
        elif (t1[i]=="0" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=hex(int(output,0))
    remain=10-len(goal)
    goal=goal[:2]+remain*"0"+goal[2:]
    return goal

def sll(n1, shamt) :
    binary_register=(bin(int(registers[n1],0)))
    temp=binary_register[2:]+"0"*shamt
    over=len(temp)-32
    output="0b"+temp[over:]
    output=hex(int(output,0))
    remain=10-len(output)
    output=output[:2]+remain*"0"+output[2:]
    return output

def sllv(n1, n2) :
    shamt=int("0x"+registers[n2][-4:],0)
    binary_register=(bin(int(registers[n1],0)))
    temp=binary_register[2:]+"0"*shamt
    over=len(temp)-32
    output="0b"+temp[over:]
    output=hex(int(output,0))
    remain=10-len(output)
    output=output[:2]+remain*"0"+output[2:]
    return output

def srl(n1, shamt) :
    binary_register=(bin(int(registers[n1],0)))
    temp="0"*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=hex(int(output,0))
    remain=10-len(output)
    output=output[:2]+remain*"0"+output[2:]
    return output

def srlv(n1, n2) :
    shamt=int("0x"+registers[n2][-4:],0)
    binary_register=(bin(int(registers[n1],0)))
    temp="0"*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=hex(int(output,0))
    remain=10-len(output)
    output=output[:2]+remain*"0"+output[2:]
    return output

def sra(n1, shamt) :
    binary_register=(bin(int(registers[n1],0)))
    MSB=str(binary_register[2])
    temp=MSB*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=hex(int(output,0))
    remain=10-len(output)
    output=output[:2]+remain*"0"+output[2:]
    return output

def srav(n1, n2) :
    shamt=int("0x"+registers[n2][-4:],0)
    binary_register=(bin(int(registers[n1],0)))
    MSB=str(binary_register[2])  
    temp=MSB*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=hex(int(output,0))
    remain=10-len(output)
    output=output[:2]+remain*"0"+output[2:]
    return output

def operate(i) :
    global is_exit
    pc_reg()
    if (len(arr4)<=i) :
        print("unknown instruction")
        is_exit=1
        return
    temp=arr4[i].replace(",","")
    temp=temp.replace("$","")
    temp_arr=temp.split()
    if (temp_arr[1] in R) :
        op=temp_arr[1]
        rd=int(temp_arr[2])
        rs=int(temp_arr[3])
        rt=int(temp_arr[4])
        if (op=="add") :
            compute=preprocess(rs)+preprocess(rt)
            compute=hex(compute)
            remain=10-len(compute)
            compute=compute[:2]+remain*"0"+compute[2:]
            registers[rd]=compute
        elif (op=="addu") :
            compute=preprocess(rs)+preprocess(rt)
            compute=hex(compute)
            remain=10-len(compute)
            compute=compute[:2]+remain*"0"+compute[2:]
            registers[rd]=compute
        elif (op=="and") :
            compute=bitwise_and(rs,rt)
            registers[rd]=compute
        elif (op=="nor") :
            compute=bitwise_nor(rs,rt)
            registers[rd]=compute
        elif (op=="or") :
            compute=bitwise_or(rs,rt)
            registers[rd]=compute
        elif (op=="slt") :
            tmp1=bin(int(registers[rs],0))
            tmp2=bin(int(registers[rt],0))
            remain1=34-len(tmp1)
            remain2=34-len(tmp2)
            tmp1=tmp1[:2]+remain1*"0"+tmp1[2:]
            tmp2=tmp2[:2]+remain2*"0"+tmp2[2:]
            str1="0b"
            str2="0b"
            if (tmp1[2]=="1" and tmp2[2]=="1") : # both are negative
                bin(int(tmp1,0)-1)
                for i in range(2,34) :
                    if (tmp1[i]=="1") :
                        str1+="0"
                    elif (tmp1[i]=="0") :
                        str1+="1"
                bin(int(tmp2,0)-1)
                for i in range(2,34) :
                    if (tmp2[i]=="1") :
                        str2+="0"
                    elif (tmp2[i]=="0") :
                        str2+="1"
                compute=("0x00000001" if ( int(str2,0)<int(str1,0)) else "0x00000000")
            elif (tmp1[2]=="1" and tmp2[2]=="0") : # rs is negative
                compute="0x00000001"
            elif (tmp1[2]=="0" and tmp2[2]=="1") : # rt is negative
                compute="0x00000000"
            else : # both are positive
                compute=("0x00000001" if ( int(registers[rs],0)<int(registers[rt],0)) else "0x00000000")
            registers[rd]=compute
        elif (op=="sltu") :

            ###########################
            compute=("0x00000001" if ( int(registers[rs],0)<int(registers[rt],0)) else "0x00000000")
            registers[rd]=compute

        elif (op=="sub") :
            compute=preprocess(rs)-preprocess(rt)
            if (compute>=0) :
                compute=hex(compute)
                remain=10-len(compute)
                compute=compute[:2]+remain*"0"+compute[2:]
                registers[rd]=compute
            else :
                num=bin(-compute)
                remain=34-len(num)
                num=num[:2]+"0"*remain+num[2:]
                temp=[]
                temp_str=""
                for i in range(2,34) :
                    if (num[i]=="1") :
                        temp.extend([0]) 
                    elif (num[i]=="0") :
                        temp.extend([1])
                for i in range(len(temp)) :
                    temp_str+=str(temp[i])
                ttemp=int(temp_str,2)+1
                registers[rd]=hex(ttemp)

        elif (op=="subu") :
            compute=preprocess(rs)-preprocess(rt)
            if (compute>=0) :
                compute=hex(compute)
                remain=10-len(compute)
                compute=compute[:2]+remain*"0"+compute[2:]
                registers[rd]=compute
            else :
                num=bin(-compute)
                remain=34-len(num)
                num=num[:2]+"0"*remain+num[2:]
                temp=[]
                temp_str=""
                for i in range(2,34) :
                    if (num[i]=="1") :
                        temp.extend([0]) 
                    elif (num[i]=="0") :
                        temp.extend([1])
                for i in range(len(temp)) :
                    temp_str+=str(temp[i])
                ttemp=int(temp_str,2)+1
                registers[rd]=hex(ttemp)
        elif (op=="xor") :
            compute=bitwise_xor(rs,rt)
            registers[rd]=compute
        else :
            print("unknown instruction")
            is_exit=1
            return
        
    elif (temp_arr[1] in Shift) :
        if (temp_arr[1] in ["sllv", "srav", "srlv"]) :
            op=temp_arr[1]
            rd=int(temp_arr[2])
            rt=int(temp_arr[3])
            rs=int(temp_arr[4])
        elif (temp_arr[1] in ["sll", "sra", "srl"]) :
            op=temp_arr[1]
            rd=int(temp_arr[2])
            rt=int(temp_arr[3])
            shamt=int(temp_arr[4])
        else :
            print("unknown instruction")
            is_exit=1
            return

        if (op=="sll") :
            compute=sll(rt,shamt)
            registers[rd]=compute
        elif (op=="sllv") :
            compute=sllv(rt,rs)
            registers[rd]=compute
        elif (op=="sra") : # sign extension
            compute=sra(rt,shamt)
            registers[rd]=compute
        elif (op=="srav") : # sign extension
            compute=srav(rt,rs)
            registers[rd]=compute
        elif (op=="srl") :
            compute=srl(rt,shamt)
            registers[rd]=compute
        elif (op=="srlv") :
            compute=srlv(rt,rs)
            registers[rd]=compute

    elif (temp_arr[1] in I) :
        if (temp_arr[1]=="lui") :
            op=temp_arr[1]
            rt=int(temp_arr[2])
            imm=str(temp_arr[3])
        else :
            op=temp_arr[1]
            rt=int(temp_arr[2])
            rs=int(temp_arr[3])
            imm=int(temp_arr[4])
        if (op=="addi") :
            compute=preprocess(rs)+imm
            #####
            if (compute<0) :
                num=bin(-compute)
                remain=34-len(num)
                num=num[:2]+"0"*remain+num[2:]
                temp=[]
                temp_str=""
                for i in range(2,34) :
                    if (num[i]=="1") :
                        temp.extend([0]) 
                    elif (num[i]=="0") :
                        temp.extend([1])
                for i in range(len(temp)) :
                    temp_str+=str(temp[i])
                ttemp=int(temp_str,2)+1
                registers[rt]=hex(ttemp)
            else :
                compute=hex(compute)
                remain=10-len(compute)
                compute=compute[:2]+remain*"0"+compute[2:]
                registers[rt]=compute
        elif (op=="addiu") :
            compute=preprocess(rs)+imm
            if (compute<0) :
                num=bin(-compute)
                remain=34-len(num)
                num=num[:2]+"0"*remain+num[2:]
                temp=[]
                temp_str=""
                for i in range(2,34) :
                    if (num[i]=="1") :
                        temp.extend([0]) 
                    elif (num[i]=="0") :
                        temp.extend([1])
                for i in range(len(temp)) :
                    temp_str+=str(temp[i])
                ttemp=int(temp_str,2)+1
                registers[rt]=hex(ttemp)
            else :
                compute=hex(compute)
                remain=10-len(compute)
                compute=compute[:2]+remain*"0"+compute[2:]
                registers[rt]=compute
        elif (op=="andi") :
            compute=bitwise_andi(rs,imm)
            registers[rt]=compute
        elif (op=="lui") :
            global lui_num
            remain=4-len(lui_arr[lui_num])
            temp="0"*remain+lui_arr[lui_num]
            compute="0x"+temp+"0000"
            lui_num+=1
            registers[rt]=compute
        elif (op=="ori") :
            compute=bitwise_ori(rs,imm)
            registers[rt]=compute
        elif (op=="slti") :
            tmp1=bin(int(registers[rs],0))
            if (imm>=0) :
                tmp2=bin(imm)
            else :
                num=bin(-imm)
                remain=34-len(num)
                num=num[:2]+"0"*remain+num[2:] # zero extend
                temp=[]
                temp_str=""
                for i in range(2,34) :
                    if (num[i]=="1") :
                        temp.extend([0]) 
                    elif (num[i]=="0") :
                        temp.extend([1])
                for i in range(len(temp)) :
                    temp_str+=str(temp[i])
                tmp2=bin(int(temp_str,2)+1)
            remain1=34-len(tmp1)
            remain2=34-len(tmp2)
            tmp1=tmp1[:2]+remain1*"0"+tmp1[2:]
            tmp2=tmp2[:2]+remain2*"0"+tmp2[2:]
            str1="0b"
            str2="0b"
            if (tmp1[2]=="1" and tmp2[2]=="1") : # both are negative
                tmp1=bin(int(tmp1,0)-1)
                for i in range(2,34) :
                    if (tmp1[i]=="1") :
                        str1+="0"
                    elif (tmp1[i]=="0") :
                        str1+="1"
                tmp2=bin(int(tmp2,0)-1)
                for i in range(2,34) :
                    if (tmp2[i]=="1") :
                        str2+="0"
                    elif (tmp2[i]=="0") :
                        str2+="1"
                compute=("0x00000001" if ( int(str2,0)<int(str1,0)) else "0x00000000")
            elif (tmp1[2]=="1" and tmp2[2]=="0") : # rs is negative
                compute="0x00000001"
            elif (tmp1[2]=="0" and tmp2[2]=="1") : # imm is negative
                compute="0x00000000"
            else : # both are positive
                compute=("0x00000001" if ( int(registers[rs],0)<imm) else "0x00000000")
            registers[rt]=compute #################

        elif (op=="sltiu") :
            tmp1=bin(int(registers[rs],0))
            if (imm>=0) :
                tmp2=bin(imm)
            else :
                num=bin(-imm)
                remain=34-len(num)
                num=num[:2]+"0"*remain+num[2:] # zero extend
                temp=[]
                temp_str=""
                for i in range(2,34) :
                    if (num[i]=="1") :
                        temp.extend([0]) 
                    elif (num[i]=="0") :
                        temp.extend([1])
                for i in range(len(temp)) :
                    temp_str+=str(temp[i])
                tmp2=bin(int(temp_str,2)+1)
            remain1=34-len(tmp1)
            remain2=34-len(tmp2)
            tmp1=tmp1[:2]+remain1*"0"+tmp1[2:]
            tmp2=tmp2[:2]+remain2*"0"+tmp2[2:]

            num1=int(tmp1,0)
            num2=int(tmp2,0)+1
            compute=("0x00000001" if ( num1<num2) else "0x00000000")
            registers[rt]=compute ####################

        elif (op=="xori") :
            compute=bitwise_xori(rs,imm)
            registers[rt]=compute
        else :
            print("unknown instruction")
            is_exit=1
            return
    else :
        print("unknown instruction")
        is_exit=1
        return

def func2() : # command == loadinst
    filename=command[9:]

    try :
        f=open(filename, "rb")
        string=f.read()
        num=len(string)/4
        for i in range(num) :
            hex=binascii.b2a_hex(string[i*4:(i+1)*4])
            convert_to_binary(hex)
        convert_to_MIPS(0)
        
    except :
        sys.stderr.write("No file: %s\n" % filename)

def func3() : # command == run
    global is_exit
    num=int(command[4:])
    for i in range(num) :
        if (i < len(arr4)) :
            operate(i)
            if (is_exit==1) :
                print("Executed %d instructions" % (i+1))
                return
            if (i==num-1) :
                print("Executed %d instructions" % (i+1))
                return
        else :
            operate(i)
            break
    print("Executed %d instructions" % (i+1)) ###??
         
def func4() : # command == registers
    for i in range(32) :
        print("$%d: %s" %(i, registers[i]))
    print("PC: %s" %(registers[32]))

def func1() : # command == read
    filename=command[5:]

    try :
        f=open(filename, "rb")
        string=f.read()
        num=len(string)/4
        for i in range(num) :
            hex=binascii.b2a_hex(string[i*4:(i+1)*4])
            convert_to_binary(hex)
        convert_to_MIPS(1)
        
    except :
        sys.stderr.write("No file: %s\n" % filename)

def convert_to_MIPS(agree) :
    # arr1 : binary code
    # arr2 : hex code
    total_num=len(arr1)

    for i in range(total_num) :
        opcode=int(arr1[i][0:6],2)

        if opcode==0 : # R type instructions
            rs=int(arr1[i][6:11],2)
            rt=int(arr1[i][11:16],2)
            rd=int(arr1[i][16:21],2)
            shamt=int(arr1[i][21:26],2)
            funct=int(arr1[i][26:],2)
            if funct==32 :
                op="add"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==33 :
                op="addu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==34 :
                op="sub"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==35 :
                op="subu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==36 :
                op="and"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==37 :
                op="or"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==38 :
                op="xor"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==39 :
                op="nor"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==42 :
                op="slt"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==43 :
                op="sltv"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rs)+", $"+str(rt)
            elif funct==24 :
                op="mult"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)+", $"+str(rt)
            elif funct==25 :
                op="multu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)+", $"+str(rt)
            elif funct==26 :
                op="div"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)+", $"+str(rt)
            elif funct==27 :
                op="divu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)+", $"+str(rt)
            elif funct==8 :
                op="jr"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)
            elif funct==9 :
                op="jalr"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)
            elif funct==17 :
                op="mthi"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)
            elif funct==19 :
                op="mtlo"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)
            elif funct==16 :
                op="mfhi"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)
            elif funct==18 :
                op="mflo"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)
            elif funct==0 :
                op="sll"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rt)+", "+str(shamt)
            elif funct==2 :
                op="srl"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rt)+", "+str(shamt)
            elif funct==3 :
                op="sra"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rt)+", "+str(shamt)
            elif funct==4 :
                op="sllv"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rt)+", $"+str(rs)
            elif funct==6 :
                op="srlv"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rt)+", $"+str(rs)
            elif funct==7 :
                op="srav"
                mips_code=str(arr2[i])+" "+op+" $"+str(rd)+", $"+str(rt)+", $"+str(rs)
            elif funct==12 :
                op="syscall"
                mips_code=str(arr2[i])+" "+op
            else :
                mips_code=str(arr2[i])+" unknown instruction"
            
        elif ((opcode==2)or(opcode==3)) : # J type instructions
            pseudo_address=int(arr1[i][6:],2)
            if opcode==2 :
                op="j"
                mips_code=str(arr2[i])+" "+op+" "+str(pseudo_address)
            elif opcode==3 :
                op="jal"
                mips_code=str(arr2[i])+" "+op+" "+str(pseudo_address)

        else : # I type instructions
            rs=int(arr1[i][6:11],2)
            rt=int(arr1[i][11:16],2)
            if arr1[i][16]=="1" :
                imm=int(arr1[i][16:],2)-1
                bin_imm1=bin(imm)[2:]
                bin_imm=bin_imm1.zfill(16)
                arr3=[]
                str1=""
                for j in range (len(bin_imm)) :
                    if int(bin_imm[j])==1 :
                        arr3.extend([0])
                    else :
                        arr3.extend([1])
                for j in range (len(arr3)) :
                    str1 += str(arr3[j])
                output="-"+str(int(str1,2))
                imm=int(output)

            else :
                imm=int(arr1[i][16:],2)

            if opcode==8 :
                op="addi"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", $"+str(rs)+", "+str(imm)
            elif opcode==9 :
                op="addiu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", $"+str(rs)+", "+str(imm)
            elif opcode==12 :
                op="andi"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", $"+str(rs)+", "+str(imm)
            elif opcode==13 :
                op="ori"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", $"+str(rs)+", "+str(imm)
            elif opcode==10 :
                op="slti"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", $"+str(rs)+", "+str(imm)
            elif opcode==11 :
                op="sltiu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", $"+str(rs)+", "+str(imm)
            elif opcode==14 :
                op="xori"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", $"+str(rs)+", "+str(imm)
            elif opcode==4 :
                op="beq"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)+", $"+str(rt)+", "+str(imm)
            elif opcode==5 :
                op="bne"
                mips_code=str(arr2[i])+" "+op+" $"+str(rs)+", $"+str(rt)+", "+str(imm)
            elif opcode==32 :
                op="lb"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==36 :
                op="lbu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==33 :
                op="lh"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==37 :
                op="lhu"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==35 :
                op="lw"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==40 :
                op="sb"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==41 :
                op="sh"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==43 :
                op="sw"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)+"($"+str(rs)+")"
            elif opcode==15 :
                op="lui"
                mips_code=str(arr2[i])+" "+op+" $"+str(rt)+", "+str(imm)
                lui_arr.append(arr2[i][4:])
            else :
                mips_code=str(arr2[i])+" unknown instruction"
        if (agree==1) :
            print("inst %d: %s" % (i, mips_code))
        elif (agree==0) :
            arr4.append(mips_code)

def convert_to_binary(hex) :
    arr=[]
    tmp=""
    for i in range(8) :
        c = hex[i]
        if c=='0': arr.append("0000")
        elif c=='1': arr.append("0001")
        elif c=='2': arr.append("0010")
        elif c=='3': arr.append("0011")
        elif c=='4': arr.append("0100")
        elif c=='5': arr.append("0101")
        elif c=='6': arr.append("0110")
        elif c=='7': arr.append("0111")        
        elif c=='8': arr.append("1000")
        elif c=='9': arr.append("1001")
        elif c=='a': arr.append("1010")
        elif c=='b': arr.append("1011")
        elif c=='c': arr.append("1100")
        elif c=='d': arr.append("1101")
        elif c=='e': arr.append("1110")
        elif c=='f': arr.append("1111")

    for i in range(8) :
        tmp+=arr[i]
    arr2.append(hex) # arr2 : hex code
    arr1.append(tmp) # arr1 : binary code

while True :
    arr1=[]
    arr2=[]
    command=raw_input("mips-sim> ")

    if (command=="exit") :
        exit()
    elif (command[0:4]=="read") :
        func1()
    elif (command[0:8]=="loadinst") :
        func2()
    elif (command[0:3]=="run") :
        func3()
    elif (command[0:]=="registers") :
        func4()
    else :
        print("wrong input")