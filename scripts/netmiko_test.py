from netmiko import ConnectHandler

import datetime
import json

date = datetime.datetime.now()
time = f"{date.year}-{date.month}-{date.day}"

with open("C:\\Projects\\CCDP-ISP\\scripts\\devices.json", "r") as vars_file:
    devices = json.load(vars_file)
vars_file.close()

for device in devices["devices"]:
    hostname = device["hostname"]
    device_type = device["device_type"]
    ip = device["ip"]
    username = device["username"]
    password = device["password"]

    current_device = {
        "device_type": device_type,
        "ip": ip,
        "username": username,
        "password": password
    }

    success = False
    counter = 0

    ##### REMEMBER OST-RR-01 are not connected to MGMT network! #####
    ### Increase global_delay_factor to 3 or 4 ###

    while success != True and counter < 3:
        try:
            counter += 1
            net_con = ConnectHandler(**current_device, global_delay_factor=4)
            running_config = net_con.send_command("show running-config")
            success = True

            with open(f"C:\\Projects\\CCDP-ISP\\backups\\{hostname}_{time}", "w") as backup_file:
                backup_file.write(running_config)
            backup_file.close()

            print(f"success: {hostname}!")
        except:
            print(f"Error with {hostname}!")
