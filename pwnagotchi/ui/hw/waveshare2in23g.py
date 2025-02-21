import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class Waveshare2in23g(DisplayImpl):
    def __init__(self, config):
        super(Waveshare2in23g, self).__init__(config, 'waveshare2in23g')
        self._display = None

    def layout(self):
        fonts.setup(10, 8, 10, 25, 25, 9)
        self._layout['width'] = 122
        self._layout['height'] = 250
        self._layout['face'] = (0, 26)
        self._layout['name'] = (5, 15)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (28, 0)
        self._layout['uptime'] = (147, 0)
        self._layout['line1'] = [0, 12, 122, 12]
        self._layout['line2'] = [0, 92, 122, 92]
        self._layout['friend_face'] = (0, 76)
        self._layout['friend_name'] = (40, 78)
        self._layout['shakes'] = (0, 93)
        self._layout['mode'] = (187, 93)
        self._layout['status'] = {
            'pos': (91, 15),
            'font': fonts.status_font(fonts.Medium),
            'max': 20
        }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare 2.23g inch display")
        from pwnagotchi.ui.hw.libs.waveshare.v2in23g.epd2in13g import EPD
        self._display = EPD()
        self._display.init()
        self._display.Clear()

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.display(buf)

    def clear(self):
        self._display.Clear()
