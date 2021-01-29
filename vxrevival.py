from gpiozero import LED, Button 
from signal import pause 
from datetime import datetime
import subprocess

rouge = LED(23) 
bouton = Button(24) 
isRecord = False

def record():
    print("OK")
    global isRecord
    global record_process
    isRecord = not isRecord
    now = datetime.now()
    filename = now.strftime("%d_%m_%Y_%H:%M:%S") + ".avi"
    if isRecord:
        record_process = subprocess.Popen(["ffmpeg","-f","v4l2","-thread_queue_size","1024","-input_format","mjpeg","-video_size","720x480",
                                           "-framerate","50","-i","/dev/video0","-f","pulse","-thread_queue_size","1024","-i","default",
                                           "-codec","copy",filename])
        rouge.on()
    else:
        record_process.terminate()
        rouge.off()
       
       
print ("Start recording with VXRevival") 
bouton.when_pressed = record
pause()
