# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
# import platform
# import time
#
# print("Python version running - " + platform.python_version())
# # test parameters
# msk = '12345'
# pwd = 'nbusr123'
# tester = ['4adea370c6c01561:b440fbee64f916eb', '763c5db11b7c2d48:896ac182a102a8c5', '93c7d5c26d1f889c:5be63957228e1ff5', 'eff65e33a1c20298:e9060d8144670d0b', 'aecbd2088e5bf5d4:ff4fe8a8d049ec86', '39a3ee207836e21a:3242ec5389839dc6', '8ba7b95233e320b3:6f8f8dddd27c703c', '6aedf928fbc1b9fb:62129b494179243e', 'aefdb1f7fef70898:cf8f3ab71f8843af', 'cea096547303a689:632667001970ae8a']
#
# msk1 = '0'
# msk2 = '74809'
#
#
# def get_auth(msk, pwd):
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
# def func(y):
#     a = 65
#     b = 97
#     c = 97
#     d = 97
#     #f = open("C://Program Files (x86)/tmp/table.txt","w")
#     #f = open("E://nks/table1.txt","w")
#     while a < 123:
#         if a > 90 and a < 97:
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
#                         if y == x:
#                             print(str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str('000' + str(i)))
#                             print("MAME")
#                             print("MAME")
#                             print("MAME")
#                             return 1
#                     for i in range(10, 100):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)) + " " + x + "\n")
#                         #f.write(x + "\n")
#                         if y == x:
#                             print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)))
#                             print("MAME")
#                             print("MAME")
#                             print("MAME")
#                             return 1
#                     for i in range(100, 1000):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)) + " " + x + "\n")
#                         #f.write(x + "\n")
#                         if y == x:
#                             print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                             print("MAME")
#                             print("MAME")
#                             print("MAME")
#                             return 1
#                     #print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                     for i in range(1000, 10000):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i) + " " + x  + "\n")
#                         #f.write(str(x) + "\n")
#                         if y == x:
#                             print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i))
#                             print("MAME")
#                             print("MAME")
#                             print("MAME")
#                             return 1
#                     d = d + 1
#                 c = c + 1
#             b = b + 1
#         a = a + 1
#
# def generate_tables():
#     a = 67
#     b = 97
#     c = 97
#     d = 97
#     #f = open("C://Program Files (x86)/tmp/table.txt","w")
#     f = open("E://nks/tableC.txt","w") ## NEZABUDNUT PREPISAT OR ELSE IM FCKD
#     while a < 123:
#         if a > 90 and a < 97:
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
#                         f.write(x + "\n")
#                     for i in range(10, 100):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('00' + str(i)) + " " + x + "\n")
#                         f.write(x + "\n")
#                     for i in range(100, 1000):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)) + " " + x + "\n")
#                         f.write(x + "\n")
#                     #print(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str('0' + str(i)))
#                     for i in range(1000, 10000):
#                         x = get_auth1(msk2, str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i))
#                         #f.write(str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d)) + str(i) + " " + x  + "\n")
#                         f.write(x + "\n")
#                     d = d + 1
#                 c = c + 1
#             b = b + 1
#         f.close()
#         return 1
#         a = a + 1
#     f.close()
#
# if __name__ == "__main__":
#     #print(get_auth('74809','AAzW1236'))
#     #y = get_auth('74809','AAzW1236')
#
#     print("Starting generating")
#     start = time.time()
#     #func(y)
#     generate_tables()
#     end = time.time()
#     print("Files generated")
#     print("Proces trval " + str((end - start)/60) + " minut.")
#
#
#     #65-90 97-122
#
#
#     # print(" ")
#     # print(" ")
#     # print(" ")
#     #
#     # for i in range(0,10):
#     #     x = get_auth1(msk1,str('000'+str(i)))
#     #     for y in tester:
#     #         if y == x:
#     #             print(str('000'+str(i)))
#     # for i in range(10,100):
#     #     x = get_auth1(msk1, str('00' + str(i)))
#     #     for y in tester:
#     #         if y == x:
#     #             print(str('00'+str(i)))
#     # for i in range(100, 1000):
#     #     x = get_auth1(msk1, str('0' + str(i)))
#     #     for y in tester:
#     #         if y == x:
#     #             print(str('0'+str(i)))
#     # for i in range(1000, 10000):
#     #     x = get_auth1(msk1, str(str(i)))
#     #     for y in tester:
#     #         if y == x:
#     #             print(str(str(i)))
#
# #print(get_auth(msk, pwd))
#
# # odpoved by mala byt: 864f64d8bc939741:82be34b8fd001c71