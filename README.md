jjproxy 
=======

一个便捷的全平台的代理方案

[How to Use](http://liruqi.github.io/jjproxy/)

搭建代理服务器

在 25 端口搭建 http/https 代理。

Ubuntu 上执行: apt-get install squid 

然后覆盖配置 squid.conf (或者只将其中的 port 配置 改为 25)

再修改我 PAC 中的代理即可使用。
