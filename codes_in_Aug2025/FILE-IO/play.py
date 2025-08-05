import time
import vlc
x = (input("Type \'play\' for a surprise.\n"))
y = x.lower()

if y == "play":
    k = vlc.MediaPlayer("tab.mp4")
    k.play()
    time.sleep(6)

