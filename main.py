import subprocess


def ping_scan(subnet):
    result = subprocess.run(['nmap', '-sn', subnet],
                   check=True,
                   text=True,
                   capture_output=True
                   )
    return result.stdout

def service_detection(ip):
    serv_out = subprocess.run(['nmap', '-sV', ip],
                            check=True,
                            text=True,
                            capture_output=True
                            )
    return serv_out.stdout


while True:

    print("1- Ping scan\n2- Service Detection\n3- Exit\n")
    print("Make Sure Enter Choice in Numbers eg. 2\n")

    choice = int(input('Select your Scan: '))

    if choice == 1:
        target = input("Enter a subnet eg. 192.168.0.1/24: ")

        try:
            output = ping_scan(target)
            print(output)
        except subprocess.CalledProcessError:
            print("[+] Ping scan failed")

    elif choice == 2:
        ser_det_target = input("Enter a target eg. 192.168.0.115: ")

        try:
            ser_det = service_detection(ser_det_target)
            print(ser_det)
        except subprocess.CalledProcessError:
            print("[+] Service Detection failed")

    elif choice == 3:
        break