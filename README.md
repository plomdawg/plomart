# plomart

Resourced used:

- [photopea.com](https://www.photopea.com/) for creating the source images (6px pencil + fill tool)
- [how to generate a random color](https://stackoverflow.com/questions/28999287/generate-random-colors-rgb)
- [how to fill an image](https://www.geeksforgeeks.org/floodfill-image-using-python-pillow/) for coloring in the body


## Creating the parts

I created a new project with a square canvas on [Photopea](https://www.photopea.com/).

![image](https://user-images.githubusercontent.com/6510862/170896772-d60c0d50-0200-426d-a7f0-dc5a9e7ac5ee.png)


Each layer holds one part, named `[part][number]`.

![image](https://user-images.githubusercontent.com/6510862/170896746-509e936b-764c-4aaa-ae37-e059fa15b10b.png)

Using `File > Export Layers`, I can save each layer as it's own .png file.

![image](https://user-images.githubusercontent.com/6510862/170896865-23b38a87-a519-4491-8ae2-295589bfb4e8.png)

These files are then placed into the `parts/` folder, and are selected at random.


## Examples

![collage](https://user-images.githubusercontent.com/6510862/170897511-dba25b84-68fd-490f-b4f5-27df4d81a08a.png)
