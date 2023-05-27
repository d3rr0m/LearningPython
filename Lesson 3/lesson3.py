from PIL import Image

image_monro = Image.open("monro.jpg")
red_channel, green_channel, blue_channel = image_monro.split()

crop_size = 50
alpha = 0.5

#
red_croped_left = red_channel.crop((crop_size, 0, image_monro.width, image_monro.height))
red_croped_middle = red_channel.crop((crop_size/2, 0, image_monro.width - crop_size/2, image_monro.height))
monro_cropped_red = Image.blend(red_croped_left, red_croped_left, alpha)

blue_croped_right = blue_channel.crop((0, 0, image_monro.width - crop_size, image_monro.height))
blue_croped_middle = blue_channel.crop((crop_size/2, 0, image_monro.width - crop_size/2, image_monro.height))
monro_cropped_blue = Image.blend(blue_croped_right, blue_croped_middle, alpha)

monro_cropped_green = green_channel.crop((crop_size/2, 0, green_channel.width - crop_size/2, green_channel.height))

avatar = Image.merge("RGB", (monro_cropped_red, monro_cropped_green, monro_cropped_blue))
avatar.save("avatar.jpg")
avatar.thumbnail((80,80))
avatar.save("avatar_thumbnail.jpg")
