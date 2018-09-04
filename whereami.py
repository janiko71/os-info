import os
import socket
import sys
import platform

machine = platform.uname()
print()
print('Platform          :', sys.platform)
print('OS version        :', sys.version)
print('Host              :', socket.gethostbyaddr(socket.gethostname()))
print('OS                :', platform.system(), platform.release())
print('Version           :', machine.version)
if (sys.platform == "win32"):
    pass
elif (sys.platform == "linux"):
    print('Version           :', platform.dist())
elif (sys.platform == "darwin"):
    print('Version           :', platform.mac_ver())
elif (sys.platform == "cygwin"):
    print('Version           :', "?")
else:
    print('Version           :', "are you from Mars?")
print()
print('Hostname          :', machine.node)
print('Machine type      :', machine.machine)
print('Processor         :', machine.processor)
print()
print('Python            :', platform.python_version())
print('Python compiler   :', platform.python_compiler())
print('Compiler Build    :', platform.python_build())
print()
print('Architecture      :', platform.architecture())
print('\'/bin/ls\'         :', platform.architecture('/bin/ls'))
print()
if (sys.platform != "win32"):
    print(os.system('cat /proc/cpuinfo'))
    print(os.system('lshw'))
