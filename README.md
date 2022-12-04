# Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate a single collage/character:

```bash
python app/plomart.py
```

Run the web app:

```bash
docker-compose up -d
```

# Notes

## Resourced Used

- [photopea.com](https://www.photopea.com/) for creating the source images (6px pencil + fill tool)
- [how to generate a random color](https://stackoverflow.com/questions/28999287/generate-random-colors-rgb)
- [how to fill an image](https://www.geeksforgeeks.org/floodfill-image-using-python-pillow/) for coloring in the body
- [creating a loading spinner button](https://dev.to/dcodeyt/create-a-button-with-a-loading-spinner-in-html-css-1c0h)

## Creating the parts

I created a new project with a square canvas on [Photopea](https://www.photopea.com/).

![image](https://user-images.githubusercontent.com/6510862/170896772-d60c0d50-0200-426d-a7f0-dc5a9e7ac5ee.png)

Each layer holds one part, named `[part][number]`. _It looks scary when all the layers are shown:_

![image](https://user-images.githubusercontent.com/6510862/170896746-509e936b-764c-4aaa-ae37-e059fa15b10b.png)

I saved each layer as it's own .png file using `File > Export Layers`.

![image](https://user-images.githubusercontent.com/6510862/170896865-23b38a87-a519-4491-8ae2-295589bfb4e8.png)

These files are then placed into the `parts/` folder.

The script [app/plomart.py](./app/plomart.py) chooses some random colors and parts to create the characters.

## Examples

![collage](https://user-images.githubusercontent.com/6510862/170970149-1f7e37e4-ac06-41ab-8874-04f2e3623c49.png)

## Adding the metrics to Home Assistant

Using a rest sensor and an exposed endpoint, I can keep track of faces generated in Home Assistant.

```yaml
- platform: rest
  name: plomart faces generated
  resource: http://art.plom.one/faces_generated
  scan_interval: 3600 # seconds = 1 hour
```

lovelace (using the custom card [apexcharts](https://github.com/RomRider/apexcharts-card)):

```yaml
type: custom:apexcharts-card
header:
  show: true
  title: Faces Generated
  show_states: true
  colorize_states: true
series:
  - entity: sensor.plomart_faces_generated
```

![image](https://user-images.githubusercontent.com/6510862/170972696-0690c99b-7a4a-47ce-a172-edda010c1ab2.png)
