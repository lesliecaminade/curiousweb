from imagekit import ImageSpec
from imagekit.processors import ResizeToFill, ResizeToFit

class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 100)]
    format = 'JPEG'
    options = {'quality': 60}

class Resize_1080(ImageSpec):
    processors = [ResizeToFit(1920, 1080)]
    format = 'JPEG'
    options = {'quality': 95}

"""
Available processors

    ResizeToFit
    ResizeToFill
    SmartResize
    Adjust
    TrimBorderColor
    Transpose

"""
