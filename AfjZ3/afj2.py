#!python
from __future__ import print_function
import os
import sys

filepath = str(sys.argv[1])
#filepath = "NKA_vysledny.txt"
#filepathOUT = "DKA.txt"
filepathOUT = str(sys.argv[2])
#slovo = "abab"
slovo = str(input("Zadaj slovo: "))
riadok = 0
pocet_stavov = 0
pocet_symbolov = 0
prechody = []
pociatocny_stav = None
stavy_akceptacne = []
stavy_neakceptacne = []
symboly = []
stavy = []
# check_sum_stavy = 0
check_sum = 0
tran1 = []
tmp = ''
tmp_prechody = []
closure = []
stavy_DKA = []
i = 0
stavy1 = stavy
stavy_DKA_tmp = []
prechody_DKA = []
tmp_values_prechodov_list = []
# tmp_values_prechodov_unique = {}
stavy_DKA_mena = []

class prechod:

    def __init__(self, odkial, kam, value):
        self.odkial = odkial
        self.kam = kam
        self.value = value

    def __str__(self):
        return "Odkial = %s, kam = %s, value = %s" % (self.odkial,self.kam,self.value)

    def __repr__(self):
        return "<Prechod - odkial:%s kam:%s value:%s>" % (self.odkial, self.kam, self.value)


def closure(transition):
    skr = 0
    tran1.clear()
    if isinstance(transition,list):
        for tt in transition:
            tran1.append(tt)
    else:
        tran1.append(transition)
    #tran1.append(transition)
    while skr < len(tran1):
        for pr in prechody:
            if pr.odkial == tran1[skr]:
               if pr.value == "Epsilon":
                    if pr.kam not in tran1:
                        tran1.append(pr.kam)
        skr = skr + 1
    return tran1


if __name__ == "__main__":

    with open(filepath) as fp:
        line = fp.readline()
        riadok = riadok + 1
        while line:
            if riadok == 1:
                pocet_stavov = int(line)
                #continue
            elif riadok == 2:
                pocet_symbolov = int(line)
                #continue
            if "," not in line:
                if(riadok > 2):
                    check_sum = check_sum + 1
                if check_sum <= (pocet_stavov + pocet_symbolov):
                    if "q" in line:
                        line = line.rstrip()
                        x = line.split(" ")
                        #if (check_sum_stavy <= pocet_stavov):
                        if "I" in x[len(x) - 1]:
                            pociatocny_stav = x[0]
                        if "F" in x[len(x) - 1]:
                            stavy_akceptacne.append(x[0])
                            stavy.append(x[0])
                        else:
                            stavy_neakceptacne.append(x[0])
                            stavy.append(x[0])
                        #else:
                            #print("Error - viac stavov na vstupe ako bolo ocakavane.")
                            #exit()
                    else:
                        if riadok > 2:
                            line = line.rstrip()
                            symboly.append(line)
                else:
                    print("Error - viac stavov a symbolov na vstupe ako bolo ocakavane.")
                    exit()
            else:
                line = line.rstrip()
                x = line.split(",")

                #tmp = prechod(x[0],x[2],x[1])
                if x[1] == "":
                    prechody.append(prechod(x[0], x[2], "Epsilon"))
                else:
                    prechody.append(prechod(x[0],x[2],x[1]))

            line = fp.readline()
            riadok = riadok + 1

    # print(pociatocny_stav)
    # print(stavy_akceptacne)
    # print(stavy_neakceptacne)
    # print(symboly)


    #jbmnt = closure(pociatocny_stav)
    #stavy_DKA.append(jbmnt)
    #tmp = ''.join(jbmnt)
    tnp = []
    tnp.append(pociatocny_stav)
    skr1 = 0
    while(skr1<len(tnp)):
        for pr in prechody:
            if pr.odkial in tnp[skr1]:
                if pr.value == "Epsilon":
                    if pr.kam not in tnp:
                        tnp.append(pr.kam)
        skr1 = skr1 + 1
    tnp1 = ''.join(tnp)
    stavy_DKA_mena.append(tnp1)
    stavy_DKA.append(tnp)
    while i < len(stavy_DKA):
        for p in prechody:
            for s in stavy_DKA[i]:
                if p.odkial in s:
                    if p.value != "Epsilon":
                        tmp_prechody.append(p)


        # for pr in tmp_prechody:
        #     if pr.kam not in stavy_DKA_tmp:
        #         stavy_DKA_tmp.append(pr.kam)
        for pr1 in tmp_prechody:
            tmp_values_prechodov_list.append(pr1.value)
        tmp_values_prechodov_unique = set(tmp_values_prechodov_list)
        if "Epsilon" in tmp_values_prechodov_unique:
            tmp_values_prechodov_unique.remove("Epsilon")
        tmp_values_prechodov_unique = list(tmp_values_prechodov_unique)

        for j in range(len(tmp_values_prechodov_unique)):
            for pr in tmp_prechody:
                if tmp_values_prechodov_unique[j] == pr.value:
                    if pr.kam not in stavy_DKA_tmp:
                        stavy_DKA_tmp.append(pr.kam)
            stavy_DKA_tmp.sort()
            stavy_DKA_tmp = closure(stavy_DKA_tmp[:])
            tmp = ''
            tmp = ''.join(stavy_DKA_tmp)
            if tmp not in stavy_DKA_mena:
                #stavy_DKA.append(stavy_DKA_tmp)
                stavy_DKA.append(stavy_DKA_tmp[:])
                stavy_DKA_mena.append(tmp)
            prechody_DKA.append(prechod(stavy_DKA[i],stavy_DKA_tmp[:],tmp_values_prechodov_unique[j]))

            stavy_DKA_tmp.clear()

        tmp_values_prechodov_list.clear()
        tmp_prechody.clear()


        i = i + 1

