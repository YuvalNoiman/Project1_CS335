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
   i = 0
   j = 0
   s3_index = -1
   while True:
      #print(s3)
      if (i == (len(s1)) and j == (len(s2))):
         break
      elif (i == (len(s1)) and j < (len(s2))):
         if (less_than(s3[s3_index][1],s2[j][0]) == False):
            #print(s2[j][0])
            #print(s3[s3_index][1])
            if (less_than(s3[s3_index][1],s2[j][1])):
                s3[s3_index][1] = s2[j][1]
         else:
            s3.append(s2[j])
            s3_index = s3_index+1
         j = j+1
      elif (i < (len(s1)) and j == (len(s2))):
         if (less_than(s3[s3_index][1],s1[i][0]) == False):
            #print(s3[s3_index][1])
            #print(s1[i][1])
            if (less_than(s3[s3_index][1],s1[i][1])):
                s3[s3_index][1] = s1[i][1]
         else:
            s3.append(s1[i])
            s3_index = s3_index+1
         i = i+1
      elif (less_than(s1[i][0],s2[j][0])):
         if (s3_index > -1):
            if (less_than(s3[s3_index][1],s1[i][0]) == False):
               if (less_than(s3[s3_index][1],s1[i][1])):
                   s3[s3_index][1] = s1[i][1]
            else:
               s3.append(s1[i])
               s3_index = s3_index+1
         else:
            s3.append(s1[i])
            s3_index = s3_index+1
         i = i+1
      else:
         if (s3_index > -1):
            if (less_than(s3[s3_index][1],s2[j][0]) == False):
               if (less_than(s3[s3_index][1],s2[j][1])):
                   s3[s3_index][1] = s2[j][1]
            else:
               s3.append(s2[j])
               s3_index = s3_index+1
         else:
            s3.append(s2[j])
            s3_index = s3_index+1
         j = j+1
   return s3

def merge_act(act1, act2):
# merges activities
   act3 = []
   if (act1[0] > act2[0]):
      act3.append(act1[0])
   else:
      act3.append(act2[0])
   if (act1[1] < act2[1]):
      act3.append(act1[1])
   else:
      act3.append(act2[1])
   return act3
   
def available(s, a):
#finds availability
   avail = []
   if (less_than(a[0],s[0][0])):
      avail.append([a[0],s[0][0]])
   for x in range(len(s)-1):
      avail.append([s[x][1],s[x+1][0]])
   if (less_than(s[len(s)-1][1],a[1])):
      avail.append([s[len(s)-1][1],a[1]])
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
   act3 = merge_act(act1, act2)
   avail = available(s3, act3)
   availm = available_meeting(avail, m)
   return availm


def main():
   person1_Schedule =[ ['12:00', '13:00'], ['16:00', '18:00']]
   #print(type(person1_Schedule))
   person1_DailyAct = ['9:00', '19:00']
   person2_Schedule = [['9:00', '10:30'], ['12:20', '14:30'], ['14:00', '15:00'], ['16:00', '17:00' ]]
   person2_DailyAct = ['9:00', '18:30']
   duration_of_meeting =30

   print(match_schedule(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, duration_of_meeting))
   print(less_than("16:00","14:00"))
   file1 = open("input.txt", "r")
   while True:
   #for x in range(4):
      try:
      #person1_Schedule =file1.readline().replace('\n', '').strip('][').split(', ')
         person1_Schedule  = ast.literal_eval(file1.readline())
      #print(person1_Schedule)
        # if (person1_Schedule == ""):
         #   break
      #print(type(person1_Schedule[0]))
         person1_DailyAct = ast.literal_eval(file1.readline())
      #print(person1_DailyAct)
         person2_Schedule = ast.literal_eval(file1.readline())
      #print(person2_Schedule)
         person2_DailyAct = ast.literal_eval(file1.readline())
      #print(person2_DailyAct)
         duration_of_meeting = int(file1.readline())
      #print(duration_of_meeting)
      #print(file1.readline())
         file1.readline()
         print(match_schedule(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, duration_of_meeting))
      #print(file1.readline())
      except:
         break

   file1.close()

if __name__ == "__main__":
    main()
