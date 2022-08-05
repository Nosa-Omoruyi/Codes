import pyqrcode

s = 'https://www.edx.org/'
url = pyqrcode.create(s)

url.png('myedx.png', scale = 8)

import os
os.system('myedx.png')

