from pygame import mixer
from datetime import datetime
from time import time

def muo(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("water.txt","a") as w:
        w.write(f"{msg} {datetime.now()}\n")
        print("\n")
if __name__ == '__main__':
    #muo("ex.mp3","stop")
        init_wat = time()
        init_eye = time()
        init_ex = time()
        w=5
        e=10
        ex=20
        while True:
            if time()-init_wat > w:
                print("Time to drink water...type drank after drinking water")
                muo("water.mp3", "drank")
                init_wat = time()
                log_now("Water drank at ")

            if time()-init_eye > e:
                print("Time to do eye exersice...type done after doing exersice..")
                muo("eye.mp3", "done")
                init_eye = time()
                log_now("eye exersice done at ")

            if time()-init_ex > ex:
                print("Time to do exersice...type done after doing exersice..")
                muo("ex.mp3", "done")
                init_ex = time()
                log_now("Physical exersice done at ")