"""Module with everything related to styles and colors in any way.

From rgb-hex converters to printing text in colors on a command-line,
this module allows you to deal with colors, also helpful when making
GUIs on Python (using tkinter, PyGame, etc.), by giving you the
colors you want in Hexadecimal to common colors to all types
of color representations supported by CSS3 too! Just name it!

Separate documentation for each function and class written with them.
To read the documentation, type `help(<function/class>)` into the CLI
"""


__authorinfo__ = \
    {

        'author': 'SFM61319',
        'github': 'https://github.com/SFM61319'
    }

__version__ = '0.0.4'


# A class to print in different colors (command-line only)
class Styles:
    """Styles class

A class to print both foreground and background in different
styles and colors (both as variables) on a command-line.

Print blue text with green background
E.g.: print(Styles.Bg.GREEN+Styles.Fg.BLUE+'Blue text'+Styles.RESET)

Or print the text in italics
E.g.: print(Styles.ITALIC+'Italic text'+Styles.RESET)

Here's what the constants are supposed to do:
    ---- Reset ----
    RESET: resets all the colors and styles used in the preceding text

    ---- Styles ----
    BOLD: bolds all the succeeding text
    DISABLE: reduces intensity (not widely supported)
    ITALIC: writes text in italics (not widely supported)
    UNDERLINE: underlines succeeding text
    SLOWBLINK: makes the text blink slowly (< 150 per minute)
    RAPIDBLINK: makes the text blink > 150/min (not widely supported)
    REVERSE: swaps default foreground and background colors and styles
    INVISIBLE: makes the foreground transparent
    STRIKETHROUGH: strikes through the text
    REVEAL: switches Conceal off (not widely supported)
    FRAME: frames the succeeding text
    ENCIRCLE: encircles the succeeding text
    OVERLINE: prints an overline on the succeeding text

    ---- Colors ----
        -- Foreground (Fg) --
        Fg.<COLOR_NAME>: sets the color to the succeeding fg
        Fg.n(<intensity>): sets the pre-selected color to fg
        Fg.rgb(<r>, <g>, <b>): sets the calculated color to fg

        -- Background (Bg) --
        Bg.<COLOR_NAME>: sets the color to the succeding bg
        Bg.n(<intensity>): sets the pre-selected color to bg
        Bg.rgb(<r>, <g>, <b>): sets the calculated color to bg

    For more info on `n`, refer to this table:
      https://i.stack.imgur.com/KTSQa.png

Please do not attempt to change these constants in the module
or the Python file this is being imported to, as it may affect
the output of the colors and may even corrupt and work irregularly
and not as expected when being ran in a Python environment

For more information on command-line styling, refer to:
  http://ascii-table.com/ansi-escape-sequences-vt-100.php
"""

    # Reset
    RESET = reset = '\x1b[00m'

    # Styles
    BOLD = bold = '\x1b[01m'
    DISABLE = disable = '\x1b[02m'
    ITALIC = italic = '\x1b[03m'
    UNDERLINE = underline = '\x1b[04m'
    SLOWBLINK = slowblink = '\x1b[05m'
    RAPIDBLINK = rapidblink = '\x1b[06m'
    REVERSE = reverse = '\x1b[07m'
    INVISIBLE = invisible = '\x1b[08m'
    STRIKETHROUGH = strikethrough = '\x1b[09m'
    REVEAL = reveal = '\x1b[28m'
    FRAME = frame = '\x1b[51m'
    ENCIRCLE = encircle = '\x1b[52m'
    OVERLINE = overline = '\x1b[53m'

    # Foreground colors
    class Foreground:
        """Foreground (Fg) sub-class to set foreground
colors of succeeding text occurences
"""

        BLACK = black = '\x1b[30m'
        RED = red = '\x1b[31m'
        GREEN = green = '\x1b[32m'
        ORANGE = orange = '\x1b[33m'
        BLUE = blue = '\x1b[34m'
        PURPLE = purple = '\x1b[35m'
        CYAN = cyan = '\x1b[36m'
        LIGHTGREY = lightgrey = '\x1b[37m'
        DARKGREY = darkgrey = '\x1b[90m'
        LIGHTRED = lightred = '\x1b[91m'
        LIGHTGREEN = lightgreen = '\x1b[92m'
        YELLOW = yellow = '\x1b[93m'
        LIGHTBLUE = lightblue = '\x1b[94m'
        PINK = pink = '\x1b[95m'
        LIGHTCYAN = lightcyan = '\x1b[96m'

        WHITE = white = '\x1b[38;2;255;255;255m'
        SPOTIFYGREEN = spotifygreen = '\x1b[38;2;29;185;84m'
        WINDOWSBLUE = '\x1b[38;2;0;120;215m'

        @staticmethod
        def n(intensity=0):
            """Returns calculated ANSI color code for unnamed bg colors

Can be used as follow:
print(Styles.Fg.n(69)+'Some random color'+Styles.RESET)

Refer to https://i.stack.imgur.com/KTSQa.png for more
information on how to use the function to get a color
"""

            if type(intensity) not in (int, float):
                raise TypeError(f'\'{intensity}\' must be of type \
\'int\' or \'float\', not {_type(intensity)}')

            if intensity < 0 or intensity > 255:
                raise ValueError(f'\'intensity\' must be ≥ 0 and ≤ 255\
, not \'{intensity}\'')

            intensity = round(intensity)

            return f'\x1b[38;5;{intensity}m'

        @staticmethod
        def rgb(red=0, blue=0, green=0):
            """Returns calculated ANSI color code for unnamed fg colors

Can be used as follows:
print(Styles.Fg.rgb(0, 120, 215)+'Windows Default Blue'+Styles.RESET)
print(Styles.Fg.rgb(29, 185, 84)+'Spotify Green'+Styles.RESET)

Note: 0 ≤ r, g, b ≤ 255
"""

            # Check if all parameters are perfect or not
            for color_value in (red, green, blue):
                if type(color_value) not in (int, float):
                    raise TypeError(f'\'{color_value}\' must be of \
type \'int\' or \'float\', not {_type(color_value)}')

                elif color_value < 0 or color_value > 255:
                    raise ValueError(f'\'color_value\' must be ≥ 0 \
and ≤ 255, not \'{color_value}\'')

            red, green, blue = round(red), round(green), round(blue)

            return f'\x1b[38;2;{red};{blue};{green}m'

    Fg = Foreground

    # Background colors
    class Background:
        """Background (Bg) sub-class to set background
colors of succeeding text occurences"""

        BLACK = black = '\x1b[40m'
        RED = red = '\x1b[41m'
        GREEN = green = '\x1b[42m'
        ORANGE = orange = '\x1b[43m'
        BLUE = blue = '\x1b[44m'
        PURPLE = purple = '\x1b[45m'
        CYAN = cyan = '\x1b[46m'
        LIGHTGREY = lightgrey = '\x1b[47m'
        DARKGREY = darkgrey = '\x1b[100m'
        LIGHTRED = lightred = '\x1b[101m'
        LIGHTGREEN = lightgreen = '\x1b[102m'
        YELLOW = yellow = '\x1b[103m'
        LIGHTBLUE = lightblue = '\x1b[104m'
        PINK = pink = '\x1b[105m'
        LIGHTCYAN = lightcyan = '\x1b[106m'

        WHITE = white = '\x1b[48;2;255;255;255m'
        SPOTIFYGREEN = spotifygreen = '\x1b[48;2;29;185;84m'
        WINDOWSBLUE = '\x1b[48;2;0;120;215m'

        @staticmethod
        def n(intensity=255):
            """Returns calculated ANSI color code for unnamed bg colors

Can be used as follow:
print(Styles.Bg.n(69)+'Some random color'+Styles.RESET)

Refer to https://i.stack.imgur.com/KTSQa.png for more
information on how to use the function to get a color
"""

            if type(intensity) not in (int, float):
                raise TypeError(f'\'{intensity}\' must be of type \
\'int\' or \'float\', not {_type(intensity)}')

            if intensity < 0 or intensity > 255:
                raise ValueError(f'\'intensity\' must be ≥ 0 and \
≤ 255, not \'{intensity}\'')

            intensity = round(intensity)

            return f'\x1b[48;5;{intensity}m'

        @staticmethod
        def rgb(red=255, blue=255, green=255):
            """Returns calculated ANSI color code for unnamed bg colors

Can be used as follows:
print(Styles.Bg.rgb(0, 120, 215)+'Windows Default Blue'+Styles.RESET)
print(Styles.Bg.rgb(29, 185, 84)+'Spotify Green'+Styles.RESET)

Note: 0 ≤ red, green, blue ≤ 255
"""

            # Check if all parameters are perfect or not
            for color_value in (red, green, blue):
                if type(color_value) not in (int, float):
                    raise TypeError(f'\'{color_value}\' must be of \
type \'int\' or \'float\', not {_type(color_value)}')

                elif color_value < 0 or color_value > 255:
                    raise ValueError(f'\'color_value\' must be ≥ 0 \
and ≤ 255, not \'{color_value}\'')

            red, green, blue = round(red), round(green), round(blue)

            return f'\x1b[48;2;{red};{blue};{green}m'

    Bg = Background


