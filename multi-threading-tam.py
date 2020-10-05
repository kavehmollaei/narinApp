from time import sleep,perf_counter
from threading import Thread


start = perf_counter()
def show(name):
    print('starting...{}'.format(name))
    sleep(3)
    print('Finishing...{}'.format(name))




t1 = Thread(target=show,args=('one',))
t2 = Thread(target=show,args=('two',))
t1.start()
t2.start()
# show('one')
# show('two')    
t1.join()
t2.join()
end = perf_counter()


print(round(end-start))