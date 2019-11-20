n =200
summation = 0
counter = 1
while counter <= n:
    summation += counter
    counter += 1
    # if summation > 10000:
    #     break
else:
    print('calcute finished')
print('counter=%d,summation=%d' % (counter, summation))

