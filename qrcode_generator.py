import qrcode

# data examples
data = ["javascript", "python", "java", "ruby", "golang"]
# file name
file_name = "my_qrcode.png"
# generate qrcode
img = qrcode.make(data=data)
# save generated qrcode as image
img.save(file_name)
