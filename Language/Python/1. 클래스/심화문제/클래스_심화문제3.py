class Device:
  def __init__(self,name,status):
    self.name = name
    self.status = status
  def turn_on(self):
    return
  def turn_off(self):
    return
  def get_status(self):
    return

class Light(Device):
  def __init__(self,name,status):
    self.name = name
    self.status = status
class Thermostat(Device):
  def __init__(self,name,status):
    self.name = name
    self.status = status
class SmartHome:
  def __init__(self,name,status):
    self.name = name
    self.status = status