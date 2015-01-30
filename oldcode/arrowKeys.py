import sys,tty,termios
from PanTilt import PanTilt

panTilt = PanTilt()

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print "up"
                panTilt.up()
        elif k=='\x1b[B':
                print "stop"
                panTilt.stop()
        elif k=='\x1b[C':
                print "right"
                panTilt.right()
        elif k=='\x1b[D':
                print "left"
                panTilt.left()
        else:
                print "not an arrow key!"
                print "key: ", k
                panTilt.stop()

def main():
        panTilt.stop()
        for i in range(0,20):
                get()
        panTilt.stop()

if __name__=='__main__':
        main()
