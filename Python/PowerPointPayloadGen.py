import urllib.parse,  base64

beacon = input ("Paste beacon command:" + " ")

command, options = beacon.split('$',  1)

encoded = command.replace ("-c", "-e")

encode64 = base64.encodebytes(options.encode('utf-16le')).decode('ascii')

fullcommand = encoded + " " + encode64

print (urllib.parse.quote(fullcommand))

#print (fullcommand)
