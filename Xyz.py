"""
    @ code by ---( Younis john )---
    @ Github : https://github.com/YounisXyz
    @ WhatsApp : https://wa.me/923494445455
    
"""
import os, sys, platform
 
os.system('rm -rf SafeUm.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf SafeUM.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('SafeUM.so'):
        os.system('curl -L https://github.com/YounisXyz/executables/blob/main/SafeUM.cpython-312.so?raw=true -o SafeUM.so') 
        import SafeUM
    else:
        import SafeUM
