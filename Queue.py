input_packets = []
E_packets = []
P_packets = []
S_packets = []

#Opening (& closing w/ 'with') file, appending each line after being stripped to master input list 
with open('input queue.txt', 'r') as packet_file:
    for line in packet_file:
        input_packets.append(line.strip())

#Getting/updating length of each queue and summing total of all
def len_update():
    global P_len
    global S_len
    global E_len
    global master_len
    P_len = len(P_packets)
    S_len = len(S_packets)
    E_len = len(E_packets)
    master_len = (P_len + S_len + E_len)

#In the event of last packet type and/or last of that specific type but not enough for full send, printing/popping all remaining of that type  
def pop_count(length, queue):
    for a in range(length):
        print(queue.pop(0))

#first getting length vals updated, then checking to see if full bundle is available, if yes sending, and continuing to all other types, if no sending the rest.         
def pop_packets():
    len_update()

    if P_status == 'go':
        for a in range(3):
            print(P_packets.pop(0))
    elif P_len > 0:
        pop_count(P_len, P_packets)
    if S_status == 'go':
        print(S_packets.pop(0))
        print(S_packets.pop(0))
    elif S_len > 0:
        pop_count(S_len, E_packets)
    if E_status == 'go':
        print(E_packets.pop(0))

#Updating length values, then seeing if full bundle of type is available  - if yes status = go, if bundle incomplete status = no        
def status_check():
    len_update()
    global P_status
    global E_status
    global S_status
    
    if P_len >= 3:
        P_status = 'go'
    else:
        P_status = 'no'
        
    if S_len >= 2:
        S_status = 'go'
    else:
        S_status = 'no'
        
    if E_len >= 1:
        E_status = 'go'
    else:
        E_status = 'no'

#Sorting master input packet list by type, adding each to own list, and checking to see if acceptable
for packet in input_packets:
    if packet[0] == "E":
        E_packets.append(packet)
    elif packet[0] == "P":
        P_packets.append(packet)
    elif packet[0] == "S":
        S_packets.append(packet)
    else:
        print('Error: Input Not Accepted')

#Getting first length values      
len_update()

#while makes sure process occurs for every packet in list
while master_len > 0:   
    #Initializing Statuses
    status_check()
    pop_packets()



    
    
    
    
    
    
    
    
    