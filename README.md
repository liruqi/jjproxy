[jjproxy](http://liruqi.github.io/jjproxy/)
=======
GFW 封锁了 HTTP/Socks5 代理，HTTP 代理是关键词过滤，Socks5 代理则是封锁协议。不过某些特殊的低端口并没有这么处理，已知的有 20，21，25。

搭建代理服务器
==============

在 25 端口搭建 http/https 代理。

Ubuntu 上执行: 

`apt-get install squid`

`curl https://raw.githubusercontent.com/liruqi/jjproxy/master/squid.conf > /et/squid3/squid.conf`

然后修改我 PAC 中的代理即可使用。
