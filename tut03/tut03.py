#def output_individual_roll():
with open("regtable_old.csv") as f:
    roll=[]
    for(i, line) in enumerate(f):
        if i==0:
            continue
        word=line.split(",")

        f1=open('output_individual_roll/{}.csv'.format(word[0]),'a')
        if not(word[0] in roll):
            roll.append(word[0])
            f1.write("rollno,register_sem,subno,sub_type\n")
        f1.write('{},{},{},{}'.format(word[0],word[1],word[3],word[8]))
        f1.close()
    #return       

#def output_by_subject():
with open("regtable_old.csv") as f:
    sub=[]
    for(i, line) in enumerate(f):
        if i==0:
            continue
        word=line.split(",")

        f2=open('output_by_subject/{}.csv'.format(word[3]),'a')
        if not(word[3] in sub):
            sub.append(word[3])
            f2.write("rollno,register_sem,subno,sub_type\n")
        f2.write('{},{},{},{}'.format(word[0],word[1],word[3],word[8]))
        f2.close()
    #return         