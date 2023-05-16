print('muhammad iddar rajab\n210511028\nT121A(R1)\n')
import os

try:
    os.mkdir('/mydirectory')
except OSError as e:
    print("Failed to create directory: ", e)