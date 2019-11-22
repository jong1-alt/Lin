import multiprocessing
import time
def worker(num):
    print('worker pass as:', num)
    time.sleep(4)
    print('worger finished as:{}'.format(num))
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    print('jobs',jobs)