import subprocess
import os

for res in os.walk('/usr/share/icons'):
    firefox_icons = [os.path.join(res[0], filename) for filename in res[2] if 'firefox' in filename]
    for icon in firefox_icons: 
        print('converting {}'.format(icon))
        subprocess.call('convert -modulate 100,70,100 {} {}'.format(icon, icon), shell=True)

