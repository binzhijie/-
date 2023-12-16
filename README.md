# Coastal Studio 官网
- [点击进入](https://binzhijie.github.io)

# 这是什么?
* 这是一个可以将字符串加密成密文的程序（中英文不限）

# 我该怎么运行？

## 电脑端用户

**要求**
- Python运行环境
    - [官网下载](https://www.python.org/downloads/)

**流程**
1. 将项目克隆至本地
2. 使用python打开main文件即可

## 手机端用户
**要求**
- Python环境
    - 手机python环境，如：Qpython3、Pydroid
    - 也可以点[此处](https://www.123pan.com/s/K9i0Vv-sXlgH.html)下载（提取码:pypy）

**流程**
1. 下载`main.py`文件
2. 在手机python运行环境中打开运行即可

# 如何实现的？
此工程的原理其实就是将一个字符加密为**Base64**，在将加密后的值经过我们的再次加密形成的。在此项目中，我们使用了`base64`这个库。

- 这是加密过程
```
old = input(':')
old = base64.b64encode(old.encode('utf-8')).decode('utf-8')
new = ''
for i in old:
    new += aaa[i]
print(new)
```

- 这是解密过程
```
old = input(':')
    new = ''
    old = split_string(old,3)
    for i in old:
        new += bbb[i]
    new = base64.b64decode(new.encode('utf-8')).decode('utf-8')
    print(new)
```
- 这是加解密字典
```
aaa = {' ':'gUo','1': 'noK', '2': 'FNA', '3': 'Rfc', '4': 'EwU', '5': 'tar', '6': 'DDY', '7': 'zoM', '8': 'VeB', '9': 'bVK', '0': 'Ymb', 'q': 'IXf', 'w': 'PnV', 'e': 'GHp', 'r': 'Lmv', 't': 'dyX', 'y': 'Sgt', 'u': 'mEk', 'i': 'KIX', 'o': 'lHw', 'p': 'eLT', 'a': 'hmL', 's': 'EAV', 'd': 'jur', 'f': 'RJP', 'g': 'DZm', 'h': 'npK', 'j': 'flK', 'k': 'ttH', 'l': 'QtG', 'z': 'icL', 'x': 'plM', 'c': 'CPo', 'v': 'DGt', 'b': 'hnj', 'n': 'Hjl', 'm': 'UMc', 'Q': 'qBw', 'W': 'izi', 'E': 'lQl', 'R': 'UMZ', 'T': 'ukq', 'Y': 'TDq', 'U': 'SaW', 'I': 'aFC', 'O': 'KLW', 'P': 'idq', 'A': 'fXz', 'S': 'nFs', 'D': 'WOD', 'F': 'tVn', 'G': 'uWC', 'H': 'Mnd', 'J': 'jqs', 'K': 'cdX', 'L': 'UFN', 'Z': 'SuD', 'X': 'xRS', 'C': 'XiH', 'V': 'lqd', 'B': 'oqq', 'N': 'qqh', 'M': 'eRo', '~': 'blr', '!': 'sJK', '@': 'uUj', '#': 'nvb', '$': 'QjO', '%': 'snk', '^': 'IZP', '&': 'LGp', '*': 'HuD', '(': 'MzO', ')': 'wlV', '`': 'DgW', '-': 'Lea', '_': 'Mqh', '=': 'EaG', '+': 'gEy', '[': 'LPQ', '{': 'EyK', ']': 'xsO', '}': 'QOa', r'\\': 'ECJ', '|': 'Czy', ';': 'OZz', ':': 'sjW', "'": 'CGw', '"': 'kLz', ',': 'Iuu', '<': 'rnT', '.': 'vRc', '>': 'LlR', '/': 'aKP', '?': 'czE'}

bbb = {'gUo':' ','noK': '1', 'FNA': '2', 'Rfc': '3', 'EwU': '4', 'tar': '5', 'DDY': '6', 'zoM': '7', 'VeB': '8', 'bVK': '9', 'Ymb': '0', 'IXf': 'q', 'PnV': 'w', 'GHp': 'e', 'Lmv': 'r', 'dyX': 't', 'Sgt': 'y', 'mEk': 'u', 'KIX': 'i', 'lHw': 'o', 'eLT': 'p', 'hmL': 'a', 'EAV': 's', 'jur': 'd', 'RJP': 'f', 'DZm': 'g', 'npK': 'h', 'flK': 'j', 'ttH': 'k', 'QtG': 'l', 'icL': 'z', 'plM': 'x', 'CPo': 'c', 'DGt': 'v', 'hnj': 'b', 'Hjl': 'n', 'UMc': 'm', 'qBw': 'Q', 'izi': 'W', 'lQl': 'E', 'UMZ': 'R', 'ukq': 'T', 'TDq': 'Y', 'SaW': 'U', 'aFC': 'I', 'KLW': 'O', 'idq': 'P', 'fXz': 'A', 'nFs': 'S', 'WOD': 'D', 'tVn': 'F', 'uWC': 'G', 'Mnd': 'H', 'jqs': 'J', 'cdX': 'K', 'UFN': 'L', 'SuD': 'Z', 'xRS': 'X', 'XiH': 'C', 'lqd': 'V', 'oqq': 'B', 'qqh': 'N', 'eRo': 'M', 'blr': '~', 'sJK': '!', 'uUj': '@', 'nvb': '#', 'QjO': '$', 'snk': '%', 'IZP': '^', 'LGp': '&', 'HuD': '*', 'MzO': '(', 'wlV': ')', 'DgW': '`', 'Lea': '-', 'Mqh': '_', 'EaG': '=', 'gEy': '+', 'LPQ': '[', 'EyK': '{', 'xsO': ']', 'QOa': '}', 'ECJ': r'\\', 'Czy': '|', 'OZz': ';', 'sjW': ':', 'CGw': "'", 'kLz': '"', 'Iuu': ',', 'rnT': '<', 'vRc': '.', 'LlR': '>', 'aKP': '/', 'czE': '?'}

```
> 字典是使用`random`库随机生成的
