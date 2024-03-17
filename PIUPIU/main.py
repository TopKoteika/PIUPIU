from PIL import Image , ImageFilter


with Image.open("-vt-1169-1-.jpg") as original:
    pic_gray = original.convert("L")
    pic_blur = original.filter(ImageFilter.BLUR)
    pic_blur.save("bl_pic.jpg")
    pic_gray.save("bw_pic.jpg")
    pic_gray.show()
    pic_blur.show()
   