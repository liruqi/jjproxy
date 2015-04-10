[jjproxy](http://liruqi.github.io/jjproxy/)
=======

本项目主要介绍如何利用国外VPS搭建多协议代理服务。

GFW 封锁了 HTTP/Socks5 代理，HTTP 代理是关键词过滤，Socks5 代理则是封锁协议。不过某些特殊的低端口并没有这么处理，已知的有 20，21，25。

[这里](http://liruqi.github.io/jjproxy/) 提供了我在 [linode](https://www.linode.com/?r=cc93760c5a1b11a4d9c06ecfa4483bcce3d8f1e1) 上搭建的公共代理。

搭建代理服务器
==============

在 25 端口搭建 http/https 代理。

Ubuntu: 
-------
`apt-get install squid`

`curl https://raw.githubusercontent.com/liruqi/jjproxy/master/squid.conf > /etc/squid3/squid.conf`

`/etc/init.d/squid restart`

CentOS:
-------
`setenforce 0`

`yum install squid`

`wget -O /etc/squid/squid.conf https://raw.githubusercontent.com/liruqi/jjproxy/4e9c08f421f80651d78cdcd6d0a33b0cda64f0ce/squid.conf`

`/etc/init.d/squid start`

然后使用 [gfwlist2pac](https://github.com/clowwindy/gfwlist2pac) 生成 PAC 即可。
