#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
gConfig = {
    "VERSION" : "20121022",
    "AUTORANGE_BUFSIZE": 8192,
    "AUTORANGE_WAITSIZE": 524288,
    "AUTORANGE_MAXSIZE": 1048576,
    "BLOCKED_DOMAINS_URI" : "https://raw.github.com/liruqi/west-chamber-season-3/master/west-chamber-proxy/status/timedout.txt",
    "REMOTE_DNS_LIST" : ["8.8.8.8", "202.181.202.140", "202.181.224.2","168.95.192.1","168.95.1.1","203.119.1.1"],
    "DNS_PROTOCOL": "udp",
    "DNS_PORT": 53,
    "DNS_CACHE_MAXSZ" : 1024,
    "SKIP_LOCAL_RESOLV" : True,
    "CONFIG_ON_STARTUP" : False,
    "BLOCKED_DOMAINS_MATCH_ROOT" : False,
    "LOCAL_PORT" : 1987,
    "HOST" : {},
    "HTTP_PROXY": "61.30.127.2",
    "HSTS_DOMAINS" : {
        "developers.facebook.com": 1,
        "groups.google.com": 1,
        "www.paypal.com" : 1,
        "www.elanex.biz" : 1,
        "jottit.com" : 1,
        "sunshinepress.org" : 1,
        "www.noisebridge.net" : 1,
        "neg9.org" : 1,
        "riseup.net" : 1,
        "factor.cc" : 1,
        "splendidbacon.com" : 1,
        "aladdinschools.appspot.com" : 1,
        "ottospora.nl" : 1,
        "www.paycheckrecords.com" : 1,
        "market.android.com" : 1,
        "lastpass.com" : 1,
        "www.lastpass.com" : 1,
        "keyerror.com" : 1,
        "entropia.de" : 1,
        "romab.com" : 1,
        "logentries.com" : 1,
        "stripe.com" : 1,
        "facebook.com": 1,
    },
    #collect domains that support HTTPS, to reduce usage of web proxy
    "HSTS_ON_EXCEPTION_DOMAINS" : {
        "s.ytimg.com": 1,
        "i1.ytimg.com": 1,
        "i2.ytimg.com": 1,
        "i3.ytimg.com": 1,
        "i4.ytimg.com": 1,
        "i1.tdimg.com": 1,
        "i2.tdimg.com": 1,
        "i3.tdimg.com": 1,
        "i4.tdimg.com": 1,
        "bits.wikimedia.org": 1,
        "www.wikipedia.org": 1,
        "www.google-analytics.com": 1,
        "apps.facebook.com": 1,
        "graph.facebook.com": 1,
        "www.youtube.com": 1,
        "m.facebook.com": 1,
    },
    "BLOCKED_DOMAINS": {
        "baidu.jp" : True,
        "search.twitter.com" : True,
        "www.baidu.jp" : True,
        "www.nicovideo.jp": True,
        "www.dailymotion.com": True,
        "ext.nicovideo.jp": True,
        "blog.roodo.com": True,
        "www.dwnews.com": True,
        "china.dwnews.com": True,
        "www.mediafire.com": True,
        "thepiratebay.org": True,
        "thepiratebay.se": True,
        "www.bbc.co.uk": True,
        "chinadigitaltimes.net": True,
        "www.wenxuecity.com": True,
        "bbs.wenxuecity.com": True,
        "www.blogger.com": True,
        "blogger.com": True,
        "plarouter.com": True,
    },
    "BLOCKED_IPS": {
        "23.21.220.40":1, "23.21.242.194":1, #dropbox
        "50.16.240.166":1, #dropbox
        "70.86.20.29" : 1, #www.bullogger.com
        "66.220.146.101": 1,
        "69.171.224.53": 1,
        "66.220.158.11": 1,
        "69.171.242.11": 1,
        "69.93.206.250": 1, #www.xys.org
        "69.163.141.215": 1, #www.zuola.com
        "174.121.98.156": 1,
        "50.22.53.157": 1,
        "50.22.53.155": 1,
        "50.63.43.1": 1,
        "72.32.231.8": 1,
        "72.52.81.24": 1,
        "72.233.2.58": 1,
        "74.125.31.141": 1,
        "74.125.39.102": 1,
        "174.121.66.230": 1,
        "107.20.170.126": 1,
        "180.235.96.30": 1,
        "204.236.224.226": 1,
        "69.163.223.11": 1, #letscorp.net
    },
    "BLOCKED_IPS_M16": {
        "174.129" : 1,
        "50.23": 1,
    },
    "BLOCKED_IPS_M24": {
        "199.16.156": 1,
        "66.220.149": 1,
        "66.220.156": 1,
        "69.171.224": 1,
        "74.125.127": 1,
        "208.109.6": 1,
        "199.59.148": 1,
        "199.59.149": 1,
        "199.59.150": 1,
    },
    "PAGE_RELOAD_HTML": """<html>
    <head>
        <script type="text/javascript" charset="utf-8">
            window.location.reload();
        </script>
    </head>
    <body>
    </body></html>""",
}

