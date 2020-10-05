import logging
import importsample

logging.basicConfig(format='%(asctime)s:>>>>%(message)s',level=logging.DEBUG ,filename='log-test.log',filemode='a')
name ='               ..... gkavehmollaei  '
print(name)
print('tell me more',name.strip('. g'))



logging.error('dsga')


print(importsample.calculte_circle(5))
'''
def m_func():

    def mib():
        print('this is for test')
    return mib


m_func()()    

def father(son_name):
    def son1():
        print('I am '+ son_name )
    def son2():
        print('I am '+ son_name)
    if son_name==son1.__name__:
        return son1()

    elif son_name==son2.__name__:
        return son2()
    else:

        return False
print(father('son2'))        

           
    '''