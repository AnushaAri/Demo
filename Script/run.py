"""check call"""
import subprocess as sb
import threading

def timeout():
    """Timeout function"""
    print 'timeout'
    #exit(3)

sb.check_call("g++ demo.cpp", shell=True)
T = threading.Timer(10, timeout)
PROC = sb.Popen("./a.out", shell=True, stdin=sb.PIPE, stdout=sb.PIPE, stderr=sb.PIPE)
#out, err = proc.communicate('hello\n')
#t.cancel()
#assert proc.returncode == 0
#assert out == 'hello\n'
#assert err == ''
#sb.check_call("hello", shell=True)


