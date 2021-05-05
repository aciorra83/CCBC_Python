# # Ex 37: Declaring a class with instance attributes
# # Instance Attributes are bound to a specific instance/object but not to any other object initialized from that class

# # Define the webrowser class
# class WeBrowser:
#     def __init__(self, page):
#         self.history = [page]
#         self.current_page = page
#         self.is_incognito = False

# # initialize objects from the class
# firefox = WeBrowser('google.com')
# chrome = WeBrowser('facebook.com')

# # Every WebBrowser instance will have a different current_page attribute. 
# # This happens because these attributes are bound to the instance and not to the class; they are instance attributes. 
# # Check this by getting the current_page attribute on different WebBrowser instances:

# print(firefox.current_page)
# print(chrome.current_page)

# Class attributes are bound to the class itself and are shared by all instances
# Ex 38: Extending our class with class attributes
# Adding a class attribute to the WeBrowser class
class WebBrowser:
    #class attribute is 'connected'
    connected = True

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
# Instantiate a WebBrowser object. We can see that the connected attribute is True for all instances:
# Passing int he 'page' arguement of google.com and facebook.com
firefox = WebBrowser('google.com')
chrome = WebBrowser('facebook.com')
print(firefox.connected)
print(chrome.connected)
# results in true because it is inherited from the PARENT class attribute
# we can check class attributes with the class itself:
print(WebBrowser.connected) # this results in a True boolean
# printing out instances __dict__ attributes, THE CONNECTED ATTRIBUTE DOES NOT APPEEAR 
print(firefox.__dict__)
print(chrome.__dict__)
# However, WeBrowser.__dict__ containes the 'connected' class attribute
print(WebBrowser.__dict__)

# Setting an class attribute like 'connected = True' to something else later in the code will override the initial class attribute:
firefox.connected = False
# Now 'connected = False' will appear in firefox.__dict__
print(firefox.__dict__)