# print()
# print()
# print()
# print(stavy_DKA)
# for k in prechody_DKA:
#     print(k)


    pociatocny_stav_DKA = stavy_DKA[0]
    stavy_akceptacne_DKA = []

    for s in stavy_DKA:
        for ss in s:
            if isinstance(ss, list):
                for sss in ss:
                    if sss in stavy_akceptacne:
                        if ss not in stavy_akceptacne_DKA:
                            stavy_akceptacne_DKA.append(ss)
            else:
                if ss in stavy_akceptacne:
                    if s not in stavy_akceptacne_DKA:
                        stavy_akceptacne_DKA.append(s)

    #print(stavy_akceptacne_DKA)
    #print()
    #print()
    #print()
    #print()
    #VYPIS DKA
    F = open(filepathOUT,"w")
    # print(len(stavy_DKA))
    # print(len(symboly))
    # for q in stavy_DKA:
    #     if q in stavy_akceptacne_DKA and q == pociatocny_stav_DKA:
    #         str1 = ''.join(q)
    #         print(str1 + "  IF")
    #     elif q in stavy_akceptacne_DKA:
    #         str1 = ''.join(q)
    #         print(str1 + "  F")
    #     elif isinstance(q[0], list):
    #         if q[0] in stavy_akceptacne_DKA:
    #             str1 = ''.join(q[0])
    #             print(str1 + "  F")
    #     else:
    #         print(q)
    # for q in symboly:
    #     print(q)
    # for k in prechody_DKA:
    #     print(k)

    F.write(str(len(stavy_DKA))+'\n')
    F.write(str(len(symboly))+'\n')
    for q in stavy_DKA:
        if q in stavy_akceptacne_DKA and q == pociatocny_stav_DKA:
            str1 = ''.join(q)
            F.write(str1 + "  IF" +'\n')
        elif q in stavy_akceptacne_DKA:
            str1 = ''.join(str(q))
            F.write(str1 + "  F" +'\n')
        elif isinstance(q[0], list):
            if q[0] in stavy_akceptacne_DKA:
                str1 = ''.join(q[0])
                F.write(str1 + "  F"+'\n')
            else:
                F.write(str(q[0][:]) + '\n')
        else:
            F.write(str(q)+'\n')
    for q in symboly:
        F.write(q+'\n')
    for k in prechody_DKA:
        F.write(str(k)+'\n')

    # print(str(len(stavy_DKA)), file = filepathOUT)
    # print(str(len(symboly)), file = filepathOUT)
    # for q in stavy_DKA:
    #     if q in stavy_akceptacne_DKA and q == pociatocny_stav_DKA:
    #         str1 = ''.join(q)
    #         print(str1 + "  IF", file = filepathOUT)
    #     elif q in stavy_akceptacne_DKA:
    #         str1 = ''.join(q)
    #         print(str1 + "  F", file = filepathOUT)
    #     elif isinstance(q[0], list):
    #         if q[0] in stavy_akceptacne_DKA:
    #             str1 = ''.join(q[0])
    #             print(str1 + "  F", file = filepathOUT)
    #     else:
    #         print(q, file = filepathOUT)
    # for q in symboly:
    #     print(q, file = filepathOUT)
    # for k in prechody_DKA:
    #     print(k, file = filepathOUT)

    F.close()


    #HLADANIE SLOVA POMOCOU DKA
    slovo1 = list(slovo)
    kde_som = pociatocny_stav_DKA
    pmc = 0
    pmcp = []
    pmcpo = []
    for char in slovo1:
        for m in prechody_DKA:
            if m.value == char:
                pmcp.append(m)
        for m in pmcp:
            pmcpo.append(m.odkial)
        for mm in range(0, len(pmcpo)):
            if isinstance(pmcpo[mm][0], list):
                pmcpo[mm] = pmcpo[mm][0]
        if isinstance(kde_som[0],list):
            kde_som = kde_som[0]
            if kde_som not in pmcpo:
                print("Automat slovo " + slovo + " NEAKCEPTUJE")
                quit()
        else:
            if kde_som not in pmcpo:
                print("Automat slovo " + slovo + " NEAKCEPTUJE")
                quit()

        for a in prechody_DKA:
            if char not in symboly:
                print("Automat slovo " + slovo + " NEAKCEPTUJE")
                quit()

            elif isinstance(a.odkial[0],list):
                if a.odkial[0] == kde_som and char == a.value:
                    kde_som = a.kam
                    break
            else:
                if a.odkial == kde_som and char == a.value:
                    kde_som = a.kam
                    break
        pmcp.clear()
        pmcpo.clear()

    if isinstance(kde_som[0],list):
        kde_som = kde_som[0]
    if kde_som in stavy_akceptacne_DKA:
        print("Automat slovo " + slovo + " AKCEPTUJE")
    else:
        print("Automat slovo " + slovo + " NEAKCEPTUJE")
