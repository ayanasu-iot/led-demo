#!/usr/bin/env python3
# coding: UTF-8
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
from threading import Thread
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="21:52")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font_date = graphics.Font()
        font.LoadFont("./a-otf24.bdf")
        font_date.LoadFont("./a-otf20.bdf")

        textColor = graphics.Color(245, 0, 111)
        timeColor = graphics.Color(61, 147, 215)
        pos = offscreen_canvas.width
        my_text = self.args.text
        start = time.time()
        while True:
            if (time.time() - start) > 30:
                exit()
            else:
                d = datetime.now()
                h = (" " + str(d.hour))[-2:]
                date_text = d.strftime("%a %m.%d")
                time_text = d.strftime("%H:%M:%S")
                offscreen_canvas.Clear()
                len = graphics.DrawText(offscreen_canvas, font_date, 4, 24, textColor, date_text)
                len1 = graphics.DrawText(offscreen_canvas, font,4, 56, timeColor, time_text)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
