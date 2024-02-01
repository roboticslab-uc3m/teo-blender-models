# TEO Blender Models
3D Blender models for TEO robot. If you are looking for the source code of the robot itself, visit the [teo-main](https://github.com/roboticslab-uc3m/teo-main) repository.

## TEO Robot Control
The goal of this project is to transfer the movements made by a human, previously captured through the MOCAP OptiTrack system, to the TEO humanoid robot using Blender environment.

### Components used in the project
- Blender files: [teo-blender-models/blender](https://github.com/roboticslab-uc3m/teo-blender-models/tree/master/blender)
- Blender script: [teo-robot-control.py](https://github.com/roboticslab-uc3m/teo-blender-models/blob/master/src/python/teo-robot-control.py)
- Blender addon: [Mocap Tools Blender 2.80](https://github.com/roboticslab-uc3m/mocap-tools/tree/master/blender)
- App to launch a csv trajectory: [launchTrajectory](https://github.com/roboticslab-uc3m/teo-blender-models/blob/master/src/cpp/launchTrajectory.cpp)
- Mocap Datasets: [Google Drive](https://drive.google.com/drive/folders/1QRin71083aNa0jIDcXIBoSTAI2zFKBtt?usp=sharing)

### Installation:
- Install [Blender](https://www.blender.org/download/)
- Add the mocap-tool addon [mocap.zip](https://github.com/jlsneto/blender-addons/releases/download/mocap-28x/mocap.zip) and activate it
- Open `teo.blend`
- Make sure you've the most current version of `teo-robot-control.py` script loaded into the project
- To properly compile the app `launchTrajectory.cpp`, install [Yarp](https://github.com/roboticslab-uc3m/installation-guides/blob/master/docs/install-yarp.md).

### Instructions for use:
To learn how to perform the matching steps between the Mocap skeleton and TEO's skeleton, you can consult the instructions [here](https://github.com/roboticslab-uc3m/teo-blender-models/blob/master/doc/teo-robot-control-instructions.md).

### Sample Videos:
If you want to consult some demonstration videos, click [here](https://github.com/roboticslab-uc3m/teo-blender-models/blob/master/doc/teo-robot-control-videos.md).

## Status
[![Issues](https://img.shields.io/github/issues/roboticslab-uc3m/teo-blender-models.svg?label=Issues)](https://github.com/roboticslab-uc3m/teo-blender-models/issues)

## Similar and Related Projects

- [imontesino/blender-plotting](https://github.com/imontesino/blender-plotting)
