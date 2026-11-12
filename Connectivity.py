"""Validates devices are up and connected"""

#Allows us to ping ping device to verify connectivity
import subprocess
#Logging used for logging devices
import logging
#Uses specific system parameters for logging
import sys
#Used to read CSV Files
import csv

#Logging Config
logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
  handlers=[
    logging.FileHandler("Connectivity.log")
    logging.StreamHandler(sys.stdout)
  ]
)

#Function to gather device information
def load_devices():
  device_list = {}
  with open('network_devices.csv', mode='r') as csv_file:
    network_devices = csv.DictReader(csv_file)
    for row in network_devices:
      device_list[row["Device Name"]] = (row["Device Address"])
  return device_list
  
#Fuction to ping devices
def ping_device(device_name, device_ip):
  try:
    ping_check = subprocess.run(["ping", "-c", "1", device_ip], capture_output=True, text=True)
    if ping_check.returncode !=0:
      logging.error(f"Ping FAILED for {device_name} {device_ip}")
      return False
    else:
      logging.info(f"Ping SUCCESSFUL for {device_name} {device_ip}")
      return True
  except Exception as e:
    logging.error(f"ERROR pinging {device_name} {device_ip}")

if __name__ == "__main__":
  device_dict = load_devices()
  for hostname, ip_address in device_dict.items():
        ping_device(hostname, ip_address)
