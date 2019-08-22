f = open("log/0816.log", 'r', encoding='UTF-8')

total = 0

while True:
    line = f.readline()
    if not line: break
    # print(line)
    # if "2019-07-26" in line:
    if "2019-08-15" in line:
        if "Entity/SHM/Node/353041080746073/Device/Status" in line:
            # print(line)
            i = line.split("(")
            # print(i)
            j = i[2].split(" bytes")
            # print(j)
            # print(j[0])
            if int(j[0]) > 50000:
                total = int(j[0]) + total
                print(j[0])

print(total)
# Entity/SHM/Node/353041080746073/Device/Status

f.close()