byte midiMsgStatus;
byte midiMsgKeyNumber;
byte midiMsgVelocity;

void assembleMidiMsg(boolean droneOn, int channel, int keyNumber, int velocity, byte (& msgArr) [3]) {
  if (droneOn == true) {
    int stat = 128 + channel;
    midiMsgStatus = stat;
    midiMsgKeyNumber = keyNumber;
    midiMsgVelocity = velocity;  
  } else {
    midiMsgStatus = 0;
    midiMsgKeyNumber = 0;
    midiMsgVelocity = 0; 
  }
  msgArr[0] = midiMsgStatus;
  msgArr[1] = midiMsgKeyNumber;
  msgArr[2] = midiMsgVelocity;
}

void setup() {
  Serial.begin(9600);
  byte msgArr[3] = {0, 0, 0};
  for (int i = 0; i < 3; i++) {
    Serial.println(msgArr[i]);
  }
  assembleMidiMsg(false, 1, 60, 60, msgArr);
  for (int i = 0; i < 3; i++) {
    Serial.println(msgArr[i]);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
