import socket
import os
import subprocess
import datetime
import time
import psutil

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
        cleanFakeTemp = fakeTemp.strip("temp='C")
        return cleanFakeTemp

def getTotalMemoryInMB():
    mem = psutil.virtual_memory()
    return mem.total / 1024 / 1024

def getTotalFreeMemoryInMB():
    mem = psutil.virtual_memory()
    return round(mem.available / 1024 / 1024)

def getTotalCpuUsage():
    cpu = psutil.cpu_percent()
    return cpu

def getRunningProcesses():
    listOfProcessNames = list()
    for proc in psutil.process_iter():
        try:
            processInfoDict = proc.as_dict(attrs=['name', 'cpu_percent', 'pid'])
            processInfoDict['vms'] = proc.memory_info().vms / (1024 * 1024)
            listOfProcessNames.append(processInfoDict)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listOfProcessNames

def getSystemBootTime():
    boottime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return boottime

def uptimeInSeconds():
    return time.time() - psutil.boot_time()