# A class to use pre-defined colors from CSS3
class Colors:
    """Colors class

A class of named Hex color codes as constants
that can be used simply by referencing them.

These names and values have been inherited from CSS3,
and there are some extra built-in colors like the
Windows Default Blue color and the Spotify Green color.

This class is completely different from the class
`Styles` (which can be used for font-styling and coloring)
"""

    ALICEBLUE = '#f0f8ff'
    ANTIQUEWHITE = '#faebd7'
    AQUA = '#00ffff'
    AQUAMARINE = '#7fffd4'
    AZURE = '#f0ffff'
    BEIGE = '#f5f5dc'
    BISQUE = '#ffe4c4'
    BLACK = '#000000'
    BLANCHEDALMOND = '#ffebcd'
    BLUE = '#0000ff'
    BLUEVIOLET = '#8a2be2'
    BROWN = '#a52a2a'
    BURLYWOOD = '#deb887'
    CADETBLUE = '#5f9ea0'
    CHARTREUSE = '#7fff00'
    CHOCOLATE = '#d2691e'
    CORAL = '#ff7f50'
    CORNFLOWERBLUE = '#6495ed'
    CORNSILK = '#fff8dc'
    CRIMSON = '#dc143c'
    CYAN = '#00ffff'
    DARKBLUE = '#00008b'
    DARKCYAN = '#008b8b'
    DARKGOLDENROD = '#b8860b'
    DARKGRAY = '#a9a9a9'
    DARKGREEN = '#006400'
    DARKKHAKI = '#bdb76b'
    DARKMAGENTA = '#8b008b'
    DARKOLIVEGREEN = '#556b2f'
    DARKORANGE = '#ff8c00'
    DARKORCHID = '#9932cc'
    DARKRED = '#8b0000'
    DARKSALMON = '#e9967a'
    DARKSEAGREEN = '#8fbc8f'
    DARKSLATEBLUE = '#483d8b'
    DARKSLATEGRAY = '#2f4f4f'
    DARKTURQUOISE = '#00ced1'
    DARKVIOLET = '#9400d3'
    DEEPPINK = '#ff1493'
    DEEPSKYBLUE = '#00bfff'
    DIMGRAY = '#696969'
    DODGERBLUE = '#1e90ff'
    FIREBRICK = '#b22222'
    FLORALWHITE = '#fffaf0'
    FORESTGREEN = '#228b22'
    FUCHSIA = '#ff00ff'
    GAINSBORO = '#dcdcdc'
    GHOSTWHITE = '#f8f8ff'
    GOLD = '#ffd700'
    GOLDENROD = '#daa520'
    GRAY = '#808080'
    GREEN = '#008000'
    GREENYELLOW = '#adff2f'
    HONEYDEW = '#f0fff0'
    HOTPINK = '#ff69b4'
    INDIANRED = '#cd5c5c'
    INDIGO = '#4b0082'
    IVORY = '#fffff0'
    KHAKI = '#f0e68c'
    LAVENDER = '#e6e6fa'
    LAVENDERBLUSH = '#fff0f5'
    LAWNGREEN = '#7cfc00'
    LEMONCHIFFON = '#fffacd'
    LIGHTBLUE = '#add8e6'
    LIGHTCORAL = '#f08080'
    LIGHTCYAN = '#e0ffff'
    LIGHTGOLDENRODYELLOW = '#fafad2'
    LIGHTGREEN = '#90ee90'
    LIGHTGREY = '#d3d3d3'
    LIGHTPINK = '#ffb6c1'
    LIGHTSALMON = '#ffa07a'
    LIGHTSEAGREEN = '#20b2aa'
    LIGHTSKYBLUE = '#87cefa'
    LIGHTSLATEGRAY = '#778899'
    LIGHTSTEELBLUE = '#b0c4de'
    LIGHTYELLOW = '#ffffe0'
    LIME = '#00ff00'
    LIMEGREEN = '#32cd32'
    LINEN = '#faf0e6'
    MAGENTA = '#ff00ff'
    MAROON = '#800000'
    MEDIUMAQUAMARINE = '#66cdaa'
    MEDIUMBLUE = '#0000cd'
    MEDIUMORCHID = '#ba55d3'
    MEDIUMPURPLE = '#9370d8'
    MEDIUMSEAGREEN = '#3cb371'
    MEDIUMSLATEBLUE = '#7b68ee'
    MEDIUMSPRINGGREEN = '#00fa9a'
    MEDIUMTURQUOISE = '#48d1cc'
    MEDIUMVIOLETRED = '#c71585'
    MIDNIGHTBLUE = '#191970'
    MINTCREAM = '#f5fffa'
    MISTYROSE = '#ffe4e1'
    MOCCASIN = '#ffe4b5'
    NAVAJOWHITE = '#ffdead'
    NAVY = '#000080'
    OLDLACE = '#fdf5e6'
    OLIVE = '#808000'
    OLIVEDRAB = '#6b8e23'
    ORANGE = '#ffa500'
    ORANGERED = '#ff4500'
    ORCHID = '#da70d6'
    PALEGOLDENROD = '#eee8aa'
    PALEGREEN = '#98fb98'
    PALETURQUOISE = '#afeeee'
    PALEVIOLETRED = '#d87093'
    PAPAYAWHIP = '#ffefd5'
    PEACHPUFF = '#ffdab9'
    PERU = '#cd853f'
    PINK = '#ffc0cb'
    PLUM = '#dda0dd'
    POWDERBLUE = '#b0e0e6'
    PURPLE = '#800080'
    REBECCAPURPLE = '#663399'
    RED = '#ff0000'
    ROSYBROWN = '#bc8f8f'
    ROYALBLUE = '#4169e1'
    SADDLEBROWN = '#8b4513'
    SALMON = '#fa8072'
    SANDYBROWN = '#f4a460'
    SEAGREEN = '#2e8b57'
    SEASHELL = '#fff5ee'
    SIENNA = '#a0522d'
    SILVER = '#c0c0c0'
    SKYBLUE = '#87ceeb'
    SLATEBLUE = '#6a5acd'
    SLATEGRAY = '#708090'
    SNOW = '#fffafa'
    SPOTIFYGREEN = '#1db954'
    SPRINGGREEN = '#00ff7f'
    STEELBLUE = '#4682b4'
    TAN = '#d2b48c'
    TEAL = '#008080'
    THISTLE = '#d8bfd8'
    TOMATO = '#ff6347'
    TURQUOISE = '#40e0d0'
    VIOLET = '#ee82ee'
    WHEAT = '#f5deb3'
    WHITE = '#ffffff'
    WHITESMOKE = '#f5f5f5'
    WINDOWSBLUE = '#0078d7'
    YELLOW = '#ffff00'
    YELLOWGREEN = '#9acd32'


