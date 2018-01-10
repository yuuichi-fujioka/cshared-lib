# coding: utf-8
import datetime
import ctypes


class GoInterface(ctypes.Structure):
    _fields_ = [
        ('t', ctypes.c_void_p),
        ('v', ctypes.c_void_p),
    ]

class GoString(ctypes.Structure):
    _fields_ = [
        ('p', ctypes.c_char_p),
        ('n', ctypes.c_int64),
    ]

    def value(self):
        return self.p[:self.n]

class Bar2_return(ctypes.Structure):
    _fields_ = [
        ('r0', GoString),
        ('r1', GoString),
    ]

# 利用する関数の定義をやる。なぜならば、.hがincludeできないからだ。
lib = ctypes.cdll.LoadLibrary('./libfoo.so')
lib.Asdf.restype = int


# goでstringを戻すケース。
ret = lib.Asdf()
print(ret)

