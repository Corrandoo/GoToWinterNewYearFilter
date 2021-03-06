from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageOps

MAXPIX = 255
DELTA = 30
EPS = 0.0001

def processik(filename, savename):
    im = Image.open(filename).convert("RGB")
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
    sn = Image.open("resources/snowdb.png").convert("RGBA")  # снег
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


def processym(filename, savename):
    im = Image.open(filename).convert("RGB")
    pixels = im.load()
    snow = Image.open('resources/snowym.png')  # СНЕГ
    snow = snow.resize((im.width, im.height))
    # oleni = Image.open('oleni.png') #ОЛЕНИ
    # oleni = oleni.resize((im.width//2, oleni.height//2))
    sani = Image.open('resources/saniym.png')  # САНИ ДЕДА
    sani = sani.resize((im.width // 5, im.height // 5))
    # sn = Image.open('snez.png') # СНЕЖИНКИ
    # sn = sn.resize((im.width//2, sn.height))
    ded = Image.open('resources/santaym.png')  # САНТА
    ded = ded.resize((im.width // 4, im.height // 3))
    for i in range(im.width):
        for j in range(im.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r, min(255, g + 10), min(255, b + 70))
    snow = snow.filter(ImageFilter.GaussianBlur(radius=1))  # ГАУСС
    im.paste(snow, (0, 0), snow)
    im.paste(snow, (0, 0), snow)
    # im.paste(oleni, (im.width-oleni.width, im.height-oleni.height), oleni)
    im.paste(sani, (0, 0), sani)
    # im.paste(sn, (0, im.height-sn.height), sn)
    im.paste(ded, (im.width - ded.width, im.height - ded.height), ded)
    im.paste(ded, (0, im.height - ded.height), ded)
    im = im.filter(ImageFilter.GaussianBlur(radius=1))  # ГАУСС

    im.save(savename)

def processvc(filename, savename):
    img = Image.open(filename).convert("RGB")
    img = img.filter(ImageFilter.DETAIL)
    enh = ImageEnhance.Contrast(img).enhance(1.3) #30% more contrast
    out = enh.filter(ImageFilter.BLUR)
    x, y = enh.size
    eX, eY = x / 2, y / 2

    n = 5
    icons = [Image.open("resources/" + str(im) + "vc.png").convert("RGBA") for im in range(1, n)]
    icons = [icon.resize((enh.width // 4, enh.height // 4), Image.ANTIALIAS) for icon in icons]
    icons[:2] = [im.convert("RGBA").rotate(-60) for im in icons[:2]]
    icons[2:] = [im.convert("RGBA").rotate(30) for im in icons[2:]]
    for i in range(1, n - 1, 2):
        icons[i] = ImageOps.mirror(icons[i])
        cor = []
    cor.append((0, 0, icons[0].width, icons[0].height))
    cor.append((enh.width - icons[0].width, 0, enh.width, icons[0].height))
    cor.append((0, enh.height - icons[0].height, icons[0].width, enh.height))
    cor.append((enh.width - icons[0].width, enh.height - icons[0].height, enh.width, enh.height))
    for i in range(n - 1):
        out.paste(icons[i], cor[i], icons[i]) #add moon
        sn = Image.open("resources/snowvc.png").convert("RGBA").resize((enh.width, enh.height))
    enh.paste(sn, (0, 0, enh.width, enh.height), sn)
    pixels = enh.load()
    dpixels = out.load()
    for j in range(enh.width):
        for i in range(enh.height):
            if (j - eX) ** 2 * eY ** 2 + (i - eY) ** 2 * eX ** 2 - eX ** 2 * eY ** 2 < EPS:
                r, g, b = [min(MAXPIX, c + DELTA) for c in pixels[j, i]]
                pixels[j, i] = (r, g, b)
            else:
                pixels[j, i] = dpixels[j, i]
    enh.save(savename)


def processmm1(fototo, savepath):
    im = Image.open(fototo).convert("RGB")
    im2 = im.copy()
    pixels = im.load()
    pixels2 = im2.load()
    for i in range(im.width):
        for j in range(im.height):
            r, g, b = pixels[i, j]
            if r < 128:
                pixels[i, j] = (r + 50, g, b)
            else:
                pixels[i, j] = (r, g, b)

            if b > 128:
                pixels[i, j] = (r, g, b - 50)
            else:
                pixels[i, j] = (r, g, b)

            if g > 128:
                pixels[i, j] = (r, g - 50, b)
            else:
                pixels[i, j] = (r, g, b)

            if g < 50 and r < 50 and b < 50:
                pixels[i, j] = (r + 50, g + 50, b + 50)
            else:
                pixels[i, j] = (r, g, b)

            if g < 200 and r < 200 and b < 200:
                pixels[i, j] = (r - 50, g - 50, b - 50)
            else:
                pixels[i, j] = (r, g, b)
    im.save(savepath)


def processmm2(fototo2, savepath2):
    im = Image.open(fototo2).convert("RGB")
    im2 = im.copy()
    pixels = im.load()
    pixels2 = im2.load()
    for i in range(im.width):
        for j in range(im2.height):
            r, g, b = pixels2[i, j]
            if r < 128:
                pixels2[i, j] = (r + 40, g, b)
            else:
                pixels2[i, j] = (r, g, b)

            if b > 128:
                pixels2[i, j] = (r, g, b - 40)
            else:
                pixels2[i, j] = (r, g, b)

            if g > 128:
                pixels2[i, j] = (r, g - 40, b)
            else:
                pixels2[i, j] = (r, g, b)

            if g < 50 and r < 50 and b < 50:
                pixels2[i, j] = (r + 40, g + 40, b + 40)
            else:
                pixels2[i, j] = (r, g, b)

            if g < 200 and r < 200 and b < 200:
                pixels2[i, j] = (r, g - 40, b - 40)
            else:
                pixels2[i, j] = (r, g, b)
    im.save(savepath2)

def processmn(filename, savename):
    name = filename
    im = Image.open(name).convert('RGBA')
    elc = Image.open('resources/elch.png').convert('RGBA')
    a = int(im.width * 0.05)
    b = int(im.height * 0.05)
    elc = elc.resize((a, a))
    ded = Image.open('resources/indexx.png').convert('RGBA')
    ded = ded.resize((int(im.width * 0.05), int(im.height * 0.07)))
    snegg = Image.open('resources/888.png').convert('RGBA')
    snegg = snegg.resize((im.width, im.height))
    pixels = im.load()
    for i in range(im.width):
        for j in range(im.height):
            r, g, b, a = pixels[i, j]
            r = min(255, r + 150)
            g = min(255, g + 55)
            b = min(255, b + 55)
            pixels[i, j] = (r, g, b, a)

    from random import randint
    v = randint(1, 20)

    for i in range(v):
        r = 0.1 * (randint(1, 9))
        o = 0.1 * (randint(1, 9))

        box = (int(im.width * r), int(im.width * o), int(im.width * r) + elc.width, int(im.width * o) + elc.height)
        # (левый верхний(x),левый верхний(y),правый нижний(x),правый нижний(y))
        im.paste(elc, box, elc)

    from random import randint
    v = randint(1, 3)

    for i in range(v):
        r = 0.1 * (randint(1, 9))
        o = 0.1 * (randint(1, 9))

        box1 = (int(im.width * r), int(im.height * o), int(im.width * r) + ded.width, int(im.height * o) + ded.height)
        # (левый верхний(x),левый верхний(y),правый нижний(x),правый нижний(y))
        im.paste(ded, box1, ded)

    box2 = (0, 0, im.width, im.height,)
    # (левый верхний(x),левый верхний(y),правый нижний(x),правый нижний(y))
    im.paste(snegg, box2, snegg)

    im.save(savename)