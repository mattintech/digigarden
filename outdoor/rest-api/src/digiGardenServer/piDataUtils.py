import socket
import os

hostname=socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

def getFreeSpaceInMb():
    st = os.statvfs('/')
    #return st.f_bavail * st.f_frsize / 1000 / 1000 ##Return macOS way...
    result = round((st.f_bavail * st.f_frsize / 1024 / 1024 ))
    return result
