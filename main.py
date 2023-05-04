
import checkFunction
import psutil
import time

# Main loop
while True:
    # Iterate over all running processes
    for process in checkFunction.get_running_processes():
        try:
            # Iterate over all files opened by the process
            for file in process.open_files():
                # Check if the file has an extension commonly associated with ransomware
                if checkFunction.is_ransomware(file.path) and checkFunction.has_changed(file.path):
                    print(
                        f"\033[1;31mPotential ransomware activity detected: {file.path}\033[0m")
                    # print("\033[1;31mPotential ransomware activity detected: {file.path}\033[0m")
                else:
                    print(
                        f"\033[1;32mAll is well with: {file.path}\033[0m")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignore any processes that we can't access
            pass

    # Wait for 60 seconds before checking again
    time.sleep(60)
