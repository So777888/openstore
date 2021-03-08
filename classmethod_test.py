# def iget_no_of_instance(ins_obj):
#     return ins_obj.__class__.no_inst
# class Kls(object):
#     no_inst = 0
#     def __init__(self):
#         Kls.no_inst = Kls.no_inst + 1
#
# ik1 = Kls()
# ik2 = Kls()
# print(iget_no_of_instance(ik1))

IND = 'ON'
def checkind():
    return (IND == 'ON')
class Kls(object):
    def __init__(self,data):
        self.data = data

    def do_reset(self):
        if checkind():
            print('Reset done for:', self.data)
    def set_db(self):
        if checkind():
            self.db = 'new db connection'
            print('DB connection made for:',self.data)
ik1 = Kls(12)
ik1.do_reset()
ik1.set_db()