# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
# import multiprocessing as mp
# import time
#
#
# def get_auth1(msk, pwd):
#     hash = SHA256.new()
#     hash.update(msk)
#     hash.update(pwd)
#     dgst = hash.digest()
#
#     salt = dgst[0:8].encode('hex')
#
#     hash = SHA256.new()
#     hash.update(salt)
#     hash.update(pwd)
#     dgst = hash.digest()
#
#     return salt + ':' + dgst[0:8].encode('hex')
#
# def func(y,a):
#     msk2 = '74809'
#     #a = 65
#     b = 97
#     c = 97
#     d = 97
#     #f = open("C://Program Files (x86)/tmp/table.txt","w")
#     #f = open("E://nks/table1.txt","w")
#     #while a < 123:
#     for oops in range(0,3):
#         if a > 90 and a < 96:
#             a = a + 1
#             continue
#         b = 97
#         while b < 123:
#             c = 97
#             while c < 123:
#                 d = 97
#                 while d < 123:
#                     for i in range(0, 10):
#                         x = get_auth1(msk2, str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str('000' + str(i)))
#                         #f.write(str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str('000' + str(i)) + " " + x + "\n")
#                         #f.write(x + "\n")
#                         for hh in y:
#                             if hh == x:
#                                 print(str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str('000' + str(i)))
#                                 print("MAME")
#                                 print("MAME")
#                                 print("MAME")
#                                 #return str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str('000' + str(i))
#                     for i in range(10, 100):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)) + " " + x + "\n")
#                         #f.write(x + "\n")
#                         for hh in y:
#                             if hh == x:
#                                 print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)))
#                                 print("MAME")
#                                 print("MAME")
#                                 print("MAME")
#                                 #return str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i))
#                     for i in range(100, 1000):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)) + " " + x + "\n")
#                         #f.write(x + "\n")
#                         for hh in y:
#                             if hh == x:
#                                 print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                                 print("MAME")
#                                 print("MAME")
#                                 print("MAME")
#                                 #return str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i))
#                     #print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                     for i in range(1000, 10000):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i) + " " + x  + "\n")
#                         #f.write(str(x) + "\n")
#                         for hh in y:
#                             if hh == x:
#                                 print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i))
#                                 print("MAME")
#                                 print("MAME")
#                                 print("MAME")
#                                 #return str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i)
#                     d = d + 1
#                 c = c + 1
#             b = b + 1
#         a = a + 1
#
#
# def f():
#     start = time.time()
#     filename = ""
#     with open(filename) as f:
#         y = f.readlines()
#     y = [x.strip() for x in y]
#
#     processes = list()
#     processes.append(mp.Process(target=func,args=(y,65)))
#     processes.append(mp.Process(target=func, args=(y, 69)))
#     processes.append(mp.Process(target=func, args=(y, 73)))
#     processes.append(mp.Process(target=func, args=(y, 77)))
#     processes.append(mp.Process(target=func, args=(y, 81)))
#     processes.append(mp.Process(target=func, args=(y, 85)))
#     processes.append(mp.Process(target=func, args=(y, 97)))
#     processes.append(mp.Process(target=func, args=(y, 101)))
#     processes.append(mp.Process(target=func, args=(y, 105)))
#     processes.append(mp.Process(target=func, args=(y, 109)))
#     processes.append(mp.Process(target=func, args=(y, 113)))
#     processes.append(mp.Process(target=func, args=(y, 117)))
#     processes.append(mp.Process(target=func, args=(y, 121)))
#     processes.append(mp.Process(target=func, args=(y, 125)))
#
#     for process in processes:
#         process.start()
#     for process in processes:
#         process.join()
#
#     end = time.time()
#     print(str(end - start))
#
#     #func(y,65)
#
# if __name__ == "__main__":
#
#     f()