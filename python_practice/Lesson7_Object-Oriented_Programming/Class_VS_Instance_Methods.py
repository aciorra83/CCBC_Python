# Ex 40: Creating Instance Methods
# In this exercise, we will implement the navigate() and clear_history() methods for the WebBrowser class we defined in the previous section:

class WebBrowser:
    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
# Add the navigate() method to the WeBrowser class

    def navigate(self, new_page):
        self.current_page = new_page
        if not self.is_incognito:
            self.history.append(new_page)

# Create the clear_history method, which will delete the browser's history:
    def clear_history(self):
        # creating a new empty list to 'clear browser history' up until the current page
        self.history [:-1] = []

# Any call to navigate will set the browser's current page to the new_page argument and then add it to the history if we're not in incognito mode 
# (incognito mode in browsers prevents browsing history from being recorded).

vivaldi = WebBrowser('gocamping.org')
print(vivaldi.current_page)
# Calling the navigate() method and passing the new_page argument 'reddit.com'
vivaldi.navigate('reddit.com')
print(vivaldi.history)

chrome = WebBrowser('example.net')
chrome.navigate('example2.net')
chrome.navigate('example2.net')
print(chrome.history)
print(chrome.current_page)
chrome.clear_history()
print(chrome.history)

# The output for chrome.navigate tells us that it is a bound method of an object in the memory location 0x107a9a390. 
# The output of opera.navigate tells us that it is a bound method of an object at a different object at memory location 0x107a9a400. 
# This shows us that the two instance methods are tied/bound to different objects.
print(chrome.navigate)


# One common use case for class methods is when you're making factory methods. A factory method is one that returns objects. 
# They can be used for returning objects of a different type or with different attributes. 
# Let's add a class method called with_incognito() to our WebBrowser class that initializes a web browser object in incognito mode:

class WebBrowser:
    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False

    def navigate(self, new_page):
        self.current_page = new_page
        if not self.is_incognito:
            self.history.append(new_page)

    def clear_history(self):
        self.history[:-1] = []

    @classmethod
    def with_incognito(cls, page):
        instance = cls(page)
        instance.is_incognito = True
        instance.history = []
        return instance
#  Print out the class method. The output tells us that it is a bound method of the WebBrowser class. 
# This illustrates what we said earlier regarding class methods and how they are bound to the class itself:
print(WebBrowser.with_incognito)

# Create a WebBrowser instance that starts off in incognito mode. Note that we call with_incognito through the class. 
# Despite not passing the cls argument in this call, Python implicitly passes the WebBrowser class to the function. All we need to pass in is the page parameter.
chrome = WebBrowser.with_incognito('shady-website.com')
print(chrome.is_incognito)
# confirm that history was not tracked while in incognito mode
print(chrome.history)


# Ex 42: Accessing Class attributes from within class methods
# In this exercise, we will create a geo_coordinates attribute in the WebBrowser class that holds the current latitude and longitude. 
# We will also add a class method called change_geo_coordinates() that will change the coordinates when called:

# Add the geo_coordinates class attribute and change the geo_coordinates() class method, like so:
class WebBrowser:
    geo_coordinates = {'lat': -4.764813, 'lng': 16.131331}
    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self. is_incognito = False

    def navigate(self, new_page):
        self.current_page = new_page
        if not self.is_incognito:
            self.history.append(new_page)
    def clear_history(self):
        self.history[:-1] = []

    @classmethod
    def with_incognito(cls, page):
        instance = cls(page)
        instance.is_incognito = True
        instance.history = []
        return instance

    @classmethod
    def change_geo_coordinates(cls, new_coordinates):
        if new_coordinates['lat'] > 90 or new_coordinates['lat'] < -90:
            print('Invalid value for lattitude. Lattitude should be within the range from -90 to 90 degrees.')
            return None
        if new_coordinates['lng'] > 180 or new_coordinates ['lng'] < -180:
            print('Invalid value for longitude. Longitude should be within the range from -180 to 180 degrees.')
            return None 
        cls.geo_coordinates = new_coordinates

#  Our class method, change_geo_coordinates, takes the new_coordinates parameter, which is a dictionary. 
#  It checks whether the latitude and longitude provided in the parameters are valid and then changes the class attribute geo_coordinates 
#  to reflect the new coordinates that have been provided. We can test this out.

# Create a WebBrowser instance, firefox, and check its geocoordinates. It fetches the attribute from the class:
firefox = WebBrowser('www.org')
print(firefox.geo_coordinates)

# Calling change_geo_coordinates on the class as we do in the next line changes the geo_coordinates attribute for all of the class's instances 
# (since they fetch the attribute from the class), and hence this change reflects for the firefox instance:
WebBrowser.change_geo_coordinates({'lat': 31, 'lng': 123})
print(firefox.geo_coordinates)
WebBrowser.change_geo_coordinates({'lat': -100, 'lng': 123})
print(firefox.geo_coordinates)
WebBrowser.change_geo_coordinates({'lat': 31, 'lng': 190})
print(firefox.geo_coordinates)