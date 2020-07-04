import binascii
import sys

arr1=[];arr2=[];arr3=[];darr1=[]
temp_arr=[]
is_exit=0
operation_number=0
total_op=0

mips_code=""

Arithmetic=["add", "addu", "and", "nor", "or", "slt", "sltu", "sub", "subu", "xor"]
Shifter=["sll", "sllv", "sra", "srav", "srl", "srlv"]
Immediate=["addi", "addiu", "andi", "lui", "ori", "slti", "sltiu", "xori"]
Multiply=["div", "divu", "mfhi", "mflo", "mthi", "mtlo", "mult", "multu"]
Memory=["lw", "lh", "lhu", "lb", "lbu", "sw", "sh", "sb"]
Branch=["jalr", "jr", "j", "jal", "beq", "bne"]
SystemCall=["syscall"]

registers=[
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000","0x00000000",
    "0x00000000","0x00000000","0x00000000"
]

instruction_memory=[]
data_memory=[]

def init() :
    # initiate registers array
    for i in range (35) :
        registers[i]="0x00000000"

def program_count(i) :
    # pc register + 4
    registers[34]=dec_to_hex((i+1)*4)

def two_complement(binray_input) :
    # give two's complement of binary input
    step1=bin(int(binray_input,0)-1)
    remain=34-len(step1)
    step2="0b"+remain*"0"+step1[2:]
    output="0b"
    for i in range (32) :
        if (step2[i+2]=="0") :
            output+="1"
        elif (step2[i+2]=="1") :
            output+="0"
    return output

def two_complement_half(binray_input) :
    # give two's complement of binary input
    step1=bin(int(binray_input,0)-1)
    remain=18-len(step1)
    step2="0b"+remain*"0"+step1[2:]
    output="0b"
    for i in range (16) :
        if (step2[i+2]=="0") :
            output+="1"
        elif (step2[i+2]=="1") :
            output+="0"
    return output

def two_complement_64bit(binray_input) :
    # give two's complement of binary input
    step1=bin(int(binray_input,0)-1)
    remain=66-len(step1)
    step2="0b"+remain*"0"+step1[2:]
    output="0b"
    for i in range (64) :
        if (step2[i+2]=="0") :
            output+="1"
        elif (step2[i+2]=="1") :
            output+="0"
    return output

def bin_to_full(binary_input) :
    # binary input : 0b00...000 type
    step1=bin(int(binary_input,0))
    remain=34-len(step1)
    output="0b"+remain*"0"+step1[2:]
    return output

def bin_to_64bit(binary_input) :
    # binary input : 0b00...000 type
    step1=bin(int(binary_input,0))
    remain=66-len(step1)
    output="0b"+remain*"0"+step1[2:]
    return output

def hex_to_full(hex_input) :
    # hex input : 0x0...00 type
    step1=hex(int(hex_input,0))
    remain=10-len(step1)
    output="0x"+remain*"0"+step1[2:]
    return output

def bin_to_dec(binary_input) :
    # binary input : 0b00...000 type
    return int(binary_input,0)

def bin_to_dec_signed(binary_input) :
    # binary input : 0b00...000 type
    step1=bin_to_full(binary_input)
    if(step1[2]=="1") :
        # negative
        output=-bin_to_dec(two_complement(step1))
    else :
        #positive
        output=bin_to_dec(step1)
    return output

def bin_to_hex(binary_input) :
    # binary input : 0b00...000 type
    step1=hex(int(binary_input,0))
    remain=10-len(step1)
    output="0x"+remain*"0"+step1[2:]
    return output

def dec_to_bin(dec_input) :
    # dec input : integer type
    step1=bin(int(dec_input))
    remain=34-len(step1)
    output="0b"+remain*"0"+step1[2:]
    return output

def dec_to_hex(dec_input) :
    # dec input : integer type
    step1=hex(int(dec_input))
    remain=10-len(step1)
    output="0x"+remain*"0"+step1[2:]
    return output

def hex_to_bin(hex_input) :
    # hex input : 0x0...00 type
    step1=bin(int(hex_input,0))
    remain=34-len(step1)
    output="0b"+remain*"0"+step1[2:]
    return output

def hex_to_dec(hex_input) :
    # hex input : 0x0...00 type
    return int(hex_input,0)

