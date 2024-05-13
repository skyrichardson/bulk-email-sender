with open('2023_12_04_13_bootcamp.csv', 'r') as t1, open('2023_12_05_13_bootcamp.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)