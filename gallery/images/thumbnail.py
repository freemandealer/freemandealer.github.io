import sys
from PIL import Image

def main(src_file_name):
    print "[processing] " + src_file_name
    img = Image.open(src_file_name)
    img_width = 600
    img_height = 600
    img.thumbnail((img_width, img_height), Image.ANTIALIAS)
    img.convert("RGB")
    out_file_name = 'thumb_' + src_file_name
    print out_file_name
    img.save(out_file_name)
    print "[complete] " + src_file_name

if __name__ == "__main__":
    main(sys.argv[1])
