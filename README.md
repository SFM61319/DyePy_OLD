# Dyepy  
A Python module to work with anything related to colors.  
  
From styling the text to changing the foreground and background colors to converting colors to and from different color spaces, or defaulting them to Hexadecimal codes/values (as most Python modules support or only accept HEX codes), this module can easily help you with ALL of it. And yeah, it even has CSS3 color support (like named colors with their respective Hex values and some added colors - which are famous or are used/seen a lot).  
  
Detailed description/documentation for each and every class and function is written to make everything in the module understandable to every python developer. It is recommended to run this module - or a program this module is being imported in - to be ran on a command-line (like [Bash](http://ftp.gnu.org/gnu/bash/bash-5.0.tar.gz "Bourne Again SHell (BASH)"), [PowerShell](https://github.com/PowerShell/PowerShell/releases "Windows PowerShell 7"), [Command Prompt](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjDyuXTzIbqAhWzQjABHbOABRMQFjANegQIAhAB&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCmd.exe&usg=AOvVaw20rJophR24-G5GxhuDu-nd "Command Prompt"), etc.) for the module to work properly and give the most accurate and complete results (although results may vary with the command-lines, and some font styles may not work if they are not supported by the command-line)  
  
[01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01111001 01101111 01110101 01110100 01110101 00101110 01100010 01100101 00101111 01100100 01010001 01110111 00110100 01110111 00111001 01010111 01100111 01011000 01100011 01010001](https://youtu.be/dQw4w9WgXcQ "Click to crack this binary code")  
  
## Installation  
The entire code in written in pure python using only its builtin packages. So, there is nothing to install (apart from python).  
It is recommended to use the [latest stable version of python](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe "Click to download") (Python 3.8.3, as of 16/06/2020).  
  
## Usage (example) 
You can either simply run the file to use its own mini command-line (kinda) using:
```powershell
python.exe dyepy.py
```  
Or you can simply copy/write this example program and run it:  
```python
# Import tkinter for demonstatration of colors
try:
    from Tkinter import Button  # Python 2

except (ModuleNotFoundError, ImportError):
    from tkinter import Button  # Python 3

# Import randint for random integers in a range
from random import randint  # Bad practice, but no collisions possible


# Import this module to the program
import dyepy


def change_bgcolor():
    """Changes the app background color and returns None"""
    
    global root
    
    rgb_list = []
    
    for _ in range(0, 3, 1):
        rgb_list.append(randint(0, 255))
    
    r, g, b = rgb_list
    
    # Change the background color to a new randomly generated color
    root.configure(background=dyepy.rgb(red=r, green=g, blue=b))


root = Tk()
root.title('Usage (Example)')
root.configure(background=dyepy.Colors.BLACK)

button = Button(root, text='Change color',
                fg=dyepy.Colors.WHITE,
                bg=dyepy.Colors.WINDOWSBLUE,
                command=change_bgcolor,
                height=10, width=10)
button.grid(row=0, column=0, pady=10, padx=10)

root.mainloop()
```  
Save this python file (say, as `example.py`) and run it on a command-line using:  
```powershell
pythonw.exe example.py
```  
  
## Meta  
[SFM61319](https://github.com/SFM61319 "My GitHub") - [u/SFM61319](https://www.reddit.com/user/SFM61319 "Yes, I'm a Redditor") - [Avinash Maddikonda](mailto:svasssakavi@gmail.com "Send a mail")  
  
## Wanna contribute?  
Everyone is welcome to update my documentation and/or the python code. And you are the 'one' in everyone.  
To contribute, follow these steps:  
 1. [Fork it](https://github.com/SFM61319/dyepy/fork "Click to fork!")  
 2. Create your feature branch by entering `git checkout -b feature/fooBar` on your [Git Bash](https://git-scm.com/download/win "Click to download")  
 3. Commit your changes by entering `git commit -am "Add some foo bar, baz"`  
 4. Push to the branch by entering `git push origin feature/fooBar`  
 5. Create a new Pull Request (PR)  
  
*That's it, you have contributed to the documentation and/or the code!*  
  
Listen here,  
### I made a Python program to make any Spotify account premium for life (because of which I have a Spotify Premium too).  
[Here is the program](https://youtu.be/dQw4w9WgXcQ "Click to download the python file")  
  
If you have any major issues/doubts/feature requests or anything else which you don't want to do on your own or which you want to contribute without forking this repository, then [please open an issue](https://github.com/SFM61319/dyepy/issues/new/choose "Open issue")  
  
### Once again, thank you for spending your precious time here, it means a lot to me!  
