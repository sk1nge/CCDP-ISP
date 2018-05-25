from netmiko import ConnectHandler

"""
  {
    "device_type": "cisco_xe",
    "ip": "10.10.123.239",
    "username": "cisco",
    "password": "cisco"
  }
"""

current_device = {
    'device_type': 'cisco_xe',
    'ip':   '10.10.123.239',
    'username': 'cisco',
    'password': 'cisco'
}

net_con = ConnectHandler(**current_device, global_delay_factor=2)
running_config = net_con.send_command("show running-config")
print(running_config)
