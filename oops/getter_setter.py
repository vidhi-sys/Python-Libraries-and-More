class device:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    # Getter method (traditional way)
    def get_name(self):
        return self.__name
    
    # Setter method (traditional way)
    def set_name(self, value):
        self.__name = value
    
    # Getter for price
    def get_price(self):
        return self.__price
    
    # Setter for price with validation
    def set_price(self, value):
        if not isinstance(value, str):
            raise ValueError("Price must be a string")
        self.__price = value
