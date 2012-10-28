项目目的
--------
* 翻墙代理，不保证数据安全性（安全性依赖于使用的远程HTTP/HTTPS代理的安全性，你所输入、浏览的信息可能会被代理服务器记录）。
* Follow up: [G+](https://plus.google.com/b/108661470402896863593/)

使用方法
--------

1. 如果没有python2.7 环境，安装 python2.7
2. Terminal: python jjproxy.py
3. 把浏览器HTTP/HTTPS 代理设置为 127.0.0.1:1987

开发者
------
* [XIAOXIA](http://xiaoxia.org), 代理原型作者
* [LIRUQI](http://liruqi.info), 后续开发, 各平台的打包、发布

代理原理
--------

1. 对抗关键词过滤: [rfc2616 - section 4.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html)
2. 对抗DNS污染: 修改PyDNS 库，实现丢弃GFW DNS 伪包。
3. 对抗IP封锁: 收集被封锁的IP, 在DNS 解析过程中尝试找到可用IP。
4. 如果没有可用IP，或者是HTTP注入导致异常，本代理会走HTTP代理。

捐赠
----
如果你喜欢这个软件，希望支持其后续开发，欢迎[捐赠](https://me.alipay.com/liruqi)。
