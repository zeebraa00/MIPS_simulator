def bin_to_full(binary_input) :
    # binary input : 0b00...000 type
    step1=bin(int(binary_input,0))
    remain=34-len(step1)
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

def two_complement(binray_input) :
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


while True :
    a=str(input("1,2,3,4,5,6,7,8,9 : "))
    if (a=="1") :
        b=str(input("bin : "))
        print(bin_to_full(b))
    elif (a=="2") :
        b=str(input("hex : "))
        print(hex_to_full(b))  
    elif (a=="3") :
        b=str(input("bin : "))
        print(bin_to_dec(b))
    elif (a=="4") :
        b=str(input("bin : "))
        print(bin_to_hex(b))
    elif (a=="5") :
        b=str(input("dec : "))
        print(dec_to_bin(b))
    elif (a=="6") :
        b=str(input("dec : "))
        print(dec_to_hex(b))
    elif (a=="7") :
        b=str(input("hex : "))
        print(hex_to_bin(b))
    elif (a=="8") :
        b=str(input("hex : "))
        print(hex_to_dec(b))
    elif (a=="9") :
        b=str(input("bin : "))
        print(two_complement(b))
    else :
        print("wrong")