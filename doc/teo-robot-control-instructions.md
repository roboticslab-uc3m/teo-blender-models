# Teo Robot Control
The goal of this project is to transfer the movements made by a human, previously captured through the MOCAP OptiTrack system, to the TEO humanoid robot using Blender environment.

## Instructions for use:
These steps are indicative and require a minimum of handling with Blender.
1. Activate the `Puppet` skeleton (intermediate skeleton) in the `Scene Collection` to visualize it in our environment.
2. Click on the `Mocap` collection to locate you here and import the elements of the captured animation.
3. Click `File` > `Import` > `.fbx` or `.bvh` (depends on the format in which you exported the animation. Let's focus on .fbx )
4. In the import window, activate the orientation in which our mocap skeleton will be imported with `Manual Orientation` and this has to coincide with the coordinate axes with which we calibrate our mocap system. In our case: `Forward: X Forward`, `Up: And Up`. In `Armature` activate `Automatic Bone Orientation`.
6. Once you've the animated mocap skeleton, to copy the rotations of the bones to our puppet skeleton, we will use the `Mocap Tools` addon. We simultaneously select the mocap skeleton and the puppet skeleton and then select: `Object properties` > `Mocap Tools` > `Guess Hierarchy Mapping`. Correct those associations that have not been made correctly or complete them manually. You can save the changes with `Save mapping`. Reactivate the `Advance Retarget` option. You should already notice that your puppet skeleton has the same pose as your mocap skeleton.
7. Within the `Scene Collection`, select the `Skeleton group`. This allows us to activate Teo's own skeleton options. Click on `Object Data Properties` and select the skeleton `layers` with which we will work, in this case the 2 that are in the group on the right, correspond to the 2 bones that act as end effectors. This allows you to view them and activate the `Bone Constraint Properties` and activate the `Copy Position` and `Copy Rotation` option. With this, we can now have the TEO TCPs in the position that we want. 
8. Finally, in the `Scripting` workspace, click on the `Run Script` button (Shortcup: Alt P) and this will enable the `Teo Robot Control` panel to be activated. Click the `Enable IK` option in the `LeftArm` and `RightArm` panels to activate inverse kinematics. Activate the option `Joint Trunk to Left Arm IK` and/or `Joint Trunk to Right Arm IK` to include the trunk in the kinematic chain (`FrontalTrunk` disabled by default)
9. Play the animation and hide those parts that we do not want to show in order to work better. From here we can use the `Export CSV` option within the `Trajectory` section of `Teo Robot Control` panel, to export our trajectory in a CSV file, later executable in the simulator or in our robot.

Note: we will probably not always achieve a successful result of the movement of Teo's skeleton relative to our mocap skeleton. This can be due to multiple reasons that must be observed and adjusted to make our trajectory as accurate as possible. If you have any questions or problems write an [issue](https://github.com/roboticslab-uc3m/teo-blender-models/issues). 

## Launch trajectory on the robot / simulator:
Note: this application is based on [examplePositionDirect](https://github.com/roboticslab-uc3m/yarp-devices/blob/offline-ip-mode/examples/cpp/examplePositionDirect/examplePositionDirect.cpp), located in `offline-ip-mode` branch within [yarp-devices](https://github.com/roboticslab-uc3m/yarp-devices/tree/offline-ip-mode) to launch offline trajectories using the PT/PVT mode for the robot. You can try some uploaded trajectories [here](https://drive.google.com/drive/folders/1DncztEjk7guPauoQXpRs-R0gQzFPd7zO?usp=sharing). 
1. Copy the trajectory files in an easily locatable place. Example: `$ ~/trajectories/`
2. Go to the directory where [launchTrayectory](https://github.com/roboticslab-uc3m/teo-blender-models/tree/master/src/cpp) application is located.
3. Compile it
```bash 
mkdir build; cd build; cmake ..
make
```
4.1. Run it on the simulator (CSP mode by default). Example:
```bash
./launchTrajectory --robot /teoSim --csv ~/trajectories/various-arm-movements.csv --period 10
```
4.2. Run it on the robot. In this case we use the `--batch` parameter to launch it in PT/PVT mode (pt by default). Example:
```bash
./launchTrajectory --robot /teo --csv ~/trajectories/various-arm-movements.csv --batch --period 10
```
