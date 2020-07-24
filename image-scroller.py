#!/usr/bin/env python
import time
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
from PIL import Image


class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/runtext.ppm")

    def run(self):
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

        double_buffer = self.matrix.CreateFrameCanvas()
        img_width, img_height = self.image.size
        pos = double_buffer.width

        # let's scroll
        xpos = -128
        while True:
            xpos += 2
            if (xpos > img_width):
                exit()
            double_buffer.Clear()
            double_buffer.SetImage(self.image, -xpos)
            double_buffer = self.matrix.SwapOnVSync(double_buffer)
            time.sleep(0.02)


if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
