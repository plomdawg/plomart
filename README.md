# plomart

Resourced used:

- [photopea.com](https://www.photopea.com/) for creating the source images (6px pencil + fill tool)
- [how to generate a random color](https://stackoverflow.com/questions/28999287/generate-random-colors-rgb)
- [how to fill an image](https://www.geeksforgeeks.org/floodfill-image-using-python-pillow/) for coloring in the body
- [adding heroku to Google Domains](https://stackoverflow.com/questions/63866651/how-to-associate-heroku-app-with-a-google-domain)
- [creating a loading spinner button](https://dev.to/dcodeyt/create-a-button-with-a-loading-spinner-in-html-css-1c0h)

## Creating the parts

I created a new project with a square canvas on [Photopea](https://www.photopea.com/).

![image](https://user-images.githubusercontent.com/6510862/170896772-d60c0d50-0200-426d-a7f0-dc5a9e7ac5ee.png)

Each layer holds one part, named `[part][number]`. *Looks awful when all the layers are shown:*

![image](https://user-images.githubusercontent.com/6510862/170896746-509e936b-764c-4aaa-ae37-e059fa15b10b.png)

Using `File > Export Layers`, I can save each layer as it's own .png file.

![image](https://user-images.githubusercontent.com/6510862/170896865-23b38a87-a519-4491-8ae2-295589bfb4e8.png)

These files are then placed into the `parts/` folder, and are selected at random.

## Examples

![collage](https://user-images.githubusercontent.com/6510862/170970149-1f7e37e4-ac06-41ab-8874-04f2e3623c49.png)
