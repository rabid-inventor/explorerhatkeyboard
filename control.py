import uinput
import time

import explorerhat

device =  uinput.Device((uinput.KEY_W,uinput.KEY_S,uinput.KEY_A,uinput.KEY_D))

def keypressA(pin):
  device.emit(uinput.KEY_A,pin.read())
def keypressW(pin):
  device.emit(uinput.KEY_W,pin.read())
def keypressS(pin):
  device.emit(uinput.KEY_S,pin.read())
def keypressD(pin):
  device.emit(uinput.KEY_D,pin.read())
  
explorerhat.input.one.changed(keypressA)  

explorerhat.input.two.changed(keypressW)
explorerhat.input.three.changed(keypressS)
explorerhat.input.four.changed(keypressD)
explorerhat.pause()
