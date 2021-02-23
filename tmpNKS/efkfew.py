# fp = open("E://nks/table1.txt", "r")
# import time
# start = time.time()
# # for i, line in enumerate(fp):
# #     continue
# with open("E://nks/table1.txt", 'r') as f:
#     lines = f.read().splitlines()
#     last_line = lines[-1]
#     print last_line
# end = time.time()
# print(end - start)
# fp.close()
# #print(i)
# #print(line)
############################################################
# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
#
# # test parameters
# msk = '74809'
# pwd = 'AAzW1236'
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
# print(get_auth(msk, pwd))