import socket


class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "\r\n")

    def connect(self, server):
        # defines the socket
        print("connecting to:" + server)
        self.irc.connect((server, 6667))  # connects to the server

    def nickuser(self, nickname):
        self.irc.send("USER " + nickname + " " + nickname + " "" + nickname + " " +
                      + nickname + " bot!\r\n")  # user authentication
        print("[+] Send USER passed ")
        self.irc.send("NICK " + nickname + "\r\n")
        print("[+] Send NICK passed")

    def channel(self, channel):
        self.irc.send("JOIN " + channel + "\r\n")  # join the chan
        print("[+] Send JOIN " + str(channel))

    def get_text(self):
        text = self.irc.recv(2040)  # receive the text
        return text
