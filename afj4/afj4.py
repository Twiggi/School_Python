#!python

import os
import sys

#filepath = "afj5.txt"
#filepathOUT = "afjOUT.txt"
filepath = sys.argv[1]
filepathOUT = sys.argv[2]
subor_out = {}
subor_out_other_way_around = {}
riadok_v_subor_out = 1
najvacsia_zatvorka = 99

def najvacsie_cislo_v_liste(l):
    cisla = []
    for i in range(0, len(l)):
        l[i] = str(l[i])
        if l[i].isdigit():
            cisla.append(l[i])
    return max(cisla)

if __name__ == "__main__":
    with open(filepath) as fp:
        line = fp.readline()


    riadok = list(line)
    orig_riadok = list(line)


    for i in range(0,len(riadok)):
        if riadok[i] == ' ':
            riadok[i] = 'ε'
            orig_riadok[i] = 'ε'

    zatvorka = 0
    for i in range(0,len(riadok)):
        if riadok[i] == "(":
            zatvorka = zatvorka + 1
            riadok[i] = zatvorka
        elif riadok[i] == ")":
            riadok[i] = zatvorka
            zatvorka = zatvorka - 1
        else:
            continue


    while int(najvacsia_zatvorka) > 0:
        najvacsia_zatvorka = najvacsie_cislo_v_liste(riadok)
        vnutorne_zatvorky = [i for i, x in enumerate(riadok) if x == najvacsia_zatvorka]
        for i in range(0,len(vnutorne_zatvorky)):
            if i%2 == 0:
                tmp = []
                for j in range(vnutorne_zatvorky[i]+1,vnutorne_zatvorky[i+1]):
                    tmp.append(riadok[j])

                if "*" in tmp:
                    for k in range(0, len(tmp)):
                        if tmp[k].isalpha():
                            subor_out[riadok_v_subor_out] = str(tmp[k])
                            subor_out_other_way_around[str(tmp[k])] = riadok_v_subor_out
                            riadok_v_subor_out = riadok_v_subor_out + 1
                    for k in range(1, len(tmp)):
                        if tmp[k] == "*":
                            subor_out[riadok_v_subor_out] = str("I," + str(subor_out_other_way_around[tmp[k-1]]))
                            subor_out_other_way_around[str("I," + str(subor_out_other_way_around[tmp[k-1]]))] = riadok_v_subor_out
                            riadok_v_subor_out = riadok_v_subor_out + 1
                    for j in range(vnutorne_zatvorky[i]+1,vnutorne_zatvorky[i+1]):
                        if "*" == riadok[j]:
                            riadok[j] = subor_out[riadok_v_subor_out-1]
                        else:
                            riadok[j] = "-"

                elif "|" in tmp:
                    for k in range(0, len(tmp)):
                        if tmp[k].isalpha():
                            subor_out[riadok_v_subor_out] = str(tmp[k])
                            subor_out_other_way_around[str(tmp[k])] = riadok_v_subor_out
                            riadok_v_subor_out = riadok_v_subor_out + 1
                    for k in range(2, len(tmp)):
                        if(k%2 == 0):
                            subor_out[riadok_v_subor_out] = str("U,"+str(subor_out_other_way_around[tmp[k-2]])+","+str(subor_out_other_way_around[tmp[k]]))
                            subor_out_other_way_around[str("U,"+str(subor_out_other_way_around[tmp[k-2]])+","+str(subor_out_other_way_around[tmp[k]]))] = riadok_v_subor_out
                            riadok_v_subor_out = riadok_v_subor_out + 1
                            for j in range(vnutorne_zatvorky[i] + 1, vnutorne_zatvorky[i + 1]):
                                if riadok[j] == tmp[k]:
                                    riadok[j] = str("U," + str(subor_out_other_way_around[tmp[k-2]]) + "," + str(subor_out_other_way_around[tmp[k]]))
                                    tmp[k] = str("U," + str(subor_out_other_way_around[tmp[k-2]]) + "," + str(subor_out_other_way_around[tmp[k]]))

                    for j in range(vnutorne_zatvorky[i] + 1, vnutorne_zatvorky[i + 1] - 1):
                        riadok[j] = "-"

                else:
                    for k in range(0, len(tmp)):
                        if tmp[k].isalpha():
                            subor_out[riadok_v_subor_out] = str(tmp[k])
                            subor_out_other_way_around[str(tmp[k])] = riadok_v_subor_out
                            riadok_v_subor_out = riadok_v_subor_out + 1
                    for k in range(1, len(tmp)):
                        subor_out[riadok_v_subor_out] = str("C,"+str(subor_out_other_way_around[tmp[k-1]])+","+str(subor_out_other_way_around[tmp[k]]))
                        subor_out_other_way_around[str("C,"+str(subor_out_other_way_around[tmp[k-1]])+","+str(subor_out_other_way_around[tmp[k]]))] = riadok_v_subor_out
                        riadok_v_subor_out = riadok_v_subor_out + 1
                        for j in range(vnutorne_zatvorky[i] + 2, vnutorne_zatvorky[i + 1]):
                            if riadok[j] == tmp[k]:
                                riadok[j] = str("C,"+str(subor_out_other_way_around[tmp[k-1]])+","+str(subor_out_other_way_around[tmp[k]]))
                                tmp[k] = str("C,"+str(subor_out_other_way_around[tmp[k-1]])+","+str(subor_out_other_way_around[tmp[k]]))

                    for j in range(vnutorne_zatvorky[i] + 1, vnutorne_zatvorky[i+1]-1):
                        riadok[j] = "-"


        riadok = list(filter((najvacsia_zatvorka).__ne__, riadok))
        riadok = list(filter(("-").__ne__, riadok))
        if najvacsia_zatvorka == '1':
            najvacsia_zatvorka = 0

    F = open(filepathOUT, "w")
    for key,value in subor_out.items():
        if value == 'ε':
            F.write(('\n'))
        else:
            F.write(str(value + "\n"))
    F.close()

    os.system('python afj3.py ' + filepathOUT)