# Hidden function `_type` to get the exact type of an object in strings
def _type(object_or_name):
    """Returns the exact type of *object_or_name* using `type`
"""

    type_ = str(type(object_or_name)).replace('<class ', '').replace('>', '')

    return type_


# A function to clamp three values such that the value
# never crosses the minimum and the maximum value
def clamp(minimum=0, value=0.5, maximum=1):
    """Returns the clamped value between *minimum* and *maximum*

A clamped value is the value itself when it lies
between the minimum and the maximum, and if the
value crosses the extremes, then the extremity
closer to the value becomes the clamped value.

E.g.:
clamp(0, 0.5, 1) -> 0.5;
clamp(0, 2, 1) -> 1;
clamp(0, -1, 1) -> 0;
"""

    for arg in (minimum, value, maximum):
        if type(arg) not in (int, float):
            raise TypeError(f'\'{arg}\' must be of type \'int\' or \
\'float\', not {_type(arg)}')

    return max(minimum, min(value, maximum))


# A function to convert RGB values to Hex values
def rgb(red=0, green=0, blue=0):
    """Returns the Hex value from an RGB value for many modules use
Hex values as their default or accepted color code values

Can also be used as a RGB-to-Hex converter
"""

    # Check if all parameters are perfect or not
    for color_value in (red, green, blue):
        if type(color_value) not in (int, float):
            raise TypeError(f'\'{color_value}\' must be of type \
\'int\' or \'float\', not {_type(color_value)}')

        elif color_value < 0 or color_value > 255:
            raise ValueError(f'\'color_value\' must be ≥ 0 and ≤ 255, \
not \'{color_value}\'')

    red, green, blue = round(red), round(green), round(blue)

    return '#%02x%02x%02x' % (red, green, blue)


# A function to convert HSV values to Hex values
def hsv(hue=0, saturation=0, value=0):
    """Returns the Hex value from an HSV value for many modules use
Hex values as their default or accepted color code values

0 ≤ hue ≤ 360; although other values is also acceptable
0 ≤ saturation, value ≤ 1; any other value will be clamped

Note: both HSB and HSV are the same colorspaces

Can also be used as a HSV-to-Hex converter
"""

    red, green, blue = hsv2rgb(hue, saturation, value)

    return rgb(red, green, blue)


hsb = hsv  # Since both are the same


# A function to convert HSL values to Hex values
def hsl(hue=0, saturation=0, luminance=0):
    """Returns the Hex value from an HSL value for many modules use
Hex values as their default or accepted color code values

0 ≤ hue ≤ 360; although a value > 360 is also acceptable
0 ≤ saturation, luminance ≤ 1; any other value will be clamped

Note: HSV and HSL are different colorspaces, for more information
refer to:
  https://en.wikipedia.org/wiki/HSL_and_HSV

Can also be used as a HSL-to-Hex converter
"""

    red, green, blue = hsl2rgb(hue, saturation, luminance)

    return rgb(red, green, blue)