def hex_to_dec_signed(hex_input) :
    # hex input : 0x0...00 type
    step1=hex_to_bin(hex_input)
    if(step1[2]=="1") :
        # negative
        output=-bin_to_dec(two_complement(step1))
    else :
        # positive
        output=bin_to_dec(step1)
    return output

def bitwise_and(n1,n2) :
    t1=hex_to_bin(registers[n1])
    t2=hex_to_bin(registers[n2])
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=bin_to_hex(output)
    return goal

def bitwise_andi(n1,imm) :
    t1=hex_to_bin(registers[n1])
    if (imm>=0) :
        t2=dec_to_bin(imm)
    else :
        t2=two_complement(dec_to_bin(-imm))
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=bin_to_hex(output)
    return goal

def bitwise_nor(n1,n2) :
    t1=hex_to_bin(registers[n1])
    t2=hex_to_bin(registers[n2])
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="0" and t2[i]=="0") :
            output+="1"
        else :
            output+="0"
    goal=bin_to_hex(output)
    return goal

def bitwise_or(n1,n2) :
    t1=hex_to_bin(registers[n1])
    t2=hex_to_bin(registers[n2])
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" or t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=bin_to_hex(output)
    return goal

def bitwise_ori(n1,imm) :
    t1=hex_to_bin(registers[n1])
    if (imm>=0) :
        t2=dec_to_bin(imm)
    else :
        t2=bin_to_full(two_complement_half(bin(-imm)))
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" or t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=bin_to_hex(output)
    return goal

