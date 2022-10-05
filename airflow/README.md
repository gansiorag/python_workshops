# How install Airflow on Windows

1. Start PowerShell from administrator.
2. dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
3. creater directory on C:\Users\NameUser\airflow
4. In Microsoft Store find the Ubuntu and Installer
5. sudo apt update && sudo apt upgrade
6. sudo nano /etc/wsl.conf
7. [automount]<br>
root = /<br>
options = "metadata"
8. 