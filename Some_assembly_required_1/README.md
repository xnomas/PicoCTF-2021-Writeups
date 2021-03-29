# Some assembly required - 1

Category: Web Exploitation </br>
AUTHOR: SEARS SCHULZ

## Solution

This was a pretty easy challenge. I simply set BurpSuite to intercept all server responses, eventually got the following response:
```
GET /JIFxzHyW8W HTTP/1.1
Host: mercury.picoctf.net:15472
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://mercury.picoctf.net:15472/index.html
Connection: close
If-Modified-Since: Tue, 16 Mar 2021 00:38:49 GMT
Cache-Control: max-age=0
```
That is a weird one, huh? Visiting the link the file `JIFxzHyW8W` is downloaded. What next? Well I just tried `cat JIFxzHyW8W`:
```
picoCTF{c733fda95299a16681f37b3ff09f901c}
```
And the very bottom was the flag. great!