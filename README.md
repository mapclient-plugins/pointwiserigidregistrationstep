Pointwise Rigid Registration Step
=================================
MAP Client plugin for rigid-body and scaling registration of two 3-D
pointclouds. A variety of registration methods are implemented allowing 
for correspondent and non-correspondent registration using rigid-body,
rigid-body plus scaling, and affine transformation.

Requires
--------
- GIAS3 - Common: https://github.com/musculoskeletal/gias3.common
- GIAS3 - Registration: https://github.com/musculoskeletal/gias3.registration
- GIAS3 - MAP Client Plugin Utilities: https://github.com/musculoskeletal/gias3.mapclientpluginutilities

Inputs
------
- **pointcloud** [nx3 NumPy Array] : source pointcloud
- **pointcloud** [nx3 NumPy Array] : target pointcloud

Outputs
-------
- **pointcloud** [nx3 NumPy Array] : registered source pointcloud
- **geometrictransform** : an object containing the registration transformation
- **registration error** [float] : RMS error of the registration

Configuration
-------------
- **identifier** : Unique name for the step.
- **UI Mode** : Whether or not to use the GUI during execution. Turn off to run workflows in batch mode.
- **Registration Method** : Select from a list of implemented registration methods. See below for an explanation of the list.
- **Min Relative Error** : Termination criteria for iterative registration methods.
- **Points to Sample** : Number of points to uniformly sample from the source and target pointclouds to use in registration.
- **Initial Translation** : Initial translation in x, y, and z to apply to the source pointcloud before iterative registration. If 0, the initial translation will be the vector from the source centre of mass to the target centre of mass.
- **Initial Rotation** : Initial Euler rotation angles about x, y, and z to apply to the source pointcloud before iterative registration. Rotation order is z, y, x.
- **Initial Scale** : Initial isotropic scale factor to apply to the source pointcloud before iterative registration.

Usage
-----
This step is used to register a source pointcloud to a target pointcloud using only rigid to affine transformations. This is done typically before high-fidelity non-rigid registration steps. 

If the source and target pointclouds are already correspondent (i.e. they have the same number of points and the order of the points are correspondent), the correspondent affine, rigid, and rigid+scale methods can be used to quickly and robustly register the pointclouds.

If there is no correspondence, then one of the ICP method can be used. For reliable results, an initial rotation should be provided in terms of Euler angles to rougly align the source to target. When using the ICP methods, is the target pointcloud is partial, the target-source ICP methods should be used. Inversely, if the source pointcloud is partial, then the source-target ICP method should be used.

In the step GUI, the translation, rotation, and scaling of the source pointcloud can be modified manually before and after automatic registration. Note that the selected registration method determines what transformation are output. For example, if _ICP Rigid Source-Target_ is selected, the scaling factor will not be output even if it was manually modified.

The final transformation can be output and passed to another step to apply the transformation to some other object. For example, a fieldwork model can be registered to a segmented surface by using points sampled on the model (Fieldwork Model Evaluation Step) as the source and vertices of the segmentation as the target. The output transformation can be passed to the Fieldwork Model Transformation Step to transform the fieldwork model to the registered position.

Step GUI
--------
- **3D Scene** : Interactive viewer for the source, target, and registered source pointclouds.
- **Visibles box** : Show or hide each of the pointclouds in the 3-D scene.
- **Reg Type** : Select the registration method.
- **Min Rel Err**: Termination criteria for iterative registration methods.
- **Samples** : Number of points to uniformly sample from the source and target pointclouds to use in registration.
- **Translations** : Translation in x, y, and z to apply to the source pointcloud. If all 0s, the initial translation will be the vector from the source centre of mass to the target centre of mass.
- **Rotations** : Euler rotation angles about x, y, and z to apply to the source pointcloud. Rotation order is z, y, x.
- **Scaling** : Isotropic scale factor to apply to the source pointcloud.
- **Register** : Run the selected registration method using the given parameters. The registered source pointcloud will be shown when done.
- **Reset** : Remove the registered source pointcloud.
- **Abort** : Abort the workflow.
- **Accept** : Finish execution of the step and output the registered source pointcloud, transformation, and error.
- **Registration Errors** : Displays registration errors.
	- **RMS** : The root-mean-squared distance between target and source points.
	- **Mean** : The mean distance between target and source points.
	- **S.D.** : The standard deviation of distances between target and source points.
- **Screeshot** : Save a screenshot of the current 3-D scene to file.
	- **Pixels X** : Width in pixels of the output image.
	- **Pixels Y** : Height in pixels of the output image.
	- **Filename** : Path of the output image file. File format is defined by the suffix of the given filename.
	- **Save Screenshot** : Take screenshot and write to file.
    
Registration Methods
--------------------
- **Correspondent Affine** : Calculates and applies an affine transformation to the source pointcloud that minimises the least-squares distance between each source point and its corresponding target point. Correspondence is assumed in the order of points in the source and target pointclouds.

- **Correspondent Rigid** : Calculates and applies a rigid-body transformation to the source pointcloud that minimises the least-squares distance between each source point and its corresponding target point. Correspondence is assumed in the order of points in the source and target pointclouds.

- **Correspondent Rigid+Scale** : Calculates and applies a rigid-body with isotropic scaling transformation to the source pointcloud that minimises the least-squares distance between each source point and its corresponding target point. Correspondence is assumed in the order of points in the source and target pointclouds.

- **ICP Rigid Source-Target** : Uses an iterative closest-point algorithm to calculate and apply a rigid-body transformation that minimises the least-squares distance between each source point and its closest target point. Source and target pointclouds do not have to be correspondent.

- **ICP Rigid Source-Target** : Uses an iterative closest-point algorithm to calculate and apply a rigid-body transformation that minimises the least-squares distance between each target point and its closest source point. Source and target pointclouds do not have to be correspondent.

- **ICP Rigid+Scale Source-Target** : Uses an iterative closest-point algorithm to calculate and apply a rigid-body with isotropic scaling transformation that minimises the least-squares distance between each source point and its closest target point. Source and target pointclouds do not have to be correspondent.

- **ICP Rigid+Scale Source-Target** : Uses an iterative closest-point algorithm to calculate and apply a rigid-body with isotropic scaling transformation that minimises the least-squares distance between each target point and its closest source point. Source and target pointclouds do not have to be correspondent.
