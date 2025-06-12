# 3-Point Orient Without Preview in Rhino3D

This custom Rhino script provides a performance-optimised alternative to Rhino's native **Orient3Pt** command by eliminating the live transformation preview. It's ideal for working with complex or heavy geometry where real-time visual feedback can cause significant lag.

## What Does It Do?

The **3-Point Orient Without Preview** tool allows you to:

* Select a set of objects.
* Define a source plane using three reference points.
* Define a target plane using three target points.
* Instantly apply the transformation without any visual preview.

This matches Rhino’s standard Orient3Pt function in outcome but skips the display-intensive preview step, making it significantly faster for large models.

## Why Use This Tool?

Rhino’s preview rendering during orientation can become unresponsive or slow when working with:

* Large-scale models
* Complex assemblies
* Lightweight hardware

By removing the preview stage, this tool provides a more responsive workflow while still maintaining full precision.

## How to Use the Script

### Load the Script in Rhino

**Method 1**:

1. Type `_RunPythonScript` into the command line.
2. Browse to and select your script file.

### Method 2 Creating a Button or Alias (Optional)

#### Toolbar Button

1. **Right-click** an empty area of the toolbar and choose **New Button**.
2. In the **Button Editor**:

   * **Left Button Command**:

     ```plaintext
     ! _-RunPythonScript "FullPathToYourScript\orient3pt_no_preview.py"
     ```

     Replace `FullPathToYourScript` with the full path to your `.py` file.
   * **Tooltip**: `3-Point Orient without live preview`.

#### Command Alias

1. Open **Tools > Options > Aliases**.
2. Add a new alias:

   * **Alias**: `orient3np`
   * **Command Macro**:

     ```plaintext
     _-RunPythonScript "FullPathToYourScript\orient3pt_no_preview.py"
     ```

### Using the Command

1. **Select** one or more objects to orient.
2. **Specify three reference points** in the model:

   * These define the source plane.
3. **Specify three target points**:

   * These define the destination plane.
4. The selected objects will be instantly transformed from the source plane to the target plane—without any preview or intermediate redraw.

### Use Cases

* Fast orientation of large building elements
* Repositioning geometry in modular assemblies
* Reducing interaction lag in high-polygon scenes
