fname = input("Enter file name: ")

tekst = open(fname)
count = 0
for linija in tekst:
    if linija.startswith("From "):
        rijeci = linija.rstrip().split()
        email = rijeci[1]
        print(email)
        count +=1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")