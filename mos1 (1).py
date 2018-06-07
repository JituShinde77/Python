# Mos Lab
import sys
#sys.stdin.readline()
num = int(raw_input("Enter the Number of Processes:"))

process = []

for i in range(0, num):
    temp =[]
    temp.append(i)
    st = int(raw_input("Start Time:"))
    temp.append(st)
    ex = int(raw_input("Ex Time:"))
    temp.append(ex)
    peroid = int(raw_input("Peroid Time:"))
    temp.append(peroid)
    temp.append(0)
    process.append(temp)

for i in process:
    print (i)

priority_queue = []
for timer in range(0, 300, 5):

    for j in process:
        if j[1] == timer:
            if j[4] != 0:
                print ("Process not completed in deadline:");
                exit()

            temp_que = []
            temp_que.append(j[0]) # Fopr ID

            temp_que.append(j[1] + j[3])
            j[4] = j[2]
            j[1] = j[1] + j[3]
            priority_queue.append(temp_que)
            priority_queue.sort(key=lambda x:x[1])

    if(len(priority_queue) != 0):
        id = priority_queue[0][0]
        print (timer, "To", timer + 5 ,"Peroid")
        print ("Process:", id, "::" ,process[id][4])

        process[id][4] -= 5
        if(process[id][4] == 0):
             del priority_queue[0]

        print (priority_queue)
