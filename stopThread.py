import ctypes
import inspect
import threading
import time



def threadStartFunc(para):
    print("Thread", para)
    print("Current threading number: ", threading.active_count())



anyThread = threading.Thread(target=threadStartFunc, args=("start",))
anyThread.start()


def stopThread(threadObj):
    if threadObj != None:
        SystemExitFlag = SystemExit
        ## The codes below is from others method of website, not from Finn, so that just can be used by ourselves. Don't use it as commercial use.
        tid = ctypes.c_long(threadObj.ident)
        if not inspect.isclass(SystemExitFlag):  ## if 'SystemExit' is not a class, that means an exception is raised. (All raised exceptions are an instance of Baseexception)
            SystemExitFlag = type(SystemExitFlag)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(SystemExitFlag))
        
        if res == 0:
            pass  #raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
        threadObj = None
    
    print("Thread end")

time.sleep(2)

stopThread(anyThread)

print("Current threading number: ", threading.active_count())


    


