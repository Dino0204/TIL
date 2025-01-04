# TV 클래스

# 속성
# 1. 현재 채널을 나타내는 channel 속성
# 2. 현재 음량을 나타내는 volume 속성
# 3. TV가 켜져 있는지 여부를 나타내는 on 속성

# 메서드
# 1. 현재 채널, 음량, TV 상태를 출력하는 show 메서드
# 2. 채널 값을 설정하는 setChannel 메서드
# 3. 현재 채널 값을 반환하는 getChannel 메서드

class TV: 
  def __init__(self,channel,volume,on):
    self.channel = channel
    self.volume = volume
    self.on = on
  
  def show(self):
    print(f'{self.channel} {self.volume} {self.on}')
  
  def setChannel(self,channel):
    self.channel = channel
  
  def getChannel(self):
    return self.channel

tv = TV(1,13,"on")
tv.show()

tv.setChannel(10)
tv.show()

print(tv.getChannel())