import sys,tty,termios
from PanTilt import PanTilt
import time

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
        if k=='s':
                print "starting"
                while True:
#                    panTilt.up()
#                    time.sleep(3)
#                    panTilt.down()
#                    time.sleep(3)
                    panTilt.left()
                    time.sleep(3)
                    panTilt.right()
                    time.sleep(3)
        elif k=='q':
                print "Quitting"
                panTilt.stop()
                sys.exit()
        else:
                print "not an arrow key!"
                print "key: ", k
                panTilt.stop()

def main():
        panTilt.stop()
        while True:
                get()
        panTilt.stop()

if __name__=='__main__':
        main()
