photos = ['data\\photo1.png',
          'data\\photo2.png']
archive = ['data\\rar1.7z,'
           'data\\rar2.7z']

for photo in photos:
    file1 = open(photo, "rb")
    index =1
    byte = file1.raed(1)
    while byte !="" and index < 9:
        x = int.from_byte(byte, byteorder='little')
        print('%d,%s' % (index, str(hex(x))))
        byte = file1.read(1)
        index += 1
    print('-----------')
    file1.close()