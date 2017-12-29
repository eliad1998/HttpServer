# -*- coding: utf-8 -*-
import socket, threading
import os.path
from headerCreator import *     # Import the header creator
from articles import putArticles
# is_number
# Checks if s is number
# The function took from the internet
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False




# getRequest
# The function get the data that the server recieved from the user.
# The function return two strings - our request type (get or post)
# In addition it return the request itself and if it modified or not
def getRequest(data):
    try:
        # Splitting the header by lines
        splitted = data.split('\n')
        #  For example there is 'GET /Files/template.html HTTP/1.1\r
        # The request and it's type is the first line of header request.
        typeRequest = splitted[0].split(' ')   # Splitting it by spaces.
        type = typeRequest[0]  # Type will be the first splitted
        request = (typeRequest[1])[1:] #   the request itself will be the second witout the '/' sign
        # Now we will check if the request is for modified or not:
        modified =  False   # Did not found the field so not modified
        # For example the modified field will look like If-Modified-Since: Tue, 30 Oct 2007 17:00:02 GMT\r'
        for i in range(0, len(splitted)):
            if (splitted[i].split(' '))[0] == "If-Modified-Since:":  # Found the field
                modified =  True
        return type, request, modified
    except IndexError:
        return None, None, None
# Adding the files/ in case of dinamic request when we need to search in files directory.
def addFiles(fileName):
    if not fileName[0:6] == "Files/":
        return "Files/" + fileName
    return fileName
# In the program we will check dinamic request.
# If the user sent wrong dinamic request we will ignore the dinamic request
def removeParameters(fileName):
    # Found a ?
    if fileName.__contains__('?'):
       if fileName.index('?') != -1:
            # Return the filename witout parameter
            return fileName[0:fileName.index('?')]
    return fileName
# Our domain:www.my-news-website.co.il
# Creating the tcp socket (tcp is stream)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Our local server.
server_ip = '127.0.0.2'
# We work on port 80 because we simulate http on browser so the client will be on the brouser and send messages via
# port 80
server_port = 80
# Binding the ip
server.bind((server_ip, server_port))
server.listen(5)

# Running the server
while True:
    # Accept
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    data = client_socket.recv(1024)

    # Receive the request from the user.
    print 'Received: ', data.split('\n')
    # Send is the what we want to send to the usr
    send = data
    # Getting the type of request and the request itself and if it modified
    typeRequest, request, modified = getRequest(data)
    # Fixing unwanted connection
    if (typeRequest == None):
        print 'Client disconnected'
        client_socket.close()
        continue
    # Sending data to the client.
    # Get request
    if typeRequest == "GET":
        #########################################
        # Dinamic request
        # Home page goes to template.html
        if request == "homepage":
            # We will go to template
            request = "template.html"
        # Number of articles to select
        number = -1
        # Checks is the homepage is int pattern homepage?id=x x- is integer
        if request[0:len("homepage?id=")] == "homepage?id=":
            if (is_number(request[len("homepage?id="): len(request)])):
                number = int(request[len("homepage?id="): len(request)])
                # We request between 1 to 8 articles
                request = "template.html"
        ##########################################

        request = removeParameters(request)
        request = addFiles(request)
        if os.path.exists(request):
            if (modified == True):   # Modified so it is in the cache
                send = addHeader304(request) # Send 304 header
            # Did not modified or not in the cache so get the data from the file
            else:
                file = open(request, "rb")
                dataToSend = file.read()
                if number >= 0 and number <= 8:   # Adding the articles to template.html
                    #dataToSend = putArticles(dataToSend)
                    dataToSend = putArticles(dataToSend, number)

                send = addHeader200(request, dataToSend) # Adding the header
        else:
            send = error404Header(request)
            print "o.o"
        client_socket.send(send)
        # We dont waiting for request because we open connection request and than close
    print 'Client disconnected'
    client_socket.close()