# A function to convert a YIQ color to Hex values
def yiq(y=0, i=0, q=0):
    """Returns the Hex value from a YIQ color space for many modules
use Hex values as their default or accepted color code values

0 ≤ y, i, q ≤ 1, all other values will be clamped

Can also be used as a YIQ-to-Hex converter
"""

    red, green, blue = yiq2rgb(y, i, q)

    return rgb(red, green, blue)


# A function to convert a CMYK color to Hex values
def cmyk(cyan=0, magenta=0, yellow=0, black_key=0):
    """Returns the Hex value from a CMYK color space for many modules
use Hex values as their default or accepted color code values

0 ≤ cyan, magenta, yellow, black_key ≤ 1, other values will be clamped

Can also be used as a CMYK-to-Hex converter
"""

    red, green, blue = cmyk2rgb(cyan, magenta, yellow, black_key)

    return rgb(red, green, blue)


# A function to convert Hex values to RGB colors
def hex2rgb(hexcode='#000000', as_string=False):
    """Returns the equivalent RGB values of a hex color *hexcode*

as_string (bool): decides if RGB values are to be returned in
strings in the format 'rgb(<red>, <green>, <blue>)' or as a tuple.
Defaults to False (returns a tuple of red, green, blue by default)
"""

    if len(hexcode) == 4:  # Repetative shortcut
        hexcode = f'#{hexcode[1]*2}{hexcode[2]*2}{hexcode[3]*2}'

    red = int(hexcode[1:3], 16)
    green = int(hexcode[3:5], 16)
    blue = int(hexcode[5:7], 16)

    if as_string:
        return f'rgb({red}, {green}, {blue})'

    return (red, green, blue)


# A function to convert Hex values to HSV colors
def hex2hsv(hexcode='#000000', as_string=False):
    """Returns the equivalent HSV/HSB values of a hex color *hexcode*

as_string (bool): decides if HSV values are to be returned in
strings in the format 'hsv(<hue>, <saturation>, <value>)' or as a tuple.
Defaults to False (returns a tuple of hue, saturation,
luminance by default)
"""

    red, green, blue = hex2rgb(hexcode)
    hue, saturation, value = rgb2hsv(red, green, blue)

    if as_string:
        return f'hsv({hue}, {saturation}, {value})'

    return (hue, saturation, value)


# A function to convert Hex values to HSL colors
def hex2hsl(hexcode='#000000', as_string=False):
    """Returns the equivalent HSL values of a hex color *hexcode*

as_string (bool): decides if HSL values are to be returned in
strings in the format 'hsl(<hue>, <saturation>, <luminance>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
luminance by default)
"""

    red, green, blue = hex2rgb(hexcode)
    hue, saturation, luminance = rgb2hsl(red, green, blue)

    if as_string:
        return f'hsl({hue}, {saturation}, {luminance})'

    return (hue, saturation, luminance)


# A function to convert Hex values to YIQ colors
def hex2yiq(hexcode='#000000', as_string=False):
    """Returns the equivalent YIQ values of a hex color *hexcode*

as_string (bool): decides if YIQ values are to be returned in
strings in the format 'yiq(<y>, <i>, <q>)' or as a tuple.
Defaults to False (returns a tuple of y, i, q by default)
"""

    red, green, blue = hex2rgb(hexcode)
    y, i, q = rgb2yiq(red, green, blue)

    if as_string:
        return f'yiq({y}, {i}, {q})'

    return (y, i, q)


# A function to convert Hex values to CMYK colors
def hex2cmyk(hexcode='#000000', as_string=False):
    """Returns the equivalent CMYK values of a hex color *hexcode*

as_string (bool): decides if CMYK values are to be returned in
strings in the format 'cmyk(<cyan>, <magenta>, <yellow>, <black_key>)'
or as a tuple. Defaults to False (returns a tuple of cyan, magenta,
yellow, key by default)
"""

    red, green, blue = hex2rgb(hexcode)
    cyan, magenta, yellow, black_key = rgb2cmyk(red, green, blue)

    if as_string:
        return f'cmyk({cyan}, {magenta}, {yellow}, {black_key})'

    return (cyan, magenta, yellow, black_key)


# A function to convert RGB colors to HSV colors
def rgb2hsv(red=0, green=0, blue=0, as_string=False):
    """Returns the equivalent HSV values of an RGB color value

as_string (bool): decides if HSV values are to be returned in
strings in the format 'hsv(<hue>, <saturation>, <value>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
value by default)
"""

    for color_value in (red, green, blue):
        if type(color_value) not in (int, float):
            raise TypeError(f'\'{color_value}\' must be of type \
\'int\' or \'float\', not {_type(color_value)}')

        if color_value > 255 or color_value < 0:
            raise ValueError(f'\'color_value\' must be ≥ 0 and ≤ 255,\
 not {color_value}')

    red /= 255
    green /= 255
    blue /= 255

    cmax = max(red, green, blue)
    cmin = min(red, green, blue)

    diff = cmax - cmin

    # Hue calculation
    if diff == 0:
        hue = 0

    elif cmax == red:
        hue = 60 * (((green - blue) / diff) % 6)

    elif cmax == green:
        hue = 60 * (((blue - red) / diff) + 2)

    elif cmax == blue:
        hue = 60 * (((red - green) / diff) + 4)

    hue = round(hue)

    # Saturation calculation
    saturation = 0 if cmax == 0 else diff / cmax

    # Value calculation
    value = cmax

    if as_string:
        return f'hsv({hue}, {saturation}, {value})'

    return (hue, saturation, value)


# A function to convert an RGB color to an HSL color
def rgb2hsl(red=0, green=0, blue=0, as_string=False):
    """Returns the equivalent HSL values of an RGB color value

as_string (bool): decides if HSL values are to be returned in
strings in the format 'hsl(<hue>, <saturation>, <luminance>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
luminance by default)
"""

    red /= 255
    green /= 255
    blue /= 255

    cmax = max(red, green, blue)
    cmin = min(red, green, blue)

    diff = cmax - cmin

    # Luminance calculation
    luminance = (cmax + cmin) / 2

    # Hue calculation
    if diff == 0:
        hue = 0

    elif cmax == red:
        hue = 60 * (((green - blue) / diff) % 6)

    elif cmax == green:
        hue = 60 * (((blue - red) / diff) + 2)

    elif cmax == blue:
        hue = 60 * (((red - green) / diff) + 4)

    hue = round(hue)

    # Saturation calculation
    saturation = 0 if diff == 0 else diff / (1 - abs(2 * luminance - 1))

    if as_string:
        return f'hsl({hue}, {saturation}, {luminance})'

    return (hue, saturation, luminance)


