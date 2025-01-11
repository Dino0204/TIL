class Device:
  def __init__(self,name,status):
    self.name = name
    self.status = status
    
  def turn_on(self):
    self.status = True
    return f"{self.name} is now on."
  
  def turn_off(self):
    self.status = False
    return f"{self.name} is now off."
  
  def get_status(self):
    return f"{"on" if self.status else "off"}"

class Light(Device):
  def __init__(self,name,status = False,brightness = 0):
    super().__init__(name,status)
    self.brightness = brightness
    self.schedules = dict()
    
  def adjust_brightness(self,brightness):
    self.brightness = brightness
    return f"{self.name}'s brightness is set to {self.brightness}."

  def schedule_brightness(self,time,brightness):
    self.schedules[time] = brightness

    return f"{self.name}'s brightness is scheduled to {brightness} at {time}."

class Thermostat(Device):
  def __init__(self,name,status = False,temperature = 0):
    super().__init__(name,status)
    self.temperature = temperature
    self.schedules = dict()
  
  def set_temperature(self, temperature):
    self.temperature = temperature
    return f"{self.name}'s temperature is set to {self.temperature} degrees."
  
  def schedule_temperature(self,time,temperature):
    self.schedules[time] = temperature
    return f"{self.name}'s temperature is scheduled to {temperature} degrees at {time}."

class SmartHome:
  def __init__(self):
    self.devices = []
    
  def add_device(self, device):
    self.devices.append(device)
    return f"{device.name} has been added to the smart home."
  
  def remove_device(self, device_name):
    for device in self.devices:
      if device.name == device_name:
        self.devices.remove(device)
        return f"{device.name} has been removed from the smart home."
    return f"{device_name} is not in the smart home."
  
  def list_devices(self):
    return "\n".join(f"{device.name} is {device.get_status()}." for device in self.devices)
  
  def run_schedules(self,time):
    return "\n".join(f"{device.adjust_brightness((device.schedules[time])) if type(device).__name__ == "Light" else device.set_temperature((device.schedules[time]))}" for device in self.devices)

home = SmartHome()
light = Light("Living Room Light")
thermostat = Thermostat("Main Thermostat")

print(home.add_device(light))
print(home.add_device(thermostat))

print(home.list_devices())

print(light.turn_on())
print(light.adjust_brightness(75))
print(thermostat.set_temperature(22))

print(home.list_devices())

print(light.schedule_brightness("06:00", 50))
print(thermostat.schedule_temperature("06:00",18))
print(home.run_schedules("06:00"))

print(home.list_devices())

print(home.remove_device("Living Room Light"))

print(home.list_devices())

print(home.remove_device("Living Room Light"))