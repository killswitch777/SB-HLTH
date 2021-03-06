# -*- coding: utf-8 -*-

from HELLTERHEAD import pyimgflip
import youtube_dl
from googletrans import Translator
from bs4 import BeautifulSoup
from pafy import pafy
import ffmpy
import goslate
import wikipedia
import shutil
import html5lib
from gtts import gTTS
from datetime import datetime
from datetime import timedelta, date
import urllib.error
import urllib.parse
import urllib.request
import pytz
import ast
import six
import subprocess
import requests
import os
import string
import re
import glob
import threading
import codecs
import json
import sys
import random
import time
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
from akad.ttypes import ChatRoomAnnouncement
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ContentType as Type
from multiprocessing import Pool, Process
from thrift import transport, protocol, server
from thrift.TRecursive import *
from thrift.TSerialization import *
from thrift.TMultiplexedProcessor import *
from thrift.unverting import *
from akad.ttypes import *
from selfbot.ttypes import *
from HELLTERHEAD import *
import HELLTERHEAD

# cl = LineClient()
cl = LineClient(
    authToken=""
)
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl, cl.server.CHANNEL_ID["LINE_TIMELINE"])
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

# ki = LineClient()
ki = LineClient(
    authToken=""
)
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki, ki.server.CHANNEL_ID["LINE_TIMELINE"])
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

# kk= LineClient()
kk = LineClient(
    authToken=""
)
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk, kk.server.CHANNEL_ID["LINE_TIMELINE"])
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))

# kc = LineClient()
kc = LineClient(
    authToken=""
)
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc, kc.server.CHANNEL_ID["LINE_TIMELINE"])
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))

# sw = LineClient()
sw = LineClient(
    authToken=""
)
sw.log("Auth Token : " + str(sw.authToken))
channel4 = LineChannel(sw, sw.server.CHANNEL_ID["LINE_TIMELINE"])
sw.log("Channel Access Token : " + str(channel4.channelAccessToken))
print("\n\n𐀀 HELLTERHEAD IS READY❗\n\n")

poll = LinePoll(cl)
call = cl
creator = [""]
owner = [""]
admin = [""]
staff = [""]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl, ki, kk, kc]
ABC = [cl, ki, kk, kc]
ghost = [sw]
Bots = [mid, Amid, Bmid, Cmid, Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []
left = []
msg_dict = {}
msg_dict1 = {}

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = sw.getProfile().displayName

settings = {
    "Picture": False,
    "group": {},
    "SpamInvite": False,
    "changeCover": False,
    "changeVideo": False,
    "groupPicture": False,
    "changePicture": False,
    "autoJoinTicket": False,
    "restartPoint": True,
    "userMention": {},
    "timeRestart": {},
    "server": {},
    "simiSimi": {},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
    ],
}

wait = {
    "Limit": 1,
    "Members": 1,
    "owner": {},
    "admin": {},
    "addadmin": False,
    "delladmin": False,
    "staff": {},
    "addstaff": False,
    "dellstaff": False,
    "bots": {},
    "addbots": False,
    "dellbots": False,
    "blacklist": {},
    "wblacklist": False,
    "dblacklist": False,
    "Talkblacklist": {},
    "Talkwblacklist": False,
    "Talkdblacklist": False,
    "talkban": False,
    "contact": False,
    "invite": False,
    "unsend": False,
    "qr": True,
    "ghost": True,
    "lang":"JP",
    "autoJoin": True,
    "autoAdd": False,
    "autoBlock": False,
    "autoRead": True,
    "Timeline": False,
    "autoLeave": False,
    "autoLeave1": False,
    "detectMention": False,
    "mentionKick": False,
    "welcomeOn": False,
    "likeOn": False,
    "stickerOn": False,
    "Addsticker": {"name": "", "status": False},
    "stk": {},
    "selfbot": True,
    "Images": {},
    "Img": {},
    "Videos": {},
    "Addimage": {"name": "", "status": False},
    "Addaudio": {"name": "", "status": False},
    "Addvideo": {"name": "", "status": False},
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": "",
    },
    "mention": "reading...",
    "Respontag": "Yes, me!",
    "welcome": "welcome",
    "leave": "thanks for join, see you next time",
    "comment": "𐀀 HELLTERHEAD\nもばんづ\nJust other people.\nIllustrator / Graphic Designer\nEast Java - ID\n\nline.me/ti/p/~mo-banzu",
    "message": "Thanks for invite, let's be friend",
}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {},
}

cctv = {
    "cyduk": {},
    "point": {},
    "sidermem": {}
}

coverId = {}

# wait["myProfile"]["displayName"] = lineProfile.displayName
# wait["myProfile"]["statusMessage"] = lineProfile.statusMessage
# wait["myProfile"]["pictureStatus"] = lineProfile.pictureStatus
# wait["myProfile"]["coverId"] = lineProfile.getProfileId

lineProfile = cl.getProfile()
backup = cl.getProfile()
backup.displayName = lineProfile.displayName
backup.statusMessage = lineProfile.statusMessage
backup.pictureStatus = lineProfile.pictureStatus
# backup.coverld = lineProfile.coverld
# backup.coverId = lineProfile.getProfileDetail

with open("creator.json", "r") as fp:
    creator = json.load(fp)
with open("owner.json", "r") as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json", "r", "utf-8")
imagesOpen = codecs.open("image.json", "r", "utf-8")
videosOpen = codecs.open("video.json", "r", "utf-8")
stickersOpen = codecs.open("sticker.json", "r", "utf-8")
audiosOpen = codecs.open("audio.json", "r", "utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)


def restartBot():
    print("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)


def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow, "(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = [
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember",
    ]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime("%A")
    bln = inihari.strftime("%m")
    for i in range(len(day)):
        if hr == day[i]:
            hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k):
            bln = bulan[k - 1]
    time = "{}, {} - {} - {} | {}".format(
        str(hasil),
        str(inihari.strftime("%d")),
        str(bln),
        str(inihari.strftime("%Y")),
        str(inihari.strftime("%H:%M:%S")),
    )
    with open("logError.txt", "a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))


def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (
            datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])
        ) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]


def download_page(url):
    version = (3, 0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib
        import request

        try:
            headers = {}
            headers[
                "User-Agent"
            ] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib, request.Request(url, headers=headers)
            resp = urllib, request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2

        try:
            headers = {}
            headers[
                "User-Agent"
            ] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except BaseException:
            return "Page Not found"


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items


def waktu(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    month, days = divmod(days,30)
    year, month = divmod(month,12)
    century, year = divmod(year,100)
    return "'\n%02d Abad\n%02d Tahun\n%02d Bulan \n%02d Hari \n%02d Jam \n%02d Menit \n%02d Detik" % (century, year, month, days, hours, mins, secs)


def speedtest(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    if days == 0:
        return "%00d" % (secs)
    elif days > 0 and weaks == 0:
        return "%00d" % (secs)
    elif days > 0 and weaks > 0:
        return "%00d" % (secs)


def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            client.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)


def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"]:
                if time.time() - temp_flood[tmp]["time"] >= 3 * 10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        cl.sendMessage(tmp, "Bot kembali aktif")
                    except Exception as error:
                        logError(error)


def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {"file": open(vids, "rb")}
        obs_params = cl.genOBSParams(
            {"oid": mid, "ver": "2.0", "type": "video", "cat": "vp.mp4"}
        )
        data = {"params": obs_params}
        r_vp = cl.server.postContent(
            "{}/talk/vp/upload.nhn".format(str(cl.server.LINE_OBS_DOMAIN)),
            data=data,
            files=files,
        )
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, "vp")
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))


def changeProfileVideo(to):
    if settings["changeProfileVideo"]["picture"] is None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings["changeProfileVideo"]["video"] is None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings["changeProfileVideo"]["video"]
        files = {"file": open(path, "rb")}
        obs_params = cl.genOBSParams(
            {"oid": cl.getProfile().mid, "ver": "2.0", "type": "video", "cat": "vp.mp4"}
        )
        data = {"params": obs_params}
        r_vp = cl.server.postContent(
            "{}/talk/vp/upload.nhn".format(str(cl.server.LINE_OBS_DOMAIN)),
            data=data,
            files=files,
        )
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Failed update profile")
        path_p = settings["changeProfileVideo"]["picture"]
        settings["changeProfileVideo"]["status"] = False
        cl.updateProfilePicture(path_p, "vp")


def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile is None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = (
            contact.displayName,
            contact.statusMessage,
        )
        cl.updateProfile(profile)
        pict = cl.downloadFileURL(
            "http://dl.profile.line-cdn.net/" + contact.pictureStatus,
            saveAs="tmp/pict.bin",
        )
        vids = cl.downloadFileURL(
            "http://dl.profile.line-cdn.net/" + contact.pictureStatus + "/vp",
            saveAs="tmp/video.bin",
        )
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)["result"]["objectId"]
    cl.updateProfileCoverById(coverId)


def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings["myProfile"]["displayName"]
    profile.statusMessage = settings["myProfile"]["statusMessage"]
    if settings["myProfile"]["videoProfile"] is None:
        profile.pictureStatus = settings["myProfile"]["pictureStatus"]
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL(
            "http://dl.profile.line-cdn.net/" + settings["myProfile"]["pictureStatus"],
            saveAs="tmp/pict.bin",
        )
        vids = cl.downloadFileURL(
            "http://dl.profile.line-cdn.net/"
            + settings["myProfile"]["pictureStatus"]
            + "/vp",
            saveAs="tmp/video.bin",
        )
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings["myProfile"]["coverId"]
    cl.updateProfileCoverById(coverId)


def backupProfile():
    profile = cl.getContact(mid)
    settings["myProfile"]["displayName"] = profile.displayName
    settings["myProfile"]["pictureStatus"] = profile.pictureStatus
    settings["myProfile"]["statusMessage"] = profile.statusMessage
    settings["myProfile"]["videoProfile"] = profile.videoProfile
    coverId = cl.getProfileDetail()["result"]["objectId"]
    settings["myProfile"]["coverId"] = str(coverId)


def sendAudioWithURL(self, to_, url):
    path = self.downloadFileWithURL(url)
    try:
        self.sendAudio(to_, path)
    except Exception as e:
        raise Exception(e)


def sendAudioWithUrl(self, to_, url):
    path = "%s/pythonLine-%1.data" % (tempfile.gettempdir(), randint(0, 9))
    r = requests.get(url, stream=True, verify=False)
    if r.status_code == 200:
        with open(path, "w") as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception("Download audio failure.")
    try:
        self.sendAudio(to_, path)
    except Exception as e:
        raise Exception(e)