def bitwise_xor(n1,n2) :
    t1=hex_to_bin(registers[n1])
    t2=hex_to_bin(registers[n2])
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="0") :
            output+="1"
        elif (t1[i]=="0" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=bin_to_hex(output)
    return goal

def bitwise_xori(n1,imm) :
    t1=hex_to_bin(registers[n1])
    if (imm>=0) :
        t2=dec_to_bin(imm)
    else :
        t2=bin_to_full(two_complement_half(dec_to_bin(-imm))) ## bug fix
    output="0b"
    for i in range(2,34) :
        if (t1[i]=="1" and t2[i]=="0") :
            output+="1"
        elif (t1[i]=="0" and t2[i]=="1") :
            output+="1"
        else :
            output+="0"
    goal=bin_to_hex(output)
    return goal

def sll(n1, shamt) :
    binary_register=hex_to_bin(registers[n1])
    temp=binary_register[2:]+"0"*shamt
    over=len(temp)-32
    output="0b"+temp[over:]
    output=bin_to_hex(output)
    return output

def sllv(n1, n2) :
    shamt=bin_to_dec("0b"+hex_to_bin(registers[n2])[-4:]) ## bug fix
    binary_register=hex_to_bin(registers[n1])
    temp=binary_register[2:]+"0"*shamt
    over=len(temp)-32
    output="0b"+temp[over:]
    output=bin_to_hex(output)
    return output

def srl(n1, shamt) :
    binary_register=hex_to_bin(registers[n1])
    temp="0"*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=bin_to_hex(output)
    return output

def srlv(n1, n2) :
    shamt=bin_to_dec("0b"+hex_to_bin(registers[n2])[-4:]) ## bug fix
    binary_register=hex_to_bin(registers[n1])
    temp="0"*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=bin_to_hex(output)
    return output

def sra(n1, shamt) :
    binary_register=hex_to_bin(registers[n1])
    MSB=str(binary_register[2])
    temp=MSB*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=bin_to_hex(output)
    return output

def srav(n1, n2) :
    shamt=bin_to_dec("0b"+hex_to_bin(registers[n2])[-4:]) ## bug fix
    binary_register=hex_to_bin(registers[n1])
    MSB=str(binary_register[2])  
    temp=MSB*shamt+binary_register[2:]
    over=len(temp)-32
    output="0b"+temp[:32]
    output=bin_to_hex(output)
    return output

def operate(i) :
    global is_exit
    global operation_number
    global total_op

    if ( hex_to_dec_signed(registers[34])+4 >= hex_to_dec("0x00010000") ) :
        print("Memory address out of range: "+registers[34])
        is_exit=1
        return
        
    elif ( hex_to_dec_signed(registers[34])+4 <= 0 ) :
        print("Memory address out of range: "+registers[34])
        is_exit=1
        return

    if (len(instruction_memory)<=i) :
        print("unknown instruction")
        program_count(i);total_op+=1
        is_exit=1
        return

    temp=instruction_memory[i].replace(",","")
    temp=temp.replace("$","")
    temp_arr=temp.split()

    if (temp_arr[1] in Arithmetic) :
        op=temp_arr[1]
        rd=int(temp_arr[2])
        rs=int(temp_arr[3])
        rt=int(temp_arr[4])
    
        if (op=="add") :
            compute=hex_to_dec(registers[rs])+hex_to_dec(registers[rt])
            compute=dec_to_hex(compute)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="addu") :
            compute=hex_to_dec(registers[rs])+hex_to_dec(registers[rt])
            compute=dec_to_hex(compute)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="and") :
            compute=bitwise_and(rs,rt)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="nor") :
            compute=bitwise_nor(rs,rt)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="or") :
            compute=bitwise_or(rs,rt)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="slt") :
            tmp1=hex_to_bin(registers[rs])
            tmp2=hex_to_bin(registers[rt])
            if (tmp1[2]=="1" and tmp2[2]=="1") : # both are negative
                str1=two_complement(tmp1)
                str2=two_complement(tmp2)
                compute=("0x00000001" if ( bin_to_dec(str2) < bin_to_dec(str1) ) else "0x00000000")
            elif (tmp1[2]=="1" and tmp2[2]=="0") : # rs is negative
                compute="0x00000001"
            elif (tmp1[2]=="0" and tmp2[2]=="1") : # rt is negative
                compute="0x00000000"
            else : # both are positive
                compute=("0x00000001" if ( hex_to_dec(registers[rs]) < hex_to_dec(registers[rt]) ) else "0x00000000")
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="sltu") :
            compute=("0x00000001" if ( hex_to_dec(registers[rs]) < hex_to_dec(registers[rt]) ) else "0x00000000")
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="sub") :
            compute=hex_to_dec(registers[rs])-hex_to_dec(registers[rt])
            if (compute>=0) :
                compute=dec_to_hex(compute)
            else :
                compute=bin_to_hex(two_complement(dec_to_bin(-compute)))
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="subu") :
            compute=hex_to_dec(registers[rs])-hex_to_dec(registers[rt])
            if (compute>=0) :
                compute=dec_to_hex(compute)
            else :
                compute=bin_to_hex(two_complement(dec_to_bin(-compute)))
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="xor") :
            compute=bitwise_xor(rs,rt)
            registers[rd]=compute
            program_count(i);total_op+=1

        else :
            print("unknown instruction")
            program_count(i);total_op+=1
            is_exit=1
            return
        
    elif (temp_arr[1] in Shifter) :
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
            program_count(i);total_op+=1
            is_exit=1
            return

        if (op=="sll") :
            compute=sll(rt,shamt)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="sllv") :
            compute=sllv(rt,rs)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="sra") : # sign extension
            compute=sra(rt,shamt)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="srav") : # sign extension
            compute=srav(rt,rs)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="srl") :
            compute=srl(rt,shamt)
            registers[rd]=compute
            program_count(i);total_op+=1

        elif (op=="srlv") :
            compute=srlv(rt,rs)
            registers[rd]=compute
            program_count(i);total_op+=1

    elif (temp_arr[1] in Immediate) :
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
            compute=hex_to_dec(registers[rs])+imm
            if (compute<0) :
                temp=bin_to_hex(two_complement(dec_to_bin(-compute)))
            else :
                temp=dec_to_hex(compute)
            registers[rt]=temp
            program_count(i);total_op+=1

        elif (op=="addiu") :
            compute=hex_to_dec(registers[rs])+imm
            if (compute<0) :
                temp=bin_to_hex(two_complement(dec_to_bin(-compute)))
            else :
                temp=dec_to_hex(compute)
            registers[rt]=temp
            program_count(i);total_op+=1

        elif (op=="andi") :
            compute=bitwise_andi(rs,imm)
            registers[rt]=compute
            program_count(i);total_op+=1

        elif (op=="lui") :
            if (int(temp_arr[3])>=0) :
                compute="0x"+dec_to_hex(temp_arr[3])[6:10]+"0000"
            else :
                compute="0x"+bin_to_hex(two_complement(dec_to_bin(temp_arr[3][1:])))[6:10]+"0000"
            registers[rt]=compute
            program_count(i);total_op+=1

        elif (op=="ori") :
            compute=bitwise_ori(rs,imm)
            registers[rt]=compute
            program_count(i);total_op+=1

        elif (op=="slti") :
            tmp1=hex_to_bin(registers[rs])
            if (imm>=0) :
                tmp2=dec_to_bin(imm)
            else :
                tmp2=two_complement(dec_to_bin(-imm))
            if (tmp1[2]=="1" and tmp2[2]=="1") : # both are negative
                tmp1=bin_to_dec(two_complement(tmp1))
                tmp2=bin_to_dec(two_complement(tmp2))
                compute=("0x00000001" if ( tmp2 < tmp1 ) else "0x00000000")
            elif (tmp1[2]=="1" and tmp2[2]=="0") : # rs is negative
                compute="0x00000001"
            elif (tmp1[2]=="0" and tmp2[2]=="1") : # imm is negative
                compute="0x00000000"
            else : # both are positive
                compute=("0x00000001" if ( hex_to_dec(registers[rs]) < imm ) else "0x00000000")
            registers[rt]=compute
            program_count(i);total_op+=1

        elif (op=="sltiu") :
            tmp1=hex_to_dec(registers[rs])
            if (imm>=0) :
                tmp2=imm
            else :
                tmp2=bin_to_dec(two_complement(dec_to_bin(-imm)))
            compute=("0x00000001" if ( tmp1<tmp2 ) else "0x00000000")
            registers[rt]=compute
            program_count(i);total_op+=1

        elif (op=="xori") :
            compute=bitwise_xori(rs,imm)
            registers[rt]=compute
            program_count(i);total_op+=1

        else :
            print("unknown instruction")
            program_count(i);total_op+=1
            is_exit=1
            return

    elif (temp_arr[1] in Multiply) :
        if (temp_arr[1] in ["div", "divu", "mult", "multu"]) :
            op=temp_arr[1]
            rs=int(temp_arr[2])
            rt=int(temp_arr[3])
        elif (temp_arr[1] in ["mfhi", "mflo", "mthi", "mtlo"]) :
            op=temp_arr[1]
            rd=int(temp_arr[2])
        else :
            print("unknown instruction")
            program_count(i);total_op+=1
            is_exit=1
            return

        if (op=="div") :
            quotient=hex_to_dec_signed(registers[rs])/hex_to_dec_signed(registers[rt])
            remainder=hex_to_dec_signed(registers[rs])%hex_to_dec_signed(registers[rt])
            if (remainder >= 0) :
                registers[32]=dec_to_hex(remainder)
            else :
                registers[32]=bin_to_hex(two_complement(dec_to_bin(-remainder)))
            if (quotient >= 0) :
                registers[33]=dec_to_hex(quotient)
            else :
                registers[33]=bin_to_hex(two_complement(dec_to_bin(-quotient)))
            program_count(i);total_op+=1
            
        elif (op=="divu") :
            quotient=hex_to_dec(registers[rs])/hex_to_dec(registers[rt])
            remainder=hex_to_dec(registers[rs])%hex_to_dec(registers[rt])
            registers[32]=dec_to_hex(remainder)
            registers[33]=dec_to_hex(quotient)
            program_count(i);total_op+=1

        elif (op=="mult") :
            step1=hex_to_dec_signed(registers[rs])*hex_to_dec_signed(registers[rt])
            if (step1>=0) :
                step2=bin_to_64bit(bin(step1))
            else :
                step2=two_complement_64bit(bin_to_64bit(bin(-step1)))
            registers[32]=bin_to_hex("0b"+step2[2:34])
            registers[33]=bin_to_hex("0b"+step2[34:66])
            program_count(i);total_op+=1

        elif (op=="multu") :
            step1=hex_to_dec(registers[rs])*hex_to_dec(registers[rt])
            step2=bin_to_64bit(bin(step1))
            registers[32]=bin_to_hex("0b"+step2[2:34])
            registers[33]=bin_to_hex("0b"+step2[34:66])
            program_count(i);total_op+=1

        elif (op=="mfhi") :
            registers[rd]=registers[32]
            program_count(i);total_op+=1

        elif (op=="mflo") :
            registers[rd]=registers[33]
            program_count(i);total_op+=1
            
        elif (op=="mthi") :
            registers[32]=registers[rd]
            program_count(i);total_op+=1

        elif (op=="mtlo") :
            registers[33]=registers[rd]
            program_count(i);total_op+=1

    elif (temp_arr[1] in Memory) :    
        step1=temp_arr[3].replace("("," ")
        step1=step1.replace(")"," ")
        step2=step1.split()
        temp_arr.pop()
        temp_arr.extend(step2)
        
        op=temp_arr[1]
        rt=int(temp_arr[2])
        rs=int(temp_arr[4])
        offset=int(temp_arr[3])    

        if (op=="lw") :
            if ( 0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4 ) :
                registers[rt]=hex_to_full(data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4])
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1

        elif (op=="lh") :
            if (0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4) :
                temp = data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][2+2*((hex_to_dec(registers[rs])-268435456+offset)%4) : 6+2*((hex_to_dec(registers[rs])-268435456+offset)%4)]
                if (temp[0] in ["8","9","a","b","c","d","e","f"]) :
                    MSB="f"
                else :
                    MSB="0"
                registers[rt]="0x"+MSB*4+temp # sign extend
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1

        elif (op=="lhu") :
            if (0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4) :
                temp = data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][2+2*((hex_to_dec(registers[rs])-268435456+offset)%4) : 6+2*((hex_to_dec(registers[rs])-268435456+offset)%4)]
                registers[rt]="0x"+"0"*4+temp # zero extend
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1
                

        elif (op=="lb") :
            if (0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4) :
                temp = data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][2+2*((hex_to_dec(registers[rs])-268435456+offset)%4) : 4+2*((hex_to_dec(registers[rs])-268435456+offset)%4)]
                if (temp[0] in ["8","9","a","b","c","d","e","f"]) :
                    MSB="f"
                else :
                    MSB="0"
                registers[rt]="0x"+MSB*4+temp # sign extend
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1


        elif (op=="lbu") :
            if (0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4) :
                temp = data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][2+2*((hex_to_dec(registers[rs])-268435456+offset)%4) : 4+2*((hex_to_dec(registers[rs])-268435456+offset)%4)]
                registers[rt]="0x"+"0"*6+temp # zero extend
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1

        elif (op=="sw") :
            if (0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4) :
                data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4]=registers[rt]
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1
            
        elif (op=="sh") :
            if (0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4) :
                data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4] = data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][:2+2*((hex_to_dec(registers[rs])-268435456+offset)%4)] + registers[rt][6:10] + data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][2+2*((hex_to_dec(registers[rs])-268435456+offset)%4)+4:]
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1

        elif (op=="sb") :
            if (0 <= (hex_to_dec(registers[rs])-268435456+offset)/4 <= 65536/4) :
                data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4] = data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][:2+2*((hex_to_dec(registers[rs])-268435456+offset)%4)] + registers[rt][8:10] + data_memory[(hex_to_dec(registers[rs])-268435456+offset)/4][2+2*((hex_to_dec(registers[rs])-268435456+offset)%4)+2:]
                program_count(i);total_op+=1
            else :
                print("Memory address alignment error: "+registers[34])
                program_count(i);total_op+=1
                is_exit=1

        else :
            print("unknown instruction")
            program_count(i);total_op+=1
            is_exit=1
            return

    elif (temp_arr[1] in Branch) :
        if (temp_arr[1] in ["beq", "bne"]) :
            op=temp_arr[1]
            rs=int(temp_arr[2])
            rt=int(temp_arr[3])
            label=int(temp_arr[4])
        elif (temp_arr[1] in ["j", "jal"]) :
            op=temp_arr[1]
            target=int(temp_arr[2])
        elif (temp_arr[1] in ["jr"]) :
            op=temp_arr[1]
            rs=int(temp_arr[2])
        elif (temp_arr[1] in ["jalr"]) :
            op=temp_arr[1]
            rd=int(temp_arr[2])
            rs=int(temp_arr[3])
        else :
            print("unknown instruction")
            program_count(i);total_op+=1
            is_exit=1
            return

        if (op=="beq") :
            if ( registers[rs] == registers[rt] ) :
                operation_number+=label
                program_count(i);total_op+=1
            else :
                program_count(i);total_op+=1

        elif (op=="bne") :
            if ( registers[rs] != registers[rt] ) :
                operation_number+=label
                program_count(i);total_op+=1
            else :
                program_count(i);total_op+=1

        elif (op=="j") :
            operation_number=target
            operate(target)
            program_count(i);total_op+=1

        elif (op=="jal") :
            registers[31]=dec_to_hex(hex_to_dec(registers[34])+4)
            operation_number=target
            operate(target)
            program_count(i);total_op+=1

        elif (op=="jr") :
            operation_number=(hex_to_dec(registers[rs])/4)
            operate(operation_number)
            program_count(i);total_op+=1

        elif (op=="jalr") :
            registers[rd]=dec_to_hex(hex_to_dec(registers[34])+4)
            operation_number=(hex_to_dec(registers[rs])/4)
            operate(operation_number)
            program_count(i);total_op+=1

    elif (temp_arr[1] in SystemCall) :
        check=hex_to_dec(registers[2])
        if (check==1) :
            print(hex_to_dec_signed(registers[4])),
            program_count(i);total_op+=1

        elif (check==4)  :
            temp=data_memory[ ((hex_to_dec(registers[4])-268435456)/4) ][2+2*((hex_to_dec(registers[4])-268435456)%4): ]
            j=1
            while True :
                if ("00" in temp) :
                    break
                else :
                    temp += data_memory[ ((hex_to_dec(registers[4])-268435456)/4) + j ][2:]
                    j+=1
            temp=temp[:temp.find("00")]
            str1=""
            for j in range (0,len(temp),2) :
                str1+=chr(hex_to_dec(hex_to_full("0x"+temp[j:j+2])))
            print(str1),
            program_count(i);total_op+=1

        elif (check==10)  :
            print("EXIT syscall")
            program_count(i);total_op+=1
            is_exit=1
            return

        else :
            print("Invalid syscall")
            program_count(i);total_op+=1
            is_exit=1
            return

    else :
        print("unknown instruction")
        program_count(i);total_op+=1
        is_exit=1
        return

