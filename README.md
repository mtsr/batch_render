# batch_render
Simple python script to batch render models using Blender

## Usage
```
usage: batch_render.py [-h] [-b BLENDER] glob

Batch imports and renders models from 4 angles using Blender

positional arguments:
  glob                  Use a glob with ** or * to select files

optional arguments:
  -h, --help            show this help message and exit
  -b BLENDER, --blender BLENDER
                        Specify the path to blender executable, defaults to path for Blender installed through Steam on Windows
```

## Custom scene setup
Edit `import.blend` to customize the scene settings to your liking.

There are currently 4 keyframes that rotate the camera and lights around the model.
