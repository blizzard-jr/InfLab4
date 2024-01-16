import timeit
def prog():
    entrfile = open('EntrFile.yaml', 'r', encoding = "utf-8")
    exitfile = open('ExitFile.json','w', encoding = "utf-8")
    newline = entrfile.readlines()
    entrfile.close()
    for i in range(len(newline)):
        newline[i] = newline[i].replace("\n", "")
    count = 0
    for i in range(len(newline)):
        str_check1 = newline[i-1].lstrip().split(": ")
        str_check2 = newline[i].lstrip().split(": ")
        try:
            str_check3 = newline[i + 1].lstrip().split(": ")
        except:
            exitfile.write('\t\t\t  "' + str_check2[0] + '" : "' + str_check2[1] + '"\n')
            continue
        if(newline[i] == "---"):
            exitfile.write("{\n")
        elif(len(str_check2) == 1 and len(str_check1) != 2):
            exitfile.write((((i-1)+i)*2*" ") + '"' + str_check2[0][:-1] + '" : [\n' + ((i*2)*"  ") + '{\n')
            count += 1
        elif(len(str_check2) == 2 and len(str_check3) > 1):
            exitfile.write('\t\t\t  "' + str_check2[0] + '" : "' + str_check2[1] + '",\n')
        elif(len(str_check2) == 2 and len(str_check3) == 1):
            exitfile.write('\t\t\t  "' + str_check2[0] + '" : "' + str_check2[1] + '"\n')
        elif(len(str_check2) == 1 and len(str_check1) == 2):
            exitfile.write('\t\t\t}\n\t\t  ],\n\t\t  "' + str_check2[0][:-1] + '" : [\n\t\t\t{\n')
            count += 1
    for i in range(6, -1, -1):
        if(i%2 == 0):
            exitfile.write(i * 2 * " " + "}\n")
        else:
            exitfile.write(i * 2 * " " + "]\n")
    exitfile.close()
print(timeit.timeit(prog, number = 100))


