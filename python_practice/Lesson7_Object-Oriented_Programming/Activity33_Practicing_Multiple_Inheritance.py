# Create a MobilePhone class that will be initialized with a memory attribute.
class MobilePhone:
    def __init__(self, memory):
        self.memory = memory

# Create a Camera class that has a take_picture() method.
class Camera:
    def take_picture(self):
        print('Say Cheese!')
        
# Create a CameraPhone class that inherits from both the MobilePhone and Camera classes.
class Camera_phone(MobilePhone, Camera):
    pass

iphone = Camera_phone('200KB')
print(iphone.memory)