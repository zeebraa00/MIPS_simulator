import binascii
import sys

arr1=[]
arr2=[]
arr4=[]

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
    num=int(command[4:])
    ok=0
    for i in range(num) :
        if (i < len(arr4)) :
            print(arr4[i])
            if (i==num-1) :
                print("Executed %d instructions" % (i+1))
        else :
            ok=i
            break
    if (ok==len(arr4)) :
        print("Executed %d instructions" % len(arr4))
        
def func4() : # command == registers
    for i in range(32) :
        print("$%d: %s" %(i, registers[i]))
    print("PC: %s" %(registers[i]))

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
    # print(tmp)
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
    elif (command[0:]=="test") :
        init()
    else :
        print("wrong input")