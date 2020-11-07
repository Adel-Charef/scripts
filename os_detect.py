# System info reminder script

import platform
import sys
import psutil

print("System: ", platform.system())
print("release version: ",platform.release())
print("python version: ",platform.python_version())
print("uname: ",platform.uname())
print("Machine: ",platform.machine())
print("Node: ",platform.node())
print("Processor: ",platform.processor())

print("Built in modules: ", sys.builtin_module_names)
print("Loaded modules: ", sys.modules)
print("Don't Write Bytecode: ", sys.dont_write_bytecode)
print("Python executable: ", sys.executable)
print("Python flags: ", sys.flags)
print("Check Internval: ", sys.getcheckinterval())
#print("dlopen() flags: ", sys.getdlopenflags())  # Does not work in Windows
print("Recursion limit: ", sys.getrecursionlimit())

print("Floating points: ", sys.float_info)
print("Float repr style: ", sys.float_repr_style)
#print("Long integer: ", sys.long_info)  # Not working in Windows
print("Max integer: ", sys.maxsize)
print("Max size: ", sys.maxsize)
print("Max unicode: ", sys.maxunicode)

print("Byte order: ", sys.byteorder)
print("Platform: ", sys.platform)
print("File system encoding: ", sys.getfilesystemencoding())
print("Default encoding: ", sys.getdefaultencoding())
print("C API version: ", sys.api_version)
print("Python version: ", sys.version)  # Human readable
print("Python version info", sys.version_info)  # As a data struct

# CPU
print((psutil.cpu_times()))

for x in range(3):
	print((psutil.cpu_percent(interval=1)))

for x in range(3):
	print((psutil.cpu_percent(interval=1, percpu=True)))

for x in range(3):
	print((psutil.cpu_times_percent(interval=1, percpu=False)))

print((psutil.cpu_count()))

print((psutil.cpu_count(logical=False)))

# DISK
import psutil


print((psutil.disk_partitions()))

print((psutil.disk_usage('/')))

print(psutil.disk_io_counters(perdisk=False))

# MEMORY
# Print total, avail, percent, used, free, active, inactive, buffered, cache
print((psutil.virtual_memory()))
# Print total, used, free, percent, sin, sout
print((psutil.swap_memory()))

# NETWORK

print((psutil.net_io_counters(pernic=True)))
# Prints inet by default
print((psutil.net_connections()))
# different kind values
print((psutil.net_connections(kind='tcp')))
#Kinds:
# inet, inet4, inet6, tcp, tcp4, tcp6, udp, udp4, udp6, unix, all

# PROCESSES
pids = psutil.pids()
print(pids)
for pid in pids:
    try:
        p = psutil.Process(pid)
        print("%d - %s" % (pid, p.name()))
    except Exception:
        pass

# USERS
print((psutil.users()))


print((psutil.boot_time()))
