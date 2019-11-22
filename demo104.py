import multiprocessing, time

def daemon():
    pName = multiprocessing.current_process().name
    print('[%s]Demon:start to ' % pName)
    time.sleep(5)
    print('[%s]Dom : stop ' % pName)

def nonDaemon():
    pName = multiprocessing.current_process().name
    print('[%s]normal:start to ' % pName)
    time.sleep(5)
    print('[%s]normal : stop ' % pName)

if __name__ == '__main__':
    d1 = multiprocessing.Process(name='daemon',
                                 target=daemon)
    d1.daemon=True
    d2 = multiprocessing.Process(name='nonDaemon',
                                 target=nonDaemon)
    d2.daemon=False
    d1.start()
    # time.sleep(1)
    d2.start()
    time.sleep(5)
    d1.join()

