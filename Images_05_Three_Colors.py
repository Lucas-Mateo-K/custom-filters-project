# Images_05_Three_Colors
# Kyle Fricke and Cheryl Farmer, Engineer Your World
# Created in August 2017, last updated in January 2020 (for Python 3)
# Read in an image file, convert it to grayscale, identify three different
# regions of the grayscale image, and color each region with a different
# color. Allow grayscale divisions and 3 colors of papers to be adjusted using
# trackbars. Display original, grayscale, colored parts, and customized image.
# Save results if desired. Destroy all windows when user has finished.

# Import libraries
import cv2
import numpy
import os.path

# Prompt user to enter name of original image.
print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

# Save original image. Create and save grayscale image, ensuring that it
# has the right number of color channels (3).
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

# Create windows for display.
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Grayscale Trackbars')
cv2.namedWindow('Color01 Trackbars')
cv2.namedWindow('Color02 Trackbars')
cv2.namedWindow('Color03 Trackbars')
cv2.namedWindow('Color01 Parts of Image')
cv2.namedWindow('Color02 Parts of Image')
cv2.namedWindow('Color03 Parts of Image')
cv2.namedWindow('Customized Image')

# Display original and grayscale images.
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)

# Create variable to read in the height, width, and number of channels (3) of
# of the original image.
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

# Create the colored papers.
Color01_paper = numpy.zeros((image_height,image_width,image_channels),
                            numpy.uint8)
Color02_paper = numpy.zeros((image_height,image_width,image_channels),
                            numpy.uint8)
Color03_paper = numpy.zeros((image_height,image_width,image_channels),
                            numpy.uint8)

# Create grayscale and color trackbar(s).
cv2.createTrackbar('gs_break_01','Grayscale Trackbars', 85, 255, lambda x:None)
cv2.createTrackbar('gs_break_02','Grayscale Trackbars', 170, 255, lambda x:None)
cv2.createTrackbar('Blue_Color01','Color01 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Green_Color01','Color01 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Red_Color01','Color01 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Blue_Color02','Color02 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Green_Color02','Color02 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Red_Color02','Color02 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Blue_Color03','Color03 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Green_Color03','Color03 Trackbars', 0, 255, lambda x:None)
cv2.createTrackbar('Red_Color03','Color03 Trackbars', 0, 255, lambda x:None)

# Initialize while loop control variable. Then start the loop.
keypressed = 1
while (keypressed != 27 and keypressed !=ord('s')):

    # Define the colors of the papers.
    Blue_Color01 = cv2.getTrackbarPos('Blue_Color01','Color01 Trackbars')
    Green_Color01 = cv2.getTrackbarPos('Green_Color01','Color01 Trackbars')
    Red_Color01 = cv2.getTrackbarPos('Red_Color01','Color01 Trackbars')
    Blue_Color02 = cv2.getTrackbarPos('Blue_Color02','Color02 Trackbars')
    Green_Color02 = cv2.getTrackbarPos('Green_Color02','Color02 Trackbars')
    Red_Color02 = cv2.getTrackbarPos('Red_Color02','Color02 Trackbars')
    Blue_Color03 = cv2.getTrackbarPos('Blue_Color03','Color03 Trackbars')
    Green_Color03 = cv2.getTrackbarPos('Green_Color03','Color03 Trackbars')
    Red_Color03 = cv2.getTrackbarPos('Red_Color03','Color03 Trackbars')

    # Assign the colors to the colored papers.
    Color01_paper[0:image_height,0:image_width, 0:image_channels] = \
                                        [Blue_Color01,Green_Color01,Red_Color01]
    Color02_paper[0:image_height,0:image_width, 0:image_channels] = \
                                        [Blue_Color02,Green_Color02,Red_Color02]
    Color03_paper[0:image_height,0:image_width, 0:image_channels] = \
                                        [Blue_Color03,Green_Color03,Red_Color03]

    # Define the break point for "light" and "dark". Force regions not to
    # overlap. Ensure right data type.
    gs_break_01 = cv2.getTrackbarPos('gs_break_01','Grayscale Trackbars')
    gs_break_02 = cv2.getTrackbarPos('gs_break_02','Grayscale Trackbars')

    if gs_break_01 > gs_break_02:
        cv2.setTrackbarPos('gs_break_01','Grayscale Trackbars', gs_break_02 - 1)

    if gs_break_02 > 254:
        cv2.setTrackbarPos('gs_break_02', 'Grayscale Trackbars', 254)

    min_grayscale_for_Color01 = [0,0,0]
    max_grayscale_for_Color01 = [gs_break_01,gs_break_01,gs_break_01]
    min_grayscale_for_Color02 = [gs_break_01+1,gs_break_01+1,gs_break_01+1]
    max_grayscale_for_Color02 = [gs_break_02,gs_break_02,gs_break_02]
    min_grayscale_for_Color03 = [gs_break_02+1,gs_break_02+1,gs_break_02+1]
    max_grayscale_for_Color03 = [255,255,255]

    min_grayscale_for_Color01 = numpy.array(min_grayscale_for_Color01,
                                            dtype = "uint8")
    max_grayscale_for_Color01 = numpy.array(max_grayscale_for_Color01,
                                            dtype = "uint8")
    min_grayscale_for_Color02 = numpy.array(min_grayscale_for_Color02,
                                            dtype = "uint8")
    max_grayscale_for_Color02 = numpy.array(max_grayscale_for_Color02,
                                            dtype = "uint8")
    min_grayscale_for_Color03 = numpy.array(min_grayscale_for_Color03,
                                            dtype = "uint8")
    max_grayscale_for_Color03 = numpy.array(max_grayscale_for_Color03,
                                            dtype = "uint8")

    # Create masks.
    block_all_but_the_Color01_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_Color01,
                                                  max_grayscale_for_Color01)
    block_all_but_the_Color02_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_Color02,
                                                  max_grayscale_for_Color02)
    block_all_but_the_Color03_parts = cv2.inRange(grayscale_image,
                                                  min_grayscale_for_Color03,
                                                  max_grayscale_for_Color03)

    # Apply masks to create colored parts.
    Color01_parts_of_image = cv2.bitwise_or(Color01_paper, Color01_paper, mask =
                                            block_all_but_the_Color01_parts)
    Color02_parts_of_image = cv2.bitwise_or(Color02_paper, Color02_paper, mask =
                                            block_all_but_the_Color02_parts)
    Color03_parts_of_image = cv2.bitwise_or(Color03_paper, Color03_paper, mask =
                                            block_all_but_the_Color03_parts)

    # Combine all colored parts to create customized image.
    customized_image = cv2.bitwise_or(Color01_parts_of_image,
                                      Color02_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, Color03_parts_of_image)

    # Display original, grayscale, colored parts, and customized image.
    cv2.imshow('Color01 Parts of Image',Color01_parts_of_image)
    cv2.imshow('Color02 Parts of Image',Color02_parts_of_image)
    cv2.imshow('Color03 Parts of Image',Color03_parts_of_image)
    cv2.imshow('Customized Image',customized_image)

    # Give a delay to tell the computer to refresh the page.
    keypressed = cv2.waitKey(1)

# We are outside the loop now, so either "s" or "esc" was pressed.
# Save images if "s" was pressed. Destroy all windows.
if keypressed == ord('s'): 
    cv2.imwrite('photo_grayscale_1.jpg',grayscale_image)
    cv2.imwrite('photo_customized_1.jpg',customized_image)
cv2.destroyAllWindows()
