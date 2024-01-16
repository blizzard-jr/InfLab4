import timeit
def prog():
    f = open('EntrFile.yaml', 'r', encoding = 'utf-8')
    r = open("dop5test.csv", 'w', encoding = 'utf-8')
    s = f.readlines()
    t = ""
    for i in range(len(s)):
        s[i] = s[i].replace("\n", "").lstrip()
    for i in range(1, len(s)):
        v = s[i].split(': ')
        p = s[i-1].split(': ')
        if(len(v) == 1):
            if(len(p) == 1):
                t += v[0][:-1] + "/"

            else:
                t = t.replace('lesson1', 'lesson2')


        if(len(v) == 2):
            try:
                l = s[i + 1].split(': ')
                r.write(t + v[0] + ',')
            except:
                r.write(t + v[0])



    r.write('\n')
    for i in range(len(s)):
        v = s[i].split(': ')
        if(len(v) == 2):
            try:
                l = s[i + 1].split(': ')
                r.write(v[1] + ',')
            except:
                r.write(t + v[0])

    f.close()
    r.close()
print(timeit.timeit(prog, number = 100))

#Shedule/-Friday/-lesson1/type,Shedule/-Friday/-lesson1/name,Shedule/-Friday/-lesson1/teacher,Shedule/-Friday/-lesson1/audience,Shedule/-Friday/-lesson1/adress,Shedule/-Friday/-lesson1/time,Shedule/-Friday/-lesson2/type,Shedule/-Friday/-lesson2/name,Shedule/-Friday/-lesson2/teacher,Shedule/-Friday/-lesson2/audience,Shedule/-Friday/-lesson2/adress,Shedule/-Friday/-lesson2/time
#Practise,Lineynaia algebra,Rvanova Alla,2426,"Kronversciy pr., d.49, lit.A",11:40 - 13:10,Lecture,Lineynaia algebra,Popov Igor,1404,"Kronverskiy pr., d.49, lit.A",13:30 - 15:00
