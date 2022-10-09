from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("mail.smtp2go.com", 2525)

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mail_from = "MAIL FROM: <patrick.merrill@sjsu.edu> \r\n"
clientSocket.send(mail_from.encode())
recv2 = clientSocket.recv(1024).decode()
print("Mail From: " + recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
rcpt_to = "RCPT TO: <merrillpe@gmail.com> \r\n"
clientSocket.send(rcpt_to.encode())
recv3 = clientSocket.recv(1024).decode()
print("RCPT TO: " + recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("DATA: " + recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send message data.
# Fill in start
subject = "Subject: SMTP Test \r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print("Message: " + recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Message ends with a single period.
# Fill in start
clientSocket.send(".\r\n".encode())
# Fill in end


# Send QUIT command and get server response.
# Fill in start
clientSocket.send("QUIT\r\n".encode())
recv6 = clientSocket.recv(1024).decode()
print("Quit: " + recv6)
clientSocket.close()
# Fill in end
