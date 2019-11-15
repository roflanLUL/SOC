import socket
import subprocess
import os

ending = True

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
adress=s.getsockname()[0]
s.close()
port = "5201"

proc = subprocess.Popen(["sctp_darn","-H",adress,"-P",port,"--listen"], shell=False)
while ending:
	out = subprocess.check_output(['sudo', 'tshark', '-i', 'ens33', '-c', '2', '-f', "sctp and port " + port, '-T', 'fields', '-e', 'data.data'])
	out=str(out)[2:-9]
	if(out != ''):
		out = bytes.fromhex(out).decode('utf-8')
		if out == 'close':
			ending = False
		else:
			os.system("echo '{}'>> tmp.txt".format(out))

proc.terminate()
