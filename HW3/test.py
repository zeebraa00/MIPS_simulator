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
        #positive
        output=bin_to_dec(step1)
    print(output)

hex_to_dec_signed("0xFFFF0000")

print(bin(123123))