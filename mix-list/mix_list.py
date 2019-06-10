#!/usr/bin/env python3
my_list= ["192.168.0.5", 5060, "UP"]
print("the first item in the list (IP): " + my_list[0] )
print("the second  item in the list (PORT): " + str(my_list[1]) )
print("the last item in the list (STATE): " + my_list[2] )

#creates new list and message
new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
print ( 'You are not Authorized to ' + new_list[5], ' on port: ' +str(new_list[0])," or "+str(new_list[2]), " or " + new_list[1], " to IPs:" + new_list[3], " and " + new_list[4])



