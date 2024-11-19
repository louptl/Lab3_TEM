import hyperspy.api as hs

# Load the .dm3 file
folder_path = '/Users/louptl/Desktop/NTNU/Material physics/Lab 3/Lab3_6/'
image_path = f'{folder_path}P1_CL100cm_SAED_Tx11p1_Ty3p5_1.dm3'   # Replace with the actual path to your .dm3 file
data = hs.load(image_path)
print(data.metadata)

# Access and print the camera length and wavelength from metadata
try:
    camera_length = data.metadata.Acquisition_instrument.TEM.camera_length
    #wavelength = data.metadata.Acquisition_instrument.TEM.beam_energy


    print(data.metadata)
except AttributeError:
    print("Camera length or wavelength not found in the metadata.")
