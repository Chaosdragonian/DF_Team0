import os
import sys
import random


name1 = sys.argv[1]
name2 = sys.argv[2]
name3 = sys.argv[3]
name4 = sys.argv[4]
name5 = sys.argv[5]
name6 = sys.argv[6]
name7 = sys.argv[7]
name8 = sys.argv[8]
name9 = sys.argv[9]
name10 = sys.argv[10]
name11 = sys.argv[11]
name12 = sys.argv[12]


slave = [name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12]
slaveteam1 = []
slaveteam2 = []
slaveteam3 = []
slaveteam4 = []

print ("[*]Real Life is Random")
random.shuffle(slave)
slaveteam1.append(slave[0])
slaveteam1.append(slave[1])
slaveteam1.append(slave[2])
slaveteam2.append(slave[3])
slaveteam2.append(slave[4])
slaveteam2.append(slave[5])
slaveteam3.append(slave[6])
slaveteam3.append(slave[7])
slaveteam3.append(slave[8])
slaveteam4.append(slave[9])
slaveteam4.append(slave[10])
slaveteam4.append(slave[11])


print ("[*] Team 1 is")
print (slaveteam1)
print ("[*] Team 2 is")
print (slaveteam2)
print ("[*] Team 3 is")
print (slaveteam3)
print ("[*] Team 4 is")
print (slaveteam4)






