import argparse
import os
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FONT_EXTENTION = ['.ttf', '.otf', '.ttc']

def parse_args():
    desc = "ttf/otf fonts to jpg images set (JUST KOREAN)"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--ttf_dir', type=str, default='ttf_dir',
                        help='directory that includes .ttf files', required=False)
    parser.add_argument('--jpg_dir', type=str, default='jpg_dir',
                        help='directory that includes results of .jpg', required=False)
    parser.add_argument('--size', type=int, default=256,
                        help='size of result jpg', required=False)
    parser.add_argument('--offset', type=int, default=20,
                        help='offset', required=False)
    parser.add_argument('--makeset', type=str, default='kr',
                        help= 'specify character set you want to make to image spliting with \',\' [kr,special,demo_v2]',
                        required=False)

    return parser.parse_args()


def draw_char(font, char, size, offset):
    img = Image.new("RGB", (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((offset, offset), char, (0, 0, 0), font=font)
    clrs = img.getcolors()
    if len(clrs) == 1:
        return None
    return img


def main():
    args = parse_args()
    ttf_dir = args.ttf_dir
    jpg_dir = args.jpg_dir

    makeset = args.makeset
    makeset = makeset.split(',')
    char_json = json.load(open('./charset.json'))    
    charset = []
    for character in makeset:
        if character not in char_json:
            print("[error] there is no key [%s] in ./charset.json" % character)
            return
        charset.extend(char_json[character])

    char_size = args.size - (args.offset * 2)

    # if jpg_dir not exist
    if not os.path.exists(jpg_dir):
        os.makedirs(jpg_dir)

    for _, _, ttfs in os.walk(ttf_dir):
        for ttf in ttfs:
            # check extention type of file and continue if it is not font file
            ext = os.path.splitext(ttf)[-1]
            if ext not in FONT_EXTENTION:
                continue

            font = ImageFont.truetype(ttf_dir + '/' + ttf, size=char_size)
            count = 0
            for c in charset:
                if count % 100 == 0:
                    print("WORKING:: %s - character %c" % (ttf, c))

                if not os.path.exists(jpg_dir + '/' + c):
                    os.makedirs(jpg_dir + '/' + c)
                img = draw_char(font, c, args.size, args.offset)
                if img:
                    # img.save(os.path.join(jpg_dir + '/' + c,
                    # "%s_%s.jpg" % (c, ttf.split('.')[0])))
                    img.save(os.path.join(jpg_dir + '/' + c,
                                        "%s.jpg" % (ttf.split('.')[0])))

                count += 1

            print("!! COMPLETE:: %s" % (ttf))

if __name__ == '__main__':
    main()