def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "「 List Member 」\n\n1. "
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num = num + 1
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except BaseException:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(
            to, textx, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "User ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention + wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num = num + 1
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except BaseException:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(
            to, textx, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hi ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention + wait["welcome"] + " to " + str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num = num + 1
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except BaseException:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(
            to, textx, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Bye ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention + wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num = num + 1
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except BaseException:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(
            to, textx, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " % (str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {"S": slen, "E": elen, "M": mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime()
        hari = str(future - today)
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += (
            mention
            + "\n• Time: "
            + datetime.strftime(timeNow, "%H:%M:%S")
            + " WIB\n• Group: "
            + str(len(gid))
            + "\n• Friends: "
            + str(len(teman))
            + "\n• Expired: In "
            + hari
            + "\n•Version: HELLTERHEAD PRO\n• Date: "
            + datetime.strftime(timeNow, "%Y-%m-%d")
            + "\n• Runtime: \n • "
            + bot
        )
        cl.sendMessage(
            to, text, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " % (str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {"S": slen, "E": elen, "M": mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(
            to, text, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention1(to, Amid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " % (str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {"S": slen, "E": elen, "M": mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(
            to, text, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention1(to, Bmid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " % (str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {"S": slen, "E": elen, "M": mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kk.sendMessage(
            to, text, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        kk.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention1(to, Cmid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " % (str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {"S": slen, "E": elen, "M": mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kc.sendMessage(
            to, text, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        kc.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention1(to, Zmid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " % (str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {"S": slen, "E": elen, "M": mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        sw.sendMessage(
            to, text, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
        )
    except Exception as error:
        sw.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"], "")
    else:
        cmd = "command"
    return cmd


# message.createdTime -> 00:00:00


def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[: len(str(unixtime)) - 3]))


def dt_to_str(dt):
    return dt.strftime("%H:%M:%S")


# delete log if pass more than 24 hours


def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (
            datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])
        ) > datetime.timedelta(1):
            del msg_dict1[msg_id]


def atend():
    print("Saving")
    with open("Log_data.json", "w", encoding="utf8") as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4, separators=(",", ": "))
    print("Save")


def atend1():
    print("Saving")
    with open("Log_data.json", "w", encoding="utf8") as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4, separators=(",", ": "))
    print("Save")


def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = (
        "「 HELP 」\n\n"
        + "「 COMMAND 」\n"
        + "• "
        + key
        + "Help\n"
        + "• "
        + key
        + "Help1\n"
        + "• "
        + key
        + "Help2\n"
        + "• "
        + key
        + "Help3\n"
        + "• "
        + key
        + "Me\n"
        + "• "
        + key
        + "Status\n"
        + "• "
        + key
        + "About\n"
        + "• "
        + key
        + "Kibar\n"
        + "• "
        + key
        + "Revive\n"
        + "• "
        + key
        + "!In\n"
        + "• "
        + key
        + "!Out\n"
        + "• "
        + key
        + "?Bye\n\n"
        + "「 PROTECT 」\n"
        + "• "
        + key
        + "Antijs stay\n"
        + "• "
        + key
        + "Ghost [in/out]\n"
        + "• "
        + key
        + "Hlth\n"
        + "• "
        + key
        + "Hlth!\n"
        + "• "
        + key
        + "Reinvite\n"
        + "• "
        + key
        + "Blacklist/blc\n"
        + "• "
        + key
        + "Blacklist @\n"
        + "• "
        + key
        + "Ban:on [contact]\n"
        + "• "
        + key
        + "Talkban:on [contact]\n"
        + "• "
        + key
        + "Unan:on [contact]\n"
        + "• "
        + key
        + "Untalkban:on [contact]\n"
        + "• "
        + key
        + "Banlist\n"
        + "• "
        + key
        + "Talkbanlist\n"
        + "• "
        + key
        + "Clearban/clb\n"
        + "• "
        + key
        + "Protectkick [on/off]\n"
        + "• "
        + key
        + "Protectjoin [on/off]\n"
        + "• "
        + key
        + "Protectinvite [on/off]\n"
        + "• "
        + key
        + "Protecturl [on/off]\n"
        + "• "
        + key
        + "Ghost [on/off]\n"
        + "• "
        + key
        + "Antijs [on/off]\n"
        + "• "
        + key
        + "Protectall [on/off]\n"
        + "• "
        + key
        + "Listprotect\n\n"
        + "「 BOT UPDATE 」\n"
        + "• "
        + key
        + "Bot[number]pict\n"
        + "• "
        + key
        + "Bot[number]name: [query]\n"
        + "• "
        + key
        + "Sprespon\n"
        + "• "
        + key
        + "Runtime\n"
        + "• "
        + key
        + "Rtime\n"
        + "• "
        + key
        + "Creator\n"
        + "• "
        + key
        + "Speed/sp\n"
        + "• "
        + key
        + "Broadcast:/bc: [text]\n"
        + "• "
        + key
        + "Setkey: [new key]\n"
        + "• "
        + key
        + "Mykey\n"
        + "• "
        + key
        + "Resetkey\n"
        + "• "
        + key
        + "Refresh\n"
        + "• "
        + key
        + "Restart\n"
        + "• "
        + key
        + "Self [on/off]\n\n"
        + "• By : DRE❗"
    )

    return helpMessage


def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = (
        "「 HELP-1 」\n\n"
        + "「 COMMAND 」\n"
        + "• "
        + key
        + "Tagall / Mention\n"
        + "• "
        + key
        + "Ginfo\n"
        + "• "
        + key
        + "Ginfo: [number]\n"
        + "• "
        + key
        + "Open\n"
        + "• "
        + key
        + "Open: [number]\n"
        + "• "
        + key
        + "Close\n"
        + "• "
        + key
        + "Close: [number]\n"
        + "• "
        + key
        + "Url\n"
        + "• "
        + key
        + "Grouplist\n"
        + "• "
        + key
        + "Grouplist[number]\n"
        + "• "
        + key
        + "Kibar\n"
        + "• "
        + key
        + "Absen\n"
        + "• "
        + key
        + "Respon\n\n"
        + "「 SAINT 」\n"
        + "• "
        + key
        + "Adminadd @ / Admindell @\n"
        + "• "
        + key
        + "Staffadd @ / Staffdell @\n"
        + "• "
        + key
        + "Botadd @ / Botdell @\n"
        + "• "
        + key
        + "Admin:on [contact]\n"
        + "• "
        + key
        + "Staff:on [contact]\n"
        + "• "
        + key
        + "Bot:on [contact]\n"
        + "• "
        + key
        + "Admin:repeat [contact]\n"
        + "• "
        + key
        + "Staff:repeat [contact]\n"
        + "• "
        + key
        + "Bot:repeat [contact]\n"
        + "• "
        + key
        + "Listadmin\n"
        + "• "
        + key
        + "Liststaff\n"
        + "• "
        + key
        + "Listbot\n"
        + "• "
        + key
        + "Contact admin\n"
        + "• "
        + key
        + "Contact staff\n"
        + "• "
        + key
        + "Contact bot\n\n"
        + "「 KEY 」\n"
        + "• "
        + key
        + "!Remove chat\n"
        + "• "
        + key
        + "?Remove chat\n"
        + "• "
        + key
        + "Mid @\n"
        + "• "
        + key
        + "Steal @\n"
        + "• "
        + key
        + "Cover @\n"
        + "• "
        + key
        + "Clone @\n"
        + "• "
        + key
        + "Restore\n"
        + "• "
        + key
        + "Backup\n"
        + "• "
        + key
        + "Myname: [nama]\n"
        + "• "
        + key
        + "Cpp [kirim foto]\n"
        + "• "
        + key
        + "Cvp [kirim video]\n"
        + "• "
        + key
        + "Updategroup\n"
        + "• "
        + key
        + "Reject\n\n"
        + "「 SPAM 」\n"
        + "• "
        + key
        + "Spamcallto @\n"
        + "• "
        + key
        + "Spamtag: [jumlah]\n"
        + "• "
        + key
        + "Spamtag @\n"
        + "• "
        + key
        + "Spamcall: [jumlah]\n"
        + "• "
        + key
        + "Spamcall\n"
        + "• "
        + key
        + "Gift: [mid] [jumlah]\n"
        + "• "
        + key
        + "Spam: [mid] [jumlah]\n\n"
        + "• By : DRE❗"
    )

    return helpMessage1


def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = (
        "「 HELP-2 」\n\n"
        + "「 STATUS 」\n"
        + "• "
        + key
        + "Invite [on/off]\n"
        + "• "
        + key
        + "Sticker [on/off]\n"
        + "• "
        + key
        + "Unsend [on/off]\n"
        + "• "
        + key
        + "Sider [on/off]\n"
        + "• "
        + key
        + "Respon [on/off]\n"
        + "• "
        + key
        + "Timeline [on/off]\n"
        + "• "
        + key
        + "Contact [on/off]\n"
        + "• "
        + key
        + "Autojoin [on/off]\n"
        + "• "
        + key
        + "Autoadd [on/off]\n"
        + "• "
        + key
        + "Welcome [on/off]\n"
        + "• "
        + key
        + "Autoleave [on/off]\n"
        + "• "
        + key
        + "Jointicket [on/off]\n\n"
        + "「 MESSAGE 」\n"
        + "• "
        + key
        + "Cek sider\n"
        + "• "
        + key
        + "Cek spam\n"
        + "• "
        + key
        + "Cek pesan\n"
        + "• "
        + key
        + "Cek respon\n"
        + "• "
        + key
        + "Cek leave\n"
        + "• "
        + key
        + "Cek welcome\n"
        + "• "
        + key
        + "Set sider: [text]\n"
        + "• "
        + key
        + "Set spam: [text]\n"
        + "• "
        + key
        + "Set pesan: [text]\n"
        + "• "
        + key
        + "Set respon: [text]\n"
        + "• "
        + key
        + "Set leave: [text]\n"
        + "• "
        + key
        + "Set welcome: [text]\n\n"
        + "「 KICKER 」\n"
        + "• "
        + key
        + "Kick! @\n"
        + "• "
        + key
        + "Kill! @\n"
        + "• "
        + key
        + "!Kick (all)\n"
        + "• "
        + key
        + "!Bye (all)\n"
        + "• "
        + key
        + "!Kibar\n\n"
        + "• By : DRE❗"
    )

    return helpMessage2


def help3():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = (
        "「 HELP-3 」\n\n"
        + "「 MUSIC 」\n"
        + "• "
        + key
        + "Listmp3\n"
        + "• "
        + key
        + "Addmp3 [Teks]\n"
        + "• "
        + key
        + "Dellmp3 [Teks]\n\n"
        + "「 VIDEO 」\n"
        + "• "
        + key
        + "Listvideo\n"
        + "• "
        + key
        + "Addvideo [Teks]\n"
        + "• "
        + key
        + "Dellvideo [Teks]\n\n"
        + "「 IMAGE 」\n"
        + "• "
        + key
        + "Listimage\n"
        + "• "
        + key
        + "Addimage [Teks]\n"
        + "• "
        + key
        + "Dellimage [Teks]\n\n"
        + "「 STICKER 」\n"
        + "• "
        + key
        + "Liststicker\n"
        + "• "
        + key
        + "Addsticker [Teks]\n"
        + "• "
        + key
        + "Dellsticker [Teks]\n\n"
        + "「 MEDIA 」\n"
        + "• "
        + key
        + "Kode wilayah\n"
        + "• "
        + key
        + "Cctv: [Kode Wilayah CCTV]\n"
        + "• "
        + key
        + "Youtube: [Query]\n"
        + "• "
        + key
        + "Fansign: [Query]\n"
        + "• "
        + key
        + "Line: [ID Line]\n"
        + "• "
        + key
        + "Apk: [Query]\n"
        + "• "
        + key
        + "Gif: [Query]\n"
        + "• "
        + key
        + "Anime: [Query]\n"
        + "• "
        + key
        + "Music: [Query]\n"
        + "• "
        + key
        + "Mp3: [Query]\n"
        + "• "
        + key
        + "Video: [Query]\n"
        + "• "
        + key
        + "Bintang: [Zodiak]\n"
        + "• "
        + key
        + "Zodiak: [Zodiak]\n"
        + "• "
        + key
        + "Cuaca: [Nama Kota]\n"
        + "• "
        + key
        + "Lokasi: [Nama Kota]\n"
        + "• "
        + key
        + "Lyric: [Judul Lagu]\n"
        + "• "
        + key
        + "Instagram: [User Name]\n"
        + "• "
        + key
        + "Ytmp3: [Query]\n"
        + "• "
        + key
        + "Ytmp4: [Query]\n"
        + "• "
        + key
        + "Birthday: [DD-MM-YYYY]\n\n"
        + "• By : DRE❗"
    )

    return helpMessage3


def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)

                return

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                            cl.updateGroup(X)
                            cl.sendMessage(
                                op.param1,
                                None,
                                contentMetadata={"mid": op.param2},
                                contentType=13,
                            )
                            cl.sendMessage(
                                op.param1,
                                "Don't open link QR group without permission!",
                            )
                except BaseException:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if (
                                op.param2 not in Bots
                                and op.param2 not in owner
                                and op.param2 not in admin
                                and op.param2 not in staff
                            ):
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                random.choice(ABC).kickoutFromGroup(
                                    op.param1, [op.param2]
                                )
                                ki.updateGroup(X)
                                ki.sendMessage(
                                    op.param1,
                                    None,
                                    contentMetadata={"mid": op.param2},
                                    contentType=13,
                                )
                                ki.sendMessage(
                                    op.param1,
                                    "Don't open link QR group without permission!",
                                )
                    except BaseException:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if (
                                    op.param2 not in Bots
                                    and op.param2 not in owner
                                    and op.param2 not in admin
                                    and op.param2 not in staff
                                ):
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    random.choice(ABC).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    kk.updateGroup(X)
                                    kk.sendMessage(
                                        op.param1,
                                        None,
                                        contentMetadata={"mid": op.param2},
                                        contentType=13,
                                    )
                                    kk.sendMessage(
                                        op.param1,
                                        "Don't open link QR group without permission!",
                                    )
                        except BaseException:
                            try:
                                if (
                                    kc.getGroup(op.param1).preventedJoinByTicket
                                    == False
                                ):
                                    if (
                                        op.param2 not in Bots
                                        and op.param2 not in owner
                                        and op.param2 not in admin
                                        and op.param2 not in staff
                                    ):
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        random.choice(ABC).kickoutFromGroup(
                                            op.param1, [op.param2]
                                        )
                                        kc.updateGroup(X)
                                        kc.sendMessage(
                                            op.param1,
                                            None,
                                            contentMetadata={"mid": op.param2},
                                            contentType=13,
                                        )
                                        kc.sendMessage(
                                            op.param1,
                                            "Don't open link QR group without permission!",
                                        )
                            except BaseException:
                                pass
            if op.type == 13:
                if mid in op.param3:
                    if wait["autoLeave"]:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)

            if op.type == 13:
                if mid in op.param3:
                    if wait["autoJoin"]:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1, "Don't invite without my commander!")
                        ki.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1, "Don't invite without my commander!")
                        kk.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1, "Don't invite without my commander!")
                        kc.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)

        if op.type == 13:
            if op.param1 in protectinvite:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                            random.choice(ABC).cancelGroupInvitation(op.param1, [_mid])
                            random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                            cl.sendMessage(
                                op.param1, "Don't invite without permission!"
                            )
                    except BaseException:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).kickoutFromGroup(
                                    op.param1, [op.param2]
                                )
                                random.choice(ABC).cancelGroupInvitation(
                                    op.param1, [_mid]
                                )
                                random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                                ki.sendMessage(
                                    op.param1, "Don't invite without permission!"
                                )
                        except BaseException:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(ABC).cancelGroupInvitation(
                                        op.param1, [_mid]
                                    )
                                    random.choice(KAC).inviteIntoGroup(
                                        op.param1, [Zmid]
                                    )
                                    kk.sendMessage(
                                        op.param1, "Don't invite without permission!"
                                    )
                            except BaseException:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [
                                        contact.mid for contact in group.invitee
                                    ]
                                    for _mid in gMembMids:
                                        random.choice(ABC).kickoutFromGroup(
                                            op.param1, [op.param2]
                                        )
                                        random.choice(ABC).cancelGroupInvitation(
                                            op.param1, [_mid]
                                        )
                                        random.choice(KAC).inviteIntoGroup(
                                            op.param1, [Zmid]
                                        )
                                        kc.sendMessage(
                                            op.param1,
                                            "Don't invite without permission!",
                                        )
                                except BaseException:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = "http://dl.profile.line.naver.jp" + contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                            cl.sendMessage(
                                op.param1,
                                "Sorry anyone can't join, protect join is actived",
                            )
                    except BaseException:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"]:
                cl.findAndAddContactsByMid(op.param1)
                sendMention(op.param1, "Hi ", "thanks for invite me!")
                cl.sendText(op.param1, wait["message"])
                cl.sendContact(op.param1, "u20452d2a7b27a3536e1172e4c8d0a8b4")

        if op.type == 19:
            if op.param1 in protectkick:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                    cl.sendMessage(op.param1, "Don't kick without permission!")
                else:
                    pass

        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                        sw.kickoutFromGroup(op.param1, [op.param2])
                        sw.sendMessage(
                            op.param1,
                            None,
                            contentMetadata={"mid": op.param2},
                            contentType=13,
                        )
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        cl.inviteIntoGroup(op.param1, [Zmid])
                        wait["blacklist"][op.param2] = True
                except BaseException:
                    try:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                            sw.kickoutFromGroup(op.param1, [op.param2])
                            sw.sendMessage(
                                op.param1,
                                None,
                                contentMetadata={"mid": op.param2},
                                contentType=13,
                            )
                            sw.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                            ki.inviteIntoGroup(op.param1, [Zmid])
                            wait["blacklist"][op.param2] = True
                    except BaseException:
                        try:
                            if (
                                op.param2 not in Bots
                                and op.param2 not in owner
                                and op.param2 not in admin
                                and op.param2 not in staff
                            ):
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                invsend = 0
                                Ticket = kk.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                                sw.kickoutFromGroup(op.param1, [op.param2])
                                sw.sendMessage(
                                    op.param1,
                                    None,
                                    contentMetadata={"mid": op.param2},
                                    contentType=13,
                                )
                                sw.leaveGroup(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kk.updateGroup(X)
                                kk.inviteIntoGroup(op.param1, [Zmid])
                                wait["blacklist"][op.param2] = True
                        except BaseException:
                            try:
                                if (
                                    op.param2 not in Bots
                                    and op.param2 not in owner
                                    and op.param2 not in admin
                                    and op.param2 not in staff
                                ):
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    invsend = 0
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    sw.kickoutFromGroup(op.param1, [op.param2])
                                    sw.sendMessage(
                                        op.param1,
                                        None,
                                        contentMetadata={"mid": op.param2},
                                        contentType=13,
                                    )
                                    sw.leaveGroup(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kc.updateGroup(X)
                                    kc.inviteIntoGroup(op.param1, [Zmid])
                                    wait["blacklist"][op.param2] = True
                            except BaseException:
                                pass

        if op.type == 19:
            if wait["ghost"]:
                try:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        G = random.choice(ABC).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(ABC).updateGroup(G)
                        Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                        sw.kickoutFromGroup(op.param1, [op.param2])
                        sw.sendMessage(
                            op.param1,
                            None,
                            contentMetadata={"mid": op.param2},
                            contentType=13,
                        )
                        sw.leaveGroup(op.param1)
                        X = random.choice(KAC).getGroup(op.param1)
                        random.choice(KAC).updateGroup(X)
                        X.preventedJoinByTicket = True
                        random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                        wait["blacklist"][op.param2] = True
                except BaseException:
                    pass

        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                    if op.param3 in mid:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            sw.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1, [op.param2])
                            G = sw.getGroup(op.param1)
                            G.preventJoinByTicket = False
                            sw.updateGroup(G)
                            Ticket = sw.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                            ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                            kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                            sw.kickoutFromGroup(op.param1, [op.param2])
                            G.preventJoinByTicket = True
                            sw.updateGroup(G)
                            wait["blacklist"][op.param2] = True
                            sw.leaveGroup(op.param1)
                            random.choice(KAC).findAndAddContactsByMid(
                                op.param1, [Zmid]
                            )
                            random.choice(KAC).findAndAddContactsByMid(
                                op.param1, [admin]
                            )
                            random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                            random.choice(KAC).inviteIntoGroup(op.param1, [admin])
                        else:
                            pass

                if op.param3 in Zmid:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                        random.choice(KAC).findAndAddContactsByMid(op.param3)
                        random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                        cl.sendMessage(op.param1, "Anti JS Invited")

                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                            random.choice(KAC).findAndAddContactsByMid(op.param3)
                            random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                            cl.sendMessage(op.param1, "Admin Invited")

                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    if op.param3 in staff:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                            random.choice(KAC).findAndAddContactsByMid(op.param3)
                            random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                            cl.sendMessage(op.param1, "Staff Invited")

                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    if op.param3 in Bots:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                            random.choice(KAC).findAndAddContactsByMid(op.param3)
                            random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                            cl.sendMessage(op.param1, "Bot Invited")
                else:
                    pass
            except BaseException:
                pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                            cl.sendMessage(
                                op.param1,
                                "Don't cancel pending member without permission!",
                            )
                    except BaseException:
                        pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1, [op.param2])
                        ki.inviteIntoGroup(op.param1, [mid, Bmid, Cmid])
                        cl.acceptGroupInvitation(op.param1)
                        kk.acceptGrouoInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            kk.kickoutFromGroup(op.param1, [op.param2])
                            kk.inviteIntoGroup(op.param1, [mid, Amid, Cmid])
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                        except BaseException:
                            try:
                                kc.kickoutFromGroup(op.param1, [op.param2])
                                kc.inviteIntoGroup(op.param1, [mid, Amid, Bmid])
                                cl.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.chaoice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                except BaseException:
                                    try:
                                        ki.kickoutFromGroup(op.param1, [op.param2])
                                        ki.inviteIntoGroup(op.param1, [mid, Bmid, Cmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        random.choice(KAC).inviteIntoGroup(
                                            op.param1, [Zmid]
                                        )
                                    except BaseException:
                                        try:
                                            kk.kickoutFromGroup(op.param1, [op.param2])
                                            kk.inviteIntoGroup(
                                                op.param1, [mid, Amid, Cmid]
                                            )
                                            cl.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                            random.choice(KAC).inviteIntoGroup(
                                                op.param1, [Zmid]
                                            )
                                        except BaseException:
                                            try:
                                                kc.kickoutFromGroup(
                                                    op.param1, [op.param2]
                                                )
                                                kc.inviteIntoGroup(
                                                    op.param1, [mid, Amid, Bmid]
                                                )
                                                cl.acceptGroupInvitation(op.param1)
                                                ki.acceptGroupInvitation(op.param1)
                                                kk.acceptGroupInvitation(op.param1)
                                                random.choice(KAC).inviteIntoGroup(
                                                    op.param1, [Zmid]
                                                )
                                            except BaseException:
                                                try:
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = False
                                                    random.choice(ABC).kickoutFromGroup(
                                                        op.param1, [op.param2]
                                                    )
                                                    random.choice(ABC).updateGroup(G)
                                                    Ticket = random.choice(
                                                        ABC
                                                    ).reissueGroupTicket(op.param1)
                                                    cl.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    ki.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kk.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kc.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = True
                                                    random.choice(ABC).updateGroup(G)
                                                    Ticket = random.choice(
                                                        ABC
                                                    ).reissueGroupTicket(op.param1)
                                                except BaseException:
                                                    try:
                                                        ki.kickoutFromGroup(
                                                            op.param1, [op.param2]
                                                        )
                                                        ki.inviteIntoGroup(
                                                            op.param1, [mid, Bmid, Cmid]
                                                        )
                                                        cl.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        kk.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        kc.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        random.choice(
                                                            KAC
                                                        ).inviteIntoGroup(
                                                            op.param1, [Zmid]
                                                        )
                                                    except BaseException:
                                                        try:
                                                            kk.kickoutFromGroup(
                                                                op.param1, [op.param2]
                                                            )
                                                            kk.inviteIntoGroup(
                                                                op.param1,
                                                                [mid, Amid, Cmid],
                                                            )
                                                            cl.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            ki.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            kc.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            random.choice(
                                                                KAC
                                                            ).inviteIntoGroup(
                                                                op.param1, [Zmid]
                                                            )
                                                        except BaseException:
                                                            try:
                                                                kc.kickoutFromGroup(
                                                                    op.param1,
                                                                    [op.param2],
                                                                )
                                                                kc.inviteIntoGroup(
                                                                    op.param1,
                                                                    [mid, Amid, Bmid],
                                                                )
                                                                cl.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                ki.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                kk.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                random.choice(
                                                                    KAC
                                                                ).inviteIntoGroup(
                                                                    op.param1, [Zmid]
                                                                )
                                                            except BaseException:
                                                                try:
                                                                    G = random.choice(
                                                                        ABC
                                                                    ).getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        False
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).kickoutFromGroup(
                                                                        op.param1,
                                                                        [op.param2],
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                    cl.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    ki.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kk.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kc.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    G = random.choice(
                                                                        ABC
                                                                    ).getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        True
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                except BaseException:
                                                                    try:
                                                                        ki.kickoutFromGroup(
                                                                            op.param1,
                                                                            [op.param2],
                                                                        )
                                                                        ki.inviteIntoGroup(
                                                                            op.param1,
                                                                            [
                                                                                mid,
                                                                                Bmid,
                                                                                Cmid,
                                                                            ],
                                                                        )
                                                                        cl.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        kk.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        kc.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        random.choice(
                                                                            KAC
                                                                        ).inviteIntoGroup(
                                                                            op.param1,
                                                                            [Zmid],
                                                                        )
                                                                    except BaseException:
                                                                        try:
                                                                            kk.kickoutFromGroup(
                                                                                op.param1,
                                                                                [
                                                                                    op.param2
                                                                                ],
                                                                            )
                                                                            kk.inviteIntoGroup(
                                                                                op.param1,
                                                                                [
                                                                                    mid,
                                                                                    Amid,
                                                                                    Cmid,
                                                                                ],
                                                                            )
                                                                            cl.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            ki.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            kc.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            random.choice(
                                                                                KAC
                                                                            ).inviteIntoGroup(
                                                                                op.param1,
                                                                                [Zmid],
                                                                            )
                                                                        except BaseException:
                                                                            try:
                                                                                kc.kickoutFromGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        op.param2
                                                                                    ],
                                                                                )
                                                                                kc.inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        mid,
                                                                                        Amid,
                                                                                        Bmid,
                                                                                    ],
                                                                                )
                                                                                cl.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                ki.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                kk.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                random.choice(
                                                                                    KAC
                                                                                ).inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        Zmid
                                                                                    ],
                                                                                )
                                                                            except BaseException:
                                                                                pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1, [op.param2])
                        kk.inviteIntoGroup(op.param1, [Amid, mid, Cmid])
                        ki.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            kc.kickoutFromGroup(op.param1, [op.param2])
                            kc.inviteIntoGroup(op.param1, [Amid, mid, Bmid])
                            ki.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                        except BaseException:
                            try:
                                cl.kickoutFromGroup(op.param1, [op.param2])
                                cl.inviteIntoGroup(op.param1, [Amid, Bmid, Cmid])
                                ki.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    G = kLrandom.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                except BaseException:
                                    try:
                                        kk.kickoutFromGroup(op.param1, [op.param2])
                                        kk.inviteIntoGroup(op.param1, [Amid, mid, Cmid])
                                        ki.acceptGroupInvitation(op.param1)
                                        cl.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        random.choice(KAC).inviteIntoGroup(
                                            op.param1, [Zmid]
                                        )
                                    except BaseException:
                                        try:
                                            kc.kickoutFromGroup(op.param1, [op.param2])
                                            kc.inviteIntoGroup(
                                                op.param1, [Amid, mid, Bmid]
                                            )
                                            ki.acceptGroupInvitation(op.param1)
                                            cl.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            random.choice(KAC).inviteIntoGroup(
                                                op.param1, [Zmid]
                                            )
                                        except BaseException:
                                            try:
                                                cl.kickoutFromGroup(
                                                    op.param1, [op.param2]
                                                )
                                                cl.inviteIntoGroup(
                                                    op.param1, [Amid, Bmid, Cmid]
                                                )
                                                ki.acceptGroupInvitation(op.param1)
                                                kk.acceptGroupInvitation(op.param1)
                                                kc.acceptGroupInvitation(op.param1)
                                                random.choice(KAC).inviteIntoGroup(
                                                    op.param1, [Zmid]
                                                )
                                            except BaseException:
                                                try:
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = False
                                                    random.choice(ABC).kickoutFromGroup(
                                                        op.param1, [op.param2]
                                                    )
                                                    kc.updateGroup(G)
                                                    Ticket = kc.reissueGroupTicket(
                                                        op.param1
                                                    )
                                                    cl.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    ki.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kk.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kc.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = True
                                                    random.choice(ABC).updateGroup(G)
                                                    Ticket = random.choice(
                                                        ABC
                                                    ).reissueGroupTicket(op.param1)
                                                except BaseException:
                                                    try:
                                                        kk.kickoutFromGroup(
                                                            op.param1, [op.param2]
                                                        )
                                                        kk.inviteIntoGroup(
                                                            op.param1, [Amid, mid, Cmid]
                                                        )
                                                        ki.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        cl.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        kc.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        random.choice(
                                                            KAC
                                                        ).inviteIntoGroup(
                                                            op.param1, [Zmid]
                                                        )
                                                    except BaseException:
                                                        try:
                                                            kc.kickoutFromGroup(
                                                                op.param1, [op.param2]
                                                            )
                                                            kc.inviteIntoGroup(
                                                                op.param1,
                                                                [Amid, mid, Bmid],
                                                            )
                                                            ki.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            cl.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            kk.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            random.choice(
                                                                KAC
                                                            ).inviteIntoGroup(
                                                                op.param1, [Zmid]
                                                            )
                                                        except BaseException:
                                                            try:
                                                                cl.kickoutFromGroup(
                                                                    op.param1,
                                                                    [op.param2],
                                                                )
                                                                cl.inviteIntoGroup(
                                                                    op.param1,
                                                                    [Amid, Bmid, Cmid],
                                                                )
                                                                ki.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                kk.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                kc.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                random.choice(
                                                                    KAC
                                                                ).inviteIntoGroup(
                                                                    op.param1, [Zmid]
                                                                )
                                                            except BaseException:
                                                                try:
                                                                    G = random.choice(
                                                                        ABC
                                                                    ).getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        False
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).kickoutFromGroup(
                                                                        op.param1,
                                                                        [op.param2],
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                    cl.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    ki.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kk.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kc.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    G = random.choice(
                                                                        ABC
                                                                    ).getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        True
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                except BaseException:
                                                                    try:
                                                                        kk.kickoutFromGroup(
                                                                            op.param1,
                                                                            [op.param2],
                                                                        )
                                                                        kk.inviteIntoGroup(
                                                                            op.param1,
                                                                            [
                                                                                Amid,
                                                                                mid,
                                                                                Cmid,
                                                                            ],
                                                                        )
                                                                        ki.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        cl.acceptGriupInvitation(
                                                                            op.param1
                                                                        )
                                                                        cl.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        random.choice(
                                                                            KAC
                                                                        ).inviteIntoGroup(
                                                                            op.param1,
                                                                            [Zmid],
                                                                        )
                                                                    except BaseException:
                                                                        try:
                                                                            kc.kickoutFromGroup(
                                                                                op.param1,
                                                                                [
                                                                                    op.param2
                                                                                ],
                                                                            )
                                                                            kc.inviteIntoGroup(
                                                                                op.param1,
                                                                                [
                                                                                    Amid,
                                                                                    mid,
                                                                                    Bmid,
                                                                                ],
                                                                            )
                                                                            ki.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            cl.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            kk.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            random.choice(
                                                                                KAC
                                                                            ).inviteIntoGroup(
                                                                                op.param1,
                                                                                [Zmid],
                                                                            )
                                                                        except BaseException:
                                                                            try:
                                                                                cl.kickoutFromGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        op.param2
                                                                                    ],
                                                                                )
                                                                                cl.inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        Amid,
                                                                                        Bmid,
                                                                                        Cmid,
                                                                                    ],
                                                                                )
                                                                                ki.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                kk.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                kc.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                random.choice(
                                                                                    KAC
                                                                                ).inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        Zmid
                                                                                    ],
                                                                                )
                                                                            except BaseException:
                                                                                pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1, [op.param2])
                        kc.inviteIntoGroup(op.param1, [Bmid, mid, Amid])
                        kk.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            cl.kickoutFromGroup(op.param1, [op.param2])
                            cl.inviteIntoGroup(op.param1, [Bmid, Amid, Cmid])
                            kk.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                        except BaseException:
                            try:
                                ki.kickoutFromGroup(op.param1, [op.param2])
                                ki.inviteIntoGroup(op.param1, [Bmid, mid, Cmid])
                                kk.acceptGroupInvitation(op.param1)
                                cl.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                except BaseException:
                                    try:
                                        ki.kickoutFromGroup(op.param1, [op.param2])
                                        ki.inviteIntoGroup(op.param1, [Bmid, mid, Cmid])
                                        kk.acceptGroupInvitation(op.param1)
                                        cl.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        random.choice(KAC).inviteIntoGroup(
                                            op.param1, [Zmid]
                                        )
                                    except BaseException:
                                        try:
                                            kc.kickoutFromGroup(op.param1, [op.param2])
                                            kc.inviteIntoGroup(
                                                op.param1, [Bmid, mid, Amid]
                                            )
                                            kk.acceptGroupInvitation(op.param1)
                                            cl.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            random.choice(KAC).inviteIntoGroup(
                                                op.param1, [Zmid]
                                            )
                                        except BaseException:
                                            try:
                                                cl.kickoutFromGroup(
                                                    op.param1, [op.param2]
                                                )
                                                cl.inviteIntoGroup(
                                                    op.param1, [Bmid, Amid, Cmid]
                                                )
                                                kk.acceptGroupInvitation(op.param1)
                                                ki.acceptGroupInvitation(op.param1)
                                                kc.acceptGroupInvitation(op.param1)
                                                random.choice(KAC).inviteIntoGroup(
                                                    op.param1, [Zmid]
                                                )
                                            except BaseException:
                                                try:
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = False
                                                    random.choice(ABC).kickoutFromGroup(
                                                        op.param1, [op.param2]
                                                    )
                                                    random.choice(ABC).updateGroup(G)
                                                    Ticket = random.choice(
                                                        ABC
                                                    ).reissueGroupTicket(op.param1)
                                                    cl.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    ki.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kk.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kc.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = True
                                                    random.choice(ABC).updateGroup(G)
                                                    Ticket = random.choice(
                                                        ABC
                                                    ).reissueGroupTicket(op.param1)
                                                except BaseException:
                                                    try:
                                                        ki.kickoutFromGroup(
                                                            op.param1, [op.param2]
                                                        )
                                                        ki.inviteIntoGroup(
                                                            op.param1, [Bmid, mid, Cmid]
                                                        )
                                                        kk.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        cl.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        kc.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        random.choice(
                                                            KAC
                                                        ).inviteIntoGroup(
                                                            op.param1, [Zmid]
                                                        )
                                                    except BaseException:
                                                        try:
                                                            kc.kickoutFromGroup(
                                                                op.param1, [op.param2]
                                                            )
                                                            kc.inviteIntoGroup(
                                                                op.param1,
                                                                [Bmid, mid, Amid],
                                                            )
                                                            kk.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            cl.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            ki.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            random.choice(
                                                                KAC
                                                            ).inviteIntoGroup(
                                                                op.param1, [Zmid]
                                                            )
                                                        except BaseException:
                                                            try:
                                                                cl.kickoutFromGroup(
                                                                    op.param1,
                                                                    [op.param2],
                                                                )
                                                                cl.inviteIntoGroup(
                                                                    op.param1,
                                                                    [Bmid, Amid, Cmid],
                                                                )
                                                                kk.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                ki.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                kc.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                random.choice(
                                                                    KAC
                                                                ).inviteIntoGroup(
                                                                    op.param1, [Zmid]
                                                                )
                                                            except BaseException:
                                                                try:
                                                                    G = random.choice(
                                                                        ABC
                                                                    ).getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        False
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).kickoutFromGroup(
                                                                        op.param1,
                                                                        [op.param2],
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                    cl.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    ki.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kk.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kc.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    random.choice(
                                                                        KAC
                                                                    ).inviteIntoGroup(
                                                                        op.param1,
                                                                        [Zmid],
                                                                    )
                                                                    G = ki.getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        True
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                except BaseException:
                                                                    try:
                                                                        ki.kickoutFromGroup(
                                                                            op.param1,
                                                                            [op.param2],
                                                                        )
                                                                        ki.inviteIntoGroup(
                                                                            op.param1,
                                                                            [
                                                                                Bmid,
                                                                                mid,
                                                                                Cmid,
                                                                            ],
                                                                        )
                                                                        kk.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        cl.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        kc.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        random.choice(
                                                                            KAC
                                                                        ).inviteIntoGroup(
                                                                            op.param1,
                                                                            [Zmid],
                                                                        )
                                                                    except BaseException:
                                                                        try:
                                                                            kc.kickoutFromGroup(
                                                                                op.param1,
                                                                                [
                                                                                    op.param2
                                                                                ],
                                                                            )
                                                                            kc.inviteIntoGroup(
                                                                                op.param1,
                                                                                [
                                                                                    Bmid,
                                                                                    mid,
                                                                                    Amid,
                                                                                ],
                                                                            )
                                                                            kk.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            cl.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            ki.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            random.choice(
                                                                                KAC
                                                                            ).inviteIntoGroup(
                                                                                op.param1,
                                                                                [Zmid],
                                                                            )
                                                                        except BaseException:
                                                                            try:
                                                                                cl.kickoutFromGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        op.param2
                                                                                    ],
                                                                                )
                                                                                cl.inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        Bmid,
                                                                                        Amid,
                                                                                        Cmid,
                                                                                    ],
                                                                                )
                                                                                kk.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                ki.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                kc.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                random.choice(
                                                                                    KAC
                                                                                ).inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        Zmid
                                                                                    ],
                                                                                )
                                                                            except BaseException:
                                                                                pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1, [op.param2])
                        cl.inviteIntoGroup(op.param1, [Cmid, Amid, Bmid])
                        kc.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            ki.kickoutFromGroup(op.param1, [op.param2])
                            ki.inviteIntoGroup(op.param1, [Cmid, mid, Bmid])
                            kc.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                        except BaseException:
                            try:
                                kk.kickoutFromGroup(op.param1, [op.param2])
                                kk.inviteIntoGroup(op.param1, [Cmid, mid, Amid])
                                kc.acceptGroupInvitation(op.param1)
                                cl.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                random.choice(KAC).inviteIntoGroup(op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(
                                        op.param1
                                    )
                                except BaseException:
                                    try:
                                        cl.kickoutFromGroup(op.param1, [op.param2])
                                        cl.inviteIntoGroup(
                                            op.param1, [Cmid, Amid, Bmid]
                                        )
                                        kc.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        random.choice(KAC).inviteIntoGroup(
                                            op.param1, [Zmid]
                                        )
                                    except BaseException:
                                        try:
                                            ki.kickoutFromGroup(op.param1, [op.param2])
                                            ki.inviteIntoGroup(
                                                op.param1, [Cmid, mid, Bmid]
                                            )
                                            kc.acceptGroupInvitation(op.param1)
                                            cl.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            random.choice(KAC).inviteIntoGroup(
                                                op.param1, [Zmid]
                                            )
                                        except BaseException:
                                            try:
                                                kk.kickoutFromGroup(
                                                    op.param1, [op.param2]
                                                )
                                                kk.inviteIntoGroup(
                                                    op.param1, [Cmid, mid, Amid]
                                                )
                                                kc.acceptGroupInvitation(op.param1)
                                                cl.acceptGroupInvitation(op.param1)
                                                ki.acceptGroupInvitation(op.param1)
                                                random.choice(KAC).inviteIntoGroup(
                                                    op.param1, [Zmid]
                                                )
                                            except BaseException:
                                                try:
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = False
                                                    random.choice(ABC).kickoutFromGroup(
                                                        op.param1, [op.param2]
                                                    )
                                                    random.choice(ABC).updateGroup(G)
                                                    Ticket = random.choice(
                                                        ABC
                                                    ).reissueGroupTicket(op.param1)
                                                    cl.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    ki.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kk.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    kc.acceptGroupInvitationByTicket(
                                                        op.param1, Ticket
                                                    )
                                                    G = random.choice(ABC).getGroup(
                                                        op.param1
                                                    )
                                                    G.preventedJoinByTicket = True
                                                    random.choice(ABC).updateGroup(G)
                                                    Ticket = random.choice(
                                                        ABC
                                                    ).reissueGroupTicket(op.param1)
                                                except BaseException:
                                                    try:
                                                        cl.kickoutFromGroup(
                                                            op.param1, [op.param2]
                                                        )
                                                        cl.inviteIntoGroup(
                                                            op.param1,
                                                            [Cmid, Amid, Bmid],
                                                        )
                                                        kc.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        ki.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        kk.acceptGroupInvitation(
                                                            op.param1
                                                        )
                                                        random.choice(
                                                            KAC
                                                        ).inviteIntoGroup(
                                                            op.param1, [Zmid]
                                                        )
                                                    except BaseException:
                                                        try:
                                                            ki.kickoutFromGroup(
                                                                op.param1, [op.param2]
                                                            )
                                                            ki.inviteIntoGroup(
                                                                op.param1,
                                                                [Cmid, mid, Bmid],
                                                            )
                                                            kc.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            cl.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            kk.acceptGroupInvitation(
                                                                op.param1
                                                            )
                                                            random.choice(
                                                                KAC
                                                            ).inviteIntoGroup(
                                                                op.param1, [Zmid]
                                                            )
                                                        except BaseException:
                                                            try:
                                                                kk.kickoutFromGroup(
                                                                    op.param1,
                                                                    [op.param2],
                                                                )
                                                                kk.inviteIntoGroup(
                                                                    op.param1,
                                                                    [Cmid, mid, Amid],
                                                                )
                                                                kc.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                cl.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                ki.acceptGroupInvitation(
                                                                    op.param1
                                                                )
                                                                random.choice(
                                                                    KAC
                                                                ).inviteIntoGroup(
                                                                    op.param1, [Zmid]
                                                                )
                                                            except BaseException:
                                                                try:
                                                                    G = random.choice(
                                                                        ABC
                                                                    ).getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        False
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).kickoutFromGroup(
                                                                        op.param1,
                                                                        [op.param2],
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                    cl.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    ki.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kk.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    kc.acceptGroupInvitationByTicket(
                                                                        op.param1,
                                                                        Ticket,
                                                                    )
                                                                    G = random.choice(
                                                                        ABC
                                                                    ).getGroup(
                                                                        op.param1
                                                                    )
                                                                    G.preventedJoinByTicket = (
                                                                        True
                                                                    )
                                                                    random.choice(
                                                                        ABC
                                                                    ).updateGroup(G)
                                                                    Ticket = random.choice(
                                                                        ABC
                                                                    ).reissueGroupTicket(
                                                                        op.param1
                                                                    )
                                                                except BaseException:
                                                                    try:
                                                                        cl.kickoutFromGroup(
                                                                            op.param1,
                                                                            [op.param2],
                                                                        )
                                                                        cl.inviteIntoGroup(
                                                                            op.param1,
                                                                            [
                                                                                Cmid,
                                                                                Amid,
                                                                                Bmid,
                                                                            ],
                                                                        )
                                                                        kc.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        ki.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        kk.acceptGroupInvitation(
                                                                            op.param1
                                                                        )
                                                                        random.choice(
                                                                            KAC
                                                                        ).inviteIntoGroup(
                                                                            op.param1,
                                                                            [Zmid],
                                                                        )
                                                                    except BaseException:
                                                                        try:
                                                                            ki.kickoutFromGroup(
                                                                                op.param1,
                                                                                [
                                                                                    op.param2
                                                                                ],
                                                                            )
                                                                            ki.inviteIntoGroup(
                                                                                op.param1,
                                                                                [
                                                                                    Cmid,
                                                                                    mid,
                                                                                    Bmid,
                                                                                ],
                                                                            )
                                                                            kc.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            cl.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            kk.acceptGroupInvitation(
                                                                                op.param1
                                                                            )
                                                                            random.choice(
                                                                                KAC
                                                                            ).inviteIntoGroup(
                                                                                op.param1,
                                                                                [Zmid],
                                                                            )
                                                                        except BaseException:
                                                                            try:
                                                                                kk.kickoutFromGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        op.param2
                                                                                    ],
                                                                                )
                                                                                kk.inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        Cmid,
                                                                                        mid,
                                                                                        Amid,
                                                                                    ],
                                                                                )
                                                                                kc.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                cl.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                ki.acceptGroupInvitation(
                                                                                    op.param1
                                                                                )
                                                                                random.choice(
                                                                                    KAC
                                                                                ).inviteIntoGroup(
                                                                                    op.param1,
                                                                                    [
                                                                                        Zmid
                                                                                    ],
                                                                                )
                                                                            except BaseException:
                                                                                pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1, [op.param2])
                        cl.findAndAddContactsByMid(op.param1, admin)
                        cl.inviteIntoGroup(op.param1, admin)
                    except BaseException:
                        try:
                            ki.kickoutFromGroup(op.param1, [op.param2])
                            ki.findAndAddContactsByMid(op.param1, admin)
                            ki.inviteIntoGroup(op.param1, admin)
                        except BaseException:
                            try:
                                kk.kickoutFromGroup(op.param1, [op.param2])
                                kk.findAndAddContactsByMid(op.param1, admin)
                                kk.inviteIntoGroup(op.param1, admin)
                            except BaseException:
                                try:
                                    kc.kickoutFromGroup(op.param1, [op.param2])
                                    kc.findAndAddContactsByMid(op.param1, admin)
                                    kc.inviteIntoGroup(op.param1, admin)
                                except BaseException:
                                    pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1, [op.param2])
                        cl.findAndAddContactsByMid(op.param1, staff)
                        cl.inviteIntoGroup(op.param1, staff)
                    except BaseException:
                        try:
                            ki.kickoutFromGroup(op.param1, [op.param2])
                            ki.findAndAddContactsByMid(op.param1, staff)
                            ki.inviteIntoGroup(op.param1, staff)
                        except BaseException:
                            try:
                                kk.kickoutFromGroup(op.param1, [op.param2])
                                kk.findAndAddContactsByMid(op.param1, staff)
                                kk.inviteIntoGroup(op.param1, staff)
                            except BaseException:
                                try:
                                    kc.kickoutFromGroup(op.param1, [op.param2])
                                    kc.findAndAddContactsByMid(op.param1, staff)
                                    kc.inviteIntoGroup(op.param1, staff)
                                except BaseException:
                                    pass
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                    if op.param2 in Setmain["RAreadMember"][op.param1]:
                        pass
                    else:
                        Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                    pass
            except BaseException:
                pass

        if op.type == 55:
            print("[ 55 ] BLACKLIST")
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
            else:
                pass

        if op.type == 65:
            if wait["unsend"]:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                            if msg_dict1[msg_id]["text"] == "Memuat gambar...":
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = "「 Gambar Dihapus 」\n"
                                ret_ = "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu kirim : {}".format(
                                    dt_to_str(
                                        cTime_to_datetime(
                                            msg_dict1[msg_id]["createdTime"]
                                        )
                                    )
                                )
                                ry = str(ryan.displayName)
                                pesan = ""
                                pesan2 = pesan + "@x \n"
                                xlen = str(len(zxc) + len(xpesan))
                                xlen2 = str(len(zxc) + len(pesan2) + len(xpesan) - 1)
                                zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(
                                    at,
                                    text,
                                    contentMetadata={
                                        "MENTION": str(
                                            '{"MENTIONEES":'
                                            + json.dumps(zx2).replace(" ", "")
                                            + "}"
                                        )
                                    },
                                    contentType=0,
                                )
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                            else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ = "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Kirim : {}".format(
                                    dt_to_str(
                                        cTime_to_datetime(
                                            msg_dict[msg_id]["createdTime"]
                                        )
                                    )
                                )
                                ret_ += "\n• Pesan : {}".format(
                                    str(msg_dict[msg_id]["text"])
                                )
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"]:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                            ginfo = cl.getGroup(at)
                            ryan = cl.getContact(msg_dict1[msg_id]["from"])
                            ret_ = "「 Sticker Dihapus 」\n"
                            ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                            ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                            ret_ += "\n• Waktu Kirim : {}".format(
                                dt_to_str(
                                    cTime_to_datetime(msg_dict1[msg_id]["createdTime"])
                                )
                            )
                            ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                            cl.sendMessage(at, str(ret_))
                            cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 55:
            print("[ 55 ] READ POINT")
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                    if op.param2 in Setmain["ARreadMember"][op.param1]:
                        pass
                    else:
                        Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                    pass
            except BaseException:
                pass

            if cctv["cyduk"][op.param1]:
                if op.param1 in cctv["point"]:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv["sidermem"][op.param1]:
                        pass
                    else:
                        cctv["sidermem"][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        sider = cl.getContact(op.param2).picturePath
                        image = "http://dl.profile.line.naver.jp" + sider
                        cl.sendImageWithURL(op.param1, image)

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1, [op.param2])
            else:
                pass

        if op.type == 26:
            if wait["selfbot"]:
                msg = op.message
                if msg._from not in Bots:
                    if msg._from in wait["blacklist"]:
                        try:
                            random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                        except BaseException:
                            try:
                                random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                            except BaseException:
                                random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                if msg._from not in Bots:
                    if wait["talkban"]:
                        if msg._from in wait["Talkblacklist"]:
                            try:
                                random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                            except BaseException:
                                try:
                                    random.choice(ABC).kickoutFromGroup(
                                        msg.to, [msg._from]
                                    )
                                except BaseException:
                                    random.choice(ABC).kickoutFromGroup(
                                        msg.to, [msg._from]
                                    )
                if "MENTION" in msg.contentMetadata.keys() is not None:
                    if wait["detectMention"]:
                        contact = cl.getContact(msg._from)
                        image = (
                            "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        )
                        name = re.findall(r"@(\w+)", msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention["MENTIONEES"]
                        for mention in mentionees:
                            if mention["M"] in Bots:
                                saints = cl.getContact(msg._from)
                                sendMention(msg.to, saints.mid, "", wait["Respontag"])
                                cl.sendMessage(
                                    msg.to,
                                    None,
                                    contentMetadata={
                                        "STKID": "25628787",
                                        "STKPKGID": "1818607",
                                        "STKVER": "1",
                                    },
                                    contentType=7,
                                )
                                cl.sendMessage(msg.to, wait["Respontag"])
                                cl.sendImageWithURL(msg.to, image)
                                rnd = ["Hallo!"]
                                p = random.choice(rnd)
                                lang = "id"
                                tts = gTTS(text=p, lang=lang)
                                tts.save("hasil.mp3")
                                cl.sendAudio(msg.to, "hasil.mp3")
                                cl.sendMessage(
                                    msg.to,
                                    None,
                                    contentMetadata={
                                        "STKID": "25628787",
                                        "STKPKGID": "1818607",
                                        "STKVER": "1",
                                    },
                                    contentType=7,
                                )
                                break
                if "MENTION" in msg.contentMetadata.keys() is not None:
                    if msg._from not in Bots:
                        if wait["detectMention"]:
                            name = re.findall(r"@(\w+)", msg.text)
                            mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                            mentionees = mention["MENTIONEES"]
                            for mention in mentionees:
                                if mention["M"] in admin:
                                    saints = cl.getContact(msg._from)
                                    sendMention(
                                        msg.to, saints.mid, "", wait["Respontag"]
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={
                                            "PRDID": "a0768339-c2d3-4189-9653-2909e9bb6f58",
                                            "PRDTYPE": "THEME",
                                            "MSGTPL": "6",
                                        },
                                        contentType=9,
                                    )
                                    break
                if "MENTION" in msg.contentMetadata.keys() is not None:
                    if msg._from not in Bots:
                        if wait["mentionKick"]:
                            name = re.findall(r"@(\w+)", msg.text)
                            mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                            mentionees = mention["MENTIONEES"]
                            for mention in mentionees:
                                if mention["M"] in admin:
                                    cl.sendMessage(msg.to, "Don't tag me!")
                                    cl.kickoutFromGroup(msg.to, [msg._from])
                                    break
                if msg.contentType == 7:
                    if wait["sticker"]:
                        msg.contentType = 0
                        cl.sendMessage(
                            msg.to,
                            "「Cek ID Sticker」\n• STKID : "
                            + msg.contentMetadata["STKID"]
                            + "\n• STKPKGID : "
                            + msg.contentMetadata["STKPKGID"]
                            + "\n• STKVER : "
                            + msg.contentMetadata["STKVER"]
                            + "\n\n「Link Sticker」"
                            + "\nline://shop/detail/"
                            + msg.contentMetadata["STKPKGID"],
                        )
                if msg.contentType == 13:
                    if wait["contact"]:
                        msg.contentType = 0
                        cl.sendMessage(msg.to, msg.contentMetadata["mid"])
                        if "displayName" in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                            image = "http://dl.profile.line.naver.jp" + path
                            cl.sendMessage(
                                msg.to,
                                "• Nama : "
                                + msg.contentMetadata["displayName"]
                                + "\n• MID : "
                                + msg.contentMetadata["mid"]
                                + "\n• Status Message : "
                                + contact.statusMessage
                                + "\n• Picture URL : http://dl.profile.line-cdn.net/"
                                + contact.pictureStatus,
                            )
                            cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 7:
                    if wait["sticker"]:
                        msg.contentType = 0
                        cl.sendMessage(
                            msg.to,
                            "• STKID : "
                            + msg.contentMetadata["STKID"]
                            + "\n• STKPKGID : "
                            + msg.contentMetadata["STKPKGID"]
                            + "\n• STKVER : "
                            + msg.contentMetadata["STKVER"]
                            + "\n\n「Link Sticker」"
                            + "\nline://shop/detail/"
                            + msg.contentMetadata["STKPKGID"],
                        )
                if msg.contentType == 13:
                    if wait["contact"]:
                        msg.contentType = 0
                        cl.sendMessage(msg.to, msg.contentMetadata["mid"])
                        if "displayName" in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                            image = "http://dl.profile.line.naver.jp" + path
                            cl.sendMessage(
                                msg.to,
                                "• Nama : "
                                + msg.contentMetadata["displayName"]
                                + "\n• MID : "
                                + msg.contentMetadata["mid"]
                                + "\n• Status Message : "
                                + contact.statusMessage
                                + "\n• Picture URL : http://dl.profile.line-cdn.net/"
                                + contact.pictureStatus,
                            )
                            cl.sendImageWithURL(msg.to, image)

                # SPAMINVITE
                if op.type == 25:
                    if settings["SpamInvite"]:
                        msg = op.message
                        man = msg._from
                        send = msg.to
                        if msg.contentType == 13:
                            if msg._from in admin:
                                korban = msg.contentMetadata["displayName"]
                                invite = msg.contentMetadata["mid"]
                                groups = client.getGroup(send)
                                pending = groups.invitee
                                targets = []
                                for x in groups.members:
                                    if korban in x.displayName:
                                        client.sendText(
                                            send, korban + " Sudah Berada Di Grup Ini"
                                        )
                                    else:
                                        targets.append(invite)
                                if targets == []:
                                    pass
                                else:
                                    for target in targets:
                                        try:
                                            cl.findAndAddContactsByMid(target)
                                            ki.findAndAddContactsByMid(target)
                                            kk.findAndAddContactsByMid(target)
                                            kc.findAndAddContactsByMid(target)
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            cl.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            ki.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kk.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            kc.createGroup("SPAM!!!", [target])
                                            cl.sendText(
                                                send,
                                                "Spam Invite ke "
                                                + korban
                                                + "\nSUCCESS...",
                                            )
                                            settings["SpamInvite"] = False
                                        except BaseException:
                                            cl.sendText(send, "Contact error")
                                            settings["SpamInvite"] = False
                                            break
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
                if msg.toType == 0:
                    to = msg._from
                elif msg.toType == 2:
                    to = msg.to
                if msg.contentType == 16:
                    if wait["Timeline"]:
                        ret_ = "「 Detail Post 」"
                        if msg.contentMetadata["serviceType"] == "GB":
                            contact = cl.getContact(sender)
                            auth = "\n• Penulis : {}".format(str(contact.displayName))
                        else:
                            auth = "\n• Penulis : {}".format(
                                str(msg.contentMetadata["serviceName"])
                            )
                        ret_ += auth
                        if "stickerId" in msg.contentMetadata:
                            stck = "\n• Sticker : https://line.me/R/shop/detail/{}".format(
                                str(msg.contentMetadata["packageId"])
                            )
                            ret_ += stck
                        if "mediaOid" in msg.contentMetadata:
                            object_ = msg.contentMetadata["mediaOid"].replace(
                                "svc=myhome|sid=h|", ""
                            )
                            if msg.contentMetadata["mediaType"] == "V":
                                if msg.contentMetadata["serviceType"] == "GB":
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(msg.contentMetadata["mediaOid"])
                                    )
                                    murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(
                                        str(msg.contentMetadata["mediaOid"])
                                    )
                                else:
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(object_)
                                    )
                                    murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(
                                        str(object_)
                                    )
                                ret_ += murl
                            else:
                                if msg.contentMetadata["serviceType"] == "GB":
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(msg.contentMetadata["mediaOid"])
                                    )
                                else:
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(object_)
                                    )
                            ret_ += ourl
                        if "text" in msg.contentMetadata:
                            text = "\n• Text : {}".format(
                                str(msg.contentMetadata["text"])
                            )
                            purl = "\n• Post URL : {}".format(
                                str(msg.contentMetadata["postEndUrl"]).replace(
                                    "line://", "https://line.me/R/"
                                )
                            )
                            ret_ += purl
                            ret_ += text
                        cl.sendMessage(to, str(ret_))
                        cl.like(url[25:58], url[66:], likeType=1005)
                        cl.comment(url[25:58], url[66:], wait["message"])
                if msg.contentType == 0:
                    msg_dict[msg.id] = {
                        "text": msg.text,
                        "from": msg._from,
                        "createdTime": msg.createdTime,
                    }
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {
                        "text": "Memuat gambar...",
                        "data": path,
                        "from": msg._from,
                        "createdTime": msg.createdTime,
                    }
                if msg.contentType == 7:
                    stk_id = msg.contentMetadata["STKID"]
                    stk_ver = msg.contentMetadata["STKVER"]
                    pkg_id = msg.contentMetadata["STKPKGID"]
                    ret_ = "\n\n「 Sticker Info 」"
                    ret_ += "\n• Sticker ID : {}".format(stk_id)
                    ret_ += "\n• Sticker Version : {}".format(stk_ver)
                    ret_ += "\n• Sticker Package : {}".format(pkg_id)
                    ret_ += "\n• Sticker URL : line://shop/detail/{}".format(pkg_id)
                    query = int(stk_id)
                    if isinstance(query, int):
                        data = (
                            "https://stickershop.line-scdn.net/stickershop/v1/sticker/"
                            + str(query)
                            + "/ANDROID/sticker.png"
                        )
                        path = cl.downloadFileURL(data)
                        msg_dict1[msg.id] = {
                            "text": str(ret_),
                            "data": path,
                            "from": msg._from,
                            "createdTime": msg.createdTime,
                        }
                if msg.contentType == 7:
                    if wait["stickerOn"]:
                        stk_id = msg.contentMetadata["STKID"]
                        stk_ver = msg.contentMetadata["STKVER"]
                        pkg_id = msg.contentMetadata["STKPKGID"]
                        with requests.session() as s:
                            s.headers["user-agent"] = "Mozilla/5.0"
                            r = s.get(
                                "https://store.line.me/stickershop/product/{}/id".format(
                                    urllib.parse.quote(pkg_id)
                                )
                            )
                            soup = BeautifulSoup(r.content, "html5lib")
                            data = soup.select("[class~=mdBtn01Txt]")[0].text
                            if data == "Lihat Produk Lain":
                                ret_ = "「 Sticker Info 」"
                                ret_ += "\n• Sticker ID : {}".format(stk_id)
                                ret_ += "\n• Sticker Package : {}".format(pkg_id)
                                ret_ += "\n• Sticker Version : {}".format(stk_ver)
                                ret_ += "\n• Sticker URL : line://shop/detail/{}".format(
                                    pkg_id
                                )
                                cl.sendMessage(msg.to, str(ret_))
                                query = int(stk_id)
                                if isinstance(query, int):
                                    data = (
                                        "https://stickershop.line-scdn.net/stickershop/v1/sticker/"
                                        + str(query)
                                        + "/ANDROID/sticker.png"
                                    )
                                    path = cl.downloadFileURL(data)
                                    cl.sendImage(msg.to, path)
                            else:
                                ret_ = "「 Sticker Info 」"
                                ret_ += (
                                    "\n• Price : "
                                    + soup.findAll(
                                        "p", attrs={"class": "mdCMN08Price"}
                                    )[0].text
                                )
                                ret_ += (
                                    "\n• Author : "
                                    + soup.select("a[href*=/stickershop/author]")[
                                        0
                                    ].text
                                )
                                ret_ += "\n• Sticker ID : {}".format(str(stk_id))
                                ret_ += "\n• Sticker Package : {}".format(str(pkg_id))
                                ret_ += "\n• Sticker Version : {}".format(str(stk_ver))
                                ret_ += "\n• Sticker URL : line://shop/detail/{}".format(
                                    str(pkg_id)
                                )
                                ret_ += (
                                    "\n• Description :\n"
                                    + soup.findAll("p", attrs={"class": "mdCMN08Desc"})[
                                        0
                                    ].text
                                )
                                cl.sendMessage(msg.to, str(ret_))
                                query = int(stk_id)
                                if isinstance(query, int):
                                    data = (
                                        "https://stickershop.line-scdn.net/stickershop/v1/sticker/"
                                        + str(query)
                                        + "/ANDROID/sticker.png"
                                    )
                                    path = cl.downloadFileURL(data)
                                    cl.sendImage(msg.to, path)
                if msg.contentType == 13:
                    if wait["contact"]:
                        msg.contentType = 0
                        cl.sendMessage(msg.to, msg.contentMetadata["mid"])
                        if "displayName" in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                            image = "http://dl.profile.line.naver.jp" + path
                            cl.sendMessage(
                                msg.to,
                                "「 Contact Info 」\n• Nama : "
                                + msg.contentMetadata["displayName"]
                                + "\n• MID : "
                                + msg.contentMetadata["mid"]
                                + "\n• Status Message : "
                                + contact.statusMessage
                                + "\n• Picture URL : http://dl.profile.line-cdn.net/"
                                + contact.pictureStatus,
                            )
                            cl.sendImageWithURL(msg.to, image)
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["invite"]:
                            msg.contentType = 0
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            invite = msg.contentMetadata["mid"]
                            groups = cl.getGroup(msg.to)
                            pending = groups.invitee
                            targets = []
                            for s in groups.members:
                                if invite in wait["blacklist"]:
                                    cl.sendMessage(
                                        msg.to,
                                        "Ter-blacklist! Hapus blacklist lalu invite lagi",
                                    )
                                    break
                                else:
                                    targets.append(invite)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        cl.findAndAddContactsByMid(target)
                                        cl.inviteIntoGroup(msg.to, [target])
                                        ryan = cl.getContact(target)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 Sukses Invite 」\nNama "
                                        ret_ = "Ketik Invite off jika sudah done"
                                        ry = str(ryan.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@x\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1
                                        )
                                        zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                        text = xpesan + zxc + ret_ + ""
                                        cl.sendMessage(
                                            msg.to,
                                            text,
                                            contentMetadata={
                                                "MENTION": str(
                                                    '{"MENTIONEES":'
                                                    + json.dumps(zx2).replace(" ", "")
                                                    + "}"
                                                )
                                            },
                                            contentType=0,
                                        )
                                        wait["invite"] = False
                                        break
                                    except BaseException:
                                        cl.sendText(msg.to, "Anda terkena limit")
                                        wait["invite"] = False
                                        break

                # ADD BOTS
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["addbots"]:
                            if msg.contentMetadata["mid"] in Bots:
                                cl.sendMessage(msg.to, "Contact itu sudah jadi bot")
                                wait["addbots"] = True
                            else:
                                Bots.append(msg.contentMetadata["mid"])
                                wait["addbots"] = True
                                cl.sendMessage(msg.to, "Berhasil menambahkan ke bot")
                    if wait["dellbots"]:
                        if msg.contentMetadata["mid"] in Bots:
                            Bots.remove(msg.contentMetadata["mid"])
                            cl.sendMessage(msg.to, "Berhasil menghapus dari bot")
                        else:
                            wait["dellbots"] = True
                            cl.sendMessage(msg.to, "Contact itu bukan bot")

                # ADD STAFF
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["addstaff"]:
                            if msg.contentMetadata["mid"] in staff:
                                cl.sendMessage(msg.to, "Contact itu sudah jadi staff")
                                wait["addstaff"] = True
                            else:
                                staff.append(msg.contentMetadata["mid"])
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to, "Berhasil menambahkan ke staff")
                    if wait["dellstaff"]:
                        if msg.contentMetadata["mid"] in staff:
                            staff.remove(msg.contentMetadata["mid"])
                            cl.sendMessage(msg.to, "Berhasil menghapus dari staff")
                            wait["dellstaff"] = True
                        else:
                            wait["dellstaff"] = True
                            cl.sendMessage(msg.to, "Contact itu bukan staff")

                # ADD ADMIN
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["addadmin"]:
                            if msg.contentMetadata["mid"] in admin:
                                cl.sendMessage(msg.to, "Contact itu sudah jadi admin")
                                wait["addadmin"] = True
                            else:
                                admin.append(msg.contentMetadata["mid"])
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to, "Berhasil menambahkan ke admin")
                    if wait["delladmin"]:
                        if msg.contentMetadata["mid"] in admin:
                            admin.remove(msg.contentMetadata["mid"])
                            cl.sendMessage(msg.to, "Berhasil menghapus dari admin")
                        else:
                            wait["delladmin"] = True
                            cl.sendMessage(msg.to, "Contact itu bukan admin")

                # ADD BLACKLIST
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["wblacklist"]:
                            if msg.contentMetadata["mid"] in wait["blacklist"]:
                                cl.sendMessage(
                                    msg.to, "Contact itu sudah ada di blacklist"
                                )
                                wait["wblacklist"] = True
                            else:
                                wait["blacklist"][msg.contentMetadata["mid"]] = True
                                wait["wblacklist"] = True
                                cl.sendMessage(
                                    msg.to, "Berhasil menambahkan ke blacklist"
                                )
                    if wait["dblacklist"]:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            del wait["blacklist"][msg.contentMetadata["mid"]]
                            cl.sendMessage(msg.to, "Berhasil menghapus dari blacklist")
                        else:
                            wait["dblacklist"] = True
                            cl.sendMessage(msg.to, "Contact itu tidak ada di blacklist")

                # ADD TALKBAN
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["Talkwblacklist"]:
                            if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                                cl.sendMessage(
                                    msg.to, "Contact itu sudah ada di Talkban"
                                )
                                wait["Talkwblacklist"] = True
                            else:
                                wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(
                                    msg.to, "Berhasil menambahkan ke Talkban"
                                )
                    if wait["Talkdblacklist"]:
                        if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                            del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                            cl.sendMessage(msg.to, "Berhasil menghapus dari Talkban")
                        else:
                            wait["Talkdblacklist"] = True
                            cl.sendMessage(msg.to, "Contact itu tidak ada di Talkban")

                # MEDIA
                if msg.contentType == 1:
                    if msg._from in admin:
                        if wait["Addimage"]["status"]:
                            path = cl.downloadObjectMsg(msg.id)
                            images[wait["Addimage"]["name"]] = str(path)
                            f = codecs.open("image.json", "w", "utf-8")
                            json.dump(
                                images, f, sort_keys=True, indent=4, ensure_ascii=False
                            )
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan gambar {}".format(
                                    str(wait["Addimage"]["name"])
                                ),
                            )
                            wait["Addimage"]["status"] = False
                            wait["Addimage"]["name"] = ""
                if msg.contentType == 2:
                    if msg._from in admin:
                        if wait["Addvideo"]["status"]:
                            path = cl.downloadObjectMsg(msg.id)
                            videos[wait["Addvideo"]["name"]] = str(path)
                            f = codecs.open("video.json", "w", "utf-8")
                            json.dump(
                                videos, f, sort_keys=True, indent=4, ensure_ascii=False
                            )
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan video {}".format(
                                    str(wait["Addvideo"]["name"])
                                ),
                            )
                            wait["Addvideo"]["status"] = False
                            wait["Addvideo"]["name"] = ""
                if msg.contentType == 7:
                    if msg._from in admin:
                        if wait["Addsticker"]["status"]:
                            stickers[wait["Addsticker"]["name"]] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"],
                            }
                            f = codecs.open("sticker.json", "w", "utf-8")
                            json.dump(
                                stickers,
                                f,
                                sort_keys=True,
                                indent=4,
                                ensure_ascii=False,
                            )
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan sticker {}".format(
                                    str(wait["Addsticker"]["name"])
                                ),
                            )
                            wait["Addsticker"]["status"] = False
                            wait["Addsticker"]["name"] = ""
                if msg.contentType == 3:
                    if msg._from in admin:
                        if wait["Addaudio"]["status"]:
                            path = cl.downloadObjectMsg(msg.id)
                            audios[wait["Addaudio"]["name"]] = str(path)
                            f = codecs.open("audio.json", "w", "utf-8")
                            json.dump(
                                audios, f, sort_keys=True, indent=4, ensure_ascii=False
                            )
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan mp3 {}".format(
                                    str(wait["Addaudio"]["name"])
                                ),
                            )
                            wait["Addaudio"]["status"] = False
                            wait["Addaudio"]["name"] = ""
                if msg.toType == 2:
                    if msg._from in admin:
                        if settings["groupPicture"]:
                            path = cl.downloadObjectMsg(msg_id)
                            settings["groupPicture"] = False
                            cl.updateGroupPicture(msg.to, path)
                            cl.sendMessage(msg.to, "Berhasil mengubah foto group")
                if msg.contentType == 1:
                    if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to, "Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to, "Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to, "Foto berhasil dirubah")

                if msg.contentType == 1:
                    if msg._from in admin:
                        if setting["changePicture"]:
                            path1 = ki.downloadObjectMsg(msg_id)
                            path2 = kk.downloadObjectMsg(msg_id)
                            path3 = kc.downloadObjectMsg(msg_id)
                            setting["changePicture"] = False
                            ki.updateProfilePicture(path1)
                            ki.sendMessage(msg.to, "Foto berhasil dirubah")
                            kk.updateProfilePicture(path2)
                            kk.sendMessage(msg.to, "Foto berhasil dirubah")
                            kc.updateProfilePicture(path3)
                            kc.sendMessage(msg.to, "Foto berhasil dirubah")
                if msg.contentType == 2:
                    if msg._from in admin:
                        if mid in Setmain["ARvideo"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARvideo"][mid]
                            cl.updateProfileVideoPicture(path)
                            cl.sendMessage(msg.to, "Foto berhasil dirubah jadi video")

                if msg.contentType == 0:
                    if Setmain["autoRead"]:
                        cl.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        for sticker in stickers:
                            if msg._from in admin:
                                if text.lower() == sticker:
                                    sid = stickers[text.lower()]["STKID"]
                                    spkg = stickers[text.lower()]["STKPKGID"]
                                    cl.sendSticker(to, spkg, sid)
                        for image in images:
                            if msg._from in admin:
                                if text.lower() == image:
                                    cl.sendImage(msg.to, images[image])
                        for audio in audios:
                            if msg._from in admin:
                                if text.lower() == audio:
                                    cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                            if msg._from in admin:
                                if text.lower() == video:
                                    cl.sendVideo(msg.to, videos[video])
                        cmd = command(text)
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "「 ON 」\nSelfbot diaktifkan")

                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "「 OFF 」\nSelfbot dinonaktifkan")

                        # HELP
                        elif cmd == "help":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage = help()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\n• User : "
                                    ret_ = str(helpMessage)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1
                                    )
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )

                        elif cmd == "help1":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage1 = help1()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\n• User : "
                                    ret_ = str(helpMessage1)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1
                                    )
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )

                        elif cmd == "help2":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage2 = help2()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\n• User : "
                                    ret_ = str(helpMessage2)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1
                                    )
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )

                        elif cmd == "help3":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage3 = help3()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\n• User : "
                                    ret_ = str(helpMessage3)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1
                                    )
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )

                        # STATUS
                        elif cmd == "status":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    md = "\n「 STATUS」\n"
                                    if wait["stickerOn"]:
                                        md += "• Sticker [ON] ☑️\n"
                                    else:
                                        md += "• Sticker [OFF] ❎\n"
                                    if wait["contact"]:
                                        md += "• Contact [ON] ☑️\n"
                                    else:
                                        md += "• Contact [OFF] ❎\n"
                                    if wait["talkban"]:
                                        md += "• Talkban [ON] ☑️\n"
                                    else:
                                        md += "• Talkban [OFF] ❎\n"
                                    if wait["unsend"]:
                                        md += "• Unsend [ON] ☑️\n"
                                    else:
                                        md += "• Unsend [OFF] ❎\n"
                                    if settings["SpamInvite"]:
                                        md += "• Spaminvite [ON] ☑️\n"
                                    else:
                                        md += "• Spaminvite [OFF] ❎\n"
                                    if wait["detectMention"]:
                                        md += "• Respon [ON] ☑️\n"
                                    else:
                                        md += "• Respon [OFF] ❎\n"
                                    if wait["Timeline"]:
                                        md += "• Timeline [ON] ☑️\n"
                                    else:
                                        md += "• Timeline [OFF] ❎\n"
                                    if wait["autoJoin"]:
                                        md += "• Autojoin [ON] ☑️\n"
                                    else:
                                        md += "• Autojoin [OFF] ❎\n"
                                    if wait["autoAdd"]:
                                        md += "• Autoadd [ON] ☑️\n"
                                    else:
                                        md += "• Autoadd [OFF] ❎\n"
                                    if settings["autoJoinTicket"]:
                                        md += "• Jointicket [ON] ☑️\n"
                                    else:
                                        md += "• Jointicket [OFF] ❎\n"
                                    if msg.to in welcome:
                                        md += "• Welcome [ON] ☑️\n"
                                    else:
                                        md += "• Welcome [OFF] ❎\n"
                                    if wait["autoLeave"]:
                                        md += "• Autoleave [ON] ☑️\n"
                                    else:
                                        md += "• Autoleave [OFF] ❎\n"
                                    if msg.to in protectqr:
                                        md += "• Protecturl [ON] ☑️\n"
                                    else:
                                        md += "• Protecturl [OFF] ❎\n"
                                    if msg.to in protectjoin:
                                        md += "• Protectjoin [ON] ☑️\n"
                                    else:
                                        md += "• Protectjoin [OFF] ❎\n"
                                    if msg.to in protectinvite:
                                        md += "• Protectinvite [ON] ☑️\n"
                                    else:
                                        md += "• Protectinvite [OFF] ❎\n"
                                    if msg.to in protectkick:
                                        md += "• Protectkick [ON] ☑️\n"
                                    else:
                                        md += "• Protectkick [OFF] ❎\n"
                                    if msg.to in protectcancel:
                                        md += "• Protectcancel [ON] ☑️\n"
                                    else:
                                        md += "• Protectcancel [OFF] ❎\n"
                                    if msg.to in protectantijs:
                                        md += "• Antijs [ON] ☑️\n"
                                    else:
                                        md += "• Antijs [OFF] ❎\n"
                                    if msg.to in ghost:
                                        md += "• Ghost [ON] ☑️\n"
                                    else:
                                        md += "• Ghost [OFF] ❎\n"
                                    ginfo = cl.getGroup(msg.to)
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHAD 」\n• User : "
                                    ret_ = "• Group : {}\n".format(str(ginfo.name))
                                    ret_ += str(md)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1
                                    )
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = (
                                        xpesan
                                        + zxc
                                        + ret_
                                        + "\n• Jam [ "
                                        + datetime.strftime(timeNow, "%H:%M:%S")
                                        + " ]"
                                        + "\n• Tanggal : "
                                        + datetime.strftime(timeNow, "%Y-%m-%d")
                                    )
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )

                        # CREATOR
                        elif cmd == "creator" or text.lower() == "creator":
                            if msg._from in admin:
                                cl.sendText(
                                    msg.to,
                                    "「 𐀀 HELLTERHEAD 」\nBy : DRE❗\nline.me/ti/p/~mo-banzu",
                                )
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(mid)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": mid},
                                        contentType=13,
                                    )

                        # ABOUT
                        elif cmd.startswith("about"):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        arr = []
                                        today = datetime.today()
                                        thn = 1995
                                        bln = 12  # isi bulannya yg sewa
                                        hr = 23  # isi tanggalnya yg sewa
                                        future = datetime(thn, bln, hr)
                                        days = str(future - today)
                                        comma = days.find(",")
                                        days = days[:comma]
                                        contact = cl.getContact(mid)
                                        favoritelist = cl.getFavoriteMids()
                                        grouplist = cl.getGroupIdsJoined()
                                        contactlist = cl.getAllContactIds()
                                        blockedlist = cl.getBlockedContactIds()
                                        eltime = time.time() - mulai
                                        bot = runtime(eltime)
                                        start = time.time()
                                        # cl.sendText("", '.')
                                        elapsed_time = time.time() - start
                                        ryan = cl.getContact(mid)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 Informasi Selfbot  」\n• User : "
                                        ret_ = "• Group : {} Group".format(
                                            str(len(grouplist))
                                        )
                                        ret_ += "\n• Friend : {} Friend".format(
                                            str(len(contactlist))
                                        )
                                        ret_ += "\n• Blocked : {} Blocked".format(
                                            str(len(blockedlist))
                                        )
                                        ret_ += "\n• Favorite : {} Favorite".format(
                                            str(len(favoritelist))
                                        )
                                        ret_ += "\n• Version : [ Selfbot Pro ]"
                                        ret_ += "\n• Expired : {} - {} - {}".format(
                                            str(hr), str(bln), str(thn)
                                        )
                                        ret_ += "\n• In Days : {} Again".format(days)
                                        ret_ += "\n• Speed : {} Second".format(
                                            str(elapsed_time)
                                        )
                                        ret_ += "\n• Runtime : {}".format(str(bot))
                                        ret_ += "\n\n• By : DRE❗"
                                        ry = str(ryan.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@x \n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1
                                        )
                                        zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                        text = xpesan + zxc + ret_ + ""
                                        cl.sendMessage(
                                            to,
                                            text,
                                            contentMetadata={
                                                "MENTION": str(
                                                    '{"MENTIONEES":'
                                                    + json.dumps(zx2).replace(" ", "")
                                                    + "}"
                                                )
                                            },
                                            contentType=0,
                                        )
                                        # cl.sendContact(to, "")
                                    except Exception as e:
                                        cl.sendMessage(msg.to, str(e))

                        # PROFILE
                        elif cmd == "me" or text.lower() == "me":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    sendMention(
                                        msg.to, sender, "「 𐀀 HELLTERHEAD 」\n", ""
                                    )
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": mid}
                                    cl.sendMessage1(msg)

                        elif text.lower() == "mid":
                            cl.sendMessage(msg.to, msg._from)

                        elif cmd.startswith("mid "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    mi = cl.getContact(key1)
                                    cl.sendMessage(
                                        msg.to,
                                        "Nama : "
                                        + str(mi.displayName)
                                        + "\nMID : "
                                        + key1,
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": key1},
                                        contentType=13,
                                    )

                        elif "Steal " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    mi = cl.getContact(key1)
                                    a = channel.getProfileCoverURL(mid=key1)
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Contact Info 」\n• Nama : "
                                        + str(mi.displayName)
                                        + "\n• MID : "
                                        + key1
                                        + "\n• Status Message : "
                                        + str(mi.statusMessage),
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": key1},
                                        contentType=13,
                                    )
                                    if "videoProfile='{" in str(cl.getContact(key1)):
                                        cl.sendVideoWithURL(
                                            msg.to,
                                            "http://dl.profile.line.naver.jp"
                                            + str(mi.picturePath)
                                            + "/vp.small",
                                        )
                                        cl.sendImageWithURL(receiver, a)
                                    else:
                                        cl.sendImageWithURL(
                                            msg.to,
                                            "http://dl.profile.line.naver.jp"
                                            + str(mi.picturePath),
                                        )
                                        cl.sendImageWithURL(receiver, a)

                        elif "Cover " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        key = eval(msg.contentMetadata["MENTION"])
                                        u = key["MENTIONEES"][0]["M"]
                                        a = channel.getProfileCoverURL(mid=u)
                                        cl.sendImageWithURL(receiver, a)
                                    except Exception as e:
                                        cl.sendText(receiver, str(e))

                        # CLONE
                        elif cmd.startswith("clone "):
                            if "MENTION" in msg.contentMetadata.keys() is not None:
                                names = re.findall(r"@(\w+)", text)
                                mention = ast.literal_eval(
                                    msg.contentMetadata["MENTION"]
                                )
                                mentionees = mention["MENTIONEES"]
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.cloneContactProfile(ls)
                                    cl.sendContact(to, sender)
                                    cl.sendMessage(to, "Clone Profile Success!")

                        elif cmd == "restoreprofile":
                            try:
                                lineProfile = cl.getProfile()
                                lineProfile.displayName = str(
                                    wait["myProfile"]["displayName"]
                                )
                                lineProfile.statusMessage = str(
                                    wait["myProfile"]["statusMessage"]
                                )
                                lineProfile.pictureStatus = str(
                                    wait["myProfile"]["pictureStatus"]
                                )
                                cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                cl.updateProfile(lineProfile)
                                coverId = str(wait["myProfile"]["coverId"])
                                cl.updateProfileCoverById(coverId)
                                cl.sendMessage(to, "Restore Profile Success!")
                            except Exception as e:
                                cl.sendMessage(to, "Restore Profile Failed!")

                        elif cmd == "backupprofile":
                            try:
                                profile = cl.getProfile()
                                wait["myProfile"]["displayName"] = str(
                                    profile.displayName
                                )
                                wait["myProfile"]["statusMessage"] = str(
                                    profile.statusMessage
                                )
                                wait["myProfile"]["pictureStatus"] = str(
                                    profile.pictureStatus
                                )
                                coverId = lineProfile.getProfileDetail()["result"][
                                    "objectId"
                                ]
                                wait["myProfile"]["coverId"] = str(coverId)
                                cl.sendMessage(to, "Backup Profile Success!")
                            except Exception as e:
                                cl.sendMessage(to, "Backup Profile Failed!")

                        # STICKER
                        elif "Sticker: " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        query = msg.text.replace("Sticker: ", "")
                                        query = int(query)
                                        if isinstance(query, int):
                                            cl.sendImageWithURL(
                                                receiver,
                                                "https://stickershop.line-scdn.net/stickershop/v1/product/"
                                                + str(query)
                                                + "/ANDROID/main.png",
                                            )
                                            cl.sendText(
                                                receiver,
                                                "https://line.me/S/sticker/"
                                                + str(query),
                                            )
                                        else:
                                            cl.sendText(
                                                receiver,
                                                "Gunakan key sticker angka bukan huruf",
                                            )
                                    except Exception as e:
                                        cl.sendText(receiver, str(e))

                        elif "/ti/g/" in msg.text.lower() == "gsearch":
                            if msg._from in admin:
                                if settings["autoJoinTicket"]:
                                    link_re = re.compile(
                                        r"(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?"
                                    )
                                    links = link_re.findall(text)
                                    n_links = []
                                    for l in links:
                                        if l not in n_links:
                                            n_links.append(l)
                                    for ticket_id in n_links:
                                        group = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(
                                            group.id, ticket_id
                                        )
                                        cl.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )

                        # REJECT
                        elif cmd == "reject":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ginvited = cl.getGroupIdsInvited()
                                    if ginvited != [] and ginvited is not None:
                                        for gid in ginvited:
                                            cl.rejectGroupInvitation(gid)
                                            ki.rejectGroupInvitation(gid)
                                            kk.rejectGroupInvitation(gid)
                                            kc.rejectGroupInvitation(gid)
                                            sw.rejectGroupInvitation(gid)
                                        cl.sendMessage(
                                            to,
                                            "Berhasil tolak sebanyak {} undangan grup".format(
                                                str(len(ginvited))
                                            ),
                                        )
                                    else:
                                        cl.sendMessage(
                                            to, "Tidak ada undangan yang tertunda"
                                        )

                        # BROADCAST
                        elif cmd.startswith("bc: "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                bc = text.replace(sep[0] + " ", "")
                                saya = cl.getGroupIdsJoined()
                                for group in saya:
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 Broadcast 」\nBroadcast by "
                                    ret_ = "{}".format(str(bc))
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1
                                    )
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        group,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )

                        # KEY
                        elif text.lower() == "mykey":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Status Setkey 」\nSetkey saat ini「 "
                                        + str(Setmain["keyCommand"])
                                        + " 」",
                                    )

                        elif cmd.startswith("setkey "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    sep = text.split(" ")
                                    key = text.replace(sep[0] + " ", "")
                                    if key in ["", " ", "\n", None]:
                                        cl.sendMessage(msg.to, "Gagal mengganti key")
                                    else:
                                        Setmain["keyCommand"] = str(key).lower()
                                        cl.sendMessage(
                                            msg.to,
                                            "「 Change Setkey 」\nSetkey diganti jadi「{}」".format(
                                                str(key).lower()
                                            ),
                                        )

                        elif text.lower() == "resetkey":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    Setmain["keyCommand"] = ""
                                    cl.sendMessage(
                                        msg.to, "「 Resetkey 」\nSetkey mu telah direset"
                                    )

                        # RESTART
                        elif cmd == "restart":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Restarting 」\n• User ",
                                        "\nLoading...",
                                        "\nRestarted!",
                                    )
                                    Setmain["restartPoint"] = msg.to
                                    restartBot()

                        # RUNTIME
                        elif cmd == "runtime":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    eltime = time.time() - mulai
                                    bot = runtime(eltime)
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 Runtime 」\n• User : "
                                    ret_ = "• {}".format(str(bot))
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1
                                    )
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )

                        # GROUP INFO
                        elif cmd == "ginfo":
                            if msg._from in admin:
                                try:
                                    G = cl.getGroup(msg.to)
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id))
                                        )
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Group Info 」\n• Name Group : {}".format(
                                            G.name
                                        )
                                        + "\n• ID Group : {}".format(G.id)
                                        + "\n• Pembuat : {}".format(
                                            G.creator.displayName
                                        )
                                        + "\n• Waktu Dibuat : {}".format(
                                            str(timeCreated)
                                        )
                                        + "\n• Jumlah Member : {}".format(
                                            str(len(G.members))
                                        )
                                        + "\n• Jumlah Pending : {}".format(gPending)
                                        + "\n• Group QR : {}".format(gQr)
                                        + "\n• Group Ticket : {}".format(gTicket),
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": G.creator.mid},
                                        contentType=13,
                                    )
                                    cl.sendImageWithURL(
                                        msg.to,
                                        "http://dl.profile.line-cdn.net/"
                                        + G.pictureStatus,
                                    )
                                except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("ginfo: "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    try:
                                        gCreator = G.creator.displayName
                                    except BaseException:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id))
                                        )
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += "「 Group Info 」"
                                    ret_ += "\n• Nama Grup : {}".format(G.name)
                                    ret_ += "\n• ID Grup : {}".format(G.id)
                                    ret_ += "\n• Pembuat : {}".format(gCreator)
                                    ret_ += "\n• Waktu Dibuat : {}".format(
                                        str(timeCreated)
                                    )
                                    ret_ += "\n• Jumlah Member : {}".format(
                                        str(len(G.members))
                                    )
                                    ret_ += "\n• Jumlah Pending : {}".format(gPending)
                                    ret_ += "\n• Group QR : {}".format(gQr)
                                    ret_ += "\n• Group Ticket : {}".format(gTicket)
                                    ret_ += "\n• Picture URL : http://dl.profile.line-cdn.net/{}".format(
                                        G.pictureStatus
                                    )
                                    ret_ += ""
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendImageWithURL(
                                        msg.to,
                                        "http://dl.profile.line-cdn.net/"
                                        + G.pictureStatus,
                                    )
                                except BaseException:
                                    pass

                        elif cmd.startswith("leave: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                group = groups[int(number) - 1]
                                for i in group:
                                    ginfo = cl.getGroup(i)
                                    if ginfo == group:
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        cl.sendMessage(
                                            msg.to,
                                            "Berhasil keluar dari grup "
                                            + str(ginfo.name),
                                        )

                        elif cmd == "friendlist":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    a = 0
                                    gid = cl.getAllContactIds()
                                    for i in gid:
                                        G = cl.getContact(i)
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            "• " + str(a) + ". " + G.displayName + "\n"
                                        )

                        # SPAMCALLTO
                        elif cmd.startswith("spamcallto "):
                            dan = text.split(" ")
                            num = int(dan[1])
                            ret_ = "╔══[ Call Private ]"
                            if "MENTION" in msg.contentMetadata.keys() is not None:
                                names = re.findall(r"@(\w+)", text)
                                mention = ast.literal_eval(
                                    msg.contentMetadata["MENTION"]
                                )
                                mentionees = mention["MENTIONEES"]
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    for var in range(0, num):
                                        group = cl.getGroup(to)
                                        members = [ls]
                                        cl.acquireGroupCallRoute(to)
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                    ret_ += "\n╠ @!"
                                ret_ += "\n╚══[ Total {} Spam Call ]".format(
                                    str(dan[1])
                                )
                                cl.sendMessage(msg.to, "Berhasil Spamcallto")

                        # CODE QR
                        elif cmd.startswith("open: "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    try:
                                        gCreator = G.creator.mid
                                        dia = cl.getContact(gCreator)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 Sukses Open QR 」\n• Creator :  "
                                        diaa = str(dia.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@a\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1
                                        )
                                        zx = {"S": xlen, "E": xlen2, "M": dia.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    except BaseException:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id))
                                        )
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += xpesan + zxc
                                    ret_ += "• Nama : {}".format(G.name)
                                    ret_ += "\n• Group QR : {}".format(gQr)
                                    ret_ += "\n• Pending : {}".format(gPending)
                                    ret_ += "\n• Group Ticket : {}".format(gTicket)
                                    ret_ += ""
                                    cl.sendMessage(
                                        receiver,
                                        ret_,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )
                                except BaseException:
                                    pass

                        elif cmd.startswith("close: "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    try:
                                        gCreator = G.creator.mid
                                        dia = cl.getContact(gCreator)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 Sukses Close QR 」\n• Creator :  "
                                        diaa = str(dia.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@a\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1
                                        )
                                        zx = {"S": xlen, "E": xlen2, "M": dia.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    except BaseException:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id))
                                        )
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += xpesan + zxc
                                    ret_ += "• Nama : {}".format(G.name)
                                    ret_ += "\n• Group QR : {}".format(gQr)
                                    ret_ += "\n• Pending : {}".format(gPending)
                                    ret_ += "\n• Group Ticket : {}".format(gTicket)
                                    ret_ += ""
                                    cl.sendMessage(
                                        receiver,
                                        ret_,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )
                                except BaseException:
                                    pass

                        elif cmd.startswith("infomem "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    no = 0
                                    ret_ = ""
                                    for mem in G.members:
                                        no += 1
                                        ret_ += (
                                            "\n "
                                            "• " + str(no) + ". " + mem.displayName
                                        )
                                    cl.sendMessage(
                                        to,
                                        "• Group Name : [ "
                                        + str(G.name)
                                        + " ]\n\n   [ List Member ]\n"
                                        + ret_
                                        + "\n\n[ Total %i Members ]" % len(G.members),
                                    )
                                except BaseException:
                                    pass

                        # QR GROUP
                        elif cmd.startswith("protectqron: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    try:
                                        protectqr[G] = True
                                        f = codecs.open("protectqr.json", "w", "utf-8")
                                        json.dump(
                                            protectqr,
                                            f,
                                            sort_keys=True,
                                            indent=4,
                                            ensure_ascii=False,
                                        )
                                        gCreator = G.creator.mid
                                        dia = cl.getContact(gCreator)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = (
                                            "「 Protect QR Diaktifkan 」\n• Creator :  "
                                        )
                                        diaa = str(dia.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@a\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1
                                        )
                                        zx = {"S": xlen, "E": xlen2, "M": dia.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    except BaseException:
                                        cl.sendText(msg.to, "Grup itu tidak ada")
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += xpesan + zxc
                                    ret_ += "• Nama Grup : {}".format(G.name)
                                    ret_ += "\n• Pending : {}".format(gPending)
                                    ret_ += "\n• Jumlah Member : {}".format(
                                        str(len(G.members))
                                    )
                                    cl.sendMessage(
                                        receiver,
                                        ret_,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        },
                                        contentType=0,
                                    )
                                except Exception as e:
                                    cl.sendMessage(to, str(e))

                        elif cmd == "open":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        X = cl.getGroup(msg.to)
                                        X.preventedJoinByTicket = False
                                        cl.updateGroup(X)
                                        cl.sendMessage(msg.to, "URL Opened")

                        elif cmd == "close":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        X = cl.getGroup(msg.to)
                                        X.preventedJoinByTicket = True
                                        cl.updateGroup(X)
                                        cl.sendMessage(msg.to, "URL Closed")

                        elif cmd == "url":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        x = cl.getGroup(msg.to)
                                        if x.preventedJoinByTicket:
                                            x.preventedJoinByTicket = False
                                            cl.updateGroup(x)
                                        gurl = cl.reissueGroupTicket(msg.to)
                                        cl.sendMessage(
                                            msg.to,
                                            "• Group :"
                                            + str(x.name)
                                            + "\n• URL Group : http://line.me/R/ti/g/"
                                            + gurl,
                                        )

                        # PROFILE UPDATE
                        elif cmd == "updategroup":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        settings["groupPicture"] = True
                                        cl.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "cpp":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    Setmain["ARfoto"][mid] = True
                                    cl.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "cvp":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    Setmain["ARvideo"][mid] = True
                                    cl.sendText(msg.to, "Kirim videonya")

                        elif cmd.startswith("myname: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = cl.getProfile()
                                    profile.displayName = string
                                    cl.updateProfile(profile)
                                    cl.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + ""
                                    )

                        # MENTION
                        elif cmd == "tagall" or text.lower() == "mention":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    group = cl.getGroup(msg.to)
                                    nama = [contact.mid for contact in group.members]
                                    nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, nm10, jml = (
                                        [],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [],
                                        len(nama),
                                    )
                                    if jml <= 20:
                                        mentionMembers(msg.to, nama)
                                    if jml > 20 and jml < 40:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                    if jml > 40 and jml < 60:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                    if jml > 60 and jml < 80:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                        for l in range(60, 80):
                                            nm4 += [nama[l]]
                                        mentionMembers(msg.to, nm4)
                                    if jml > 80 and jml < 100:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                        for l in range(60, 80):
                                            nm4 += [nama[l]]
                                        mentionMembers(msg.to, nm4)
                                        for m in range(80, 100):
                                            nm5 += [nama[m]]
                                        mentionMembers(msg.to, nm5)
                                    if jml > 100 and jml < 120:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                        for l in range(60, 80):
                                            nm4 += [nama[l]]
                                        mentionMembers(msg.to, nm4)
                                        for m in range(80, 100):
                                            nm5 += [nama[m]]
                                        mentionMembers(msg.to, nm5)
                                        for n in range(100, 120):
                                            nm6 += [nama[n]]
                                        mentionMembers(msg.to, nm6)
                                    if jml > 120 and jml < 140:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                        for l in range(60, 80):
                                            nm4 += [nama[l]]
                                        mentionMembers(msg.to, nm4)
                                        for m in range(80, 100):
                                            nm5 += [nama[m]]
                                        mentionMembers(msg.to, nm5)
                                        for n in range(100, 120):
                                            nm6 += [nama[n]]
                                        mentionMembers(msg.to, nm6)
                                        for o in range(120, 140):
                                            nm7 += [nama[o]]
                                        mentionMembers(msg.to, nm7)
                                    if jml > 140 and jml < 160:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                        for l in range(60, 80):
                                            nm4 += [nama[l]]
                                        mentionMembers(msg.to, nm4)
                                        for m in range(80, 100):
                                            nm5 += [nama[m]]
                                        mentionMembers(msg.to, nm5)
                                        for n in range(100, 120):
                                            nm6 += [nama[n]]
                                        mentionMembers(msg.to, nm6)
                                        for o in range(120, 140):
                                            nm7 += [nama[o]]
                                        mentionMembers(msg.to, nm7)
                                        for p in range(140, 160):
                                            nm8 += [nama[p]]
                                        mentionMembers(msg.to, nm8)
                                    if jml > 160 and jml < 180:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                        for l in range(60, 80):
                                            nm4 += [nama[l]]
                                        mentionMembers(msg.to, nm4)
                                        for m in range(80, 100):
                                            nm5 += [nama[m]]
                                        mentionMembers(msg.to, nm5)
                                        for n in range(100, 120):
                                            nm6 += [nama[n]]
                                        mentionMembers(msg.to, nm6)
                                        for o in range(120, 140):
                                            nm7 += [nama[o]]
                                        mentionMembers(msg.to, nm7)
                                        for p in range(140, 160):
                                            nm8 += [nama[p]]
                                        mentionMembers(msg.to, nm8)
                                        for q in range(160, 180):
                                            nm9 += [nama[q]]
                                        mentionMembers(msg.to, nm9)
                                    if jml > 180 and jml < 200:
                                        for i in range(0, 20):
                                            nm1 += [nama[i]]
                                        mentionMembers(msg.to, nm1)
                                        for j in range(20, 40):
                                            nm2 += [nama[j]]
                                        mentionMembers(msg.to, nm2)
                                        for k in range(40, 60):
                                            nm3 += [nama[k]]
                                        mentionMembers(msg.to, nm3)
                                        for l in range(60, 80):
                                            nm4 += [nama[l]]
                                        mentionMembers(msg.to, nm4)
                                        for m in range(80, 100):
                                            nm5 += [nama[m]]
                                        mentionMembers(msg.to, nm5)
                                        for n in range(100, 120):
                                            nm6 += [nama[n]]
                                        mentionMembers(msg.to, nm6)
                                        for o in range(120, 140):
                                            nm7 += [nama[o]]
                                        mentionMembers(msg.to, nm7)
                                        for p in range(140, 160):
                                            nm8 += [nama[p]]
                                        mentionMembers(msg.to, nm8)
                                        for q in range(160, 180):
                                            nm9 += [nama[q]]
                                        mentionMembers(msg.to, nm9)
                                        for r in range(180, 200):
                                            nm10 += [nama[r]]
                                        mentionMembers(msg.to, nm10)

                        # KICK ALL
                        elif "!bye" in msg.text:
                            if msg._from in admin:
                                if msg.toType == 2:
                                    print("BOOM❗")
                                    _name = msg.text.replace("!bye", "")
                                    gs = cl.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to, "Not found!.")
                                    else:
                                        for target in targets:
                                            if target not in admin and Bots:
                                                try:
                                                    klist = [cl]
                                                    kicker = random.choice(klist)
                                                    kicker.kickoutFromGroup(
                                                        msg.to, [target]
                                                    )
                                                    kicker.cancelGroupInvitation(
                                                        op.param1, [_mid]
                                                    )
                                                    print(msg.to, [g.mid])
                                                except Exception as e:
                                                    break

                        # ABSEN
                        elif cmd == "absen":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": mid}
                                    cl.sendMessage1(msg)
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Amid}
                                    ki.sendMessage1(msg)
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Bmid}
                                    kk.sendMessage1(msg)
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Cmid}
                                    kc.sendMessage1(msg)
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Zmid}
                                    sw.sendMessage1(msg)

                        # REMOVE CHAT
                        elif text.lower() == "!removechat":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        ki.removeAllMessages(op.param2)
                                        kk.removeAllMessages(op.param2)
                                        kc.removeAllMessages(op.param2)
                                        sw.removeAllMessages(op.param2)
                                        ki.sendText(msg.to, "Chat dibersihkan...")
                                        kk.sendText(msg.to, "Chat dibersihkan...")
                                        kc.sendText(msg.to, "Chat dibersihkan...")
                                        sw.sendText(msg.to, "Chat dibersihkan...")
                                    except BaseException:
                                        pass

                        elif text.lower() == "?removechat":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        cl.removeAllMessages(op.param2)
                                        cl.sendText(msg.to, "Chat dibersihkan...")
                                    except BaseException:
                                        pass

                        # KICKER
                        elif "!kick" in msg.text:
                            if msg._from in Bots:
                                if msg.toType == 2:
                                    print("BOOM❗")
                                    _name = msg.text.replace("!kick", "")
                                    gs = cl.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = kk.getGroup(msg.to)
                                    gs = kc.getGroup(msg.to)
                                    gs = sw.getGroup(msg.to)
                                    ki.sendMessage(
                                        to,
                                        "「 𐀀 HELLTERHEAD WAS HERE! 」\n\n\n"
                                        " █▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░▒▓█\n"
                                        " █▓▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌\n"
                                        "█▓▒▒░░░░░░░ 𐀀 HELLTERHEAD ░░░░░░▒▓█\n"
                                        "█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓\n"
                                        "█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓█\n"
                                        "█▓▓█▒░░░▒█▄▒▒░░░░░░░░▒▒░▄█▒░░░▒█▓▓█\n"
                                        " █▓█▒░▒▒▒░░▀▀█▄▄░░░░▄▄█▀▀░░▒▒▒░▒▒▐██\n"
                                        " █▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░█▀▒▒▒▄▄▄▓▓▒▒▐▓█\n"
                                        " ██▌▒▓███▓████▓▒▐▌░▐▌▒▓████▓███▓▒▐██\n"
                                        " ██▒▒▓███▓▓▓███▓▄░░▄▓████▓▓▓███▓▒▒██\n"
                                        " █▓▒▒▓█████████▓▒░░▒▓█████████▓▒▒▓█\n"
                                        "  █▓▒░▒▓██████▓▓▄▀░▀ ▄▓▓██████▓▒▒▓█\n"
                                        "   █▓▒░▒▒▓▓▓▄▄▄▀▒░░░░▒▀▄▄▄▓▓▓▒▒░▓█\n"
                                        "     █▓▒░▒▒▒░░░░░░▒▒▒░░░░░░▒▒▒░▒▓█\n"
                                        "      █▓▓▒▒░░██░░▒▓█▓▒░░██░░▒▒▓▓█\n"
                                        "      ▀██▓▓▒░░▀░▒▓███▓▒░▀░░▒▓▓██\n"
                                        "       ░▀▓▓▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀\n"
                                        "       ░░█▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██\n\n\n"
                                        "By : DRE❗\n"
                                        "line.me/ti/p/~mo-banzu",
                                    )
                                    kk.sendMessage(
                                        to,
                                        "「 𐀀 HELLTERHEAD WAS HERE! 」\n\n\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n\n"
                                        "RATA GAK RATA TETAP PLAY❗\n"
                                        "SILAHKAN KALAU BISA TANGKIS, ADA KATA TERAKHIR?\n"
                                        "SELAMAT MENIKMATI PERTUNJUKAN\n\n\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n\n"
                                        "By : DRE❗\n"
                                        "line.me/ti/p/~mo-banzu\n"
                                        "line.me/ti/p/~@722tmgxp",
                                    )
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to, "Not found!")
                                    else:
                                        for target in targets:
                                            if target not in Bots:
                                                try:
                                                    klist = [cl, ki, kk, kc, sw]
                                                    kicker = random.choice(klist)
                                                    kicker.kickoutFromGroup(
                                                        msg.to, [target]
                                                    )
                                                    kicker.cancelGroupInvitation(
                                                        op.param1, [_mid]
                                                    )
                                                    print(msg.to, [g.mid])
                                                except BaseException:
                                                    cl.sendMessage(msg.to, "")

                        elif cmd == "hellterhead!" or cmd == "hlth!":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    start = time.time()
                                    cl.sendMessage(msg.to, "[ 𐀀 HELLTERHEAD ]")
                                    elapsed_time = time.time()
                                    ki.sendMessage(
                                        msg.to, "READY❗".format(str(elapsed_time))
                                    )
                                    kk.sendMessage(
                                        msg.to, "READY❗".format(str(elapsed_time))
                                    )
                                    kc.sendMessage(
                                        msg.to, "READY❗".format(str(elapsed_time))
                                    )
                                    sw.sendMessage(msg.to, "DONE❗")
                                    cl.sendMessage(msg.to, "line.me/ti/p/~mo-banzu")

                        elif cmd == "reinvite":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to, Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to, Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to, Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to, Ticket)
                                G = ki.getGroup(msg.to)
                                ki.updateGroup(G)

                        elif cmd == "respon":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ki.sendMessage(msg.to, responsename1)
                                    kk.sendMessage(msg.to, responsename2)
                                    kc.sendMessage(msg.to, responsename3)
                                    sw.sendMessage(msg.to, responsename4)

                        # BOT
                        elif cmd == "stay":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        ginfo = cl.getGroup(msg.to)
                                        cl.inviteIntoGroup(msg.to, [Zmid])
                                    except BaseException:
                                        pass

                        elif cmd == "!in":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    G = cl.getGroup(msg.to)
                                    ginfo = cl.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    ki.acceptGroupInvitationByTicket(msg.to, Ticket)
                                    kk.acceptGroupInvitationByTicket(msg.to, Ticket)
                                    kc.acceptGroupInvitationByTicket(msg.to, Ticket)
                                    G = ki.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)

                        elif cmd == "!out":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    G = cl.getGroup(msg.to)
                                    ki.leaveGroup(msg.to)
                                    kk.leaveGroup(msg.to)
                                    kc.leaveGroup(msg.to)

                        # ASSIST
                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to, Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to, Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGropup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to, Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        # GHOST
                        elif cmd == "ghost in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to, Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ghost out":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        # RESPON SPEED
                        elif cmd == "sprespon":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    get_profile_time_start = time.time()
                                    get_profile = cl.getProfile()
                                    get_profile_time = (
                                        time.time() - get_profile_time_start
                                    )
                                    get_group_time_start = time.time()
                                    get_group = cl.getGroupIdsJoined()
                                    get_group_time = time.time() - get_group_time_start
                                    get_contact_time_start = time.time()
                                    get_contact = cl.getContact(mid)
                                    get_contact_time = (
                                        time.time() - get_contact_time_start
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Respon Speed 」\n\n• Get Profile\n   %.10f\n• Get Contact\n   %.10f\n• Get Group\n   %.10f"
                                        % (
                                            get_profile_time / 3,
                                            get_contact_time / 3,
                                            get_group_time / 3,
                                        ),
                                    )

                        # BOT ON OFF
                        elif "Antijs " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Antijs ", "")
                                if spl == "on":
                                    if msg.to in protectantijs:
                                        msgs = "Anti JS sudah aktif"
                                    else:
                                        protectantijs.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Anti JS Diaktifkan\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectantijs:
                                        protectantijs.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = (
                                            "Anti JS Dinonaktifkan\nDi Group : "
                                            + str(ginfo.name)
                                        )
                                    else:
                                        msgs = "Anti JS sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif "Ghost " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Ghost ", "")
                                if spl == "on":
                                    if msg.to in ghost:
                                        msgs = "Ghost sudah aktif"
                                    else:
                                        ghost.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Diaktifkan\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in ghost:
                                        ghost.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Dinonaktifkan\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    else:
                                        msgs = "Ghost sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        # REVIVE
                        elif cmd == "revive":
                            if msg._from in admin:
                                try:
                                    cl.inviteIntoGroup(
                                        to, ["u20452d2a7b27a3536e1172e4c8d0a8b4"]
                                    )
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    cl.kickoutFromGroup(
                                        to, ["u20452d2a7b27a3536e1172e4c8d0a8b4"]
                                    )
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healty"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healty"
                                else:
                                    sil1 = "Sick"
                                cl.sendMessage(
                                    to,
                                    "「 Kesehatan 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil
                                    ),
                                )
                                try:
                                    ki.inviteIntoGroup(
                                        to, ["ub5eb16f715987714ce367228ffdeb67c"]
                                    )
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    ki.kickoutFromGroup(
                                        to, ["ub5eb16f715987714ce367228ffdeb67c"]
                                    )
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healty"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healty"
                                else:
                                    sil1 = "Sick"
                                ki.sendMessage(
                                    to,
                                    "「 Kesehatan 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil
                                    ),
                                )
                                try:
                                    kk.inviteIntoGroup(
                                        to, ["ub8c4edef669a257681023a4f69826e74"]
                                    )
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    kk.kickoutFromGroup(
                                        to, ["ub8c4edef669a257681023a4f69826e74"]
                                    )
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healty"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healty"
                                else:
                                    sil1 = "Sick"
                                kk.sendMessage(
                                    to,
                                    "「 Kesehatan 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil
                                    ),
                                )
                                try:
                                    kc.inviteIntoGroup(
                                        to, ["u603d3bb1c44e4a1ccb04acf97a0eec6f"]
                                    )
                                    has = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                try:
                                    kc.kickoutFromGroup(
                                        to, ["u603d3bb1c44e4a1ccb04acf97a0eec6f"]
                                    )
                                    has1 = "OK"
                                except BaseException:
                                    has == "OK"
                                if has == "OK":
                                    sil = "Healty"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healty"
                                else:
                                    sil1 = "Sick"
                                kc.sendMessage(
                                    to,
                                    "「 Kesehatan 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil
                                    ),
                                )
                                try:
                                    sw.inviteIntoGroup(
                                        to, ["ubd03637cf11cc36de6f30d55d2723659"]
                                    )
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    sw.kickoutFromGroup(
                                        to, ["ubd03637cf11cc36de6f30d55d2723659"]
                                    )
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healty"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healty"
                                else:
                                    sil1 = "Sick"
                                sw.sendMessage(
                                    to,
                                    "「 Kesehatan 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil
                                    ),
                                )

                        # GROUP LIST
                        elif cmd == "grouplist":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    a = 0
                                    gid = cl.getGroupIdsJoined()
                                    for i in gid:
                                        G = cl.getGroup(i)
                                        a = a + 1
                                        end = "\n"
                                        ma += "╠ " + str(a) + ". " + G.name + "\n"
                                    cl.sendMessage(
                                        msg.to,
                                        "╔══[ GROUP LIST ]\n║\n"
                                        + ma
                                        + "║\n╚══[ Total「"
                                        + str(len(gid))
                                        + "」Groups ]",
                                    )

                        elif cmd == "grouplist1":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = ki.getGroupIdsJoined()
                                for i in gid:
                                    G = ki.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                ki.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total「"
                                    + str(len(gid))
                                    + "」Groups ]",
                                )

                        elif cmd == "grouplist2":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = kk.getGroupIdsJoined()
                                for i in gid:
                                    G = kk.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                kk.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total「"
                                    + str(len(gid))
                                    + "」Groups ]",
                                )

                        elif cmd == "grouplist3":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = kc.getGroupIdsJoined()
                                for i in gid:
                                    G = kc.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                kc.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total「"
                                    + str(len(gid))
                                    + "」Groups ]",
                                )

                        elif cmd == "grouplist4":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = sw.getGroupIdsJoined()
                                for i in gid:
                                    G = sw.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                sw.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total「"
                                    + str(len(gid))
                                    + "」Groups ]",
                                )

                        # LIST SAINT
                        elif cmd == "listadmin":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    a = 0
                                    b = 0
                                    c = 0
                                    for m_id in owner:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in admin:
                                        b = b + 1
                                        end = "\n"
                                        mb += (
                                            str(b)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in staff:
                                        c = c + 1
                                        end = "\n"
                                        mc += (
                                            str(c)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Daftar User Admin 」\n\n"
                                        + mb
                                        + "\nTotal「%s」Admin" % (str(len(admin))),
                                    )

                        elif cmd == "liststaff":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    a = 0
                                    b = 0
                                    c = 0
                                    for m_id in owner:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in admin:
                                        b = b + 1
                                        end = "\n"
                                        mb += (
                                            str(b)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in staff:
                                        c = c + 1
                                        end = "\n"
                                        mc += (
                                            str(c)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Daftar User Staff 」\n\n"
                                        + mc
                                        + "\nTotal「%s」Staff" % (str(len(staff))),
                                    )

                        elif cmd == "listbot":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    a = 0
                                    for m_id in Bots:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Daftar User Bot 」\n\n"
                                        + ma
                                        + "\nTotal「%s」Bot" % (str(len(Bots))),
                                    )

                        # LIST PROTECT
                        elif cmd == "listprotect":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    md = ""
                                    me = ""
                                    a = 0
                                    b = 0
                                    c = 0
                                    d = 0
                                    e = 0
                                    gid = protectqr
                                    for group in gid:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectkick
                                    for group in gid:
                                        b = b + 1
                                        end = "\n"
                                        mb += (
                                            str(b)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectcancel
                                    for group in gid:
                                        c = c + 1
                                        end = "\n"
                                        mc += (
                                            str(c)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectjoin
                                    for group in gid:
                                        d = d + 1
                                        end = "\n"
                                        md += (
                                            str(d)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectinvite
                                    for group in gid:
                                        e = e + 1
                                        end = "\n"
                                        me += (
                                            str(e)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 𐀀 HELLTERHEAD  」\n\n• PROTECT URL :\n"
                                        + ma
                                        + "\n• PROTECT KICK :\n"
                                        + mb
                                        + "\n• PROTECT CANCEL :\n"
                                        + mc
                                        + "\n• PROTECT JOIN :\n"
                                        + md
                                        + "\n• PROTECT INVITE :\n"
                                        + me
                                        + "\n• Total「%s」Protection"
                                        % (
                                            str(
                                                len(protectqr)
                                                + len(protectkick)
                                                + len(protectcancel)
                                                + len(protectjoin)
                                                + len(protectinvite)
                                            )
                                        ),
                                    )

                        # GHOST KICKER
                        elif "Kill! " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        if target not in Bots:
                                            try:
                                                G = cl.getGroup(msg.to)
                                                G.preventedJoinByTicket = False
                                                cl.updateGroup(G)
                                                invsend = 0
                                                Ticket = cl.reissueGroupTicket(msg.to)
                                                sw.acceptGroupInvitationByTicket(
                                                    msg.to, Ticket
                                                )
                                                sw.kickoutFromGroup(msg.to, [target])
                                                sw.leaveGroup(msg.to)
                                                X = cl.getGroup(msg.to)
                                                X.preventedJoinByTicket = True
                                                cl.updateGroup(X)
                                            except BaseException:
                                                pass

                        elif "Kick! " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        if target not in Bots:
                                            try:
                                                random.choice(ABC).kickoutFromGroup(
                                                    msg.to, [target]
                                                )
                                            except BaseException:
                                                pass

                        # BOT UPDATE
                        elif cmd == "bot1pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "bot2pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "bot3pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "bot4pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendText(msg.to, "Kirim fotonya")

                        elif cmd.startswith("bot1name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = ki.getProfile()
                                    profile.displayName = string
                                    ki.updateProfile(profile)
                                    ki.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + ""
                                    )

                        elif cmd.startswith("bot2name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = kk.getProfile()
                                    profile.displayName = string
                                    kk.updateProfile(profile)
                                    kk.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + ""
                                    )

                        elif cmd.startswith("bot3name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = kc.getProfile()
                                    profile.displayName = string
                                    kc.updateProfile(profile)
                                    kc.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + ""
                                    )

                        elif cmd.startswith("bot4name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = sw.getProfile()
                                    profile.displayName = string
                                    sw.updateProfile(profile)
                                    sw.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + ""
                                    )

                        # SAINT
                        elif "Adminadd " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            admin.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan admin"
                                            )
                                        except BaseException:
                                            pass

                        elif "Staffadd " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            staff.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan staff"
                                            )
                                        except BaseException:
                                            pass

                        elif "Botadd " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            Bots.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan bot"
                                            )
                                        except BaseException:
                                            pass

                        elif "Admindell " in msg.text:
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Saints:
                                        try:
                                            admin.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus admin"
                                            )
                                        except BaseException:
                                            pass

                        elif "Staffdell " in msg.text:
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Saints:
                                        try:
                                            staff.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus staff"
                                            )
                                        except BaseException:
                                            pass

                        elif "Botdell " in msg.text:
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Saints:
                                        try:
                                            Bots.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus bot"
                                            )
                                        except BaseException:
                                            pass

                        elif cmd == "admin:on" or text.lower() == "admin:on":
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == "admin:repeat":
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == "staff:on":
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == "staff:repeat":
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == "bot:on":
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == "bot:repeat":
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == "refresh":
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to, "Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == "contact admin":
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact staff" or text.lower() == "contact staff":
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact bot" or text.lower() == "contact bot":
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact on" or text.lower() == "contact on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = True
                                    cl.sendText(msg.to, "Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == "contact off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = False
                                    cl.sendText(msg.to, "Deteksi contact dinonaktifkan")

                        # BANNED
                        elif "Talkban " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            wait["Talkblacklist"][target] = True
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan blacklist"
                                            )
                                        except BaseException:
                                            pass

                        elif "Untalkban " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            del wait["Talkblacklist"][target]
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus blacklist"
                                            )
                                        except BaseException:
                                            pass

                        elif cmd == "talkban:on" or text.lower() == "talkban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Talkwblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == "untalkban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Talkdblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif "Ban " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            wait["blacklist"][target] = True
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan blacklist"
                                            )
                                        except BaseException:
                                            pass

                        elif "Unban " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            del wait["blacklist"][target]
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus blacklist"
                                            )
                                        except BaseException:
                                            pass

                        elif cmd == "ban:on" or text.lower() == "ban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["wblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == "unban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["dblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == "banlist":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if wait["blacklist"] == {}:
                                        cl.sendMessage(msg.to, "Tidak ada banlist")
                                    else:
                                        ma = ""
                                        a = 0
                                        for m_id in wait["blacklist"]:
                                            a = a + 1
                                            end = "\n"
                                            ma += (
                                                str(a)
                                                + ". "
                                                + cl.getContact(m_id).displayName
                                                + "\n"
                                            )
                                        cl.sendMessage(
                                            msg.to,
                                            "• Blacklist User\n\n"
                                            + ma
                                            + "\n• Total「%s」Blacklist User"
                                            % (str(len(wait["blacklist"]))),
                                        )

                        elif cmd == "talkbanlist" or text.lower() == "talkbanlist":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if wait["Talkblacklist"] == {}:
                                        cl.sendMessage(msg.to, "Tidak ada talkban user")
                                    else:
                                        ma = ""
                                        a = 0
                                        for m_id in wait["Talkblacklist"]:
                                            a = a + 1
                                            end = "\n"
                                            ma += (
                                                str(a)
                                                + ". "
                                                + cl.getContact(m_id).displayName
                                                + "\n"
                                            )
                                        cl.sendMessage(
                                            msg.to,
                                            "「 𐀀 HELLTERHEAD 」\n• Talkban User\n\n"
                                            + ma
                                            + "\n• Total「%s」Talkban User"
                                            % (str(len(wait["Talkblacklist"]))),
                                        )

                        elif cmd == "blacklist" or text.lower() == "blc":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if wait["blacklist"] == {}:
                                        cl.sendMessage(msg.to, "Tidak ada blacklist")
                                    else:
                                        ma = ""
                                        for i in wait["blacklist"]:
                                            ma = cl.getContact(i)
                                            cl.sendMessage(
                                                msg.to,
                                                None,
                                                contentMetadata={"mid": i},
                                                contentType=13,
                                            )

                        elif cmd == "clearban" or text.lower() == "clb":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["blacklist"] = {}
                                    ragets = cl.getContacts(wait["blacklist"])
                                    mc = "「%i」User Blacklist" % len(ragets)
                                    cl.sendMessage(msg.to, "Sukses membersihkan" + mc)

                        # TAG ALL
                        elif msg.text in ["Tagall"]:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama) // 20
                                for a in range(k + 1):
                                    txt = u""
                                    s = 0
                                    b = []
                                    for i in group.members[a * 20 : (a + 1) * 20]:
                                        b.append(
                                            {"S": str(s), "E": str(s + 6), "M": i.mid}
                                        )
                                        s += 7
                                        txt += u"@Zero \n"
                                    cl.sendMessage(
                                        msg.to,
                                        text=txt,
                                        contentMetadata={
                                            u"MENTION": json.dumps({"MENTIONEES": b})
                                        },
                                        contentType=0,
                                    )

                        # LEAVE
                        elif cmd == "?bye":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    G = cl.getGroup(msg.to)
                                    cl.sendText(msg.to, "Bye! " + str(G.name))
                                    cl.leaveGroup(msg.to)

                        # CODE GAME
                        elif text.lower() == "codelp":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to, "「 LINE PLAY 」\n\n Ava Code : HH-7079-6405"
                                )

                        elif text.lower() == "codezpt":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to, "「 ZEPETO 」\n\n Ava Code : UTEUW4"
                                )
                                cl.sendMessage(
                                    msg.to,
                                    "https://zepeto.me/qr?zepeto://HOME/PROFILE/CARD?UTEUW4",
                                )

                        #RESPON TIME
                        elif cmd == "rtime":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    get_profile_time_start = time.time()
                                    get_profile = cl.getProfile()
                                    get_profile_time = (
                                        time.time() - get_profile_time_start
                                    )
                                    get_group_time_start = time.time()
                                    get_group = cl.getGroupIdsJoined()
                                    get_group_time = time.time() - get_group_time_start
                                    get_contact_time_start = time.time()
                                    get_contact = cl.getContact(mid)
                                    get_contact_time = (
                                        time.time() - get_contact_time_start
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Respontime 」\n\n • Get Profile\n   %.10f\n • Get Contact\n   %.10f\n • Get Group\n   %.10f"
                                        % (
                                            get_profile_time / 3,
                                            get_contact_time / 3,
                                            get_group_time / 3,
                                        ),
                                    )

                        # SPEED
                        elif cmd == "speed" or cmd == "sp":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    start = time.time()
                                    time.sleep(0.0009)
                                    elapsed_time = time.time() - start
                                    cl.sendMessage(
                                        msg.to, "{} Second".format(str(elapsed_time))
                                    )
                                    ki.sendMessage(
                                        msg.to, "{} Second".format(str(elapsed_time))
                                    )
                                    kk.sendMessage(
                                        msg.to, "{} Second".format(str(elapsed_time))
                                    )
                                    kc.sendMessage(
                                        msg.to, "{} Second".format(str(elapsed_time))
                                    )
                                    sw.sendMessage(
                                        msg.to, "{} Second".format(str(elapsed_time))
                                    )

                        # LURKING
                        elif cmd == "lurking on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    Setmain["RAreadPoint"][msg.to] = msg_id
                                    Setmain["RAreadMember"][msg.to] = {}
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Lurking 」\nBerhasil diaktifkan\n\n• Jam [ "
                                        + datetime.strftime(timeNow, "%H:%M:%S")
                                        + " ]"
                                        + "\n• Tanggal : "
                                        + datetime.strftime(timeNow, "%Y-%m-%d"),
                                    )

                        elif cmd == "lurking off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    del Setmain["RAreadPoint"][msg.to]
                                    del Setmain["RAreadMember"][msg.to]
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Lurking 」\nBerhasil dinonaktifkan\n\n• Jam [ "
                                        + datetime.strftime(timeNow, "%H:%M:%S")
                                        + " ]"
                                        + "\n• Tanggal : "
                                        + datetime.strftime(timeNow, "%Y-%m-%d"),
                                    )

                        elif cmd == "lurkers":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.to in Setmain["RAreadPoint"]:
                                        if Setmain["RAreadMember"][msg.to] != {}:
                                            aa = []
                                            for x in Setmain["RAreadMember"][msg.to]:
                                                aa.append(x)
                                            try:
                                                arrData = ""
                                                textx = "  「 Daftar Member 」\n\n「 Total {} Sider 」\n".format(
                                                    str(len(aa))
                                                )
                                                arr = []
                                                no = 1
                                                b = 1
                                                for i in aa:
                                                    b = b + 1
                                                    end = "\n"
                                                    mention = "@x\n"
                                                    slen = str(len(textx))
                                                    elen = str(
                                                        len(textx) + len(mention) - 1
                                                    )
                                                    arrData = {
                                                        "S": slen,
                                                        "E": elen,
                                                        "M": i,
                                                    }
                                                    arr.append(arrData)
                                                    tz = pytz.timezone("Asia/Jakarta")
                                                    timeNow = datetime.now(tz=tz)
                                                    textx += mention
                                                    if no < len(aa):
                                                        no += 1
                                                        textx += str(b) + ". "
                                                    else:
                                                        try:
                                                            no = "[ {} ]".format(
                                                                str(
                                                                    cl.getGroup(
                                                                        msg.to
                                                                    ).name
                                                                )
                                                            )
                                                        except BaseException:
                                                            no = "  "
                                                msg.to = msg.to
                                                msg.text = (
                                                    textx
                                                    + "\n• Jam [ "
                                                    + datetime.strftime(
                                                        timeNow, "%H:%M:%S"
                                                    )
                                                    + " ]"
                                                    + "\n• Tanggal : "
                                                    + datetime.strftime(
                                                        timeNow, "%Y-%m-%d"
                                                    )
                                                )
                                                msg.contentMetadata = {
                                                    "MENTION": str(
                                                        '{"MENTIONEES":'
                                                        + json.dumps(arr)
                                                        + "}"
                                                    )
                                                }
                                                msg.contentType = 0
                                                cl.sendMessage1(msg)
                                            except BaseException:
                                                pass
                                            try:
                                                del Setmain["RAreadPoint"][msg.to]
                                                del Setmain["RAreadMember"][msg.to]
                                            except BaseException:
                                                pass
                                            Setmain["RAreadPoint"][msg.to] = msg.id
                                            Setmain["RAreadMember"][msg.to] = {}
                                        else:
                                            cl.sendText(msg.to, "User kosong!")
                                    else:
                                        cl.sendText(msg.to, "Ketik lurking on dulu")

                        # SIDER
                        elif cmd == "sider on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        cl.sendMessage(
                                            msg.to,
                                            "「 Status Sider 」\n\nBerhasil diaktifkan\n\n• Jam [ "
                                            + datetime.strftime(timeNow, "%H:%M:%S")
                                            + " ]"
                                            + "\n• Tanggal : "
                                            + datetime.strftime(timeNow, "%Y-%m-%d"),
                                        )
                                        del cctv["point"][msg.to]
                                        del cctv["sidermem"][msg.to]
                                        del cctv["cyduk"][msg.to]
                                    except BaseException:
                                        pass
                                    cctv["point"][msg.to] = msg.id
                                    cctv["sidermem"][msg.to] = ""
                                    cctv["cyduk"][msg.to] = True

                        elif cmd == "sider off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.to in cctv["point"]:
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        cctv["cyduk"][msg.to] = False
                                        cl.sendMessage(
                                            msg.to,
                                            "「 Status Sider 」\n\nBerhasil dinonaktifkan\n\n• Jam [ "
                                            + datetime.strftime(timeNow, "%H:%M:%S")
                                            + " ]"
                                            + "\n• Tanggal : "
                                            + datetime.strftime(timeNow, "%Y-%m-%d"),
                                        )
                                    else:
                                        cl.sendMessage(msg.to, "Sudah tidak aktif")

                        # FANSIGN
                        elif cmd.startswith("fansign: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                anu = msg.text.replace(sep[0] + " ", " ")
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    r = web.get(
                                        "https://farzain.xyz/api/premium/fs.php?apikey=apikey_saintsbot&id={}".format(
                                            urllib.parse.quote(anu)
                                        )
                                    )
                                    data = r.text
                                    data = json.loads(data)
                                    if data["status"] == "success":
                                        ret_ = data["url"]
                                        cl.sendImageWithURL(msg.to, ret_)
                                    else:
                                        cl.sendMessage(msg.to, "Error")

                        # POST
                        elif cmd.startswith("post: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                post = msg.text.replace(sep[0] + " ", "")
                                with requests.session() as s:
                                    s.headers[
                                        "user-agent"
                                    ] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = s.get(
                                        "http://m.jancok.com/klik/{}/".format(
                                            urllib.parse.quote(post)
                                        )
                                    )
                                    soup = BeautifulSoup(r.content, "html5lib")
                                    ret_ = "「 Postingan 」\n\n"
                                    try:
                                        for title in soup.select(
                                            "[class~=badge-item-title]"
                                        ):
                                            ret_ += "• Judul : " + title.get_text()
                                            ret_ += "\n• Link : m.jancok.com"
                                        for link in soup.find_all("img", limit=1):
                                            cl.sendMessage(msg.to, ret_)
                                            cl.sendImageWithURL(msg.to, link.get("src"))
                                    except Exception as e:
                                        cl.sendMessage(msg.to, "Post kosong")
                                        print(str(e))

                        # LINE
                        elif cmd.startswith("line: "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                user = text.replace(sep[0] + " ", "")
                                conn = cl.findContactsByUserid(user)
                                try:
                                    anu = conn.mid
                                    dn = conn.displayName
                                    bio = conn.statusMessage
                                    sendMention(
                                        to,
                                        anu,
                                        "「 Contact Line ID 」\n• Nama : ",
                                        "\n• Nick : "
                                        + dn
                                        + "\n• Bio : "
                                        + bio
                                        + "\n• Contact Link : http://line.me/ti/p/~"
                                        + user,
                                    )
                                    cl.sendContact(to, anu)
                                except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        # INVITE
                        elif cmd.startswith("invite: "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                nick = text.replace(sep[0] + " ", "")
                                conn = cl.findContactsByUserid(nick)
                                cl.findAndAddContactsByMid(conn.mid)
                                cl.inviteIntoGroup(msg.to, [conn.mid])
                                group = cl.getGroup(msg.to)
                                xname = cl.getContact(conn.mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = "「 Sukses Diinvite 」\nNama contact "
                                recky = str(xname.displayName)
                                pesan = ""
                                pesan2 = pesan + "@a\n"
                                xlen = str(len(zxc) + len(xpesan))
                                xlen2 = str(len(zxc) + len(pesan2) + len(xpesan) - 1)
                                zx = {"S": xlen, "E": xlen2, "M": xname.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + "ke grup " + str(group.name) + ""
                                cl.sendMessage(
                                    receiver,
                                    text,
                                    contentMetadata={
                                        "MENTION": str(
                                            '{"MENTIONEES":'
                                            + json.dumps(zx2).replace(" ", "")
                                            + "}"
                                        )
                                    },
                                    contentType=0,
                                )

                        # YOUTUBE
                        elif cmd.startswith("youtube: "):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ", "")
                            params = {"search_query": search}
                            r = requests.get(
                                "https://www.youtube.com/results", params=params
                            )
                            soup = BeautifulSoup(r.content, "html5lib")
                            ret_ = "╔══[ Result Youtube ]"
                            datas = []
                            for data in soup.select(".yt-lockup-title > a[title]"):
                                if "&lists" not in data["href"]:
                                    datas.append(data)
                            for data in datas:
                                ret_ += "\n╠═ [ {} ]".format(str(data["title"]))
                                ret_ += "\n╠══ https://www.youtube.com{}".format(
                                    str(data["href"])
                                )
                            ret_ += "\n╚══[ Total {} Video ]".format(len(datas))
                            cl.sendMessage(to, str(ret_))

                        # MEME
                        elif cmd.startswith("meme: "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ", "")
                                query = keyword.split("|")
                                atas = query[0]
                                bawah = query[1]
                                r = requests.get("https://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                try:
                                    num = int(query[2])
                                    namamem = data["data"]["memes"][num - 1]
                                    meme = int(namamem["id"])
                                    api = pyimgflip.Imgflip(username="", password="")
                                    result = api.caption_image(meme, atas, bawah)
                                    sendMention(
                                        msg.to,
                                        msg._from,
                                        "「 Meme Image 」\nTunggu ",
                                        "\nFoto sedang diproses...",
                                    )
                                    cl.sendImageWithURL(msg.to, result["url"])
                                except Exception as e:
                                    cl.sendText(msg.to, " " + str(e))

                        elif cmd.startswith("listmeme"):
                            if msg._from in admin:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ", "")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "「 Daftar Meme Image 」\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". " + str(aa["name"])
                                    hasil += " "
                                    ret_ = "\n\nSelanjutnya ketik:\nListmeme | angka\nGet-meme text1 | text2 | angka"
                                    cl.sendText(msg.to, hasil + ret_)
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        sendMention(
                                            msg.to,
                                            msg._from,
                                            "「 Meme Image 」\nTunggu ",
                                            "\nFoto sedang diproses...",
                                        )
                                        cl.sendText(msg.to, hasil)
                                        cl.sendImageWithURL(msg.to, gambar["url"])
                                    except Exception as e:
                                        cl.sendText(msg.to, " " + str(e))

                        # GIF
                        elif cmd.startswith("gif: "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ", "")
                                count = urutan.split("|")
                                search = str(count[0])
                                r = requests.get(
                                    "https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="
                                    + str(search)
                                )
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "「 Pencarian Gif 」\n"
                                    for aa in data["results"]:
                                        no += 1
                                        hasil += (
                                            "\n" + str(no) + ". " + str(aa["title"])
                                        )
                                        ret_ = "\n\nSelanjutnya Get-gif {} | angka\nuntuk melihat detail video".format(
                                            str(search)
                                        )
                                    cl.sendText(msg.to, hasil + ret_)
                                elif len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        b = data["results"][num - 1]
                                        c = str(b["id"])
                                        hasil = "Informasi gif ID " + str(c)
                                        hasil += "\n"
                                        cl.sendText(msg.to, hasil)
                                        dl = str(b["media"][0]["loopedmp4"]["url"])
                                        cl.sendVideoWithURL(msg.to, dl)
                                    except Exception as e:
                                        cl.sendText(msg.to, " " + str(e))

                        # CUACA
                        elif cmd.startswith("cuaca: "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                location = text.replace(separate[0] + " ", "")
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    r = web.get(
                                        "http://api.corrykalam.net/apicuaca.php?kota={}".format(
                                            urllib.parse.quote(location)
                                        )
                                    )
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "「 Status Cuaca 」\n"
                                        ret_ += "\n• Lokasi : " + data[0].replace(
                                            "Temperatur di kota ", ""
                                        )
                                        ret_ += (
                                            "\n• Suhu : "
                                            + data[1].replace("Suhu : ", "")
                                            + " C"
                                        )
                                        ret_ += (
                                            "\n• Kelembaban : "
                                            + data[2].replace("Kelembaban : ", "")
                                            + " %"
                                        )
                                        ret_ += (
                                            "\n• Tekanan Udara : "
                                            + data[3].replace("Tekanan udara : ", "")
                                            + " HPa"
                                        )
                                        ret_ += (
                                            "\n• Kecepatan Angin : "
                                            + data[4].replace("Kecepatan angin : ", "")
                                            + " m/s"
                                        )
                                        ret_ += "\n\nJam : " + datetime.strftime(
                                            timeNow, "%H:%M:%S"
                                        )
                                        ret_ += "\nTanggal : " + datetime.strftime(
                                            timeNow, "%Y-%m-%d"
                                        )
                                    cl.sendMessage(msg.to, str(ret_))
                        # LOKASI
                        elif cmd.startswith("lokasi: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ", "")
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    r = web.get(
                                        "http://api.corrykalam.net/apiloc.php?lokasi={}".format(
                                            urllib.parse.quote(location)
                                        )
                                    )
                                    data = r.text
                                    data = json.loads(data)
                                    if (
                                        data[0] != ""
                                        and data[1] != ""
                                        and data[2] != ""
                                    ):
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(
                                            str(data[1]), str(data[2])
                                        )
                                        ret_ = "「 Info Lokasi 」"
                                        ret_ += "\n•  Location : " + data[0]
                                        ret_ += "\n•  Google Maps : " + link
                                    else:
                                        ret_ = "[Details Location] Error : Location not found"
                                    cl.sendMessage(msg.to, str(ret_))

                        # MUSIC
                        elif cmd.startswith("music: "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                url = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = url.json()
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Music ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk mengirim music, silahkan gunakan command {}Music {}|「number」".format(str(setKey), str(search))
                                    cl.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        url = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = url.json()
                                        ret_ = "╔══[ Music ] "
                                        ret_ += "\n╠ Title : {}".format(str(data["result"]["song"]))
                                        ret_ += "\n╠ Album : {}".format(str(data["result"]["album"]))
                                        ret_ += "\n╠ Size : {}".format(str(data["result"]["size"]))
                                        ret_ += "\n╠ Link : {}".format(str(data["result"]["mp3"][0]))
                                        ret_ += "\n╚══[ Finish ]"
                                        cl.sendImageWithURL(to, str(data["result"]["img"]))
                                        cl.sendMessage(to, str(ret_))
                                        cl.sendAudioWithURL(to, str(data["result"]["mp3"][0]))

                        # LYRIC
                        elif cmd.startswith("lyric: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ", "")
                                params = {"songname": search}
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    r = web.get(
                                        "https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(
                                            urllib.parse.urlencode(params)
                                        )
                                    )
                                    try:
                                        data = json.loads(r.text)
                                        for song in data:
                                            songs = song[5]
                                            lyric = songs.replace("ti:", "Title - ")
                                            lyric = lyric.replace("ar:", "Artist - ")
                                            lyric = lyric.replace("al:", "Album - ")
                                            removeString = "[1234567890.:]"
                                            for char in removeString:
                                                lyric = lyric.replace(char, "")
                                            ret_ = "╔══[ Lyric ]"
                                            ret_ += "\n╠ Song : {}".format(
                                                str(song[0])
                                            )
                                            ret_ += "\n╠ Duration : {}".format(
                                                str(song[1])
                                            )
                                            ret_ += "\n╠ Link : {}".format(str(song[3]))
                                            ret_ += "\n╚══[ Finish ]\n\nLyric :\n{}".format(
                                                str(lyric)
                                            )
                                            cl.sendText(msg.to, str(ret_))
                                    except BaseException:
                                        cl.sendText(to, "Lyric not found")

                        # IMAGE
                        elif cmd.startswith("image: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ", "")
                                url = "https://api.xeonwz.ga/api/image/google?q={}".format(
                                    urllib.parse.quote(search)
                                )
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    r = web.get(url)
                                    data = r.text
                                    data = json.loads(data)
                                    if data["data"] != []:
                                        start = timeit.timeit()
                                        items = data["data"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        cl.sendText(
                                            msg.to,
                                            "「Google Image」\nType : Search Image\nTime Taken : %seconds"
                                            % (start),
                                        )
                                        cl.sendImageWithURL(msg.to, str(path))

                        # YOUTUBE MP3
                        elif cmd.startswith("ytmp3: "):
                            if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ", "")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url = (
                                        "https://www.youtube.com/results?search_query="
                                    )
                                    mozhdr = {
                                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3"
                                    }
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers=mozhdr)
                                    soupeddata = BeautifulSoup(
                                        sb_get.content, "html.parser"
                                    )
                                    yt_links = soupeddata.find_all(
                                        "a", class_="yt-uix-tile-link"
                                    )
                                    x = yt_links[1]
                                    yt_href = x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    bestaudio = vid.getbestaudio()
                                    bestaudio.bitrate
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        shi = bestaudio.url
                                        me = best.url
                                        vin = s.url
                                        hasil = ""
                                        title = "• Judul : " + str(vid.title)
                                        author = "\n• Author : " + str(vid.author)
                                        durasi = "\n• Duration : " + str(vid.duration)
                                        suka = "\n• Likes : " + str(vid.likes)
                                        rating = "\n• Rating : " + str(vid.rating)
                                        deskripsi = "\n• Descriotion : " + str(
                                            vid.description
                                        )
                                    cl.sendImageWithURL(msg.to, me)
                                    cl.sendAudioWithURL(msg.to, shi)
                                    cl.sendText(
                                        msg.to,
                                        title
                                        + author
                                        + durasi
                                        + suka
                                        + rating
                                        + deskripsi,
                                    )
                                except Exception as e:
                                    cl.sendText(msg.to, str(e))

                        # YOUTUBE MP4
                        elif cmd.startswith("ytmp4: "):
                            if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ", "")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url = (
                                        "https://www.youtube.com/results?search_query="
                                    )
                                    mozhdr = {
                                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3"
                                    }
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers=mozhdr)
                                    soupeddata = BeautifulSoup(
                                        sb_get.content, "html.parser"
                                    )
                                    yt_links = soupeddata.find_all(
                                        "a", class_="yt-uix-tile-link"
                                    )
                                    x = yt_links[1]
                                    yt_href = x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        me = best.url
                                        hasil = ""
                                        title = "• Judul : " + str(vid.title)
                                        author = "\n• Author : " + str(vid.author)
                                        durasi = "\n• Duration : " + str(vid.duration)
                                        suka = "\n• Likes : " + str(vid.likes)
                                        rating = "\n• Rating : " + str(vid.rating)
                                        deskripsi = "\n• Description : " + str(
                                            vid.description
                                        )
                                    cl.sendVideoWithURL(msg.to, me)
                                    cl.sendText(
                                        msg.to,
                                        title
                                        + author
                                        + durasi
                                        + suka
                                        + rating
                                        + deskripsi,
                                    )
                                except Exception as e:
                                    cl.sendText(msg.to, str(e))

                        # CCTV
                        elif cmd.startswith("kode wilayah"):
                            if msg._from in admin:
                                ret_ = "「 Daftar Kode Wilayah 」\n\n"
                                ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                                ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                                ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                                ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                                ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                                ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                                ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                                ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                                ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                                ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                                ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                                ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                                ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                                ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                                ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                                ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                                ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                                cl.sendMessage(to, ret_)

                        elif cmd.startswith("cctv: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                cct = msg.text.replace(sep[0] + " ", "")
                                with requests.session() as s:
                                    s.headers[
                                        "user-agent"
                                    ] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = s.get(
                                        "http://lewatmana.com/cam/{}/bundaran-hi/".format(
                                            urllib.parse.quote(cct)
                                        )
                                    )
                                    soup = BeautifulSoup(r.content, "html5lib")
                                    try:
                                        ret_ = "「 Informasi CCTV 」\nDaerah "
                                        ret_ += soup.select(
                                            "[class~=cam-viewer-title]"
                                        )[0].text
                                        ret_ += "\nCCTV update per 5 menit"
                                        vid = soup.find("source")["src"]
                                        ret = "Untuk melihat wilayah lainnya, Ketik kode wilayah"
                                        cl.sendMessage(to, ret_)
                                        cl.sendVideoWithURL(to, vid)
                                        cl.sendMessage(to, ret)
                                    except BaseException:
                                        cl.sendMessage(to, "Data cctv tidak ditemukan!")

                        # APK
                        elif cmd.startswith("apk: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ", "")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers["user-agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    r = s.get(
                                        "https://apkpure.com/id/search?q={}".format(
                                            str(search)
                                        )
                                    )
                                    soup = BeautifulSoup(r.content, "html5lib")
                                    data = soup.findAll(
                                        "dl", attrs={"class": "search-dl"}
                                    )
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "「 Pencarian Aplikasi 」\n"
                                        for apk in data:
                                            num += 1
                                            link = (
                                                "https://apkpure.com"
                                                + apk.find("a")["href"]
                                            )
                                            title = apk.find("a")["title"]
                                            ret_ += "\n {}. {}".format(
                                                str(num), str(title)
                                            )
                                        ret_ += "\n\n Total {} Result".format(
                                            str(len(data))
                                        )
                                        ret = "Selanjutnya ketik:\nGet-apk {} | angka".format(
                                            str(search)
                                        )
                                        cl.sendMessage(to, str(ret_))
                                        cl.sendMessage(to, str(ret))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            apk = data[num - 1]
                                            with requests.session() as s:
                                                s.headers["user-agent"] = random.choice(
                                                    settings["userAgent"]
                                                )
                                                r = s.get(
                                                    "https://apkpure.com{}/download?from=details".format(
                                                        str(apk.find("a")["href"])
                                                    )
                                                )
                                                soup = BeautifulSoup(
                                                    r.content, "html5lib"
                                                )
                                                data = soup.findAll(
                                                    "div",
                                                    attrs={
                                                        "class": "fast-download-box"
                                                    },
                                                )
                                                for down in data:
                                                    load = down.select(
                                                        "a[href*=https://download.apkpure.com/]"
                                                    )[0]
                                                    file = load["href"]
                                                    ret_ = (
                                                        "File info :\n"
                                                        + down.find(
                                                            "span",
                                                            attrs={"class": "file"},
                                                        ).text
                                                    )
                                                    with requests.session() as web:
                                                        web.headers[
                                                            "user-agent"
                                                        ] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                        r = web.get(
                                                            "https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(
                                                                urllib.parse.quote(file)
                                                            )
                                                        )
                                                        data = r.text
                                                        data = json.loads(data)
                                                        ret_ += (
                                                            "\nLink Download :\n"
                                                            + data["data"]["url"]
                                                        )
                                                    cl.sendMessage(to, str(ret_))

                        # ANIME
                        elif cmd.startswith("anime: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                anime = msg.text.replace(sep[0] + " ", "%20")
                                with requests.session() as web:
                                    web.headers[
                                        "user-agent"
                                    ] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = web.get(
                                    "https://kitsu.io/api/edge/anime?filter[text]={}".format(
                                        urllib.parse.quote(anime)
                                    )
                                )
                                data = r.text
                                data = json.loads(data)
                                ret_ = ""
                                if data["data"] != []:
                                    for a in data["data"]:
                                        if a["attributes"]["subtype"] == "TV":
                                            sin = a["attributes"]["synopsis"]
                                            translator = Translator()
                                            hasil = translator.translate(sin, dest="id")
                                            sinop = hasil.text
                                            ret_ += "「 Anime {} 」".format(
                                                str(a["attributes"]["canonicalTitle"])
                                            )
                                            ret_ += "\n• Rilis : " + str(
                                                a["attributes"]["startDate"]
                                            )
                                            ret_ += "\n• Rating : " + str(
                                                a["attributes"]["ratingRank"]
                                            )
                                            ret_ += "\n• Type : " + str(
                                                a["attributes"]["subtype"]
                                            )
                                            ret_ += "\n• Sinopsis :\n" + str(sinop)
                                            ret_ += "\n\n"
                                            cl.sendImageWithURL(
                                                msg.to,
                                                str(
                                                    a["attributes"]["posterImage"][
                                                        "small"
                                                    ]
                                                ),
                                            )
                                cl.sendMessage(msg.to, str(ret_))

                        # ZODIAK
                        elif cmd.startswith("zodiak: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ", "")
                                r = requests.post(
                                    "https://aztro.herokuapp.com/?sign={}&day=today".format(
                                        urllib.parse.quote(query)
                                    )
                                )
                                data = r.text
                                data = json.loads(data)
                                data1 = data["description"]
                                data2 = data["color"]
                                translator = Translator()
                                hasil = translator.translate(data1, dest="id")
                                hasil1 = translator.translate(data2, dest="id")
                                A = hasil.text
                                B = hasil1.text
                                ret_ = "「 Ramalan zodiak {} hari ini 」\n".format(
                                    str(query)
                                )
                                ret_ += str(A)
                                ret_ += "\n\n• Tanggal : " + str(data["current_date"])
                                ret_ += "\n• Rasi Bintang : " + query
                                ret_ += " (" + str(data["date_range"] + ")")
                                ret_ += "\n• Pasangan Zodiak : " + str(
                                    data["compatibility"]
                                )
                                ret_ += "\n• Angka Keberuntungan : " + str(
                                    data["lucky_number"]
                                )
                                ret_ += "\n• Waktu Keberuntungan : " + str(
                                    data["lucky_time"]
                                )
                                ret_ += "\n• Warna Kesukaan : " + str(B)
                                cl.sendMessage(msg.to, str(ret_))

                        # BINTANG
                        elif cmd.startswith("bintang: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ", "")
                                with requests.session() as s:
                                    s.headers[
                                        "user-agent"
                                    ] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = s.get(
                                        "https://www.vemale.com/zodiak/{}".format(
                                            urllib.parse.quote(url)
                                        )
                                    )
                                    soup = BeautifulSoup(r.content, "html5lib")
                                    ret_ = ""
                                    for a in soup.select("div.vml-zodiak-detail"):
                                        ret_ += a.h1.string
                                        ret_ += "\n" + a.h4.string
                                        ret_ += " : " + a.span.string + ""
                                    for b in soup.select("div.col-center"):
                                        ret_ += "\n• Tanggal : " + b.string
                                    for d in soup.select("div.number-zodiak"):
                                        ret_ += "\n• Angka Keberuntungan : " + d.string
                                    for c in soup.select("div.paragraph-left"):
                                        ta = c.text
                                        tab = ta.replace("    ", "")
                                        tabs = tab.replace(".", ".\n")
                                        ret_ += "\n" + tabs
                                        # print (ret_)
                                    cl.sendMessage(msg.to, str(ret_))

                        # PRANK TELEPON
                        elif cmd.startswith("telepon: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                nomor = text.replace(sep[0] + " ", "")
                                r = requests.get(
                                    "http://apisora2.herokuapp.com/prank/call/?no={}".format(
                                        urllib.parse.quote(nomor)
                                    )
                                )
                                data = r.text
                                data = json.loads(data)
                                ret_ = "「 Pranked Telepon 」"
                                ret_ += "\n• Status : {}".format(str(data["status"]))
                                ret_ += "\n• Tujuan " + str(data["result"])
                                cl.sendMessage(msg.to, str(ret_))

                        # PRANK SMS
                        elif cmd.startswith("sms: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                nomor = text.replace(sep[0] + " ", "")
                                r = requests.get(
                                    "http://apisora2.herokuapp.com/prank/sms/?no={}".format(
                                        urllib.parse.quote(nomor)
                                    )
                                )
                                data = r.text
                                data = json.loads(data)
                                ret_ = "「 Pranked SMS 」"
                                ret_ += "\n• Status : {}".format(str(data["status"]))
                                ret_ += "\n• Tujuan " + str(data["result"])
                                cl.sendMessage(msg.to, str(ret_))

                        # VIDEO
                        elif cmd.startswith("video: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ", "")
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    url = web.get(
                                        "http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(
                                            urllib.parse.quote(search)
                                        )
                                    )
                                    data = url.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        video = random.choice(
                                            data["result"]["videolist"]
                                        )
                                        vid = video["url"]
                                        start = timeit.timeit()
                                        ret = "「 Informasi Video 」\n"
                                        ret += "• Judul : {}".format(
                                            str(data["result"]["title"])
                                        )
                                        ret += "\n• Author : {}".format(
                                            str(data["result"]["author"])
                                        )
                                        ret += "\n• Durasi : {}".format(
                                            str(data["result"]["duration"])
                                        )
                                        ret += "\n• Like : {}".format(
                                            str(data["result"]["likes"])
                                        )
                                        ret += "\n• Rating : {}".format(
                                            str(data["result"]["rating"])
                                        )
                                        ret += "\n• Time Taken : {}".format(str(start))
                                        ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(
                                            str(data["result"]["description"])
                                        )
                                        cl.sendText(msg.to, str(ret))
                                        cl.sendVideoWithURL(msg.to, str(vid))

                        # MP3
                        elif cmd.startswith("mp3: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ", "")
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(
                                        settings["userAgent"]
                                    )
                                    url = web.get(
                                        "http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(
                                            urllib.parse.quote(search)
                                        )
                                    )
                                    data = url.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        audio = random.choice(
                                            data["result"]["audiolist"]
                                        )
                                        aud = audio["url"]
                                        start = timeit.timeit()
                                        ret = "「 Informasi Mp3 」\n"
                                        ret += "• Judul : {}".format(
                                            str(data["result"]["title"])
                                        )
                                        ret += "\n• Author : {}".format(
                                            str(data["result"]["author"])
                                        )
                                        ret += "\n• Durasi : {}".format(
                                            str(data["result"]["duration"])
                                        )
                                        ret += "\n• Like : {}".format(
                                            str(data["result"]["likes"])
                                        )
                                        ret += "\n• Rating : {}".format(
                                            str(data["result"]["rating"])
                                        )
                                        ret += "\n• Time Taken : {}".format(str(start))
                                        ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(
                                            str(data["result"]["description"])
                                        )
                                        cl.sendText(msg.tpppo, str(ret))
                                        cl.sendAudioWithURL(msg.to, str(aud))

                        # INSTAGRAM
                        elif cmd.startswith("instagram: "):
                            if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    instagram = msg.text.replace(sep[0] + " ", "")
                                    response = requests.get(
                                        "https://www.instagram.com/"
                                        + instagram
                                        + "?__a=1"
                                    )
                                    data = response.json()
                                    namaIG = str(data["graphql"]["user"]["full_name"])
                                    bioIG = str(data["graphql"]["user"]["biography"])
                                    mediaIG = str(
                                        data["graphql"]["user"][
                                            "edge_owner_to_timeline_media"
                                        ]["count"]
                                    )
                                    verifIG = str(
                                        data["graphql"]["user"]["is_verified"]
                                    )
                                    usernameIG = str(
                                        data["graphql"]["user"]["username"]
                                    )
                                    followerIG = str(
                                        data["graphql"]["user"]["edge_followed_by"][
                                            "count"
                                        ]
                                    )
                                    profileIG = data["graphql"]["user"][
                                        "profile_pic_url_hd"
                                    ]
                                    privateIG = str(
                                        data["graphql"]["user"]["is_private"]
                                    )
                                    followIG = str(
                                        data["graphql"]["user"]["edge_follow"]["count"]
                                    )
                                    link = (
                                        "• Link : "
                                        + "https://www.instagram.com/"
                                        + instagram
                                    )
                                    text = (
                                        "「 Instagram User 」\n• Name : "
                                        + namaIG
                                        + "\n• Username : "
                                        + usernameIG
                                        + "\n• Follower : "
                                        + followerIG
                                        + "\n• Following : "
                                        + followIG
                                        + "\n• Total post : "
                                        + mediaIG
                                        + "\n• Verified : "
                                        + verifIG
                                        + "\n• Private : "
                                        + privateIG
                                        + "\n• Biography : "
                                        + bioIG
                                        + ""
                                        "\n" + link
                                    )
                                    cl.sendImageWithURL(msg.to, profileIG)
                                    cl.sendMessage(msg.to, str(text))
                                except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        # INFO BIRTHDAY
                        elif cmd.startswith("birthday: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ", "")
                                r = requests.get(
                                    "https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal="
                                    + tanggal
                                )
                                data = r.text
                                data = json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cl.sendMessage(
                                    msg.to,
                                    "「 Date Info 」\n"
                                    + "• Date : "
                                    + lahir
                                    + "\n• Age : "
                                    + usia
                                    + "\n• Birthday : "
                                    + ultah
                                    + "\n• Zodiak : "
                                    + zodiak,
                                )

                        # SPAM TAG
                        elif cmd.startswith("spamtag: "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    proses = text.split(":")
                                    strnum = text.replace(proses[0] + ":", "")
                                    num = int(strnum)
                                    Setmain["RAlimit"] = num
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Spamtag 」\nBerhasil diubah jadi {} kali".format(
                                            str(strnum)
                                        ),
                                    )

                        elif cmd.startswith("spamtag "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if (
                                        "MENTION"
                                        in msg.contentMetadata.keys()
                                        is not None
                                    ):
                                        key = eval(msg.contentMetadata["MENTION"])
                                        key1 = key["MENTIONEES"][0]["M"]
                                        zx = ""
                                        zxc = " "
                                        zx2 = []
                                        pesan2 = "@a" " "
                                        xlen = str(len(zxc))
                                        xlen2 = str(len(zxc) + len(pesan2) - 1)
                                        zx = {"S": xlen, "E": xlen2, "M": key1}
                                        zx2.append(zx)
                                        zxc += pesan2
                                        msg.contentType = 0
                                        msg.text = zxc
                                        lol = {
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        }
                                        msg.contentMetadata = lol
                                        jmlh = int(Setmain["RAlimit"])
                                        if jmlh <= 1000:
                                            for x in range(jmlh):
                                                try:
                                                    cl.sendMessage1(msg)
                                                except Exception as e:
                                                    cl.sendText(msg.to, str(e))
                                        else:
                                            cl.sendText(msg.to, "Jumlah melebihi 1000")

                        # SPAM CALL
                        elif cmd.startswith("call "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if (
                                        "MENTION"
                                        in msg.contentMetadata.keys()
                                        is not None
                                    ):
                                        key = eval(msg.contentMetadata["MENTION"])
                                        key1 = key["MENTIONEES"][0]["M"]
                                        zx = ""
                                        zxc = " "
                                        zx2 = []
                                        pesan2 = "@a" " "
                                        xlen = str(len(zxc))
                                        xlen2 = str(len(zxc) + len(pesan2) - 1)
                                        zx = {"S": xlen, "E": xlen2, "M": key1}
                                        zx2.append(zx)
                                        zxc += pesan2
                                        msg.contentType = 0
                                        msg.text = zxc
                                        lol = {
                                            "MENTION": str(
                                                '{"MENTIONEES":'
                                                + json.dumps(zx2).replace(" ", "")
                                                + "}"
                                            )
                                        }
                                        msg.contentMetadata = lol
                                        jmlh = int(key1)
                                        if jmlh <= 1000:
                                            for x in range(jmlh):
                                                try:
                                                    cl.sendMessage1(msg)
                                                except Exception as e:
                                                    cl.sendText(msg.to, str(e))

                        elif cmd == "spamcall":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        group = cl.getGroup(to)
                                        members = [mem.mid for mem in group.members]
                                        cl.sendMessage(
                                            msg.to,
                                            "Berhasil mengundang {} undangan Call Grup".format(
                                                str(wait["limit"])
                                            ),
                                        )
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)

                        elif cmd.startswith("spamcall: "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    proses = text.split(":")
                                    strnum = text.replace(proses[0] + ":", "")
                                    num = int(strnum)
                                    wait["limit"] = num
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Spamcall 」\nBerhasil diubah jadi {} kali".format(
                                            str(strnum)
                                        ),
                                    )

                        elif cmd.startswith("spamcall "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    proses = text.split(" ")
                                    strnum = text.replace(proses[0] + " ", "")
                                    group = cl.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    jumlah = int(strnum)
                                    cl.sendText(
                                        msg.to,
                                        "Undangan call grup {} sukses".format(
                                            str(strnum)
                                        ),
                                    )
                                    if jumlah <= 1000:
                                        for x in range(jumlah):
                                            try:
                                                call.acquireGroupCallRoute(to)
                                                call.inviteIntoGroupCall(
                                                    to, contactIds=members
                                                )
                                            except Exception as e:
                                                cl.sendText(msg.to, str(e))

                        # GIFT
                        elif "Gift: " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    korban = msg.text.replace("Gift: ", "")
                                    korban2 = korban.split()
                                    midd = korban2[0]
                                    jumlah = int(korban2[1])
                                    cl.sendText(
                                        msg.to,
                                        "「 Spam Gift 」\nBerhasil spamgift {} kali".format(
                                            str(jumlah)
                                        ),
                                    )
                                    if jumlah <= 1000:
                                        for var in range(0, jumlah):
                                            cl.sendMessage(
                                                midd,
                                                None,
                                                contentMetadata={
                                                    "PRDID": "a0768339-c2d3-4189-9653-2909e9bb6f58",
                                                    "PRDTYPE": "THEME",
                                                    "MSGTPL": "6",
                                                },
                                                contentType=9,
                                            )

                        # SPAM
                        elif "Spam: " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    korban = msg.text.replace("Spam: ", "")
                                    korban2 = korban.split()
                                    midd = korban2[0]
                                    jumlah = int(korban2[1])
                                    cl.sendText(
                                        msg.to,
                                        "「 Spam Chat 」\nBerhasil spamchat {} kali".format(
                                            str(jumlah)
                                        ),
                                    )
                                    if jumlah <= 1000:
                                        for var in range(0, jumlah):
                                            cl.sendMessage(
                                                midd, str(Setmain["RAmessage1"])
                                            )

                        # IMAGE
                        elif cmd.startswith("addimage "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in images:
                                    wait["Addimage"]["status"] = True
                                    wait["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json", "w", "utf-8")
                                    json.dump(
                                        images,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim fotonya")
                                else:
                                    cl.sendText(msg.to, "Foto itu sudah dalam list")

                        elif cmd.startswith("dellimage "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in images:
                                    cl.deleteFile(images[str(name.lower())])
                                    del images[str(name.lower())]
                                    f = codecs.open("image.json", "w", "utf-8")
                                    json.dump(
                                        images,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus image {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(msg.to, "Foto itu tidak ada dalam list")

                        elif text.lower() == "listimage":
                            if msg._from in admin:
                                no = 0
                                ret_ = "「 Daftar Image 」\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal「{}」Images".format(str(len(images)))
                                cl.sendText(to, ret_)

                        # VIDEO
                        elif cmd.startswith("addvideo "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in videos:
                                    wait["Addvideo"]["status"] = True
                                    wait["Addvideo"]["name"] = str(name.lower())
                                    videos[str(name.lower())] = ""
                                    f = codecs.open("video.json", "w", "utf-8")
                                    json.dump(
                                        videos,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim videonya")
                                else:
                                    cl.sendText(msg.to, "Video itu sudah dalam list")

                        elif cmd.startswith("dellvideo "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in videos:
                                    cl.deleteFile(videos[str(name.lower())])
                                    del videos[str(name.lower())]
                                    f = codecs.open("video.json", "w", "utf-8")
                                    json.dump(
                                        videos,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus video {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(
                                        msg.to, "Video itu tidak ada dalam list"
                                    )

                        elif text.lower() == "listvideo":
                            if msg._from in admin:
                                no = 0
                                ret_ = "「 Daftar Video 」\n\n"
                                for video in videos:
                                    no += 1
                                    ret_ += str(no) + ". " + video.title() + "\n"
                                ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                                cl.sendText(to, ret_)

                        # MP3
                        elif cmd.startswith("addmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in audios:
                                    wait["Addaudio"]["status"] = True
                                    wait["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json", "w", "utf-8")
                                    json.dump(
                                        audios,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim mp3 nya")
                                else:
                                    cl.sendText(msg.to, "Mp3 itu sudah dalam list")

                        elif cmd.startswith("dellmp3 "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json", "w", "utf-8")
                                    json.dump(
                                        audios,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus mp3 {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(msg.to, "Mp3 itu tidak ada dalam list")

                        elif cmd == "listmp3":
                            no = 0
                            ret_ = "「 Daftar Lagu 」\n\n"
                            for audio in audios:
                                no += 1
                                ret_ += str(no) + ". " + audio.title() + "\n"
                            ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                            cl.sendText(to, ret_)

                        # STICKER
                        elif cmd.startswith("addsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in stickers:
                                    wait["Addsticker"]["status"] = True
                                    wait["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("sticker.json", "w", "utf-8")
                                    json.dump(
                                        stickers,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim stickernya")
                                else:
                                    cl.sendText(msg.to, "Sticker itu sudah dalam list")

                        elif cmd.startswith("dellsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json", "w", "utf-8")
                                    json.dump(
                                        stickers,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus sticker {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(
                                        msg.to, "Sticker itu tidak ada dalam list"
                                    )

                        elif text.lower() == "liststicker":
                            if msg._from in admin:
                                no = 0
                                ret_ = "「 Daftar Sticker 」\n\n"
                                for sticker in stickers:
                                    no += 1
                                    ret_ += str(no) + ". " + sticker.title() + "\n"
                                ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                                cl.sendText(to, ret_)

                        # LAMBANG
                        elif cmd == "lambang":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    cl.sendMessage(msg.to, "Nick : ⌬")
                                    cl.sendMessage(msg.to, "Bio : ❲HΞXΛGOИ❳")

                        # KIBAR
                        elif cmd == "kibar":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    cl.sendMessage(msg.to, "⌬ ❲HΞXΛGOИ❳")

                        # KIBAR KICKER
                        elif cmd == "!kibar":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    cl.sendContact(to, mid)
                                    cl.sendMessage(
                                        msg.to,
                                        "「 𐀀 HELLTERHEAD WAS HERE! 」\n\n\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n\n\n\n"
                                        " █▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░▒▓█\n"
                                        " █▓▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌\n"
                                        "█▓▒▒░░░░░░░ 𐀀 HELLTERHEAD ░░░░░░▒▓█\n"
                                        "█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓\n"
                                        "█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓█\n"
                                        "█▓▓█▒░░░▒█▄▒▒░░░░░░░░▒▒░▄█▒░░░▒█▓▓█\n"
                                        " █▓█▒░▒▒▒░░▀▀█▄▄░░░░▄▄█▀▀░░▒▒▒░▒▒▐██\n"
                                        " █▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░█▀▒▒▒▄▄▄▓▓▒▒▐▓█\n"
                                        " ██▌▒▓███▓████▓▒▐▌░▐▌▒▓████▓███▓▒▐██\n"
                                        " ██▒▒▓███▓▓▓███▓▄░░▄▓████▓▓▓███▓▒▒██\n"
                                        " █▓▒▒▓█████████▓▒░░▒▓█████████▓▒▒▓█\n"
                                        "  █▓▒░▒▓██████▓▓▄▀░▀ ▄▓▓██████▓▒▒▓█\n"
                                        "   █▓▒░▒▒▓▓▓▄▄▄▀▒░░░░▒▀▄▄▄▓▓▓▒▒░▓█\n"
                                        "     █▓▒░▒▒▒░░░░░░▒▒▒░░░░░░▒▒▒░▒▓█\n"
                                        "      █▓▓▒▒░░██░░▒▓█▓▒░░██░░▒▒▓▓█\n"
                                        "      ▀██▓▓▒░░▀░▒▓███▓▒░▀░░▒▓▓██\n"
                                        "       ░▀▓▓▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀\n"
                                        "       ░░█▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██\n\n\n\n"
                                        "RATA GAK RATA TETAP PLAY❗\n"
                                        "SILAHKAN KALAU BISA TANGKIS, ADA KATA TERAKHIR?\n"
                                        "SELAMAT MENIKMATI PERTUNJUKAN\n\n\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n\n\n"
                                        "By : DRE❗\n"
                                        "line.me/ti/p/~mo-banzu\n"
                                        "line.me/ti/p/~@722tmgxp",
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={
                                            "STKID": "15996978",
                                            "STKPKGID": "1416471",
                                            "STKVER": "1",
                                        },
                                        contentType=7,
                                    )

                        # HELLTERHEAD
                        elif cmd == "hellterhead" or cmd == "hlth":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    start = time.time()
                                    cl.sendMessage(msg.to, "PING!!!")
                                    elapsed_time = time.time() - start
                                    cl.sendMessage(
                                        msg.to, "READY❗ ".format(str(elapsed_time))
                                    )

                        # ADD SAINT
                        elif "Adminadd " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            admin.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan admin"
                                            )
                                        except BaseException:
                                            pass

                        elif "Staffadd " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            staff.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan staff"
                                            )
                                        except BaseException:
                                            pass

                        elif "Botadd " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            Bots.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan bot"
                                            )
                                        except BaseException:
                                            pass

                        elif "Admindell " in msg.text:
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Saints:
                                        try:
                                            admin.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus admin"
                                            )
                                        except BaseException:
                                            pass

                        elif "Staffdell " in msg.text:
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Saints:
                                        try:
                                            staff.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus staff"
                                            )
                                        except BaseException:
                                            pass

                        elif "Botdell " in msg.text:
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Saints:
                                        try:
                                            Bots.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus bot"
                                            )
                                        except BaseException:
                                            pass

                        elif cmd == "admin:on" or text.lower() == "admin:on":
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to, "Please send to contact...")

                        elif cmd == "admin:repeat" or text.lower() == "admin:repeat":
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to, "Please send to contact...")

                        elif cmd == "staff:on" or text.lower() == "staff:on":
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to, "Please send to contact...")

                        elif cmd == "staff:repeat" or text.lower() == "staff:repeat":
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to, "Please send to contact...")

                        elif cmd == "bot:on" or text.lower() == "bot:on":
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to, "Please send to contact...")

                        elif cmd == "bot:repeat" or text.lower() == "bot:repeat":
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to, "Please send to contact...")

                        elif cmd == "refresh" or text.lower() == "refresh":
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to, "Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == "cadmin":
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact staff" or text.lower() == "cstaff":
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact bot" or text.lower() == "cbot":
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        # WELCOME
                        elif "Welcome " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Welcome ", "")
                                if spl == "on":
                                    if msg.to in welcome:
                                        msgs = "Welcome Message sudah aktif"
                                    else:
                                        welcome.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(
                                        msg.to, "「 Status Welcome 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in welcome:
                                        welcome.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    else:
                                        msgs = "Welcome Message sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Welcome 」\n" + msgs
                                    )
                        # PROTECTION
                        elif "Protecturl " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protecturl ", "")
                                if spl == "on":
                                    if msg.to in protectqr:
                                        msgs = "Protect URL sudah aktif"
                                    else:
                                        protectqr.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect URL 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in protectqr:
                                        protectqr.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    else:
                                        msgs = "Protect URL sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect URL 」\n" + msgs
                                    )

                        elif "Protectkick " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectkick ", "")
                                if spl == "on":
                                    if msg.to in protectkick:
                                        msgs = "Protect kick sudah aktif"
                                    else:
                                        protectkick.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect kick 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in protectkick:
                                        protectkick.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    else:
                                        msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect kick 」\n" + msgs
                                    )

                        elif "Protectjoin " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectjoin ", "")
                                if spl == "on":
                                    if msg.to in protectjoin:
                                        msgs = "Protect join sudah aktif"
                                    else:
                                        protectjoin.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Join 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in protectjoin:
                                        protectjoin.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    else:
                                        msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Join 」\n" + msgs
                                    )

                        elif "Protectcancel " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectcancel ", "")
                                if spl == "on":
                                    if msg.to in protectcancel:
                                        msgs = "Protect cancel sudah aktif"
                                    else:
                                        protectcancel.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Cancel 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in protectcancel:
                                        protectcancel.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    else:
                                        msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Cancel 」\n" + msgs
                                    )

                        elif "Protectinvite " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectinvite ", "")
                                if spl == "on":
                                    if msg.to in protectinvite:
                                        msgs = "Protect invite sudah aktif"
                                    else:
                                        protectinvite.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Invite 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in protectinvite:
                                        protectinvite.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                    else:
                                        msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Invite 」\n" + msgs
                                    )

                        elif "Protectall " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectall ", "")
                                if spl == "on":
                                    if msg.to in protectqr:
                                        msgs = "Protect QR : ON"
                                    else:
                                        protectqr.append(msg.to)
                                    if msg.to in protectkick:
                                        msgs = "Protect kick : ON"
                                    else:
                                        protectkick.append(msg.to)
                                    if msg.to in protectinvite:
                                        msgs = "Protect invite : ON"
                                    else:
                                        protectinvite.append(msg.to)
                                    if msg.to in protectcancel:
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                        msgs += "\nSemua protection diaktifkan"
                                    else:
                                        protectcancel.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                        msgs += "\nSemua protection diaktifkan"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protection 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in protectqr:
                                        protectqr.remove(msg.to)
                                    else:
                                        msgs = "Protect QR : OFF"
                                    if msg.to in protectkick:
                                        protectkick.remove(msg.to)
                                    else:
                                        msgs = "Protect kick : OFF"
                                    if msg.to in protectinvite:
                                        protectinvite.remove(msg.to)
                                    else:
                                        msgs = "Protect invite : OFF"
                                    if msg.to in protectcancel:
                                        protectcancel.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                        msgs += "\nSemua protection dinonaktifkan"
                                    else:
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + str(
                                            ginfo.name
                                        )
                                        msgs += "\nSemua protection dinonaktifkan"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protection 」\n" + msgs
                                    )

                        # COMMAND ON OFF
                        elif cmd == "spaminvite on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    settings["SpamInvite"] = True
                                    cl.sendMessage(msg.to, "Spam invite diaktifkan")
                                    cl.sendMessage(msg.to, "Kirim kontaknya...")

                        elif cmd == "spaminvite off":
                            if not wait["selfbot"]:
                                if msg._from in admin:
                                    settings["SpamInvite"] = False
                                    cl.sendMessage(msg.to, "Spam invite dinonaktifkan")

                        elif cmd == "unsend on" or text.lower() == "unsend on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["unsend"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Unsend 」\n• User ",
                                        "\nDeteksi unsend diaktifkan",
                                    )

                        elif cmd == "unsend off" or text.lower() == "unsend off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["unsend"] = False
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Unsend 」\n• User ",
                                        " \nDeteksi unsend dinonaktifkan",
                                    )

                        elif cmd == "timeline on" or text.lower() == "timeline on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Timeline"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Timeline 」\n• User ",
                                        "\nDeteksi timeline diaktifkan",
                                    )

                        elif cmd == "timeline off" or text.lower() == "timeline off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Timeline"] = False
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Timeline 」\n• User ",
                                        "\nDeteksi timeline dinonaktifkan",
                                    )

                        elif cmd == "invite on" or text.lower() == "invite on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["invite"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Invite 」\n• User ",
                                        "\nInvite via contact diaktifkan",
                                    )

                        elif cmd == "invite off" or text.lower() == "invite off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["invite"] = False
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Invite 」\n• User ",
                                        " \nInvite via contact dinonaktifkan",
                                    )

                        elif cmd == "notag on" or text.lower() == "notag on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["mentionKick"] = True
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Notag 」\nNotag telah diaktifkan",
                                    )

                        elif cmd == "notag off" or text.lower() == "notag off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["mentionKick"] = False
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Notag 」\nNotag telah dinonaktifkan",
                                    )

                        elif cmd == "contact on" or text.lower() == "contact on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Contact 」\n• User ",
                                        "\nDeteksi contact diaktifkan",
                                    )

                        elif cmd == "contact off" or text.lower() == "contact off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = False
                                    cl.sendText(
                                        msg.to,
                                        sender,
                                        "「 Status Contact 」\n• User ",
                                        "\nDeteksi contact dinonaktifkan",
                                    )

                        elif cmd == "respon on" or text.lower() == "respon on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["detectMention"] = True
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Respon 」\nAuto respon diaktifkan",
                                    )

                        elif cmd == "respon off" or text.lower() == "respon off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["detectMention"] = False
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Respon 」\nAuto respon dinonaktifkan",
                                    )

                        elif cmd == "autojoin on" or text.lower() == "autojoin on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoJoin"] = True
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autojoin 」\nAuto join telah diaktifkan",
                                    )

                        elif cmd == "autojoin off" or text.lower() == "autojoin off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoJoin"] = False
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autojoin 」\nAuto join telah dinonaktifkan",
                                    )

                        elif cmd == "autoleave on" or text.lower() == "autoleave on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoLeave"] = True
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autoleave 」\nAuto leave telah diaktifkan",
                                    )

                        elif cmd == "autoleave off" or text.lower() == "autoleave off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoLeave"] = False
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autoleave 」\nAuto leave telah dinonaktifkan",
                                    )

                        elif cmd == "autoblock on" or text.lower() == "autoblock on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoBlock"] = True
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autoblock 」\nAuto block telah diaktifkan",
                                    )

                        elif cmd == "autoblock off" or text.lower() == "autoblock off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoBlock"] = False
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autoblock 」\nAuto block telah dinonaktifkan",
                                    )

                        elif cmd == "autoadd on" or text.lower() == "autoadd on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoAdd"] = True
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autoadd 」\nAuto add telah diaktifkan",
                                    )

                        elif cmd == "autoadd off" or text.lower() == "autoadd off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoAdd"] = False
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Autoadd 」\nAuto add telah dinonaktifkan",
                                    )

                        elif cmd == "sticker on" or text.lower() == "sticker on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["stickerOn"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Sticker Check 」\nSticker check diaktifkan",
                                    )

                        elif cmd == "sticker off" or text.lower() == "sticker off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["stickerOn"] = False
                                    cl.sendText(
                                        msg.to,
                                        "「 Status Sticker Check 」\nSticker check dinonaktifkan",
                                    )

                        elif cmd == "jointicket on" or text.lower() == "jointicket on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    settings["autoJoinTicket"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Jointicket 」\nJoin ticket telah diaktifkan",
                                    )

                        elif (
                            cmd == "jointicket off" or text.lower() == "jointicket off"
                        ):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    settings["autoJoinTicket"] = False
                                    cl.sendText(
                                        msg.to,
                                        sender,
                                        "「 Status Jointicket 」\nJoin ticket telah dinonaktifkan",
                                    )

                        # SETTING MESSAGE
                        elif "Set pesan: " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Set pesan: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti pesan message"
                                    )
                                else:
                                    wait["message"] = spl
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Berhasil Diganti 」\nPesan message diganti jadi :\n\n{}".format(
                                            str(spl)
                                        ),
                                    )

                        elif "Set welcome: " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Set welcome: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti welcome message"
                                    )
                                else:
                                    wait["welcome"] = spl
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Berhasil Diganti 」\nWelcome message diganti jadi :\n\n{}".format(
                                            str(spl)
                                        ),
                                    )

                        elif "Set leave: " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Set leave: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti leave message"
                                    )
                                else:
                                    wait["leave"] = spl
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Berhasil Diganti 」\nLeave message diganti jadi :\n\n{}".format(
                                            str(spl)
                                        ),
                                    )

                        elif "Set respon: " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Set respon: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti respon message"
                                    )
                                else:
                                    wait["Respontag"] = spl
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Berhasil Diganti 」\nRespon message diganti jadi :\n\n{}".format(
                                            str(spl)
                                        ),
                                    )

                        elif "Set spam: " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Set spam: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti spam message"
                                    )
                                else:
                                    Setmain["RAmessage1"] = spl
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Berhasil Diganti 」\nSpam message diganti jadi :\n\n{}".format(
                                            str(spl)
                                        ),
                                    )

                        elif "Set sider: " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Set sider: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti sider message"
                                    )
                                else:
                                    wait["mention"] = spl
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Berhasil Diganti 」\nSider message diganti jadi :\n\n{}".format(
                                            str(spl)
                                        ),
                                    )
                        #CHECK MESSAGE
                        elif text.lower() == "msg pesan":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Message 」\nPesan message :\n\n"
                                    + str(wait["message"]),
                                )

                        elif text.lower() == "msg welcome":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Welcome 」\nWelcome message :\n\n"
                                    + str(wait["welcome"]),
                                )

                        elif text.lower() == "msg leave":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Leave 」\nLeave message :\n\n"
                                    + str(wait["leave"]),
                                )

                        elif text.lower() == "msg respon":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Respon 」\nRespon message :\n\n"
                                    + str(wait["Respontag"]),
                                )

                        elif text.lower() == "msg spam":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Spam 」\nSpam message :\n\n"
                                    + str(Setmain["RAmessage1"]),
                                )

                        elif text.lower() == "msg sider":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Sider 」\nSider message :\n\n"
                                    + str(wait["mention"]),
                                )

                        # JOIN TICKET
                        elif "/ti/g/" in msg.text.lower():
                            if wait["selfbot"]:
                                if settings["autoJoinTicket"]:
                                    link_re = re.compile(
                                        r"(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?"
                                    )
                                    links = link_re.findall(text)
                                    n_links = []
                                    for l in links:
                                        if l not in n_links:
                                            n_links.append(l)
                                    for ticket_id in n_links:
                                        group = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(
                                            group.id, ticket_id
                                        )
                                        cl.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )
                                        group1 = ki.findGroupByTicket(ticket_id)
                                        ki.acceptGroupInvitationByTicket(
                                            group1.id, ticket_id
                                        )
                                        ki.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )
                                        group2 = kk.findGroupByTicket(ticket_id)
                                        kk.acceptGroupInvitationByTicket(
                                            group2.id, ticket_id
                                        )
                                        kk.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )
                                        group3 = kc.findGroupByTicket(ticket_id)
                                        kc.acceptGroupInvitationByTicket(
                                            group3.id, ticket_id
                                        )
                                        kc.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )

    except Exception as error:
        print(error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(
                    target=bot, args=(op,)
                )  # self.OpInterrupt[op.type], args=(op,)
                # thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
