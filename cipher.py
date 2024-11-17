# add your code here
alphabet = "abcdefghijklmnopqrstuvwxyz"
partone=""
parttwo=""
newalphabet=""
message = input("Please enter your message: ").lower()
key = int(input("Please enter the key: "))

if key == 0:
    newalphabet = alphabet
elif key > 0:
    partone = alphabet[:key]
    parttwo = alphabet[key:]
    newalphabet = parttwo + partone
else:
    partone = alphabet[:(26 + key)]
    parttwo = alphabet[(26 + key):]
    newalphabet = parttwo + partone
encrypted=""
for message_index in range(0,len(message)):
    if message[message_index] == " ":
        encrypted+= " "
    for alphabet_index in range(0,len(newalphabet)):
        if message[message_index] == alphabet[alphabet_index]:
            encrypted+= newalphabet[alphabet_index]

print(encrypted)