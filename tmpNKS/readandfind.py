import time
def cisloVriadku(TietoHashe):
    fp = open("E://nks/tableB.txt", "r")
    cisla = list()
    for i, line in enumerate(fp):
        line = line.strip()
        for TentoHash in TietoHashe:
            if line == TentoHash:
                cisla.append(i)
    fp.close()
    return cisla

def findandtell(num):
    a = 65
    b = 97
    c = 97
    d = 97
    number = 0
    #num = cisloVriadku(FindThis)
    if num < 0:
        return -1
    while a < 123:
        if a > 90 and a < 97:
            a = a + 1
            continue
        b = 97
        while b < 123:
            c = 97
            while c < 123:
                d = 97
                while d < 123:
                    for i in range(0, 10):
                        if number == num:
                            print(str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str('000' + str(i)))
                            print("MAME")
                            print("MAME")
                            print("MAME")
                            #return str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str('000' + str(i))
                        number = number + 1
                    for i in range(10, 100):
                        #x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)))
                        #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)) + " " + x + "\n")
                        if number == num:
                            print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)))
                            print("MAME")
                            print("MAME")
                            print("MAME")
                            #return str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i))
                        number = number + 1
                    for i in range(100, 1000):
                        #x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
                        #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)) + " " + x + "\n")
                        if number == num:
                            print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
                            print("MAME")
                            print("MAME")
                            print("MAME")
                            #return str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i))
                        number = number + 1
                    #print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
                    for i in range(1000, 10000):
                        #x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i))
                        #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i) + " " + x  + "\n")
                        if number == num:
                            print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i))
                            print("MAME")
                            print("MAME")
                            print("MAME")
                            #return str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i)
                        number = number + 1
                    d = d + 1
                c = c + 1
            b = b + 1
        a = a + 1

if __name__ == "__main__":
#     h = "f40212a63ce990a4:d3b7e7dd60fcbe5f"
    start = time.time()
    filename = "E://nks/nnn/74809.auth"
    with open(filename) as f:
        y = f.readlines()
    y = [x.strip() for x in y]

    bra = cisloVriadku(y)
    print(bra)
    if len(bra) > 0:
        for b in bra:
            print(findandtell(b))
    else:
        print("Hash sa tu nenachadza")
    end = time.time()
    print(str(end - start))
#     print(findandtell(h))