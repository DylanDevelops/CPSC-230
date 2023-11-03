import qrcode

img = qrcode.make('Some text')
type(img)

img.save('some_file.png')