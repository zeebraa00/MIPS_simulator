import binascii
import sys

arr1=[]
arr2=[]

def func1() :
    filename=command[5:]
    address=filename

    try :
        f=open(address, "rb")
        string=f.read()
        num=len(string)/4
        for i in range(num) :
            hex=binascii.b2a_hex(string[i*4:(i+1)*4])
            convert_to_binary(hex)
        convert_to_MIPS()
        
    except :
        sys.stderr.write("No file: %s\n" % filename)

def convert_to_MIPS() :
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
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==33 :
                op="addu"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==34 :
                op="sub"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==35 :
                op="subu"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==36 :
                op="and"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==37 :
                op="or"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==38 :
                op="xor"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==39 :
                op="nor"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==42 :
                op="slt"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==43 :
                op="sltv"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rs, rt))
            elif funct==24 :
                op="mult"
                print("inst %d: %s %s $%d, $%d" % (i, arr2[i], op, rs, rt))
            elif funct==25 :
                op="multu"
                print("inst %d: %s %s $%d, $%d" % (i, arr2[i], op, rs, rt))
            elif funct==26 :
                op="div"
                print("inst %d: %s %s $%d, $%d" % (i, arr2[i], op, rs, rt))
            elif funct==27 :
                op="divu"
                print("inst %d: %s %s $%d, $%d" % (i, arr2[i], op, rs, rt))
            elif funct==8 :
                op="jr"
                print("inst %d: %s %s $%d" % (i, arr2[i], op, rs))
            elif funct==9 :
                op="jalr"
                print("inst %d: %s %s $%d" % (i, arr2[i], op, rs))
            elif funct==17 :
                op="mthi"
                print("inst %d: %s %s $%d" % (i, arr2[i], op, rs))
            elif funct==19 :
                op="mtlo"
                print("inst %d: %s %s $%d" % (i, arr2[i], op, rs))
            elif funct==16 :
                op="mfhi"
                print("inst %d: %s %s $%d" % (i, arr2[i], op, rd))
            elif funct==18 :
                op="mflo"
                print("inst %d: %s %s $%d" % (i, arr2[i], op, rd))
            elif funct==0 :
                op="sll"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rd, rt, shamt))
            elif funct==2 :
                op="srl"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rd, rt, shamt))
            elif funct==3 :
                op="sra"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rd, rt, shamt))
            elif funct==4 :
                op="sllv"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rt, rs))
            elif funct==6 :
                op="srlv"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rt, rs))
            elif funct==7 :
                op="srav"
                print("inst %d: %s %s $%d, $%d, $%d" % (i, arr2[i], op, rd, rt, rs))
            elif funct==12 :
                op="syscall"
                print("inst %d: %s %s" % (i, arr2[i], op))
            else :
                print("inst %d: %s unknown instruction" % (i, arr2[i]))
            
        elif ((opcode==2)or(opcode==3)) : # J type instructions
            pseudo_address=int(arr1[i][6:],2)
            if opcode==2 :
                op="j"
                print("inst %d: %s %s %s" % (i, arr2[i], op, pseudo_address))
            elif opcode==3 :
                op="jal"
                print("inst %d: %s %s %s" % (i, arr2[i], op, pseudo_address))

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
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rt, rs, imm))
            elif opcode==9 :
                op="addiu"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rt, rs, imm))
            elif opcode==12 :
                op="andi"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rt, rs, imm))
            elif opcode==13 :
                op="ori"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rt, rs, imm))
            elif opcode==10 :
                op="slti"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rt, rs, imm))
            elif opcode==11 :
                op="sltiu"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rt, rs, imm))
            elif opcode==14 :
                op="xori"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rt, rs, imm))
            elif opcode==4 :
                op="beq"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rs, rt, imm))
            elif opcode==5 :
                op="bne"
                print("inst %d: %s %s $%d, $%d, %d" % (i, arr2[i], op, rs, rt, imm))
            elif opcode==32 :
                op="lb"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==36 :
                op="lbu"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==33 :
                op="lh"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==37 :
                op="lhu"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==35 :
                op="lw"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==40 :
                op="sb"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==41 :
                op="sh"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==43 :
                op="sw"
                print("inst %d: %s %s $%d, %d($%d)" % (i, arr2[i], op, rt, imm, rs))
            elif opcode==15 :
                op="lui"
                print("inst %d: %s %s $%d, %d" % (i, arr2[i], op, rt, imm))
            else :
                print("inst %d: %s unknown instruction" % (i, arr2[i]))

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
    arr2.append(hex)
    arr1.append(tmp)

while True :
    arr1=[]
    arr2=[]
    command=raw_input("mips-sim> ")

    if (command=="exit") :
        exit()
    elif (command[0:4]=="read") :
        func1()
    else :
        print("wrong input")