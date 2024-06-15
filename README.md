Here is the updated README with added images and a detailed section explaining what is included in the project:

---

# Photo-Editor

## Overview
Photo-Editor is a Python-based application for editing photos using OpenCV. It offers a variety of image processing functions to enhance and manipulate images.

## Features
- **Image Loading and Saving:** Load images from files and save edited images.
- **Image Filters:** Apply various filters such as grayscale, blur, and edge detection.
- **Transformations:** Perform transformations like rotation, scaling, and cropping.
- **Drawing Tools:** Draw shapes, lines, and text on images, with options for color changes.
- **Free Drawing:** Draw freely on a blank canvas.
- **Add Images:** Insert images onto your canvas for composite editing.

## Requirements
- Python 3.8 or higher
- OpenCV 4.4.0

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/noavisl/Photo-Editor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Photo-Editor
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main application:
```bash
python main.py
```
Follow the on-screen instructions to load and edit images.

## File Structure
- `main.py`: The main application script.
- `img_functions.py`: Contains image processing functions.
- `images/`: Directory to store sample and processed images.


## Project Components
This section provides detailed information about each component of the Photo-Editor project.

### Home Page
The main interface where users can start editing their photos.
![Home Page](Description%20pictures/homePage.png)

### Add Image
Functionality to add images onto the canvas for composite editing.
![Add Image](Description%20pictures/addImg.png)

### Add Text
Window for adding text to images with options for font, size, and color.
![Add Text Window](Description%20pictures/addTextWindow.png)

### Color Change
Options to change the color of text or shapes on the canvas.
![Color Window](Description%20pictures/colorWin.png)
![Before Change Color](Description%20pictures/beforeChangeColor.png)
![After Change Color](Description%20pictures/changeColor.png)

### Cut Image
Tool for cropping images to the desired size.
![Cut Image](Description%20pictures/cutImg.png)

### Free Drawing
Tool for freehand drawing on a blank canvas or existing image.
![Free Drawing](Description%20pictures/freeDraw.png)

### Shape Drawing
Window for adding shapes like rectangles, circles, and lines with customizable options.
![Shape Window](Description%20pictures/shapeWin.png)

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a pull request.

## License
This project is licensed under the MIT License.

---

For more details, visit the [GitHub repository](https://github.com/noavisl/Photo-Editor).

---

You can replace the placeholders with actual images from your project. Make sure the images are stored in the `images` directory of your project.