# 69.171.228.0/24 for facebook
blockedIpString = """69.171.228.5
69.171.228.6
69.171.228.11
69.171.228.12
69.171.228.15
69.171.228.16
69.171.228.19
69.171.228.20
69.171.228.23
69.171.228.24
69.171.228.27
69.171.228.28
69.171.228.31
69.171.228.35
69.171.228.36
69.171.228.50
69.171.228.51
69.171.228.70
69.171.228.71
69.171.228.74
69.171.228.75
69.171.228.79
69.171.228.229
69.171.228.230
69.171.228.231
69.171.228.232
69.171.228.233
69.171.228.234
69.171.228.244
69.171.228.245
69.171.228.246
69.171.228.247
69.171.228.248
69.171.228.249
69.171.228.250
69.171.228.251
69.171.228.252
69.171.228.253
69.171.228.254
"""

# 69.171.229.0/24 for facebook
blockedIpString += """69.171.229.11
69.171.229.12
69.171.229.13
69.171.229.14
69.171.229.15
69.171.229.16
69.171.229.20
69.171.229.23
69.171.229.24
69.171.229.27
69.171.229.28
69.171.229.31
69.171.229.32
69.171.229.46
69.171.229.47
69.171.229.51
69.171.229.70
69.171.229.71
69.171.229.72
69.171.229.73
69.171.229.74
69.171.229.76
69.171.229.77
69.171.229.229
69.171.229.230
69.171.229.231
69.171.229.232
69.171.229.233
69.171.229.234
69.171.229.244
69.171.229.245
69.171.229.246
69.171.229.247
69.171.229.248
69.171.229.249
69.171.229.250
69.171.229.251
69.171.229.252
69.171.229.253
69.171.229.254
"""

# 69.171.224.0/24 for facebook
blockedIpString += """69.171.224.1
69.171.224.2
69.171.224.3
69.171.224.4
69.171.224.5
69.171.224.6
69.171.224.32
69.171.224.33
69.171.224.34
69.171.224.35
69.171.224.36
69.171.224.37
69.171.224.38
69.171.224.39
69.171.224.40
69.171.224.41
69.171.224.48
69.171.224.49
69.171.224.50
69.171.224.51
69.171.224.52
69.171.224.53
69.171.224.54
69.171.224.55
69.171.224.56
69.171.224.57
69.171.224.64
69.171.224.65
69.171.224.66
69.171.224.67
69.171.224.68
69.171.224.80
69.171.224.81
69.171.224.82
69.171.224.83
69.171.224.84
69.171.224.96
69.171.224.97
69.171.224.98
69.171.224.99
69.171.224.100
69.171.224.112
69.171.224.113
69.171.224.114
69.171.224.115
69.171.224.116"""

# 69.171.234.0/24 for facebook
blockedIpString += """
69.171.234.16
69.171.234.17
69.171.234.19
69.171.234.32
69.171.234.35
69.171.234.48
69.171.234.49
69.171.234.64
69.171.234.65
69.171.234.68
69.171.234.80
69.171.234.82
69.171.234.83
69.171.234.96
69.171.234.98"""

