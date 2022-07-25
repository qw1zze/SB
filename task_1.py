mask = ' 0123456789'
for i in mask:
    for j in mask:
        ch = '6' + str(i) + '6' + str(j) + '6'
        ch = int(ch.replace(' ', ''))
        if ch % 666 == 0:
            print(ch, ch // 666)
