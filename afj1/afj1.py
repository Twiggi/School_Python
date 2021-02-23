#!python
import sys

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

filepath = str(sys.argv[1])
#filepath = "afj1.txt"
premenne = {}
riadok = 1
y = [None] * 1000
bol_jump = 0
pocet_riadkov = file_len(filepath)

with open(filepath) as fp:
    line = fp.readline()
    y[riadok] = fp.tell()
    riadok = riadok + 1
    while line:
        line = fp.readline()
        y[riadok] = fp.tell()
        riadok = riadok + 1


    riadok = 1
    fp.seek(y[riadok])
    y[riadok] = fp.tell()
    #line = fp.readline()

with open(filepath) as fp:
   line = fp.readline()
   y[riadok] = fp.tell()
   while line:
   #for i, line in enumerate(fp):

       line = line.rstrip()
       x = line.split(",")

       if x[0] == 'READ':
          premenne[x[1]] = input("Zadaj hodnotu i: ")


       elif x[0] == '=':
            #if x[1] in premenne:
            if any(c.isalpha() for c in x[2]):
                if x[2] in premenne:
                    premenne[x[1]] = premenne[x[2]]
                else:
                    print("Chyba na riadku - " + str((riadok + 1)))
                    print("Premenna " + x[2] + " neexistuje")
                    break
            else:
                    premenne[x[1]] = x[2]
            #else:
                #premenne[x[1]] = x[2]


       elif x[0] == '==':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                        if int(premenne.get(x[1])) == int(premenne.get(x[2])):
                            premenne[x[3]] = 1
                        else:
                            premenne[x[3]] = 0
                   else:
                        print("Chyba na riadku - " + str(riadok + 1))
                        print("Premenna s nazvom - " + x[2] + " neexistuje")
                        break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                    if int(premenne.get(x[1])) == int(x[2]):
                        premenne[x[3]] = 1
                    else:
                        premenne[x[3]] = 0
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                    if int(x[1]) == int(premenne.get(x[2])):
                        premenne[x[3]] = 1
                    else:
                        premenne[x[3]] = 0
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               if int(x[1]) == int(x[2]):
                   premenne[x[3]] = 1
               else:
                   premenne[x[3]] = 0


       elif x[0] == 'JUMPT':
           if x[1] in premenne:
               if premenne[x[1]] == 1:
                    if int(int(x[2])) > pocet_riadkov:
                         print("Chyba na riadku - " + str(riadok + 1))
                         print("Riadok out of boundaries")
                         break
                    riadok = int(x[2]) - 1
                    bol_jump = 1
                    fp.seek(y[riadok])
                    y[riadok] = fp.tell()
                    line = fp.readline()
           else:
               print("Chyba na riadku - " + str(riadok))
               print("Premenna " + x[1] + " nebola definovana!")
               break


       elif x[0] == 'JUMPF':
           if x[1] in premenne:
                if premenne[x[1]] == 0:
                    if int(int(x[2])) > pocet_riadkov:
                         print("Chyba na riadku - " + str(riadok + 1))
                         print("Riadok out of boundaries")
                         break
                    riadok = int(x[2]) - 1
                    bol_jump = 1
                    fp.seek(y[riadok])
                    y[riadok] = fp.tell()
                    line = fp.readline()
           else:
               print("Chyba na riadku - " + str(riadok))
               print("Premenna " + x[1] + " nebola definovana!")
               break


       elif x[0] == '*':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                       premenne[x[3]] = int(premenne[x[1]]) * int(premenne[x[2]])
                   else:
                       print("Chyba na riadku - " + str(riadok + 1))
                       print("Premenna s nazvom - " + x[2] + " neexistuje")
                       break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                   premenne[x[3]] = int(premenne[x[1]]) * int(x[2])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                   premenne[x[3]] = int(x[1]) * int(premenne[x[2]])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               premenne[x[3]] = int(x[1]) * int(x[2])


       elif x[0] == '-':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                       premenne[x[3]] = int(premenne[x[1]]) - int(premenne[x[2]])
                   else:
                       print("Chyba na riadku - " + str(riadok + 1))
                       print("Premenna s nazvom - " + x[2] + " neexistuje")
                       break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                   premenne[x[3]] = int(premenne[x[1]]) - int(x[2])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                   premenne[x[3]] = int(x[1]) - int(premenne[x[2]])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               premenne[x[3]] = int(x[1]) - int(x[2])


       elif x[0] == '+':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                       premenne[x[3]] = int(premenne[x[1]]) + int(premenne[x[2]])
                   else:
                       print("Chyba na riadku - " + str(riadok + 1))
                       print("Premenna s nazvom - " + x[2] + " neexistuje")
                       break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                   premenne[x[3]] = int(premenne[x[1]]) + int(x[2])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                   premenne[x[3]] = int(x[1]) + int(premenne[x[2]])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               premenne[x[3]] = int(x[1]) + int(x[2])


       elif x[0] == '<':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                       premenne[x[3]] = int(premenne[x[1]]) < int(premenne[x[2]])
                   else:
                       print("Chyba na riadku - " + str(riadok + 1))
                       print("Premenna s nazvom - " + x[2] + " neexistuje")
                       break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                   premenne[x[3]] = int(premenne[x[1]]) < int(x[2])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                   premenne[x[3]] = int(x[1]) < int(premenne[x[2]])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               premenne[x[3]] = int(x[1]) < int(x[2])


       elif x[0] == '>':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                       premenne[x[3]] = int(premenne[x[1]]) > int(premenne[x[2]])
                   else:
                       print("Chyba na riadku - " + str(riadok + 1))
                       print("Premenna s nazvom - " + x[2] + " neexistuje")
                       break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                   premenne[x[3]] = int(premenne[x[1]]) > int(x[2])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                   premenne[x[3]] = int(x[1]) > int(premenne[x[2]])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               premenne[x[3]] = int(x[1]) > int(x[2])


       elif x[0] == '>=':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                       premenne[x[3]] = int(premenne[x[1]]) >= int(premenne[x[2]])
                   else:
                       print("Chyba na riadku - " + str(riadok + 1))
                       print("Premenna s nazvom - " + x[2] + " neexistuje")
                       break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                   premenne[x[3]] = int(premenne[x[1]]) >= int(x[2])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                   premenne[x[3]] = int(x[1]) >= int(premenne[x[2]])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               premenne[x[3]] = int(x[1]) >= int(x[2])


       elif x[0] == '<=':
           if any(c.isalpha() for c in x[1]) and any(c.isalpha() for c in x[2]):
               if x[1] in premenne:
                   if x[2] in premenne:
                       premenne[x[3]] = int(premenne[x[1]]) >= int(premenne[x[2]])
                   else:
                       print("Chyba na riadku - " + str(riadok + 1))
                       print("Premenna s nazvom - " + x[2] + " neexistuje")
                       break
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[1]):
               if x[1] in premenne:
                   premenne[x[3]] = int(premenne[x[1]]) >= int(x[2])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[1] + " neexistuje")
                   break
           elif any(c.isalpha() for c in x[2]):
               if x[2] in premenne:
                   premenne[x[3]] = int(x[1]) >= int(premenne[x[2]])
               else:
                   print("Chyba na riadku - " + str(riadok + 1))
                   print("Premenna s nazvom - " + x[2] + " neexistuje")
                   break
           else:
               premenne[x[3]] = int(x[1]) >= int(x[2])

       elif x[0] == 'JUMP':
           if int(int(x[1])) > pocet_riadkov:
               print("Chyba na riadku - " + str(riadok + 1))
               print("Riadok out of boundaries")
               break;
           riadok = int(x[1]) - 1
           fp.seek(y[riadok])
           y[riadok] = fp.tell()
           line = fp.readline()
           bol_jump = 1




       elif x[0] == 'WRITE':
           if premenne.get(x[1]) != None:
                print(premenne.get(x[1]))
           else:
               print("Chyba na riadku - " + str(riadok + 1))
               print("PREMENNA S NAZVOM " + x[1] + " NEEXISTUJE!")
               break

       elif x[0] == 'NOP':
           random_premenna = 0


       if bol_jump == 0:
            line = fp.readline()
            riadok = riadok + 1
            y[riadok] = fp.tell()
       if bol_jump == 1:
           bol_jump = 0

