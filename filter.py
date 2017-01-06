from PIL import Image
from PIL import ImageFilter

def processik(filename, savename):
    im = Image.open(filename)
    pixels = im.load()

    snow = Image.open('resources/snowik.png')
    hat = Image.open('resources/hatik.png')
    rides = Image.open('resources/santaridesik.png')
    salut = Image.open('resources/salutik.png')
    ramka = Image.open('resources/ramkasnegik.png')
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


def processdb(filename, savename):
    im = Image.open(filename).convert("RGB")
    sn = Image.open("snowdb.png").convert("RGBA")  # снег
    sn = sn.resize((im.width, im.height))  # снег
    px = im.load()
    pix = sn.load()  # снег

    sum_r, sum_g, sum_b = (0, 0, 0)

    for x in range(im.width):
        for y in range(im.height):
            r, g, b = px[x, y]

            sum_r += r
            sum_g += g
            sum_b += b
            if r > g and r > b:
                r = min(255, r + 60)  # красный
                g = min(255, g + 40)  # зелёный
                b = min(255, b + 40)  # синий
                px[x, y] = (r, g, b)
            elif g > r and g > b:
                r = min(255, r + 40)  # красный
                g = min(255, g + 40)  # зелёный
                b = min(255, b + 40)  # синий
                px[x, y] = (r, g, b)
            else:
                r = min(255, r + 40)  # красный
                g = min(255, g + 40)  # зелёный
                b = min(255, b + 40)  # синий
            px[x, y] = (r, g, b)

    for ex in range(sn.width):
        for ey in range(sn.height):
            re, gr, bl = px[ex, ey]
            S = re // 3 + gr // 3 + bl // 3
            if (S > 155):
                pix[ex, ey] = (0, 0, 0, 0)
            re, gr, bl, al = pix[ex, ey]
            re = min(255, re + 5)  # красный
            gr = min(255, gr + 70)  # зелёный
            bl = min(255, bl + 200)  # синий
            pix[ex, ey] = (re, gr, bl, al)

    sn = sn.filter(ImageFilter.GaussianBlur(radius=0.8))  # размытие
    im.paste(sn, (0, 0), sn)  # снег
    im.save(savename)