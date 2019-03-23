import hmac
message1 = b'Hello,world!'
message2 = b'I\'ll back!'
key = b'secret'

h = hmac.new(key, message1, digestmod='MD5')
h.update(message2)
hm = h.hexdigest()
print(hm)
