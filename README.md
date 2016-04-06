jjproxy
=======

本项目主要介绍如何利用国外VPS搭建多协议代理服务。

GFW 封锁了 HTTP/Socks5 代理，HTTP 代理是关键词过滤，Socks5 代理则是封锁协议。不过某些特殊的低端口并没有这么处理，已知的有 20，21，25。

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

`wget -O /etc/squid/squid.conf https://raw.githubusercontent.com/liruqi/jjproxy/master/squid-centos.conf`

`/etc/init.d/squid start`

