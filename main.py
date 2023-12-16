import random

def split_string(s, interval=1):
    result = []
    for i in range(0, len(s), interval):
        result.append(s[i:i+interval])
    return result

# ABC = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#
# old = """1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*()`-_=+[{]}\|;:'",<.>/?"""

# new = """sdfghjklzxcvKLZXC0qweM~!@#$%^&*()`-_=+riopbnmQWEtyVBN[{123456789uRTYUIOPAS]}\|;a",<.>/?"""

aaa = {' ':'gUo','1': 'noK', '2': 'FNA', '3': 'Rfc', '4': 'EwU', '5': 'tar', '6': 'DDY', '7': 'zoM', '8': 'VeB', '9': 'bVK', '0': 'Ymb', 'q': 'IXf', 'w': 'PnV', 'e': 'GHp', 'r': 'Lmv', 't': 'dyX', 'y': 'Sgt', 'u': 'mEk', 'i': 'KIX', 'o': 'lHw', 'p': 'eLT', 'a': 'hmL', 's': 'EAV', 'd': 'jur', 'f': 'RJP', 'g': 'DZm', 'h': 'npK', 'j': 'flK', 'k': 'ttH', 'l': 'QtG', 'z': 'icL', 'x': 'plM', 'c': 'CPo', 'v': 'DGt', 'b': 'hnj', 'n': 'Hjl', 'm': 'UMc', 'Q': 'qBw', 'W': 'izi', 'E': 'lQl', 'R': 'UMZ', 'T': 'ukq', 'Y': 'TDq', 'U': 'SaW', 'I': 'aFC', 'O': 'KLW', 'P': 'idq', 'A': 'fXz', 'S': 'nFs', 'D': 'WOD', 'F': 'tVn', 'G': 'uWC', 'H': 'Mnd', 'J': 'jqs', 'K': 'cdX', 'L': 'UFN', 'Z': 'SuD', 'X': 'xRS', 'C': 'XiH', 'V': 'lqd', 'B': 'oqq', 'N': 'qqh', 'M': 'eRo', '~': 'blr', '!': 'sJK', '@': 'uUj', '#': 'nvb', '$': 'QjO', '%': 'snk', '^': 'IZP', '&': 'LGp', '*': 'HuD', '(': 'MzO', ')': 'wlV', '`': 'DgW', '-': 'Lea', '_': 'Mqh', '=': 'EaG', '+': 'gEy', '[': 'LPQ', '{': 'EyK', ']': 'xsO', '}': 'QOa', '\\': 'ECJ', '|': 'Czy', ';': 'OZz', ':': 'sjW', "'": 'CGw', '"': 'kLz', ',': 'Iuu', '<': 'rnT', '.': 'vRc', '>': 'LlR', '/': 'aKP', '?': 'czE'}

bbb = {'gUo':' ','noK': '1', 'FNA': '2', 'Rfc': '3', 'EwU': '4', 'tar': '5', 'DDY': '6', 'zoM': '7', 'VeB': '8', 'bVK': '9', 'Ymb': '0', 'IXf': 'q', 'PnV': 'w', 'GHp': 'e', 'Lmv': 'r', 'dyX': 't', 'Sgt': 'y', 'mEk': 'u', 'KIX': 'i', 'lHw': 'o', 'eLT': 'p', 'hmL': 'a', 'EAV': 's', 'jur': 'd', 'RJP': 'f', 'DZm': 'g', 'npK': 'h', 'flK': 'j', 'ttH': 'k', 'QtG': 'l', 'icL': 'z', 'plM': 'x', 'CPo': 'c', 'DGt': 'v', 'hnj': 'b', 'Hjl': 'n', 'UMc': 'm', 'qBw': 'Q', 'izi': 'W', 'lQl': 'E', 'UMZ': 'R', 'ukq': 'T', 'TDq': 'Y', 'SaW': 'U', 'aFC': 'I', 'KLW': 'O', 'idq': 'P', 'fXz': 'A', 'nFs': 'S', 'WOD': 'D', 'tVn': 'F', 'uWC': 'G', 'Mnd': 'H', 'jqs': 'J', 'cdX': 'K', 'UFN': 'L', 'SuD': 'Z', 'xRS': 'X', 'XiH': 'C', 'lqd': 'V', 'oqq': 'B', 'qqh': 'N', 'eRo': 'M', 'blr': '~', 'sJK': '!', 'uUj': '@', 'nvb': '#', 'QjO': '$', 'snk': '%', 'IZP': '^', 'LGp': '&', 'HuD': '*', 'MzO': '(', 'wlV': ')', 'DgW': '`', 'Lea': '-', 'Mqh': '_', 'EaG': '=', 'gEy': '+', 'LPQ': '[', 'EyK': '{', 'xsO': ']', 'QOa': '}', 'ECJ': '\\', 'Czy': '|', 'OZz': ';', 'sjW': ':', 'CGw': "'", 'kLz': '"', 'Iuu': ',', 'rnT': '<', 'vRc': '.', 'LlR': '>', 'aKP': '/', 'czE': '?'}

while True:
    inp = input('0:加密  1:解密 x:Exit :')
    if inp == '0':
        old = input(':')
        new = ''
        for i in old:
            new += aaa[i]
        print(new)

    elif inp == '1':
        old = input(':')
        new = ''
        old = split_string(old,3)
        for i in old:
            new += bbb[i]
        print(new)
    elif inp == 'x':
        break
    print('\n')
# for i in aaa:
#     bbb[aaa[i]] = i
# print(aaa)
# print(bbb)

# a = {}
#
# for i in old:
#     s = ''
#     for j in range(3):
#         s += ABC[random.randint(0,len(ABC)-1)]
#
#     a[i]=s
#
# print(a)