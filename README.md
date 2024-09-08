# Vending
Setting up a raspberry pi to take webhooks from UP and release product in vending machine


Read: https://code.visualstudio.com/docs/python/python-tutorial on how to set up virtual environment in vscode.

For reference:
Git:
git add --all
git commit -m ''

Raspberry pi:
sudo python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)

Static IP:
Current IP:                 hostname -I                                     192.168.0.231
Default interface:          ip r | grep default                             default via 192.168.0.1
                            route | grep '^default' | grep -o "[^ ]*$"      wlan0
                            sudo nano /etc/resolv.conf                      nameserver 192.168.0.1

sudo nano /etc/dhcpcd.conf
input:
static ip_address=192.168.0.231/24
static routers=192.168.0.1
static domain_name_servers=192.169.0.1

sudo shutdown -r now
sudo reboot


