from PIL import Image, ImageDraw

im = Image.open("pexels-photo-132037.jpeg")
line_color_white = "#ffffff"

imsize_width = im.size[0]
imsize_height = im.size[1]

x = 4  #가로 x칸
y = 4  #세로 y칸

n_x = imsize_width / x
n_y = imsize_height / y

arr_x = [i*n_x for i in range(x)]
arr_y = [i*n_y for i in range(y)]

#그림그리기
draw = ImageDraw.Draw(im)

#가로줄
for i in arr_y:
    draw.line((0, i, imsize_width, i), fill=line_color_white)

#세로줄
for i in arr_x:
    draw.line((i, 0, i, imsize_height), fill=line_color_white)

#대각선
draw.line((0, 0) + im.size, fill=line_color_white)
draw.line((0, imsize_height, imsize_width, 0), fill=line_color_white)


del draw, x, y
im.save('newName.jpg')
