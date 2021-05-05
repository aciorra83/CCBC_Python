# In this exercise, we're going to create a counter that will be incremented each time a new WebBrowser object is instantiated:

# Add the class attribute number_of_web_browsers, which will serve as the counter and will start at 0:
class WeBrowser:
    number_of_web_browsers = 0
    connected = True
    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
        # modifying the __init__ constructor method to increment the counter by 1
        WeBrowser.number_of_web_browsers += 1
# initial check to county number_of_web_browsers
print(WeBrowser.number_of_web_browsers)
# instantiate a new object and check the counter:
opera = WeBrowser('opera.com')
print(WeBrowser.number_of_web_browsers)
# the counter now increments with every instance created
edge = WeBrowser('microsof.com')
print(WeBrowser.number_of_web_browsers)


# Activity 30: Creating a Class Attribute

# Declare the Elevator class by adding an occupancy limit class attribute. Max occupancy is 8 people.
class Elevator:
    occupancy_limit = 8
    def __init__(self, occupants):
# Add the initializer, which will check whether the occupancy limit will be exceeded, and print a message indicating how many people should alight.
        if occupants > self.occupancy_limit:
            print(f'There are too many occupants on the elevator. {occupants - self.occupancy_limit} occupants must exit the elevator')
        self.occupants = occupants
# Finally, create a few instances after the class declaration to test the class out:
elevator1 = Elevator(6)
elevator2 = Elevator(10)
print('Elevator 1 occupants: ', elevator1.occupants)
print('Elevator 2 occupants: ', elevator2.occupants)

