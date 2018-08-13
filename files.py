#1.Enter records
#2.Read Record
#choice 1 -> Enter name: Enter address _->save(Y/N)
#Y ->append mode ma kholne
#N ->exit
#choice 2 ->  no record.. read mode


print("1.Enter records")
print("2.Read records")
choice = input("Enter choice (1/2):")
while choice == 1 or choice == 2:
    if choice == 1:
        c = True
        while c:
            i = input("Enter name: ")
            j = input("Enter address: ")
            save = input("Do you want to save?(y/n): ")
            c = (save == 'y')
            p = open("RecordFile.txt",'a')
            p.write(i)
            p.write(j)
            #elif save == 'n':
                #print("Records hasn't been saved.")
            #else:
                #print("Invalid input.")


    else:
        p = open("RecordFile.txt",'r')

p.close()
