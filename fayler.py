##Ex_149
# def tox5 (name):
#     try:
#         with open (name, "r") as file:
#             result = file.readlines()
#         result = "".join(result[:10])
#         return result
#     except FileNotFoundError:
#         return "Sxal fayli anun"

# a = input("fayli anun: ")
# print(tox5(a))


## Ex_150
# def tox5 (name):
#     try:
#         with open (name, "r") as file:
#             result = file.readlines()
#         result = "".join(result[-10:])
#         return result
#     except FileNotFoundError:
#         return "Sxal fayli anun"

# a = input("fayli anun: ")
# print(tox5(a))


##Ex_151
# def miacum(names):
#     n = int()
#     for i in range(len(names)):
#         try:
#             with open (names[i], "r") as file:
#                 n = i
#                 break
#         except FileNotFoundError:
#             print(f"{names[i]} anunov fayl chi gtnvel:")
#     else:
#         return
    
#     for i in range(n + 1, len(names)):
#         try:
#             with open (names[i], "r") as file:
#                 result = file.read()
#             with open (names[n], "a") as file1:
#                 file1.write(result)
#         except FileNotFoundError:
#             print(f"{names[i]} anunov fayl chi gtnvel:")
        

# mylist = []
# while True:
#     a = input("enter file name(Enter to finish): ")
#     if a == "":
#         break
#     else:
#         mylist.append(a)
# miacum(mylist)


##Ex_152
# def hamarakalum(name):
#     try:
#         with open (name, "r") as file:
#             result = file.readlines()
#         for i in range(len(result)):
#             result[i] = str(i) + ": " + result[i]
#         with open ("hamarakalum.txt", "w") as file1:
#             file1.write("".join(result))

#     except FileNotFoundError:
#         return "Sxal fayli anun"

# a = input("fayli anun: ")
# print(hamarakalum(a))


## Ex_153
# with open ("text.txt", "r") as file:
#     result = file.read()
# result = result.replace("\n", "")
# result = result.split(" ")
# result.sort(key = len)
# max_len = len(result[-1])
# print(f"max len: {max_len}")
# for i in range(len(result) - 1, -1, -1):
#     if len(result[i]) == max_len:
#         print(result[i])
#     else:
#         break


##Ex_154
# def qanak(name):
#     try:
#         mdi = {}
#         with open (name, "r") as file:
#             result = file.read().lower()
#         for i in result:
#             if i.isalpha():
#                 if i in mdi:
#                     mdi[i] += 1
#                 else:
#                     mdi[i] = 1
#         return mdi
#     except FileNotFoundError:
#         return "Sxal fayli anun"
    
# a = input("enter file name: ")
# print(qanak(a))


##Ex_155
# def qanak(name):
#     try:
#         mdi = {}
#         with open (name, "r") as file:
#             result = file.read().lower()
#         result = result.split(" ")
#         for i in result:
#             s = ""
#             for j in i:
#                 if j.isalpha():
#                     s += j
#             if s in mdi:
#                 mdi[s] += 1
#             else:
#                 mdi[s] = 1
#             s = ""
#         s = ""
#         maax = max(mdi.values())
#         for i in mdi:
#             if mdi[i] == maax:
#                 s += i + "  "
#         return s
#     except FileNotFoundError:
#         return "Sxal fayli anun"
    
# a = input("enter file name: ")
# print(qanak(a))


##Ex_156
# suum = int()
# while True:
#     a = input("Enter number(Enter for finish): ")
#     if a == "":
#         print(f"sum: {suum}")
#         break
#     try:
#         a = int(a)
#         suum += a
#         print(f"sum: {suum}")
#     except ValueError:
#         print("Enter NUMBER")


##Ex_157
# mdi = {
#     "A+": 5.0, "C+": 2.3,
#     "A": 4.0, "C": 2.0,
#     "A-": 3.7, "C-": 1.7,
#     "B+": 3.3, "D+": 1.3,
#     "B": 3.0, "D": 1.0,
#     "B-": 2.7, "F": 0,
# }
# gnahatakan = input("gnahatakan: ")
# try:
#     print(mdi[gnahatakan.upper()])
# except KeyError:
#     try:
#         gnahatakan = float(gnahatakan)
#         for i in mdi:
#             if mdi[i] == gnahatakan:
#                 print(i)
#                 break
#         else:
#             print("Sxal mutq")
#     except ValueError:
#         print("Sxal mutq")


