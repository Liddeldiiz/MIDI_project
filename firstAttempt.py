# (0xnc, 0xkk, 0xvv)
# n is the command (note on (0x9), note off (0x8))
# c is the channel (1 to 16)
# kk is the key number (0 to 127, where C is key number 60)
# vv is the striking velocity (0 to 127)


midiMsg = ""

droneOn = False
channel = 1
keyNumber = 60
velocity = 0

def assembleMidiMSG(midiMsg, droneOn, channel, keyNumber, velocity):
    midiMsgStatus = ""
    midiMsgKeyNumber = ""
    midiMsgVelocity = ""

    if droneOn == True:
        midiMsgStatus = "1001"
        midiMsgKeyNumberB = str(bin(keyNumber))
        midiMsgKeyNumber = midiMsgKeyNumberB[2:]
        midiMsgVelocityB = str(bin(velocity))
        midiMsgVelocity = midiMsgVelocityB[2:]
    else:
        midiMsgStatus = "1000"
        midiKeyNumberB = str(bin(0))
        midiKeyNumber = midiKeyNumber[:2]
        midiMsgVelocityB = str(bin(0))
        midiMsgVelocity = midiMsgVelocity[:2]

    midiMsg += midiMsgStatus + midiMsgKeyNumber + midiMsgVelocity
    if midiMsg == "":
        print("MidiMsg empty")
    return midiMsg

print(assembleMidiMSG(midiMsg, True, channel, keyNumber, velocity))