# 74.125.0.0/16
blockedIpString += """74.125.71.88
74.125.71.89
74.125.71.99
74.125.71.100
74.125.71.101
74.125.71.106
74.125.71.113
74.125.71.116
74.125.71.121
74.125.71.128
74.125.71.138
74.125.71.139
74.125.71.150
74.125.71.160
74.125.71.161
74.125.71.162
74.125.71.163
74.125.71.188
74.125.71.192
"""

for ip in blockedIpString.split("\n"):
    if len(ip) > 0:
        gConfig["BLOCKED_IPS"][ip] = 1

blockedDomainString = """0to255.com
1-apple.com.tw
12vpn.com
173ng.com
1984bbs.org
1pondo.tv
2008xianzhang.info
213.251.145.96
301works.org
315lz.com
365singles.com.ar
36rain.com
4bluestones.biz
6park.com
7capture.com
89-64.org
9999cn.com
99bbs.com
9bis.com
9bis.net
aboutgfw.com
acgkj.com
aculo.us
adult168.com
adultfriendfinder.com
advanscene.com
advertfan.com
aenhancers.com
aftygh.gov.tw
ait.org.tw
aiweiweiblog.com
aiyori.org
alabout.com
alasbarricadas.org
alexlur.org
alkasir.com
allaboutalpha.com
alliance.org.hk
allonlinux.free.fr
alternate-tools.com
alwaysdata.net
americangreencard.com
anchorfree.com
anthonycalzadilla.com
antiwave.net
aolchannels.aol.com
api.proxlet.com
apigee.com
app.heywire.com
appledaily.com.tw
apps.hloli.net
archive.org
areca-backup.org
art-or-porn.com
asiaharvest.org
atnext.com
axureformac.com
badassjs.com
basetimesheightdividedby2.com
bbs.51.ca
bbs.kimy.com.tw
bbs.morbell.com
bbsfeed.com
bd.zhe.la
beijing1989.com
beijingspring.com
benjaminste.in
berlintwitterwall.com
bestforchina.org
beta.usejump.com
bettween.com
bfnn.org
bignews.org
bigsound.org
bill2-software.com
billywr.com
blinkx.com
blockcn.com
blog.51.ca
blog.aiweiwei.com
blog.birdhouseapp.com
blog.bitly.com
blog.boxcar.io
blog.chinatimes.com
blog.dayoneapp.com
blog.dribbble.com
blog.fizzik.com
blog.foolsmountain.com
blog.gowalla.com
blog.hotpotato.com
blog.ifttt.com
blog.instagram.com
blog.iphone-dev.org
blog.joeyrobert.org
blog.kangye.org
blog.kl.am
blog.lightbox.com
blog.mongodb.org
blog.path.com
blog.pchome.com.tw
blog.pentalogic.net
blog.pikchur.com
blog.pilotmoon.com
blog.rockmelt.com
blog.romanandreg.com
blog.sogoo.org
blog.sparrowmailapp.com
blog.usa.gov
blog.xuite.net
blogcatalog.com
blogimg.jp
bloodshed.net
boardreader.com
bobulate.com
bolin.netfirms.com
bonjourlesgeeks.com
books.com.tw
bookshelfporn.com
bot.nu
bowenpress.com
boxun.com
boxun.tv
br.st
bralio.com
brandonhutchinson.com
break.com
breakingtweets.com
brightkite.com
brizzly.com
budaedu.org
bugbeep.com
bugclub.org
bullog.org
bullogger.com
c-est-simple.com
c-spanvideo.org
c1522.mooo.com
calebelston.com
canadameet.com
caobian.info
caochangqing.com
catholic.org.hk
cbs.ntu.edu.tw
cc9007.spaces.live.com
cdjp.org
cdpweb.org
cecc.gov
changp.com
chaos.e-spacy.com
chengmingmag.com
cherrysave.com
chevronwp7.com
china101.com
chinaaffairs.org
chinacomments.org
chinadigitaltimes.net
chinaeweekly.com
chinagfw.org
chinagreenparty.org
chinainterimgov.org
chinasocialdemocraticparty.com
chinaway.org
chinaworker.info
chinesen.de
chinesenewsnet.com
chrispederick.com
chrispederick.net
christianstudy.com
chrlcg-hk.org
chuizi.net
civicparty.hk
civilhrfront.org
cl.ly
classicalguitarblog.net
clientsfromhell.net
cn.dayabook.com
cnd.org
cocoa.zonble.net
codeboxapp.com
comefromchina.com
comnews.gio.gov.tw
cookingtothegoodlife.com
coolaler.com
coolder.com
cpj.org
crd-net.org
crossthewall.net
csuchen.de
cubicle17.com
cyberghost.natado.com
cydia.ifuckgfw.com
cynscribe.com
dabr.co.uk
dabr.mobi
dadazim.com
dailymotion.com
dajiyuan.com
dalailamaworld.com
dalianmeng.org
danke4china.net
dapu-house.gov.tw
davidslog.com
default.secureserver.net
democrats.org
derekhsu.homeip.net
desc.se
deutsche-welle.de
developers.box.net
devio.us
diaoyuislands.org
digitalnomadsproject.org
dimitrik.free.fr
discuss.com.hk
dit-inc.us
dl.box.net
dojin.com
dongde.com
dongtaiwang.com
dongtaiwang.net
dongyangjing.com
dotheyfolloweachother.com
dowei.org
doxygen.org
dphk.org
dtiblog.com
dtiserv2.com
duckmylife.com
duihua.org
duoweitimes.com
duping.net
dupola.com
dupola.net
dw-world.com
dw-world.de
dwnews.com
dzze.com
eamonnbrennan.com
echofon.com
edubridge.com
eevpn.com
efksoft.com
eic-av.com
emacsblog.org
en.favotter.net
epochtimes.com
erights.net
eriversoft.com
ernestmandel.org
etizer.org
etools.ncol.com
everyday-carry.com
exploader.net
f.cl.ly
falsefire.com
fanfou.im
fangbinxing.com
fangeming.com
farwestchina.com
faststone.org
fbcdn.net
fc2.com
feer.com
fgmtv.org
fileserve.com
fillthesquare.org
firstfivefollowers.com
flecheinthepeche.fr
fourface.nodesnoop.com
fourthinternational.org
fredwilson.vc
free-ssh.com
free-vpn.info
freegateget.googlepages.com
freessh.us
freewallpaper4.me
freexinwen.com
friendfeed.com
frommel.net
fsurf.com
ftchinese.com
funp.com
furinkan.com
furl.net
futurechinaforum.org
futuremessage.org
gabocorp.com
gaoming.net
gardennetworks.com
gardennetworks.org
gartlive.com
gather.com
geek-art.net
geekmade.co.uk
generesis.com
getcloudapp.com
getsmartlinks.com
ggssl.com
ginx.com
givemesomethingtoread.com
globalmuseumoncommunism.org
globalvoicesonline.org
gmhz.org
goldwave.com
gongmeng.info
gongminliliang.com
goodreaders.com
goodreads.com
gopetition.com
gov.tw
gpass1.com
grandtrial.org
graphis.ne.jp
great-firewall.com
greatfirewall.biz
greenvpn.net
gtricks.com
guancha.org
gzone-anime.info
h-china.org
hahlo.com
hasaowall.com
hcc.gov.tw
hdtvb.net
heartyit.com
hechaji.com
hellonewyork.us
helloqueer.com
hellotxt.com
helpeachpeople.com
hen.bao.li
highrockmedia.com
hihiforum.com
hiitch.com
hjclub.info
hk.myblog.yahoo.com
hk32168.com
hkgolden.com
hkjp.org
hkreporter.com
hkzone.org
hnjhj.com
hootsuite.com
hotspotshield.com
hougaige.com
hqcdp.org
hudatoriq.web.id
huping.net
hutianyi.net
hwinfo.com
i2p2.de
ialmostlaugh.com
identi.ca
ifcss.org
illusionfactory.com
ilove80.be
im.tv
imageflea.com
imagevenue.com
imkev.com
incredibox.fr
iner.gov.tw
info.51.ca
interestinglaugh.com
internationalrivers.org
internetfreedom.org
internetpopculture.com
ipicture.ru
ippotv.com
ironicsoftware.com
ironpython.net
ithelp.ithome.com.tw
itweet.net
jayparkinsonmd.com
joachims.org
juliereyc.com
jyzj.waqn.com
k2.xrea.com
ka-wai.com
kagyuoffice.org.tw
kanzhongguo.com
khcc.gov.tw
kineox.free.fr
kinghost.com
kk.gov.tw
klccab.gov.tw
kmh.gov.tw
kompozer.net
koolsolutions.com
kt.kcome.org
kurtmunger.com
ladbrokes.com
laogai.org
laomiu.com
laptoplockdown.com
lenwhite.com
lesscss.org
letscorp.net
liaowangxizang.net
libertytimes.com.tw
linux-engineer.net
list.ly
littlebigdetails.com
liudejun.com
liujianshu.com
livevideo.com
log.riku.me
london.neighborhoodr.com
longtermly.net
lookingglasstheatre.org
lovequicksilver.com
lsforum.net
lupm.org
lvhai.org
lyricsquote.com
m.plixi.com
m.slandr.net
m.tweete.net
madmenunbuttoned.com
magazines.sina.com.tw
mail-archive.com
makemymood.com
markmilian.com
marxist.net
mashable.com
matainja.com
megurineluka.com
melon-peach.com
mesotw.com
middle-way.net
mimivip.com
minghui.org
mingpao.com
minimalmac.com
mitbbs.com
mitbbs.org
mixero.com
mizzmona.com
mk5000.com
mlcool.com
mmaaxx.com
mobileways.de
modfetish.com
mondex.org
morningsun.org
moviefap.com
mpinews.com
mrtweet.com
msguancha.com
mtw.tl
multiply.com
mvdis.gov.tw
my.keso.cn
mychinamyhome.com
mypaper.pchome.com.tw
myparagliding.com
mypopescu.com
myvlog.im.tv
n.yam.com
navigeaters.com
ncree.gov.tw
networkedblogs.com
newcenturymc.com
newchen.com
news.pchome.com.tw
news.pts.org.tw
news.sina.com.hk
news.sina.com.tw
news.yam.com
newsminer.com
newtalk.tw
nexton-net.jp
ngensis.com
nhri.gov.tw
nicovideo.jp
nmp.gov.tw
nmtl.gov.tw
notes.alexdong.com
nrk.no
ntdtv.com
nurgo-software.com
observechina.net
october-review.org
ohloh.net
olumpo.com
osfoora.com
ourdearamy.com
oursogo.com
ow.ly
pacificpoker.com
pandora.tv
paper-replika.com
pbwiki.com
pbworks.com
pbxes.com
pbxes.org
peacehall.com
peerpong.com
pekingduck.org
penchinese.com
pengyulong.com
pign.net
ping.fm
plusbb.com
popyard.org
porn2.com
post.anyu.org
powerapple.com
powercx.com
privacybox.de
prosiben.de
proxomitron.info
prozz.net
psiphon.civisec.org
ptt.cc
pulse.yahoo.com
pureconcepts.net
purepdf.com
puttycm.free.fr
qkshare.com
qoos.com
qstatus.com
qtweeter.com
quadedge.com
qvodzy.org
r.mzstatic.com
radiovaticana.org
rangzen.org
ranyunfei.com
rayfme.com
read100.com
readingtimes.com.tw
redtube.com
referer.us
renminbao.com
renyurenquan.org
retweeteffect.com
retweetrank.com
rfachina.com
rileyguide.com
rocmp.org
rsf-chinese.org
rsf.org
rthk.org.hk
rubyinstaller.org
rutube.ru
sacom.hk
salvation.org.hk
sandnoble.com
sanmin.com.tw
sapikachu.net
savetibet.org
secretchina.com
secretgarden.no
secure.wikimedia.org
seezone.net
sendoid.com
sesawe.net
sexandsubmission.com
sfileydy.com
shangfang.org
shapeservices.com
share.youthwant.com.tw
sharecool.org
sharkdolphin.com
shaunthesheep.com
shell.cjb.net
shenshou.org
shizhao.org
sitebro.tw
skimtube.com
slavasoft.com
slinkset.com
smile-cca22.nicovideo.jp
sobees.com
sod.co.jp
sogclub.com
sokamonline.com
soundofhope.org
soup.io
space-scape.com
speckleapp.com
spencertipping.com
starp2p.com
sthoo.com
stickam.com
stickeraction.com
storagenewsletter.com
strongvpn.com
subacme.rerouted.org
sugarsync.com
sytes.net
t.co
t.orzdream.com
t35.com
tagwalk.com
taiwankiss.com
taiwannation.50webs.com
taiwantt.org.tw
tangben.com
taolun.info
tbpic.info
tchb.gov.tw
tchrd.org
teamseesmic.com
techlifeweb.com
technorati.com
techparaiso.com
the-sun.on.cc
thebcomplex.com
thedw.us
thepiratebay.org
thepiratebay.se
thetibetpost.com
thetrotskymovie.com
tianhuayuan.com
tiantibooks.org
tianzhu.org
tibet.com
tibet.net
tibet.org.tw
tibetwrites.org
tncsec.gov.tw
tomayko.com
toutfr.com
transgressionism.org
travelinlocal.com
trendsmap.com
trustedbi.com
tsquare.tv
tuanzt.com
tui.orzdream.com
turbobit.net
turbotwitter.com
tv-intros.com
tv.com
tvunetworks.com
tw.news.yahoo.com
twa.sh
twbbs.org
tweepguide.com
tweeplike.me
tweete.net
tweetmeme.com
tweetree.com
tweetwally.com
twibase.com
twibs.com
twifan.com
twiffo.com
twimbow.com
twistar.cc
twisternow.com
twit2d.com
twitlonger.com
twitoaster.com
twitonmsn.com
twitpic.com
twitstat.com
twitter.jp
twittergadget.com
twitthat.com
twiyia.com
twstar.net
twt.fm
twtr2src.ogaoga.org
twttr.com
twyac.org
ultravpn.fr
ultraxs.com
unholyknight.com
unknownspace.org
urlparser.com
us.to
usacn.com
usinfo.state.gov
usmc.mil
uwants.net
v70.us
veempiire.com
veoh.com
views.fm
vinniev.com
voachineseblog.com
waffle1999.com
wahas.com
wanderinghorse.net
wanfang.gov.tw
wangjinbo.org
web.pts.org.tw
web2project.net
webshots.com
weigegebyc.dreamhosters.com
weijingsheng.org
wengewang.com
wengewang.org
wenku.com
wenxuecity.com
wenyunchao.com
westca.com
wexiaobo.org
wezhiyong.org
wforum.com
whereiswerner.com
whyx.org
wiki.jqueryui.com
wiki.keso.cn
wiki.oauth.net
wiki.phonegap.com
wikimedia.org.mo
wikiwiki.jp
willw.net
wiredbytes.com
wlx.sowiki.net
woeser.com
woopie.jp
wordpress.com
worldjournal.com
wpoforum.com
wqyd.org
wuerkaixi.com
wufi.org.tw
wujie.net
wukangrui.net
www.freetibet.org
www.getyouram.com
www.kanzhongguo.com
www.macrovpn.com
www.mitbbs.com
www.moztw.org
www.powerpointninja.com
www.tv.com
www.vegorpedersen.com
www.voy.com
www.vpncup.com
www.wan-press.org
www.zaurus.org.uk
x365x.com
xiezhua.com
xinsheng.net
xizang-zhiye.org
xxxx.com.au
xys.dxiong.com
xys.org
yatsen.gov.tw
yegle.net
yidio.com
yilubbs.com
yipub.com
yong.hu
youmaker.com
youpai.org
your-freedom.net
yunchao.net
yyii.org
yzzk.com
zarias.com
zeutch.com
zh.pokerstrategy.com
zhao.jinhai.de
zhongmeng.org
zhufeng.me
zlib.net
zonaeuropa.com
zuihulu.net
zuo.la"""

for d in blockedDomainString.split("\n"):
    if len(d) > 0:
        gConfig["BLOCKED_DOMAINS"][d] = True

