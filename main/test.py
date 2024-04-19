import time
from pywinauto.application import Application

app = Application(backend="win32").connect(process=18880, timeout=10)
# form = app.window(title_re="Form1")
# form.SetFocus()
# form = app.window(title_re="windowtitle")
# print('start')
# form.send_keystrokes('a')

