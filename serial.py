"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    >>> serial
    <SerialGenerator: start=100 next=101>
    """
    def __init__(self, start=0):
        """Initializes data structure for generate and reset functions"""
        self.start = self.next = start

    def generate(self):
        """Returns next serial number."""

        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets number to original start number"""
        self.next = self.start

    def __repr__(self):
        """Represents Serial Generator class"""
        return f"<Serial Generator: start={self.start} next={self.next}>"