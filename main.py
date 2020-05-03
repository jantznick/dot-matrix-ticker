import time

from PIL import ImageFont
import fact, weather

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219

font = ImageFont.truetype("pixelmix.ttf", 8)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)

degreeSymbol = "°"

cool_fact= fact.return_fact()
temp, weatherDescription = weather.get_tempAndDescription()

fullmsg = f'Current Weather: {temp}{degreeSymbol} and {weatherDescription}. Did you know? {cool_fact}'
width,height = font.font.getsize(fullmsg)

virtual = viewport(device, width=width[0], height=8)

def main():
	while True:
		with canvas(virtual) as draw:
			draw.text((32,0), str(fullmsg), fill="white", font=font)
			width,height = font.font.getsize(fullmsg)

		for offset in range(32 + width[0]):
			virtual.set_position((offset,0))
			time.sleep(.1)


if __name__ == '__main__':
	print(fullmsg)
	main()
