#__name__ keyword

"""
When we import our own python file it can run the code from the imported file also which can lead to mistakes errors etc.
We can make sure it will not happen by writing the main code in a if statement:
- if __name__ == "__main__"
- Whole code.

"""

import test

test.welcome()