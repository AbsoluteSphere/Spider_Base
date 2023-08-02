import socket
import re
def images_data(i):
    client = socket.socket()
    client.connect(('pic.netbian.com', 80))
    http_req = 'GET ' + i + ' HTTP/1.0\r\nHost:pic.netbian.com\r\nUser-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36\r\n\r\n'
    client.send(http_req.encode())
    data = client.recv(1024)
    result = b''
    while data:
        result += data
        data = client.recv(1024)
    images = re.findall(b'\r\n\r\n(.*)', result, re.S)
    with open('./img/' + i.split("/")[6], 'wb') as f:
        f.write(images[0])
if __name__ == '__main__':
    url = ['http://pic.netbian.com/uploads/allimg/220211/004115-1644511275bc26.jpg',
           'https://pic.netbian.com/uploads/allimg/220215/233510-16449393101c46.jpg',
           'https://pic.netbian.com/uploads/allimg/211120/005250-1637340770807b.jpg']
    for i in url:
        images_data(i)