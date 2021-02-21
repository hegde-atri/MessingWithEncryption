password = input("Enter your password: ")
passwordAr = []
secure = []
securePass = []
stage1 = []
stage2 = []
key = 11111111
for i in password:
    passwordAr.append(i)

for i in passwordAr:
    secure.append(ord(i))

print("Made your password into characters, and then into the corresponding int value: " + secure)
for i in secure:
    securePass.append(i ^ key)

print("used XOR gate on each integer: " + securePass)

for i in securePass:
    stage1.append(i ^ key)

print("applied XOR gate on the stored int array: " + stage1)
for i in stage1:
    stage2.append(chr(i))

print("Turned the integers we got into characters: " + stage2)
