import os
import time

def notify_with_sound(message, title="Reminder"):
    os.system(f'''osascript -e 'display notification "{message}" with title "{title}"' ''')
    os.system(f'say -v Samantha "Time to Drink Water"')

while True:
    notify_with_sound("Time to drink water!", "Reminder")
    time.sleep(3600) #1 Hour
