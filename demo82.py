class Empolyee(object):
    def __init__(self):
        self.work_content ='work'

    def doWork(self):
        print('working on %s' % self.work_content)
class RD(Empolyee):
    def __init__(self):
        self.work_content ="research*development"

rd1 = RD()
rd1.doWork()

