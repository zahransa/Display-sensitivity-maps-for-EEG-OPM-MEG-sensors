# Display-sensitivity-maps-for-EEG-OPM-MEG-sensors
Such maps are used to know how much sources are visible by a type of sensor, and how much projections shadow some sources
- Task to do (Export the channel from Brainstorm to Matlab (extract the meg), Compute the lead field, in the script of reduce.py compute the sensitivity map, om Bst plot using the Imaggridmap

- In the paper (Sensitivity of MEG and EEG to Source Orientation) They extracted the forward field for each source from the lead field matrix. This latter is available in the head model file of Brainstorm. We can then reproduce the operations described in the paper using a custom made script we will need to write. It will yield an array of values, one per source location, which we can store in the ImageGridAmp variable of a Brainstorm source file. For this, we can use the reduce.py script and then replace the contents with ImageGridAmp values.

![image](https://user-images.githubusercontent.com/29655962/88534353-31150b80-d008-11ea-9bc0-1a80dab70cd9.png)

- In Brainstorm:
Define some source activity, with the process "Simulate > Simulate generic signal"
http://neuroimage.usc.edu/brainstorm/Tutorials/TimeFrequency#Simulation
Create a scout to which you want to set this activity (you can use the menu “Scout > New: Coordinates” to create a new ROI based on MNI coordinates)
http://neuroimage.usc.edu/brainstorm/Tutorials/Scouts#Scout_toolbar_and_menus
Associate the signal with the cortex patch and use this to simulate EEG or MEG recordings, with process “Simulate > Simulate recordings from scouts” (select the simulated signal in Process1, and select the scout in the process options)
