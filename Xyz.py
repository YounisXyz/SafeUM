"""
    @ code by ---( Younis john )---
    @ Github : https://github.com/YounisXyz
    @ WhatsApp : https://wa.me/923194999455
    
"""
import os, sys, platform
 
os.system('rm -rf Safeum.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Safeum.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Safeum.so'):
        os.system('curl -L https://github.com/YounisXyz/executables/blob/main/Safeum.cpython-312.so?raw=true -o Safeum.so') 
        import Safeum
    else:
        import Safeum
