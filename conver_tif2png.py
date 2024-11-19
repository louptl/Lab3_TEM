from PIL import Image
import os

def convert_tif_to_png(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.tif'):
            # Full path for the input file
            tif_path = os.path.join(source_folder, filename)
            
            # Open the .tif image
            with Image.open(tif_path) as img:
                # Prepare the .png file path
                png_filename = os.path.splitext(filename)[0] + '.png'
                png_path = os.path.join(destination_folder, png_filename)
                
                # Save the image as .png
                img.save(png_path, 'PNG')
                print(f"Converted {filename} to {png_filename}")

# Example usage
source_folder = '/Users/louptl/Desktop/NTNU/Material physics/Lab 3/Lab3_6/TIF'      # Replace with the path to your .tif files
destination_folder = '/Users/louptl/Desktop/NTNU/Material physics/Lab 3/Lab3_6/PNG'  # Replace with the path where .png files will be saved

convert_tif_to_png(source_folder, destination_folder)
