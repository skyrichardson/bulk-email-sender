with open('2023-11-12_13_bootcamp.csv', 'r') as t1, open('2023_11_26_13_bootcamp.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)