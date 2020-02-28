'''
  Diogo Costa
  28/02/2020

  Description:
    Create a program to wake up your colleagues
    In each 5 minutes launch a video.
'''
import time
import webbrowser

currentTime = time.time()
while True:
    webbrowser.open_new('https://www.youtube.com/watch?v=IOCiyimPLq8')
    time.sleep(30.0 - ((time.time() - currentTime) % 30.0))
