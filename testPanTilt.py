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
        if k=='w':
                print "up"
                panTilt.up()
        elif k=='s':
                print "stop"
                panTilt.down()
        elif k=='d':
                print "right"
                panTilt.right()
        elif k=='a':
                print "left"
                panTilt.left()
        elif k==' ':
                print "stop"
                panTilt.stop()
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
