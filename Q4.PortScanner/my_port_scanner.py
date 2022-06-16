import nmap


begin = input("Enter the beginner port  : ")
if begin.isdigit():
    begin = int(begin)
else:
    print("Please enter a valid port number")
    exit()

end = input("Enter the end port number to begin scanning : ")
if end.isdigit():
    end = int(end)
else:
    print("Please enter a valid port number")
    exit()
target = input("Enter target ip : ")

scanner = nmap.PortScanner()

for i in range(begin, end+1):

    res = scanner.scan(target, str(i))

    res = res['scan'][target]['tcp'][i]['state']

    print(f'port {i} is {res}.')