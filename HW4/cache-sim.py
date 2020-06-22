import sys

def hex_to_bin(hex_input) :
    # hex input : 0x0...00 type
    step1=bin(int(hex_input,0))
    remain=34-len(step1)
    output="0b"+remain*"0"+step1[2:]
    return output

def hex_to_dec(hex_input) :
    # hex input : 0x0...00 type
    return int(hex_input,0)

#############################################################################################
#############################################################################################

load_or_store=[]
address=[]
tag_array=[];tag_array_2=[]
valid_bit=[];valid_bit_2=[]
lru=[]
dirty=[];dirty_2=[]

hit_num=0
miss_num=0
write_num=0

cache_type=int(sys.argv[1])
file_num=sys.argv[2]

#############################################################################################
#############################################################################################

if (cache_type==0) :
    for i in range (1024) :
        valid_bit.append("0")
        tag_array.append("0"*18)

elif (cache_type==1) :
    for i in range (1024) :
        valid_bit.append(0)
        tag_array.append("0"*17)
        lru.append(0)
        valid_bit_2.append(0)
        tag_array_2.append("0"*17)
        dirty.append(0)
        dirty_2.append(0)
        
else :
    sys.stderr.write("wrong input")

#############################################################################################
#############################################################################################

filename="trace"+file_num+".txt"

try :
    f=open(filename, "rb")
    input=f.readlines()
    total_operation=len(input)
    for line in input : 
        load_or_store.append(line[0])
        address.append(line[2:10])
except :
    sys.stderr.write("No file: %s\n" % filename)  

#############################################################################################
#############################################################################################

for i in range (total_operation) :
    full_instruction=hex_to_bin("0x"+address[i])

    if ( (cache_type==0) and (load_or_store[i]=="L") ) :

        now_tag=full_instruction[2:20]  
        now_index=int(full_instruction[20:30],2)
        now_offset=full_instruction[30:34]

        if (valid_bit[now_index]==1) :
            if (tag_array[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
            else :
                print(i,"miss")
                miss_num+=1
                tag_array[now_index]=now_tag

        else :
            print(i,"miss")
            miss_num+=1
            tag_array[now_index]=now_tag
            valid_bit[now_index]=1


    elif ( (cache_type==0) and (load_or_store[i]=="S") ) :

        now_tag=full_instruction[2:20]  
        now_index=int(full_instruction[20:30],2)
        now_offset=full_instruction[30:34]

        if (valid_bit[now_index]==1) :
            if (tag_array[now_index]==now_tag) :
                print(i,"write_hit")
                write_num+=1
                hit_num+=1
            else :
                print(i,"write_miss")
                write_num+=1
                miss_num+=1

        else :
            print(i,"write_miss")
            miss_num+=1
            write_num+=1

#############################################################################################
#############################################################################################

    elif ( (cache_type==1) and (load_or_store[i]=="L") ) :

        now_tag=full_instruction[2:19]  
        now_index=int(full_instruction[19:28],2)
        now_offset=full_instruction[28:34]
        
        if ( (valid_bit[now_index]==0) and (valid_bit_2[now_index]==0) ) :
            print(i,"miss")
            miss_num+=1
            lru_num=lru[now_index]
            if (lru_num==0) :
                tag_array[now_index]=now_tag
                valid_bit[now_index]=1
                lru[now_index]=1
            else :
                tag_array_2[now_index]=now_tag
                valid_bit_2[now_index]=1
                lru[now_index]=0
        
        elif ( (valid_bit[now_index]==1) and (valid_bit_2[now_index]==0) ) :
            if (tag_array[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
                lru[now_index]=1
            else :
                print(i,"miss")
                miss_num+=1
                valid_bit_2[now_index]=1
                tag_array_2[now_index]=now_tag
                lru[now_index]=0

        elif ( (valid_bit[now_index]==0) and (valid_bit_2[now_index]==1) ) :
            if (tag_array_2[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
                lru[now_index]=1
            else :
                print(i,"miss")
                miss_num+=1
                valid_bit[now_index]=1
                tag_array[now_index]=now_tag
                lru[now_index]=1

        else :
            if (tag_array[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
                lru[now_index]=1
            elif (tag_array_2[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
                lru[now_index]=0
            else :
                print(i,"miss")
                miss_num+=1

                lru_num=lru[now_index]
                if (lru_num==0) :
                    if (dirty[now_index]==1) :
                        write_num+=1 ##########################
                        print("MemWrite")
                        dirty[now_index]=0
                    valid_bit[now_index]=1
                    tag_array[now_index]=now_tag
                    lru[now_index]=1
                else :
                    if (dirty_2[now_index]==1) :
                        write_num+=1 ##########################
                        print("MemWrite")
                        dirty_2[now_index]=0
                    tag_array_2[now_index]=now_tag
                    valid_bit_2[now_index]=1
                    lru[now_index]=0

#############################################################################################
#############################################################################################

    elif ( (cache_type==1) and (load_or_store[i]=="S") ) :

        now_tag=full_instruction[2:19]  
        now_index=int(full_instruction[19:28],2)
        now_offset=full_instruction[28:34]

        if ( (valid_bit[now_index]==0) and (valid_bit_2[now_index]==0) ) :
            miss_num+=1
            print(i,"miss")
            if (lru[now_index]==0) :
                valid_bit[now_index]=1
                tag_array[now_index]=now_tag
                dirty[now_index]=1
                lru[now_index]=1
            else :
                valid_bit_2[now_index]=1
                tag_array_2[now_index]=now_tag
                dirty_2[now_index]=1
                lru[now_index]=0

        elif ( (valid_bit[now_index]==1) and (valid_bit_2[now_index]==0) ) :
            if (tag_array[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
                # dirty[now_index]=1
                lru[now_index]=1

            else :
                print(i,"miss")
                miss_num+=1
                valid_bit_2[now_index]=1
                tag_array_2[now_index]=now_tag
                dirty_2[now_index]=1
                lru[now_index]=0

        elif ( (valid_bit[now_index]==0) and (valid_bit_2[now_index]==1) ) :
            if (tag_array_2[now_index]==now_tag) :
                hit_num+=1
                print(i,"hit")
                # dirty_2[now_index]=1
                lru[now_index]=0

            else :
                print(i,"miss")
                miss_num+=1
                valid_bit[now_index]=1
                tag_array[now_index]=now_tag
                dirty[now_index]=1
                lru[now_index]=1

        else :
            if (tag_array[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
                dirty[now_index]=1 ##########
                lru[now_index]=1
            elif (tag_array_2[now_index]==now_tag) :
                print(i,"hit")
                hit_num+=1
                dirty_2[now_index]=1 ############
                lru[now_index]=0
            else : ##########################################################
                if (lru[now_index]==0) :
                    miss_num+=1
                    print(i,"miss")
                    valid_bit[now_index]=1
                    tag_array[now_index]=now_tag
                    if (dirty[now_index]==1) :
                        write_num+=1
                    dirty[now_index]=1
                    lru[now_index]=1

                elif (lru[now_index]==1) :
                    miss_num+=1
                    print(i,"miss")
                    valid_bit_2[now_index]=1
                    tag_array_2[now_index]=now_tag
                    if (dirty_2[now_index]==1) :
                        write_num+=1
                    dirty_2[now_index]=1
                    lru[now_index]=0 

    else :
        sys.stderr.write("wrong input")

#############################################################################################
#############################################################################################

print("{0} {1}" .format(miss_num, write_num ))