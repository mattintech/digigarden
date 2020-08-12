import socket
import os
import subprocess

hostname=socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

def getFreeSpaceInMb():
    st = os.statvfs('/')
    #return st.f_bavail * st.f_frsize / 1000 / 1000 ##Return macOS way...
    result = round((st.f_bavail * st.f_frsize / 1024 / 1024 ))
    return result

def getPiTemp():
    try:
        resultFromSubprocess = subprocess.run(['/opt/vc/bin/vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
        cleanResult = resultFromSubprocess.stip("temp='C")
        return cleanResult
    except:
        #this won't exist if testing outside of a PI
        fakeTemp="temp=45.5'C"
        x = fakeTemp.strip("temp='C")
        print(x)
        return x
