import os, platform, subprocess
from subprocess import call
import subprocess

from subprocess import CalledProcessError

# call('ls -l')
# print(subprocess.call(['ls','-l']))

# command='ls -la'``
ls_output=subprocess.check_output(['lscpu']).strip().decode()
# print(ls_output)
# print(type(ls_output))


# lscpu = subprocess.check_output(['lscpu'])
# print(lscpu.decode("utf-8"))
# l = lscpu.decode()
# print(l.split('\n'))
# ls_out = ls_output.split("\n")
# print(ls_output)

# test=subprocess.Popen('ls',stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(test.stdout.read().decode('utf-8'))
# print('kaveh')


# pro=subprocess.Popen('top',stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
# stdout,stderr=pro.communicate()
# print(stderr)


ping_commnad=subprocess.run(['ls', '-la'],stdout=subprocess.PIPE)


# print(ping_commnad.stdout.decode('utf-8'))

# if ping_commnad.returncode == 0:
    # print('oh lalal')

# if ping_commnad.returncode==0:
'''
with open ('output.txt','w') as f:
    s=subprocess.run(['ping -c4 192.168.50.1'],shell=True,stdout=f,stderr=subprocess.DEVNULL)
    
    
    if s.returncode !=0:
        print('host is Unreachable')
    else:
        print('pinging...')    
    
        
'''        
        
        # if s.returncode==0:
            # print('Connection is ok')
        # print(s.stdout)
        # else:         # print('not connected')


host = '192.168.4.48'
with open ('output.txt','w') as f:
    try:
        s=subprocess.run(['ping -c2 {}'.format(host)],shell=True,stderr=subprocess.DEVNULL,stdout=f)
        if s.returncode !=0:
            print('host is Unreachable')
        else:
            print('pinging...') 
        
        # print(s.stdout.decode('utf-8'))
    except CalledProcessError as err:
        print('not connected...',err)
        f.write(str(err))
        
    
# comm=subprocess.call(['ls'], shell=True)                    
# print(comm)
'''
subprocess.Popen(['ping', '-c3', '192.168.50.1'],stdout=subprocess.DEVNULL)

textList=['ka','mo']
outF = open("myOutFile.txt", "w")
outF.writelines(("\nSee you soon!", "\nOver and out."))
# outF.write(["See you soon!", "Over and out."])
# outF.close()
'''