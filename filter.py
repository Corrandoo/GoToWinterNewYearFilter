from PIL import Image

def process(filename, savename):
    im = Image.open(filename)
    pixels = im.load()

    snow = Image.open('resources/snow.png')
    hat = Image.open('resources/hat.png')
    rides = Image.open('resources/santarides.png')
    salut = Image.open('resources/salut.png')
    ramka = Image.open('resources/ramkasneg.png')
    pixels = im.load()
    imWidth = im.width
    imHeight = im.height

    snow = snow.resize((imWidth, imHeight))
    hat = hat.resize((int(imWidth * 0.1), int(imHeight * 0.1)))
    rides = rides.resize((int(imWidth * 0.3), int(imHeight * 0.3)))
    salut = salut.resize((int(imWidth * 0.3), int(imHeight * 0.3)))
    ramka = ramka.resize((imWidth, imHeight))

    im.paste(snow, (0, 0), snow)

    for i in range(im.width):
        for j in range(im.height):
            r, g, b = pixels[i, j]
            a = (r + g + b) // 3
            if a > 235:
                r = r - r * 0.2
                g = g - g * 0.2
                b = b - b * 0.2
            r = min(255, int(r * 1.1))
            g = min(255, int(g * 1.2))
            b = min(255, int(b * 1.55))
            r = min(255, int(r * 1.1))
            g = min(255, int(g * 1.1))
            b = min(255, int(b * 1.1))
            pixels[i, j] = (r, g, b)

    im.paste(hat, (im.width - hat.width, 0), hat)
    im.paste(hat, (im.width // 2 - hat.width // 2, 0), hat)
    im.paste(rides, (0, im.height - rides.height), rides)
    im.paste(salut, (0, 0), salut)
    im.paste(ramka, (0, 0), ramka)

    im.save(savename)