##Ex_158
# def koment(name):
#     try:
#         with open (name, "r") as file:
#             rezult = file.readlines()
#         for i in range(len(rezult) - 1, -1, -1):
#             if rezult[i][0] == "#":
#                 del rezult[i]
#         return "".join(rezult)
#     except FileNotFoundError:
#         return "Sxal fayli anun"
        
# a = input("fayli anun: ")
# if koment(a) == "Sxal fayli anun":
#     print(koment(a))
# else:
#     b = input("nor stexcvox fayli anun: ")
#     with open (b, "w") as file:
#         file.write(koment(a))


##Ex_159
# import random

# with open("text.txt", "r") as file:
#     rezult = file.read().split("\n")

# parol = ""
# while len(parol) < 7 or len(parol) > 11:
#     parol = ""
#     while True:
#         bar1 = random.randint(0, len(rezult) - 1)
#         if len(rezult[bar1]) > 3:
#             parol += rezult[bar1].capitalize()
#             break
#     while True:
#         bar2 = random.randint(0, len(rezult) - 1)
#         if len(rezult[bar2]) > 3:
#             parol += rezult[bar2].capitalize()
#             break
# print(parol)


##Ex_160
# with open("text.txt", "r") as file:
#     rezult = file.read().split("\n")
# norm = []
# bacar = []
# for i in rezult:
#     if "cei" in i:
#         norm.append(i)
#     elif "ie" in i:
#         norm.append(i)
#     elif "ei" in i:
#         bacar.append(i)
# print(norm)
# print(bacar)


##Ex_162
# with open("text.txt", "r") as file:
#     rezult = file.read().replace("\n", " ").split(" ")

# mdi = {}
# count = 0
# alph = "abcdefghijklmnopqrstuvwxyz"
# for i in alph:
#     for j in rezult:
#         if i in j:
#             if i in mdi:
#                 mdi[i] += 1
#             else:
#                 mdi[i] = 1
# for i in mdi:
#     mdi[i] = round(mdi[i] / len(rezult), 2) 
# print(f"{mdi}\namenaqich handipox tary: {sorted(mdi, key=mdi.get)[1]}")


##Ex_163-166 chem grum


##Ex_167
# with open("text2.txt", "r") as file1:
#     rez1 = file1.read().replace("\n", " ").lower().split(" ")
# with open("text.txt", "r") as file2:
#     rez2 = file2.read().replace("\n", " ").lower().split(" ")
# mdi = {}
# for i in rez1:
#     mdi[i] = 0
# for i in rez2:
#     if i in mdi:
#         print(i, end="   ")



##Ex_168
# with open("text.txt", "r") as file:
#     rez = file.read().replace("\n", " ").lower().split(" ")
# for i in range(len(rez) - 1):
#     if rez[i] == rez[i + 1]:
#         print(rez[i + 1])


##Ex_169
# with open("text2.txt", "r") as sluj_file:
#     slujebnie = sluj_file.read().replace("\n", " ").lower().split(" ")
# with open("text.txt", "r") as file:
#     rezult = file.read().replace("\n", "\n ").lower().split(" ")
# new_text = ""
# for i in rezult:
#     for j in slujebnie:
#         if j in i:
#             new_text += i.replace(j, "*" * len(j)) + " "
#             break
#     else:
#         new_text += i + " "
# with open("text.txt", "w") as file:
#     file.write(new_text)
        

##Ex_171
# with open("text2.txt", "r") as file:
#     rezult = file.read().replace("\n", " ").split(" ") 
# leen = 0
# for i in range(len(rezult) - 1):
#     leen += len(rezult[i]) + 1
#     if leen + len(rezult[i + 1]) > 48:
#         # rezult.insert(i + 1, "\n")
#         rezult[i] += "\n"
#         leen = 0
# print(" ".join(rezult))

##Ex_171

