import timeit
import re
def prog():
    r1 = r"[-]?\w*[:]"
    r2 = r".*[:] .*"
    entrfile = open('EntrFile.yaml', 'r', encoding = "utf-8")
    exitfile = open('dop2.json', 'w', encoding = "utf-8")
    newline = entrfile.readlines()
    for i in range(len(newline)):
        newline[i] = newline[i].replace("\n", "")
    newline.pop(0)
    for i in range(len(newline)):
        spaces = i*"\t"
        str_checker = newline[i].lstrip()
        str_checker1 = str_checker.split(": ")
        str_checker2 = newline[i-1].lstrip()
        try:
            str_checker3 = newline[i + 1].lstrip()
        except:
            exitfile.write('\t\t\t  "' + str_checker1[0] + '" : "' + str_checker1[1] + '"\n')
            continue
        if(re.fullmatch(r1, str_checker)):
            if(i<4):
                exitfile.write(spaces + '{\n' + spaces + "  " + '"' + str_checker[:-1] + '" : [\n')
            else:
                exitfile.write('\t\t  "' + str_checker[:-1] + '" : [\n\t\t\t')
        elif(re.fullmatch(r2, str_checker)):
            if(re.fullmatch(r1, str_checker3)):
                exitfile.write('\t\t\t  "' + str_checker1[0] + '" : "' + str_checker1[1] + '"\n\t\t\t}\n\t\t  ],\n')
            elif(re.fullmatch(r1, str_checker2) and i < 7):
                exitfile.write('\t\t\t{\n\t\t\t  "' + str_checker1[0] + '" : "' + str_checker1[1] + '",\n')
            elif (re.fullmatch(r1, str_checker2) and i > 7):
                exitfile.write('{\n\t\t\t  "' + str_checker1[0] + '" : "' + str_checker1[1] + '",\n')
            else:
                exitfile.write('\t\t\t  "' + str_checker1[0] + '" : "' + str_checker1[1] + '",\n')

    for i in range(6, -1, -1):
        if(i%2 == 0):
            exitfile.write(i * 2 * " " + "}\n")
        else:
            exitfile.write(i * 2 * " " + "]\n")
    exitfile.close()

print(timeit.timeit(prog, number = 100))








