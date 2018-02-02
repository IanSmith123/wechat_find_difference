import os

from PIL import Image, ImageChops


class WeiChatFindDifference:
    def __init__(self):
        self.filename = "f.png"

    def screen_shot(self):
        os.system(f"adb shell screencap -p /sdcard/{self.filename}")
        os.system(f"adb pull /sdcard/{self.filename} ./{self.filename}")

    def diff_pic(self):
        pic_obj = Image.open(self.filename)
        width = pic_obj.size[0]
        height = pic_obj.size[1]
        pic1_left_up = 142 / 720 * width, 110 / 1280 * height
        pic2_left_up = 142 / 720 * width, 684 / 1280 * height

        single_size = (692 - 142) / 720 * width, (660 - 110) / 1280 * height
        pic_obj1 = pic_obj.crop((pic1_left_up[0], pic1_left_up[1], single_size[0]+pic1_left_up[0], single_size[1]+pic1_left_up[1]))
        pic_obj2 = pic_obj.crop((pic2_left_up[0], pic2_left_up[1], single_size[0]+pic2_left_up[0], single_size[1]+pic2_left_up[1]))

        diff = ImageChops.difference(pic_obj1, pic_obj2)
        diff.show()
        diff.save("picture/diff.png")


def main():
    # 正在准备截图
    diff = WeiChatFindDifference()
    diff.screen_shot()
    diff.diff_pic()



main()

