class IndexOutOfBoundsError(Exception):
    
    def __init__(self, message="Index out of bounds"):
        super().__init__(message)

class InvalidInputError(Exception):
   
    def __init__(self, message="Invalid input"):
        super().__init__(message)

