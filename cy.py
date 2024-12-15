# import os

# def list_files_and_dirs(path):
#     items = os.listdir(path)
#     print(f"Contents of {path}:")
#     for item in items:
#         print(item)

# path = "E:"  # Current directory
# list_files_and_dirs(path)

# import os

# def sleep_windows():
#     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
#     print("Putting the computer to sleep...")

# sleep_windows()
# import ctypes
# import time

# def turn_off_screen():
#     # Send the command to turn off the monitor
#     ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)  # WM_SYSCOMMAND and SC_MONITORPOWER
#     print("Screen turned off.")
#     time.sleep(5)  # Wait 5 seconds (simulate keeping the screen off)

# turn_off_screen()
# i=0
# while i<10:
#     i=i+1
#     print(i)

for i in range(1,11):
    print(i)
    

