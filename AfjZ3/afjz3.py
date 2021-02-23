#!python
import sys
import os


class prechod:

    def __init__(self, odkial, kam, value):
        self.odkial = odkial
        self.kam = kam
        self.value = value

    def __str__(self):
        return "Odkial = %s, kam = %s, value = %s" % (self.odkial, self.kam, self.value)

    def __repr__(self):
        return "<Prechod - odkial:%s kam:%s value:%s>" % (self.odkial, self.kam, self.value)


filepath = str(sys.argv[1])
outputNKA = str(sys.argv[2])
outputDKA = str(sys.argv[3])
#filepath = "afj1.txt"
#outputNKA = "NKA_vysledny.txt"
#outputDKA = "DKA.txt"
na_ktorom_som_riadku = 1
subor = {}
stavy = []
stavy_init = []
stavy_akceptacne = []
prechody = []
prvy_symbol_v_riadku = 'a'
i = 0
riadok = []
k = 1
automaty = {}
tmp = []
akceptacne_v_automate = []
akceptacne_v_automate2 = []
init_v_hladanom_automate = []
init_v_hladanom_automate2 = []
tmp_stavy123 = {}

if __name__ == "__main__":
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            subor[str(k)] = line.strip('\n')
            k = k + 1
            line = fp.readline()

    with open(filepath) as fp:
        line = fp.readline()
        line = line.strip('\n')
        if line != '':
            prvy_symbol_v_riadku = line[0]
        while line or na_ktorom_som_riadku <= len(subor):
            if line == '':  # je to prazdny (epsilon) vyraz
                stavy_init.append('q' + str(i))
                stavy_akceptacne.append('q' + str(i))
                stavy.append(('q' + str(i)))

                tmp.append('q' + str(i) + ' IF')

                i = i + 1

                automaty[str(na_ktorom_som_riadku)] = tmp

                tmp = []

            if len(line) == 1:
                if line not in stavy:
                    stavy_init.append('q' + str(i))
                    stavy_akceptacne.append('q' + str(i + 1))
                    stavy.append('q' + str(i))
                    stavy.append('q' + str(i + 1))

                    xyp9x = 'q' + str(i)
                    dupreeh = 'q' + str(i + 1)
                    if xyp9x in stavy_akceptacne and xyp9x in stavy_init:
                        tmp.append(xyp9x + " IF")
                    elif xyp9x in stavy_akceptacne and xyp9x not in stavy_init:
                        tmp.append(xyp9x + " F")
                    elif xyp9x not in stavy_akceptacne and xyp9x in stavy_init:
                        tmp.append(xyp9x + " I")
                    else:
                        tmp.append(xyp9x)

                    if dupreeh in stavy_akceptacne and dupreeh in stavy_init:
                        tmp.append(dupreeh + " IF")
                    elif dupreeh in stavy_akceptacne and dupreeh not in stavy_init:
                        tmp.append(dupreeh + " F")
                    elif dupreeh not in stavy_akceptacne and dupreeh in stavy_init:
                        tmp.append(dupreeh + " I")
                    else:
                        tmp.append(dupreeh)

                    i = i + 2
                    prechody.append(
                        prechod(stavy_init[len(stavy_init) - 1], stavy_akceptacne[len(stavy_akceptacne) - 1], line))

                    tmp.append(
                        prechod(stavy_init[len(stavy_init) - 1], stavy_akceptacne[len(stavy_akceptacne) - 1], line))

                    automaty[str(na_ktorom_som_riadku)] = tmp

                    tmp = []
                else:
                    print("CHYBA - Takyto symbol bol zadany uz predtym.")
                    exit()

            if prvy_symbol_v_riadku == 'I':
                # check ci existuje riadok
                riadok = line.split(',')
                if int(riadok[1]) > len(subor.keys()):
                    print("CHYBA - Referencia na riadok, ktory neexistuje.")
                    exit()
                stavy_init.append('q' + str(i))  # vytvorim novy pociatocny stav
                stavy_akceptacne.append('q' + str(i))  # pociatocny je aj akceptacny
                stavy.append('q' + str(i))  # a je to aj stav ako taky... DUH

                tmp.append('q' + str(i) + " IF")

                i = i + 1  # zvysenie i kvoli nazvom stavov

                hladany_automat = automaty.get(riadok[1])  # najdem automat ktory chcem iterovat
                # init_v_hladanom_automate = list(set(hladany_automat) & set(stavy_init))     #najdem v nom pociatocny stav
                for a in hladany_automat:
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'I' in b:
                            c = b.replace("I", "")
                            init_v_hladanom_automate.append(c)

                # akceptacne_v_automate = list(set(hladany_automat) & set(stavy_akceptacne))  #najdem v nom akceptacne stavy
                for a in hladany_automat:
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'F' in b:
                            c = b.replace("F", "")
                            c = c.replace("I", "")
                            akceptacne_v_automate.append(c)
                akceptacne_v_automate = set(akceptacne_v_automate)

                # tmp1 = list(akceptacne_v_automate)
                # tmp1.append(init_v_hladanom_automate[0])
                for s in hladany_automat:  # pridam veci do noveho automatu
                    if (s, str) and "," not in str(s):  # je to stav, nie prechod
                        s = s.replace(" ", "")
                        s = s.replace("F", "")
                        s = s.replace("I", "")

                        if s in akceptacne_v_automate:
                            tmp.append(s + " F")
                        else:
                            tmp.append(s)
                    else:
                        tmp.append(s)

                # tmp_stav_init_pre_iter = automaty.values()
                prechody.append(prechod(str(stavy_init[len(stavy_init) - 1]), str(init_v_hladanom_automate[0]),
                                        'ε'))  # nastavit novy init, tym ze spravi epsilon prechod z noveho init do stareho init
                tmp.append(prechod(str(stavy_init[len(stavy_init) - 1]), str(init_v_hladanom_automate[0]), 'ε'))
                for device in akceptacne_v_automate:
                    prechody.append(
                        prechod(device, init_v_hladanom_automate[0], 'ε'))  # z akceptacnych do povodnych init
                    tmp.append(prechod(device, init_v_hladanom_automate[0], 'ε'))
                stavy_init.remove(init_v_hladanom_automate[0])  # povodny init stav uz nie je init

                automaty[str(na_ktorom_som_riadku)] = tmp  # vytvorim automat pre prislusny riadok

                tmp = []
                init_v_hladanom_automate = []
                akceptacne_v_automate = []

            if prvy_symbol_v_riadku == 'C':
                # check ci existuje riadok
                riadok = line.split(',')
                if int(riadok[1]) > len(subor.keys()):
                    print("CHYBA - Referencia na riadok, ktory neexistuje.")
                    exit()

                hladany_automat = automaty.get(riadok[1]).copy()  # najdem prvy automat
                hladany_automat2 = automaty.get(riadok[2]).copy()  # najdem druhy automat

                for a in hladany_automat:  # najdem v prvom pociatocny stav
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'I' in b:
                            c = b.replace("I", "")
                            c = c.replace("F", "")
                            init_v_hladanom_automate.append(c)

                for a in hladany_automat2:  # najdem v druhom pociatocny stav
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'I' in b:
                            c = b.replace("I", "")
                            c = c.replace("F", "")
                            init_v_hladanom_automate2.append(c)

                for a in hladany_automat:  # najdem v prvom akceptacne stavy
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'F' in b:
                            c = b.replace("F", "")
                            c = c.replace("I", "")
                            akceptacne_v_automate.append(c)
                akceptacne_v_automate = set(akceptacne_v_automate)

                for a in hladany_automat2:  # najdem v druhom akceptacne stavy
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'F' in b:
                            c = b.replace("F", "")
                            c = c.replace("I", "")
                            akceptacne_v_automate2.append(c)
                akceptacne_v_automate2 = set(akceptacne_v_automate2)

                for s in hladany_automat:  # pridam veci do noveho automatu
                    if (s, str) and "," not in str(s):  # je to stav, nie prechod
                        s = s.replace(" ", "")
                        s = s.replace("F", "")
                        s = s.replace("I", "")

                        if s in init_v_hladanom_automate:
                            tmp.append(s + " I")
                        else:
                            tmp.append(s)
                    else:  # je to prechod
                        tmp.append(s)

                hladany_automat2TMP = []
                for h in hladany_automat2:
                    if (h, str) and "," not in str(h):
                        hladany_automat2TMP.append(h.split(" ")[0])

                for s in hladany_automat2:  # pridam veci do noveho automatu
                    if (s, str) and "," not in str(s):  # je to stav, nie prechod
                        s = s.replace(" ", "")
                        s = s.replace("F", "")
                        s = s.replace("I", "")

                        if s in akceptacne_v_automate2:
                            cislo_za_q = int(list(filter(str.isdigit, s))[0])
                            s1 = s.replace(str(cislo_za_q), str(i))
                            hladany_automat2[hladany_automat2TMP.index(s)] = s1
                            tmp_stavy123[s] = s1
                            tmp.append(s1 + " F")
                            i = i + 1
                        else:
                            cislo_za_q = int(list(filter(str.isdigit, s))[0])
                            s1 = s.replace(str(cislo_za_q), str(i))
                            hladany_automat2[hladany_automat2TMP.index(s)] = s1
                            tmp_stavy123[s] = s1
                            tmp.append(s1)
                            i = i + 1
                    else:  # je to prechod
                        tmp_prechod = prechod(tmp_stavy123[s.odkial], tmp_stavy123[s.kam], s.value)
                        tmp.append(tmp_prechod)

                for s in akceptacne_v_automate:  # zo vsetkych finalnych stavov prveho automatu spravim prechod na 'ε' do init stavu druheho automatu
                    prechody.append(prechod(s, tmp_stavy123[init_v_hladanom_automate2[0]], 'ε'))
                    tmp.append(prechod(s, tmp_stavy123[init_v_hladanom_automate2[0]], 'ε'))

                automaty[str(na_ktorom_som_riadku)] = tmp

                tmp = []
                akceptacne_v_automate = []
                akceptacne_v_automate2 = []
                init_v_hladanom_automate = []
                init_v_hladanom_automate2 = []
                tmp_stavy123.clear()

            if prvy_symbol_v_riadku == 'U':
                # check ci existuje riadok
                riadok = line.split(',')
                if int(riadok[1]) > len(subor.keys()):
                    print("CHYBA - Referencia na riadok, ktory neexistuje.")
                    exit()

                stavy_init.append('q' + str(i))  # vytvorim novy pociatocny stav
                stavy.append('q' + str(i))  # a je to aj stav ako taky

                tmp.append('q' + str(i) + " I")

                i = i + 1  # zvysenie i kvoli nazvom stavov

                hladany_automat = automaty.get(riadok[1]).copy()  # najdem prvy automat
                hladany_automat2 = automaty.get(riadok[2]).copy()  # najdem druhy automat

                for a in hladany_automat:  # najdem v prvom pociatocny stav
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'I' in b:
                            c = b.replace("I", "")
                            c = c.replace("F", "")
                            init_v_hladanom_automate.append(c)

                for a in hladany_automat2:  # najdem v druhom pociatocny stav
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'I' in b:
                            c = b.replace("I", "")
                            c = c.replace("F", "")
                            init_v_hladanom_automate2.append(c)

                for a in hladany_automat:  # najdem v prvom akceptacne stavy
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'F' in b:
                            c = b.replace("F", "")
                            c = c.replace("I", "")
                            akceptacne_v_automate.append(c)
                akceptacne_v_automate = set(akceptacne_v_automate)

                for a in hladany_automat2:  # najdem v druhom akceptacne stavy
                    if (a, str) and "," not in str(a):
                        b = a.replace(" ", "")
                        if 'F' in b:
                            c = b.replace("F", "")
                            c = c.replace("I", "")
                            akceptacne_v_automate2.append(c)
                akceptacne_v_automate2 = set(akceptacne_v_automate2)

                for s in hladany_automat:  # pridam veci do noveho automatu
                    if (s, str) and "," not in str(s):  # je to stav, nie prechod
                        s = s.replace(" ", "")
                        s = s.replace("F", "")
                        s = s.replace("I", "")

                        if s in akceptacne_v_automate:
                            tmp.append(s + " F")
                        else:
                            tmp.append(s)
                    else:  # je to prechod
                        tmp.append(s)

                for s in hladany_automat2:  # pridam veci do noveho automatu
                    if (s, str) and "," not in str(s):  # je to stav, nie prechod
                        s = s.replace(" ", "")
                        s = s.replace("F", "")
                        s = s.replace("I", "")

                        if s in akceptacne_v_automate2:
                            tmp.append(s + " F")
                        else:
                            tmp.append(s)
                    else:  # je to prechod
                        tmp.append(s)

                prechody.append(prechod(stavy_init[len(stavy_init) - 1], init_v_hladanom_automate[0], 'ε'))
                prechody.append(prechod(stavy_init[len(stavy_init) - 1], init_v_hladanom_automate2[0], 'ε'))
                tmp.append(prechod(stavy_init[len(stavy_init) - 1], init_v_hladanom_automate[0], 'ε'))
                tmp.append(prechod(stavy_init[len(stavy_init) - 1], init_v_hladanom_automate2[0], 'ε'))

                automaty[str(na_ktorom_som_riadku)] = tmp

                tmp = []
                akceptacne_v_automate = []
                akceptacne_v_automate2 = []
                init_v_hladanom_automate = []
                init_v_hladanom_automate2 = []

            line = fp.readline()
            line = line.strip('\n')
            if line != '':
                prvy_symbol_v_riadku = line[0]
            else:
                prvy_symbol_v_riadku = 'X'
            na_ktorom_som_riadku = na_ktorom_som_riadku + 1



    #zapis NKA
    pocet_stavov_v_NKA = 0
    pocet_symbolov_v_NKA = []
    sym = []
    for p in automaty[str(len(automaty.keys()))]:
        if (p, str) and "," not in str(p):
            pocet_stavov_v_NKA = pocet_stavov_v_NKA + 1
        else:
            pocet_symbolov_v_NKA.append(p.value)
    pocet_symbolov_v_NKA = set(pocet_symbolov_v_NKA)
    F = open(outputNKA, "w")
    F.write(str(pocet_stavov_v_NKA) + '\n')
    F.write(str(len(pocet_symbolov_v_NKA) - 1) + '\n')
    for p in automaty[str(len(automaty.keys()))]:
        if (p, str) and "," not in str(p):
            F.write(str(p) + '\n')
    for p in automaty[str(len(automaty.keys()))]:
        if (p, str) and "," not in str(p):
            continue
        else:
            sym.append(p.value)
    sym = set(sym)
    sym.remove('ε')
    for sy in sym:
        F.write(sy + '\n')
    for p in automaty[str(len(automaty.keys()))]:
        if (p, str) and "," not in str(p):
            continue
        else:
            if p.value == 'ε':
                F.write(str(p.odkial) + ',,' + str(p.kam) + '\n')
            else:
                F.write(str(p.odkial) + ',' + str(p.value) + ',' + str(p.kam) + '\n')
    F.close()

    #volanie zadania 2, pre DKA a hladanie slova
    os.system('python afj2.py ' + outputNKA + ' ' + outputDKA)
