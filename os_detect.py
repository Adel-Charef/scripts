import platform

def Detect():
    os = platform.system()
    release = platform.release()
    pv = platform.python_version()
    uname = platform.uname()
    machine = platform.machine()
    node = platform.node()
    processor = platform.processor()
    data = {
            'os':os,
            'release': release,
            'python_version':pv,
            'uname':uname,
            'machine':machine,
            'node':node,
            'processor':processor
    }
    return data

print(Detect())

