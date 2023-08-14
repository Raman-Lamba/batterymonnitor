import subprocess
import time

def show_notification(message, timeout):
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Battery Alert" sound name "Submarine"'])
    time.sleep(timeout)
# Rest of the code remains the same
def get_battery_level():
    result = subprocess.run(['pmset', '-g', 'batt'], stdout=subprocess.PIPE, text=True)
    output = result.stdout
    for line in output.split('\n'):
        if 'InternalBattery' in line:
            parts = line.split('\t')
            for part in parts:
                if '%' in part:
                    return int(part.split('%')[0])
    return None

while True:
    battery_level = get_battery_level()
    if battery_level is not None and battery_level >= 80:
        print("Battery level is at 80% or above. Warning!")
        show_notification("Battery level is at 80% or above. Please unplug the charger.",300)
    time.sleep(300)  # Check every 5 minutes

