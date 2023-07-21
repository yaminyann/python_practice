# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Can't devaided by Zero")
#     except TypeError:
#         print("Unsupport type . did you using Strinng?")
#
# print(div(10,2))
# print(div(3,0))
# print(div(9,3))
# print(div("12",3))



# import io
# file_name = "file.txt"
# mode = "r"
#
# try:
#     with open(file_name,mode) as fp:
#         content = fp.read()
#         print(content)
# except FileNotFoundError:
#     print("filename not found")
# except io.UnsupportedOperation:
#     print("are u sure file are readable?")
# except Exception as e:
#     print(e)
