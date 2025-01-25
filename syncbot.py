import subprocess
import ctypes
import time
import logging

# Setup logging
logging.basicConfig(filename='syncbot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def is_admin():
    """Check if the script is run with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logging.error(f"Error checking admin privileges: {e}")
        return False

def run_command(command):
    """Run a command in the subprocess and return the output."""
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        logging.info(f"Command '{command}' executed successfully.")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command '{command}': {e}")
        return None

def check_for_updates():
    """Check for available system updates."""
    logging.info("Checking for updates...")
    output = run_command(['powershell', '-Command', 'Get-WindowsUpdate'])
    if output:
        logging.info("Updates found:\n" + output)
    else:
        logging.info("No updates found.")

def install_updates():
    """Install available system updates."""
    logging.info("Installing updates...")
    run_command(['powershell', '-Command', 'Install-WindowsUpdate -AcceptAll -AutoReboot'])

def main():
    if not is_admin():
        logging.error("SyncBot must be run as an administrator.")
        print("SyncBot must be run as an administrator.")
        return

    logging.info("SyncBot started.")
    check_for_updates()
    user_input = input("Do you want to install the updates? (yes/no): ").strip().lower()
    if user_input in ["yes", "y"]:
        install_updates()
    else:
        logging.info("Update installation cancelled by user.")
    
    logging.info("SyncBot finished.")

if __name__ == "__main__":
    main()