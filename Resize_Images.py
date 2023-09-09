import os              # OS Library
from PIL import Image  # pillow library 
from tkinter import messagebox # Tkinter Library

def Resize(new_width,new_height, input_folder, output_folder):


    # Define the input & output Folders
    # input_folder    # put the path of input folder 
    # output_folder  # put the path of output folder

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder,exist_ok=True)

    # Get a list of all image files in the input folder 
    image_files=[f for f in os.listdir(input_folder) if f.lower().endswith((".png",".jpg",".jpeg",".bmp"))]

    # # Set the new dimesions 
    # new_width 
    # new_height  

    #iterate through the image files and resize each one 
    for image_file in image_files :
        #open the image file
        input_path=os.path.join(input_folder,image_file)
        image=Image.open(input_path)

        #resize the image
        resize_image=image.resize((new_width,new_height))
        
        # save the resized image with the same name in output folder 
        output_path=os.path.join(output_folder, image_file)
        resize_image.save(output_path)

        #close the image
        image.close()
        resize_image.close()

    # messagebox.showinfo(title="Message Title",message="Complete ..")

