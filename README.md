# SyncBot

SyncBot is a Python script designed to automate the process of checking for and installing system updates on Windows machines. This script utilizes PowerShell commands to interface with Windows Update and requires administrative privileges to execute.

## Features

- Checks for available system updates.
- Provides a log of update checks and installations.
- Prompts the user to install updates if available.
- Automatically reboots the system if necessary after installing updates.

## Requirements

- Windows Operating System
- Python 3.x
- Administrative privileges

## Installation

1. Clone the repository or download the `syncbot.py` file.
2. Ensure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).

## Usage

1. Open a command prompt with administrative privileges.
2. Navigate to the directory containing `syncbot.py`.
3. Run the script using Python:

   ```bash
   python syncbot.py
   ```

4. Follow the on-screen instructions to check for and install updates.

## Logging

SyncBot logs its operations to a file named `syncbot.log` in the same directory as the script. This log includes timestamps and details of each operation for troubleshooting and record-keeping.

## Notes

- SyncBot must be run as an administrator to function correctly.
- The script uses PowerShell commands and requires the Windows Update PowerShell Module. Ensure that your system has the necessary permissions and configurations to run these commands.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any damage or loss caused by the use of this script.