# A function to convert an RGB color to YIQ color
def rgb2yiq(red=0, green=0, blue=0, as_string=False):
    """Returns the equivalent YIQ values of an RGB color value

as_string (bool): decides if YIQ values are to be returned in
strings in the format 'yiq(<y>, <i>, <q>)' or as a tuple.
Defaults to False (returns a tuple of y, i, q by default)
"""

    red /= 255
    blue /= 255
    green /= 255

    y = 0.30 * red + 0.59 * green + 0.11 * blue
    i = 0.74 * (red - y) - 0.27 * (blue - y)
    q = 0.48 * (red - y) + 0.41 * (blue - y)

    y = round(clamp(value=y) * 255)
    i = round(clamp(value=i) * 255)
    q = round(clamp(value=q) * 255)

    if as_string:
        return f'yiq({y}, {i}, {q})'

    return (y, i, q)


# A function to convert an RGB color to CMYK color
def rgb2cmyk(red=0, green=0, blue=0, as_string=False):
    """Returns the equivalent CMYK values of an RGB color value

as_string (bool): decides if CMYK values are to be returned in
strings in the format 'cmyk(<cyan>, <magenta>, <yellow>, <key>)'
or as a tuple. Defaults to False (returns a tuple of cyan, magenta,
yellow, key by default)
"""

    red /= 255
    green /= 255
    blue /= 255

    black_key = 1 - max(red, green, blue)

    white_key = 1 - black_key if black_key != 1 else 1

    cyan = (1 - red - black_key) / white_key
    magenta = (1 - green - black_key) / white_key
    yellow = (1 - blue - black_key) / white_key

    if black_key == int(black_key):
        black_key = int(black_key)

    if cyan == int(cyan):
        cyan = int(cyan)

    if magenta == int(magenta):
        magenta = int(magenta)

    if yellow == int(yellow):
        yellow = int(yellow)

    if as_string:
        return f'cmyk({cyan}, {magenta}, {yellow}, {black_key})'

    return (cyan, magenta, yellow, black_key)