def func1() :
    # command == read
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

def func2() :
    # command == loadinst
    filename=command[9:]

    try :
        f=open(filename, "rb")
        string=f.read()
        num=len(string)/4
        for i in range(num) :
            hex=binascii.b2a_hex(string[i*4:(i+1)*4])
            convert_to_binary(hex)
        convert_to_MIPS(0) # instructions saved in instruction_memory
        
    except :
        sys.stderr.write("No file: %s\n" % filename)

def func3() :
    # command == run
    global is_exit
    global operation_number
    operation_number=0 # initiate

    num=int(command[4:])
    while True :
        if (operation_number < len(instruction_memory)) :
            operate(operation_number)
            if (is_exit==1) :
                print("Executed %d instructions" % (total_op))
                return
            if (operation_number==num-1) :
                print("Executed %d instructions" % (total_op+1))
                return
        else :
            program_count(operation_number)
            break
        operation_number+=1
    print("Executed %d instructions" % (total_op+1))
         
def func4() :
    # command == registers
    for i in range(32) :
        print("$%d: %s" %(i, registers[i]))
    print("HI: %s" %(registers[32]))
    print("LO: %s" %(registers[33]))    
    print("PC: %s" %(registers[34]))

def func5() :
    # command == loaddata
    filename=command[9:]

    try :
        f=open(filename, "rb")
        string=f.read()
        num=len(string)
        for i in range(num) :
            hex=binascii.b2a_hex(string[i:(i+1)])
            darr1.append(hex)
        quotient = num / 4
        remainder = num % 4

        for i in range(quotient) :
            temp1="0x"
            for j in range(4) :
                temp1+=(darr1[4*i+j])
            data_memory.append(temp1)
        temp2="0x"
        for i in range(remainder) :
            temp2+=(darr1[quotient*4+i])
        remainder=10-len(temp2)
        temp2="0x"+temp2[2:]+"F"*remainder
        data_memory.append(temp2)
        for i in range (51200) :
            data_memory.append("0xFFFFFFFF")

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
                op="sltu"
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
                mips_code=str(arr2[i])+"unknown instruction"
            
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
            else :
                mips_code=str(arr2[i])+" unknown instruction"
        if (agree==1) :
            print("inst %d: %s" % (i, mips_code))
        elif (agree==0) :
            instruction_memory.append(mips_code)

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
    elif (command[0:8]=="loaddata") :
        func5()
    else :
        print("wrong input")