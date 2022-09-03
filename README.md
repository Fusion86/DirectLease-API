# DirectLease API

DirectLease API which their mobile client uses to display prices.
Using this (private) API might not be legal, so keep that in mind.

## How to find this information?

Download their app on some android device and install/setup mitmproxy.  
Because SSL pinning is used in their app we need to bypass that. For this we use Frida.  
Install the frida-server on your android and start it. Next we run `frida -U --codeshare pcipolloni/universal-android-ssl-pinning-bypass-with-frida -f com.app_it_up.dl_tankservice` ([read this post for more info](https://securitygrind.com/bypassing-android-ssl-pinning-with-frida/))  
Now we can see all the app traffic.

We still need to figure out how to calculate the `X-Checksum` header.
For this we can use [dex2jar](https://github.com/pxb1988/dex2jar) in combination with [bytecode-viewer](https://github.com/Konloch/bytecode-viewer) or [JD-GUI](http://java-decompiler.github.io/).  
Search for the `X-Checksum` string and figure out what their code does to calculate the checksum.
