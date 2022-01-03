# My Solution for assignment  1
# Wrote By Orel Rahum
from flask import Flask
import requests
import multiprocessing
from PIL import Image, ImageDraw

##################################################################################################
### Console colors
W = '\033[0m'  # white
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
T = '\033[93m'  # tan

##################################################################################################
# Part 1+2
print("\n##########################################################################################")
print("                                      part 1+2 \n")
print("Write the following code: a = 1/0;")
try:
    a = 1 / 0
except:
    print(G + "impossible to write it , we  can't devide by zero" + W)

##################################################################################################
# Part 3
print("\n##########################################################################################")
print("                                      part 3 \n")
print("Is the following code legal?")
print("try:")
print("    x = 1")
print("    finally:")
print('print("finally")')
print(G + "no, finally should be same indentation like try" + W)

##################################################################################################
# Part 4
print("\n##########################################################################################")
print("                                      part 4 \n")
print("What exception types can be caught by the following handler?")
print("Except:")
print(G + "general except can be caught all exception type" + W)

##################################################################################################
# Part 5
print("\n##########################################################################################")
print("                                      part 5 \n")

print("What is wrong with using the above type of exception handler?")
print(G + "we cant to know which problem is caught and we cant focus on spesific problem " + W)

##################################################################################################
# Part 6
print("\n##########################################################################################")
print("                                      part 6 \n")

print("What exceptions can be caught by the following handlers?")
print(G + "except IOError : its catch wrong input/output")
print("except ZeroDivisionError : catch devide by zero" + W)

##################################################################################################
# Part 7
print("\n##########################################################################################")
print("                                      part 7 \n")

print("Create a text file named “words.txt”")

output_file = "words.txt"
with open(output_file, "a") as output:
    pass
print(G + 'file "word.txt was created' + W)
##################################################################################################
# Part 8
print("\n##########################################################################################")
print("                                      part 8 \n")
print('Write your name into "words.txt" file')
my_name = "Orel Rahum"
with open(output_file, "a") as file:
    file.write(f"{my_name}\n")

print(G + 'My name Added to "words.txt"' + W)

##################################################################################################
# Part 9
print("\n##########################################################################################")
print("                                      part 9 \n")

print("Read your file content and print it")

with open(output_file, "r", encoding='utf-8') as file:
    lines = file.read().splitlines()
    last_line = lines[-1]
    print(G + last_line + W)

##################################################################################################
# Part 10
print("\n##########################################################################################")
print("                                      part 10 \n")

print("Write Hebrew content into your text file and print its content programmatically.")
my_name = "אוראל רחום"
with open(output_file, "a", encoding='utf-8') as file:
    file.write(f"{my_name}\n")

with open(output_file, "r", encoding='utf-8') as file:
    lines = file.read().splitlines()
    last_line = lines[-1]
    print(G + last_line + W)

##################################################################################################
# Part 11
print("\n##########################################################################################")
print("                                      part 11 \n")
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/content")
def read():
    return open("words.txt", "r", encoding='utf-8').read(), 200


@app.route("/register")
def register():
    open("words.txt", 'a', encoding='utf-8').write("hello")
    return "success", 201


def run_app():
    app.run(port=30000)


def status_code_checker():
    status_code_content = requests.get("http://127.0.0.1:30000/content").status_code
    status_code_register = requests.get("http://127.0.0.1:30000/register").status_code
    print(f"127.0.0.1/content status code is {status_code_content}")
    print(f"127.0.0.1/content status code is {status_code_register}")


#p1 = multiprocessing.Process(target=run_app).run()
#p2 = multiprocessing.Process(target=status_code_checker).run()

##################################################################################################
# Part 12
print("\n##########################################################################################")
print("                                      part 12 \n")
img = Image.new('RGB', (100, 30), color=(73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10, 10), "DevOps-Expert 0812", fill=(255, 255, 0))
img.save('DevOps-Expert.png')
print(G + 'Create image called DevOps-Expert.png' + W)
