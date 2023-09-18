# Name: Yuval Noiman
# Date: 9/18/2023
# File Purpose: Calculates meeting availability

def merge_schedule(s1, s2):
# merges schedules
   s3 = []
   return s3 
  
def merge_act(act1, act2):
# merges activities
   act3 = []
   return act3
   
def available(s, a):
#finds availability
   avail = []
   return avail

def available_meeting(avail, m):
#finds availablility with meeting time of at least m
   availm = []
   return availm
   
def matchschedule(s1, act1, s2, act2, m):
#matches scehduels availabilty for meeting time of at least m
   s3 = merge_schedule(s1, s2)
   act3 = merge_act(act1, act2)
   avail = available(s3, act3)
   availm = available_meeting(avail, m)
   return availm
