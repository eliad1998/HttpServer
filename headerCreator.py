import os.path

# Getting the file type
def getFileType(fileName):
    return  os.path.splitext(fileName)[1][1:]
# Return the content type field in the http header by the file type
def getContentType(fileType):
    switch =  {
        # Images
        "png": "image/png",
        "jpg": "image/jpg",
        "gif":  "image/gif",
        "ico":  "image/x-icon",
        "jpeg": "image/jpeg",
        # Text types
        "html": "text/html",    #html
        "css": "text/css",      #css
        "js": "text/javascript",    # javascript
        # Font types
        "woff": "application/font-woff2",
        "ttf": "application/font-ttf",
        "svg": "application/font-svg",
        "eot": "application/font-eot",
        "otf": "application/font-otf",
    }
    return switch.get(fileType, "text/html")

def addHeader200(fileName, dataToSend):
    send = ""
    send += "HTTP/1.1 200 OK\r\n"
    # We only do demo for http header so we choose a date
    send += "Date: Sun, 26 Sep 2010 20:09:20 GMT \r\n"
    # Adding last modified the same way by a randomal date
    send += "Last-Modified: Tue, 30 Oct 2007 17:00:02 GMT\r\n"
    # Length field
    send+= "Content-Length: " + str(len(dataToSend)) + "\r\n"
    fileType = getFileType(fileName)
    # Adding content type header
    send +=  "Content-type: " + getContentType(fileType) +  "\r\n"
    # Closing the connection after the http response
    send+= "Connection: Keep-Alive\r\n"
    # End of headers
    send += "\r\n"
    send += dataToSend
    return send

def addHeader304(fileName):
    send = ""
    send += "HTTP/1.1 304 Not Modified\r\n"
    # We only do demo for http header so we choose a date
    send += "Date: Sun, 26 Sep 2010 20:09:20 GMT \r\n"
    # Adding last modified the same way by a randomal date
    send += "Last-Modified: Tue, 30 Oct 2007 17:00:02 GMT\r\n"
    # Length field
  #  send += "Content-Length: " + str(len(dataToSend)) + "\r\n"
    fileType = getFileType(fileName)
    # Adding content type header
    send += "Content-type: " + getContentType(fileType) + "\r\n"
    # Closing the connection after the http response
    send += "Connection: Keep-Alive\r\n"
    # End of headers
    send += "\r\n"
    return send
# Error 404 not found
def error404Header(fileName):
    send = ""
    send += "HTTP/1.1 404 Not Found\r\n"
    # We only do demo for http header so we choose a date
    send += "Date: Sun, 26 Sep 2010 20:09:20 GMT \r\n"
    # Length field
    # still don't know which len to sencd
    # We won't add a length. Only if i want to create error 404 page..
    fileType = getFileType(fileName)
    # Adding content type header
    send += "Content-type: " + getContentType(fileType) + "\r\n"
    # Closing the connection after the http response
    send += "Connection: Keep-Alive\r\n"
    # End of headers
    send += "\r\n"
    return send