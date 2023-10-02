# Name: Yuval Noiman
# Date: 9/18/2023
# File Purpose: Calculates meeting availability
import ast

def less_than(string1, string2):
#compares times
   if (len(string1) == 4 and len(string2) == 5):
      return True
   elif (len(string1) == 5 and len(string2) == 4):
      return False
   elif (string1 < string2):
      return True
   else:
      return False

def time_in_minutes(string1, string2):
#finds difference in time for strings
   if (len(string1) == 4):
      time = (int(string1[0:1]) * 60) + int(string1[2:4])
   else:
      time = (int(string1[0:2]) * 60) + int(string1[3:5])
   if (len(string2) == 4):
      return ((int(string2[0:1]) * 60) + int(string2[2:4])) - time
   else:
      return ((int(string2[0:2]) * 60) + int(string2[3:5])) - time

def merge_schedule(s1, s2):
# merges schedules
   s3 = []
   #if (len(s1) == 0 and len(s2) == 0):
   #   return []
   i = 0
   j = 0
   while True:
      if (i == (len(s1)) and j == (len(s2))):
         break
      elif (i == (len(s1)) and j < (len(s2))):
         s3.append(s2[j])
         j = j+1
      elif (i < (len(s1)) and j == (len(s2))):
         s3.append(s1[i])
         i = i+1
      elif (less_than(s1[i][0],s2[j][0])):
         s3.append(s1[i])
         i = i+1
      else:
         s3.append(s2[j])
         j = j+1
   #return s3
   #print(s3)

   k = 0
   while (k < len(s3)-1):
      if (less_than(s3[k][1], s3[k+1][0]) == False):
         if (less_than(s3[k][1], s3[k+1][1])):
            s3[k][1] = s3[k+1][1]
         s3.pop(k+1)
      else:
         k = k + 1
   return s3

def merge_act(act1, act2):
# merges activities
   act3 = []
   if (less_than(act1[0],act2[0]) == False):
      act3.append(act1[0])
   else:
      act3.append(act2[0])
   if (less_than(act1[1],act2[1])):
      act3.append(act1[1])
   else:
      act3.append(act2[1])
   return act3
   
def available(s, a):
#finds availability
   avail = []
   if (len(a) == 0):
      return avail
   if (len(s) == 0):
      avail.append([a[0],a[1]])
      return avail
   if (less_than(a[0],s[0][0]) and less_than(s[0][0],a[1])):
      avail.append([a[0],s[0][0]])
   #else:
   #elif(less_than(s[0][0],a[1]) == False):
   #elif(less_than(a[0],s[0][0]) == False):
      #avail.append([a[0],a[1]])
      #return avail
   for x in range(len(s)-1):
      if (less_than(a[0],s[x+1][0])):
         if (less_than(s[x+1][0],a[1]) and less_than(a[0],s[x][1])):
            avail.append([s[x][1],s[x+1][0]])
           # print(avail)
         #else:
         elif (less_than(a[0],s[x][1])):
            avail.append([s[x][1],a[1]])
            #print(avail)
            return avail
         #else:
         elif (less_than(s[x+1][0],a[1])):
            avail.append([a[0],s[x+1][0]])
            #print(avail)
   if (less_than(s[len(s)-1][1],a[1]) and less_than(a[0],s[x+1][0])):
      avail.append([s[len(s)-1][1],a[1]])
      #print(avail)
   if (len(avail) == 0):
      avail.append([a[0],a[1]])
   return avail

def available_meeting(avail, m):
#finds availablility with meeting time of at least m
   availm = []
   for x in range(len(avail)):
      if (time_in_minutes(avail[x][0],avail[x][1]) >= m):
         availm.append(avail[x])
   return availm
   
def match_schedule(s1, act1, s2, act2, m):
#matches schedules availability for meeting time of at least m
   s3 = merge_schedule(s1, s2)
   #print(s3)
   if (len(act1) == 0 or len(act2) == 0):
      return []
   if (less_than(act1[0],act1[1]) and less_than(act2[0],act2[1])):
      act3 = merge_act(act1, act2)
      #print(act3)
      avail = available(s3, act3)
      #print(avail)
      availm = available_meeting(avail, m)
   if (less_than(act1[1],act1[0]) and less_than(act2[1],act2[0])):
      act3 = (merge_act(act1,act2))
      act3_p1 = ["0:00",act3[1]]
      act3_p2 = [act3[0],"23:59"]
      avail1 = available(s3, act3_p1)
      avail2 = available(s3, act3_p2)
      availm1 = available_meeting(avail1, m)
      availm2 = available_meeting(avail2, m)
      return availm1 + availm2
   if (less_than(act1[1],act1[0])):
      act3_p1 = [act2[0],act1[1]]
      if (time_in_minutes(act3_p1[0],act3_p1[1]) <= 0):
         act3_p1 = []
      act3_p2 = [act1[0],act2[1]]
      if (time_in_minutes(act3_p2[0],act3_p2[1]) <= 0):
         act3_p2 = []
      avail1 = available(s3, act3_p1)
      avail2 = available(s3, act3_p2)
      availm1 = available_meeting(avail1, m)
      availm2 = available_meeting(avail2, m)
      return availm1 + availm2
   if (less_than(act2[1],act2[0])):
      #print(s3)
      act3_p1 = [act1[0],act2[1]]
      #print(time_in_minutes(act3_p1[0],act3_p1[1]))
      if (time_in_minutes(act3_p1[0],act3_p1[1]) <= 0):
         act3_p1 = []
      act3_p2 = [act2[0],act1[1]]
      if (time_in_minutes(act3_p2[0],act3_p2[1]) <= 0):
         act3_p2 = []
      avail1 = available(s3, act3_p1)
      #print(avail1)
      avail2 = available(s3, act3_p2)
      availm1 = available_meeting(avail1, m)
      availm2 = available_meeting(avail2, m)
      return availm1 + availm2
    
   return availm


def main():

   file1 = open("input.txt", "r")
   file2 = open("output.txt","w")
   while True:
      try:
         person1_Schedule  = ast.literal_eval(file1.readline())
         person1_DailyAct = ast.literal_eval(file1.readline())
         person2_Schedule = ast.literal_eval(file1.readline())
         person2_DailyAct = ast.literal_eval(file1.readline())
         duration_of_meeting = int(file1.readline())
         file1.readline()
         print(match_schedule(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, duration_of_meeting))
         file2.write(str(match_schedule(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, duration_of_meeting)))
         file2.write("\n")
         file2.write("\n")
         print("")
      except:
         break

   file1.close()
   file2.close()

if __name__ == "__main__":
    main()
