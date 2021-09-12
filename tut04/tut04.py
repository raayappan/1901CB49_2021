import csv
import os
from openpyxl import Workbook
os.system('cls')

def output_by_subject():
    sub=dict()
    with open("regtable_old.csv") as f:
        r=csv.reader(f)
        #print(r)
        for word in r:
            if word[0]=="rollno":
                continue
            if not(word[3] in sub):
                sub[word[3]]=[["rollno","register_sem","subno","sub_type"]]
                sub[word[3]].append([word[0],word[1],word[3],word[8]]) 
            else:
                sub[word[3]].append([word[0],word[1],word[3],word[8]]) 
        for i in sub:
            wb=Workbook() 
            sheet=wb.active
            for j in sub[i]:
                sheet.append(j)
            wb.save('output_by_subject/{}.xlsx'.format(i))      
    return

def output_individual_roll():
    roll=dict()
    with open("regtable_old.csv") as f:
        r=csv.reader(f)
        #print(r)
        for word in r:
            if word[0]=="rollno":
                continue
            if not(word[0] in roll):
                roll[word[0]]=[["rollno","register_sem","subno","sub_type"]]
            else:
               roll[word[0]].append([word[0],word[1],word[3],word[8]]) 
        for i in roll:
            wb=Workbook() 
            sheet=wb.active
            for j in roll[i]:
                sheet.append(j)
            wb.save('output_individual_roll/{}.xlsx'.format(i))      
    return

output_by_subject()
output_individual_roll()