


fr = open('sample.txt' , mode= 'r' , encoding='utf-8')
fw = open('output.txt' , mode= 'r' , encoding='utf-8')

while True:
    line = fr.readline()
    if not line : break

    print('내용', line.replace('\n' , ''))
    fw.write(line)

fr.close()
fw.close()