# A function to convert an HSV color to an RGB color
def hsv2rgb(hue=0, saturation=0, value=0, as_string=False):
    """Returns the equivalent RGB values of an HSV color value

as_string (bool): decides if RGB values are to be returned in
strings in the format 'rgb(<red>, <green>, <blue>)' or as a tuple.
Defaults to False (returns a tuple of red, green, blue by default)
"""

    # Check if parameters are perfect or not
    if type(hue) not in (int, float):
        raise TypeError(f'\'{hue}\' must be of type \'int\' or \
\'float\', not {_type(hue)}')

    hue -= 360 * (hue // 360)  # Cycle clamping *hue* in [0, 360]
    hue /= 360

    for color_value in (saturation, value):
        if type(color_value) not in (int, float):
            raise TypeError(f'\'{color_value}\' must be of type \
\'int\' or \'float\', not {_type(color_value)}')

    saturation = clamp(value=saturation)
    value = clamp(value=value)

    if saturation == 0:
        value *= 255
        red = green = blue = value

        return (red, green, blue)

    i = int(hue * 6)
    f = hue * 6 - i
    p = 255 * (value * (1 - saturation))
    q = 255 * (value * (1 - saturation * f))
    t = 255 * (value * (1 - saturation * (1 - f)))

    value *= 255
    i %= 6

    if i == 0:
        red, green, blue = (value, t, p)

    elif i == 1:
        red, green, blue = (q, value, p)

    elif i == 2:
        red, green, blue = (p, value, t)

    elif i == 3:
        red, green, blue = (p, q, value)

    elif i == 4:
        red, green, blue = (t, p, value)

    elif i == 5:
        red, green, blue = (value, p, q)

    if as_string:
        return f'rgb({red}, {green}, {blue})'

    return (red, green, blue)


# A function to convert an HSV color to an HSL color
def hsv2hsl(hue=0, saturation=0, value=0, as_string=False):
    """Returns the equivalent HSL values of an HSV color value

as_string (bool): decides if HSL values are to be returned in
strings in the format 'hsl(<hue>, <saturation>, <value>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
value by default)
"""

    red, green, value = hsv2rgb(hue, saturation, value)
    hue, saturation, luminance = rgb2hsl(red, green, value)

    if as_string:
        return f'hsl({hue}, {saturation}, {luminance})'

    return (hue, saturation, luminance)


# A function to convert an HSV color to a YIQ color
def hsv2yiq(hue=0, saturation=0, value=0, as_string=False):
    """Returns the equivalent YIQ values of an HSV color value

as_string (bool): decides if YIQ values are to be returned in
strings in the format 'yiq(<y>, <i>, <q>)' or as a tuple.
Defaults to False (returns a tuple of y, i, q by default)
"""

    red, green, blue = hsv2rgb(hue, saturation, value)
    y, i, q = rgb2yiq(red, green, blue)

    if as_string:
        return f'yiq({y}, {i}, {q})'

    return (y, i, q)


# A function to convert an HSV color to a CMYK color
def hsv2cmyk(hue=0, saturation=0, value=0, as_string=False):
    """Returns the equivalent CMYK values of an HSV color value

as_string (bool): decides if CMYK values are to be returned in
strings in the format 'cmyk(<cyan>, <magenta>, <yellow>, <key>)'
or as a tuple. Defaults to False (returns a tuple of cyan, magenta,
yellow, key by default)
"""

    red, green, blue = hsv2rgb(hue, saturation, value)
    cyan, magenta, yellow, black_key = rgb2cmyk(red, green, blue)

    if as_string:
        return f'cmyk({cyan}, {magenta}, {yellow}, {black_key})'

    return (cyan, magenta, yellow, black_key)


# A function to convert HSL color to an RGB color
def hsl2rgb(hue=0, saturation=0, luminance=0, as_string=False):
    """Returns the equivalent RGB values of an HSL color value

as_string (bool): decides if RGB values are to be returned in
strings in the format 'rgb(<red>, <green>, <blue>)' or as a tuple.
Defaults to False (returns a tuple of red, green, blue by default)
"""

    # Check if parameters are perfect or not
    if type(hue) not in (int, float):
        raise TypeError(f'\'{hue}\' must be of type \'int\' or \
\'float\', not {_type(hue)}')

    hue -= 360 * (hue // 360)

    for color_value in (saturation, luminance):
        if type(color_value) not in (int, float):
            raise TypeError(f'\'{color_value}\' must be of type \
\'int\' or \'float\', not {_type(color_value)}')

    saturation = clamp(value=saturation)
    luminance = clamp(value=luminance)

    c = (1 - abs(2 * luminance - 1)) * saturation
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = luminance - c / 2

    if 0 <= hue < 60:
        red, green, blue = (c, x, 0)

    if 60 <= hue < 120:
        red, green, blue = (x, c, 0)

    if 120 <= hue < 180:
        red, green, blue = (0, c, x)

    if 180 <= hue < 240:
        red, green, blue = (0, x, c)

    if 240 <= hue < 300:
        red, green, blue = (x, 0, c)

    if 300 <= hue < 360:
        red, green, blue = (c, 0, x)

    red = round((red + m) * 255)
    green = round((green + m) * 255)
    blue = round((blue + m) * 255)

    if as_string:
        return f'rgb({red}, {green}, {blue})'

    return (red, green, blue)


# A function to convert an HSL color to an HSV color
def hsl2hsv(hue=0, saturation=0, luminance=0, as_string=False):
    """Returns the equivalent HSV values of an HSL color value

as_string (bool): decides if HSV values are to be returned in
strings in the format 'hsv(<hue>, <saturation>, <value>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
value by default)
"""

    red, green, blue = hsl2rgb(hue, saturation, luminance)
    hue, saturation, value = rgb2hsv(red, green, blue)

    if as_string:
        return f'hsv({hue}, {saturation}, {value})'

    return (hue, saturation, value)


# A function to convert an HSL color to a YIQ color
def hsl2yiq(hue=0, saturation=0, luminance=0, as_string=False):
    """Returns the equivalent YIQ values of an HSL color value

as_string (bool): decides if YIQ values are to be returned in
strings in the format 'yiq(<y>, <i>, <q>)' or as a tuple.
Defaults to False (returns a tuple of y, i, q by default)
"""

    red, green, blue = hsl2rgb(hue, saturation, luminance)
    y, i, q = rgb2yiq(red, green, blue)

    if as_string:
        return f'yiq({y}, {i}, {q})'

    return (y, i, q)


# A function to convert an HSL color to a CMYK color
def hsl2cmyk(hue=0, saturation=0, luminance=0, as_string=False):
    """Returns the equivalent CMYK values of an HSL color value

as_string (bool): decides if CMYK values are to be returned in
strings in the format 'cmyk(<cyan>, <magenta>, <yellow>, <key>)'
or as a tuple. Defaults to False (returns a tuple of cyan, magenta,
yellow, key by default)
"""

    red, green, blue = hsl2rgb(hue, saturation, luminance)
    cyan, magenta, yellow, black_key = rgb2cmyk(red, green, blue)

    if as_string:
        return f'cmyk({cyan}, {magenta}, {yellow}, {black_key})'

    return (cyan, magenta, yellow, black_key)


# A function to convert a YIQ color to an RGB color
def yiq2rgb(y=0, i=0, q=0, as_string=False):
    """Returns the equivalent RGB values of a YIQ color value

as_string (bool): decides if RGB values are to be returned in
strings in the format 'rgb(<red>, <green>, <blue>)' or as a tuple.
Defaults to False (returns a tuple of red, green, blue by default)
"""

    for value in (y, i, q):
        if type(value) not in (int, float):
            raise TypeError(f'\'{value}\' must be of type \'int\' or \
\'float\', not {_type(value)}')

    y = clamp(0, y, 1)
    i, q = clamp(0, i, 1), clamp(0, q, 1)

    red = y + 0.9468822170900693 * i + 0.6235565819861433 * q
    green = y - 0.27478764629897834 * i - 0.6356910791873801 * q
    blue = y - 1.1085450346420322 * i + 1.7090069284064666 * q

    red = round(clamp(value=red) * 255)
    green = round(clamp(value=green) * 255)
    blue = round(clamp(value=blue) * 255)

    if as_string:
        return f'rgb({red}, {green}, {blue})'

    return (red, green, blue)


# A function to convert a YIQ color to an HSV color
def yiq2hsv(y=0, i=0, q=0, as_string=False):
    """Returns the equivalent HSV values of a YIQ color value

as_string (bool): decides if HSV values are to be returned in
strings in the format 'hsv(<hue>, <saturation>, <value>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
value by default)
"""

    red, green, blue = yiq2rgb(y, i, q)
    hue, saturation, value = rgb2hsv(red, green, blue)

    if as_string:
        return f'hsv({hue}, {saturation}, {value})'

    return (hue, saturation, value)


# A function to convert a YIQ color to an HSL color
def yiq2hsl(y=0, i=0, q=0, as_string=False):
    """Returns the equivalent HSL values of a YIQ color value

as_string (bool): decides if HSL values are to be returned in
strings in the format 'hsl(<hue>, <saturation>, <luminance>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
luminance by default)
"""

    red, green, blue = yiq2rgb(y, i, q)
    hue, saturation, luminance = rgb2hsl(red, green, blue)

    if as_string:
        return f'hsl({hue}, {saturation}, {luminance})'

    return (hue, saturation, luminance)


# A function to convert a YIQ color to a CMYK color
def yiq2cmyk(y=0, i=0, q=0, as_string=False):
    """Returns the equivalent CMYK values of a YIQ color value

as_string (bool): decides if CMYK values are to be returned in
strings in the format 'cmyk(<cyan>, <magenta>, <yellow>, <key>)'
or as a tuple. Defaults to False (returns a tuple of cyan, magenta,
yellow, black_key by default)
"""

    red, green, blue = yiq2rgb(y, i, q)
    cyan, magenta, yellow, black_key = rgb2cmyk(red, green, blue)

    if as_string:
        return f'cmyk({cyan}, {magenta}, {yellow}, {black_key})'

    return (cyan, magenta, yellow, black_key)


# A function to convert a CMYK color to an RGB color
def cmyk2rgb(cyan=0, magenta=0, yellow=0, black_key=0, as_string=False):
    """Returns the equivalent RGB values of an CMYK color value

as_string (bool): decides if RGB values are to be returned in
strings in the format 'rgb(<red>, <green>, <blue>)' or as a tuple.
Defaults to False (returns a tuple of red, green, blue by default)
"""

    for color in (cyan, magenta, yellow, black_key):
        if type(color) not in (int, float):
            raise TypeError(f'\'{color}\' must be of type \'int\' or \
\'float\', not {_type(color)}')

    cyan = clamp(value=cyan)
    magenta = clamp(value=magenta)
    yellow = clamp(value=yellow)
    black_key = clamp(value=black_key)

    red = 255 * (1 - cyan) * (1 - black_key)
    green = 255 * (1 - magenta) * (1 - black_key)
    blue = 255 * (1 - yellow) * (1 - black_key)

    if as_string:
        return f'rgb({red}, {green}, {blue})'

    return (red, green, blue)


# A function to convert a CMYK color to an HSV color
def cmyk2hsv(cyan=0, magenta=0, yellow=0, black_key=0, as_string=False):
    """Returns the equivalent HSV values of an CMYK color value

as_string (bool): decides if HSV values are to be returned in
strings in the format 'hsv(<hue>, <saturation>, <value>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
value by default)
"""

    red, green, blue = cmyk2rgb(cyan, magenta, yellow, black_key)
    hue, saturation, value = rgb2hsv(red, green, blue)

    if as_string:
        return f'hsv({hue}, {saturation}, {value})'

    return (hue, saturation, value)


# A function to convert a CMYK color to an HSL color
def cmyk2hsl(cyan=0, magenta=0, yellow=0, black_key=0, as_string=False):
    """Returns the equivalent HSL values of an CMYK color value

as_string (bool): decides if HSL values are to be returned in
strings in the format 'hsl(<hue>, <saturation>, <luminance>)'
or as a tuple. Defaults to False (returns a tuple of hue, saturation,
value by default)
"""

    red, green, blue = cmyk2rgb(cyan, magenta, yellow, black_key)
    hue, saturation, luminance = rgb2hsl(red, green, blue)

    if as_string:
        return f'hsl({hue}, {saturation}, {luminance})'

    return (hue, saturation, luminance)


# A function to convert a CMYK color to a YIQ color
def cmyk2yiq(cyan=0, magenta=0, yellow=0, black_key=0, as_string=False):
    """Returns the equivalent YIQ values of an CMYK color value

as_string (bool): decides if YIQ values are to be returned in
strings in the format 'yiq(<y>, <i>, <q>)' or as a tuple.
Defaults to False (returns a tuple of y, i, q by default)
"""

    red, green, blue = cmyk2rgb(cyan, magenta, yellow, black_key)
    y, i, q = rgb2yiq(red, green, blue)

    if as_string:
        return f'yiq({y}, {i}, {q})'

    return (y, i, q)


# A function to extract red, green, blue values from an RGB color
def extract_rgb(rgb='rgb(0, 0, 0)'):
    """Extracts and returns red, green, blue values from an RGB
string, set, list, tuple, or a dictionary, as a tuple object.

E.g.:
rgb = 'rgb(69, 69, 69)'
rgb = {69, 69, 69}  # Order: red, green, blue
rgb = [69, 69, 69]  # Order: red, green, blue
rgb = (69, 69, 69)  # Order: red, green, blue
rgb = {
    'red': 69,
    'green': 69,
    'blue': 69
}

Note: Dictionary keys may be different but also unique,
and, the color values order is: red, green, blue
"""

    # Extraction from a `str` object (string)
    if isinstance(rgb, str):
        rgb = rgb.replace(' ', '')  # Remove whitespaces
        rgb = rgb.replace('rgb(', '').replace(')', '')  # Remove non-ints
        rgb = rgb.split(',')  # Extract RGB values to a list
        rgb = list(map(float, rgb))  # Convert strings to numbers
        rgb = tuple(map(round, rgb))  # Round floating-points to ints

        return rgb

    # Extraction from a `set` object (set)
    if isinstance(rgb, set):
        return tuple(round(float(value)) for value in rgb)

    # Extraction from a `list` object (list)
    if isinstance(rgb, list):
        rgb = list(map(float, rgb))
        rgb = tuple(map(round, rgb))

        return rgb

    # Extraction from a `tuple` object (tuple)
    if isinstance(rgb, tuple):
        rgb = list(map(float, list(rgb)))
        rgb = tuple(map(round, rgb))

        return rgb

    # Extraction from a `dict` object (dict.values)
    if isinstance(rgb, dict):
        return tuple(round(float(value)) for value in rgb.values())

    else:
        raise TypeError(f'unacceptable type {_type(rgb)} recieved')


# A function to extract hue, saturation, value values from an RGB color
def extract_hsv(hsv='hsv(0, 0, 0)'):
    """Extracts and returns hue, saturation, value values from an HSV
string, set, list, tuple, or a dictionary, as a tuple object.

E.g.:
hsv = 'hsv(0, 1, 1)'
hsv = {0, 1, 1}  # Order: hue, saturation, value
hsv = [0, 1, 1]  # Order: hue, saturation, value
hsv = (0, 1, 1)  # Order: hue, saturation, value
hsv = {
    'hue': 0,
    'saturation': 1,
    'value': 1
}

Note: Dictionary keys may be different but also unique,
and, the color values order is: hue, saturation, value
"""

    # Extraction from a `str` object (string)
    if isinstance(hsv, str):
        hsv = hsv.replace(' ', '')  # Remove whitespaces
        hsv = hsv.replace('hsv(', '').replace(')', '')  # Remove non-ints
        hsv = hsv.split(',')  # Extract HSV values to a list
        hsv = list(map(float, hsv))  # Convert strings to numbers
        hsv = tuple(map(round, hsv))  # Round floating-points to ints

        return hsv

    # Extraction from a `set` object (set)
    if isinstance(hsv, set):
        return tuple(round(float(value)) for value in hsv)

    # Extraction from a `list` object (list)
    if isinstance(hsv, list):
        hsv = list(map(float, hsv))
        hsv = tuple(map(round, hsv))

        return hsv

    # Extraction from a `tuple` object (tuple)
    if isinstance(hsv, tuple):
        hsv = list(map(float, list(hsv)))
        hsv = tuple(map(round, hsv))

        return hsv

    # Extraction from a `dict` object (dict.values)
    if isinstance(hsv, dict):
        return tuple(round(float(value)) for value in hsv.values())

    else:
        raise TypeError(f'unacceptable type {_type(hsv)} recieved')


# A function to extract hue, saturation,
# luminance values from an HSL color
def extract_hsl(hsl='hsl(0, 0, 0)'):
    """Extracts and returns hue, saturation, luminance values from an
HSL string, set, list, tuple, or a dictionary, as a tuple object.

E.g.:
hsl = 'hsl(0, 1, 0.5)'
hsl = {0, 1, 0.5}  # Order: hue, saturation, luminance
hsl = [0, 1, 0.5]  # Order: hue, saturation, luminance
hsl = (0, 1, 0.5)  # Order: hue, saturation, luminance
hsl = {
    'hue': 0,
    'saturation': 1,
    'luminance': 0.5
}

Note: Dictionary keys may be different but also unique,
and, the color values order is: hue, saturation, luminance
"""

    # Extraction from a `str` object (string)
    if isinstance(hsl, str):
        hsl = hsl.replace(' ', '')  # Remove whitespaces
        hsl = hsl.replace('hsl(', '').replace(')', '')  # Remove non-ints
        hsl = hsl.split(',')  # Extract HSL values to a list
        hsl = list(map(float, hsl))  # Convert strings to numbers
        hsl = tuple(map(round, hsl))  # Round floating-points to ints

        return hsl

    # Extraction from a `set` object (set)
    if isinstance(hsl, set):
        return tuple(round(float(value)) for value in hsl)

    # Extraction from a `list` object (list)
    if isinstance(hsl, list):
        hsl = list(map(float, hsl))
        hsl = tuple(map(round, hsl))

        return hsl

    # Extraction from a `tuple` object (tuple)
    if isinstance(hsl, tuple):
        hsl = list(map(float, list(hsl)))
        hsl = tuple(map(round, hsl))

        return hsl

    # Extraction from a `dict` object (dict.values)
    if isinstance(hsl, dict):
        return tuple(round(float(value)) for value in hsl.values())

    else:
        raise TypeError(f'unacceptable type {_type(hsl)} recieved')


# A function to extract hue, saturation, value values from an RGB color
def extract_yiq(yiq='yiq(255, 127, 127)'):
    """Extracts and returns y, i, q values from a YIQ string,
set, list, tuple, or a dictionary, as a tuple object.

E.g.:
yiq = 'yiq(255, 127, 127)'
yiq = {255, 127, 127}  # Order: y, i, q
yiq = [255, 127, 127]  # Order: y, i, q
yiq = (255, 127, 127)  # Order: y, i, q
yiq = {
    'y': 255,
    'i': 127,
    'q': 127
}

Note: Dictionary keys may be different but also unique,
and, the color values order is: y, i, q
"""

    # Extraction from a `str` object (string)
    if isinstance(yiq, str):
        yiq = yiq.replace(' ', '')  # Remove whitespaces
        yiq = yiq.replace('yiq(', '').replace(')', '')  # Remove non-ints
        yiq = yiq.split(',')  # Extract YIQ values to a list
        yiq = list(map(float, yiq))  # Convert strings to numbers
        yiq = tuple(map(round, yiq))  # Round floating-points to ints

        return yiq

    # Extraction from a `set` object (set)
    if isinstance(yiq, set):
        return tuple(round(float(value)) for value in yiq)

    # Extraction from a `list` object (list)
    if isinstance(yiq, list):
        yiq = list(map(float, yiq))
        yiq = tuple(map(round, yiq))

        return yiq

    # Extraction from a `tuple` object (tuple)
    if isinstance(yiq, tuple):
        yiq = list(map(float, list(yiq)))
        yiq = tuple(map(round, yiq))

        return yiq

    # Extraction from a `dict` object (dict.values)
    if isinstance(yiq, dict):
        return tuple(round(float(value)) for value in yiq.values())

    else:
        raise TypeError(f'unacceptable type {_type(yiq)} recieved')


# A function to extract hue, saturation, value values from an RGB color
def extract_cmyk(cmyk='cmyk(0, 1, 1, 0)'):
    """Extracts and returns cyan, magenta, yellow, key values from
a CMYK string, set, list, tuple, or a dictionary, as a tuple object.

E.g.:
cmyk = 'cmyk(0, 1, 1, 0)'
cmyk = {0, 1, 1, 0}  # Order: cyan, magenta, yellow, key
cmyk = [0, 1, 1, 0]  # Order: cyan, magenta, yellow, key
cmyk = (0, 1, 1, 0)  # Order: cyan, magenta, yellow, key
cmyk = {
    'cyan': 0,
    'magenta': 1,
    'yellow': 1,
    'key': 0
}

Note: Dictionary keys may be different but also unique,
and, the color values order is: cyan, magenta, yellow, key
"""

    # Extraction from a `str` object (string)
    if isinstance(cmyk, str):
        cmyk = cmyk.replace(' ', '')  # Remove whitespaces
        cmyk = cmyk.replace('cmyk(', '').replace(')', '')
        cmyk = cmyk.split(',')  # Extract CMYK values to a list
        cmyk = list(map(float, cmyk))  # Convert strings to numbers
        cmyk = tuple(map(round, cmyk))  # Round floating-points to ints

        return cmyk

    # Extraction from a `set` object (set)
    if isinstance(cmyk, set):
        return tuple(round(float(value)) for value in cmyk)

    # Extraction from a `list` object (list)
    if isinstance(cmyk, list):
        cmyk = list(map(float, cmyk))
        cmyk = tuple(map(round, cmyk))

        return cmyk

    # Extraction from a `tuple` object (tuple)
    if isinstance(cmyk, tuple):
        cmyk = list(map(float, list(cmyk)))
        cmyk = tuple(map(round, cmyk))

        return cmyk

    # Extraction from a `dict` object (dict.values)
    if isinstance(cmyk, dict):
        return tuple(round(float(value)) for value in cmyk.values())

    else:
        raise TypeError(f'unacceptable type {_type(cmyk)} recieved')


# Driver code
if __name__ == '__main__':
    print('Welcome to DyePy\'s mini command-line interpreter.\n')
    while True:
        # Acts like a command-line REFL for python
        func = input('python> ')

        try:
            func = eval(func)

        except (SyntaxError, Exception):

            if func == '' or func.isspace():    # Empty line
                func = None

            else:   # Any other error handled by printing this *func*
                func = 'Invalid statement/function call!'

        print(func) if func is not None else None
