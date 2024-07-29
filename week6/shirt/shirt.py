from os.path import splitext
from PIL import Image, ImageOps
import sys

def main():
    check_len()
    input_file, output_file = sys.argv[1], sys.argv[2]
    split_files(input_file, output_file)
    combine_image(input_file, output_file)

def check_extension(file):
    extension = [".png", ".jpg", ".jpeg"]
    if file not in extension:
        return False
    return True

def check_len():
    len_argv = len(sys.argv)

    if len_argv > 3:
        sys.exit("Too many command-line arguments")
    if len_argv < 3:
        sys.exit("Too few command-line arguments")

def split_files(input_file,output_file):
    file1 = splitext(input_file)
    file2 = splitext(output_file)

    if check_extension(file1[1]) == False:
        sys.exit("Invalid Input")
    if check_extension(file1[1]) == False:
        sys.exit("Invalid Output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and Output have different extensions")

def combine_image(input_file,output_file):
    try:
        image_file = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size

    muppet = ImageOps.fit(image_file,size)
    muppet.paste(shirt, shirt)
    muppet.save(output_file)

if __name__ =="__main__":
    main()

