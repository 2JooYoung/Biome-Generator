import maya.cmds as cmds
import random

# Function to print values of sliders and toggles
def printVal(slider1, slider2, radioGrp, weather, season):
    global cmds
    terrain = cmds.radioButtonGrp(radioGrp, q=True, select=True)
    print("Terrain:", ("Flat" if terrain == 1 else "Mountain"))
    print("Trees:", cmds.intSliderGrp(slider1, q=True, v=True))
    print("Rocks:", cmds.floatSliderGrp(slider2, q=True, v=True))
    weather_vals = cmds.checkBoxGrp(weather, q=True, va3=True)
    print("Weather:", "Sunny" if weather_vals[0] else "Rainy" if weather_vals[1] else "Snowy")
    season_val = cmds.radioButtonGrp(season, q=True, select=True)
    seasons = ["Summer", "Fall", "Winter", "Spring"]
    print("Season:", seasons[season_val - 1])

# Window name
smtb = 'BiomeGenerator'

# Check if window exists
if cmds.window(smtb, exists=True):
    cmds.deleteUI(smtb)

# Create window
smtb = cmds.window(smtb, title='Biome Generator', widthHeight=(600, 350), sizeable=False)
cmds.columnLayout(adjustableColumn=True)

# UI Elements
radioGrp = cmds.radioButtonGrp(label='Select Terrain', numberOfRadioButtons=2, labelArray2=['Flat', 'Mountain'])
slider1 = cmds.intSliderGrp(label='Trees', min=0, max=30, value=0, step=1, field=True)
slider2 = cmds.intSliderGrp(label='Rocks', min=0, max=20, value=0, field=True)
weather = cmds.checkBoxGrp(numberOfCheckBoxes=3, label='Weather', labelArray3=['Sunny', 'Rainy', 'Snowy'], v1=True, v2=False, v3=False)
season = cmds.radioButtonGrp(label='Select Season', numberOfRadioButtons=4, labelArray4=['Spring', 'Summer', 'Fall', 'Winter'])




# Function to print values of sliders and toggles, duplicate terrain, and color it based on the season
def printVal(slider1, slider2, radioGrp, weather, season):
    global cmds
    terrain = cmds.radioButtonGrp(radioGrp, q=True, select=True)
    print("Terrain:", ("Flat" if terrain == 1 else "Mountain"))

    # Define the object to duplicate based on the terrain selection
    terrain_object = 'plain_terrain' if terrain == 1 else 'mountain_terrain'



    # Check if the selected terrain object exists
    if cmds.objExists(terrain_object):
        duplicated_object = cmds.duplicate(terrain_object)[0]  # Duplicate and get the name of the new object
        cmds.move(0, 0, 0, duplicated_object)  # Move the duplicated object to the coordinates (0,0,0)

        # Color the duplicated terrain based on the season
        season_val = cmds.radioButtonGrp(season, q=True, select=True)
        colors = {
            1: (0.5, 1.0, 0.5),  # Light green for Spring
            2: (0.0, 0.5, 0.0),  # Deep green for Summer
            3: (0.55, 0.27, 0.07), # Brown for Fall
            4: (1.0, 1.0, 1.0)   # White for Winter
        }
        color = colors.get(season_val, (1, 1, 1))  # Default color white
        material = cmds.shadingNode('lambert', asShader=True)  # Create a new Lambert material
        cmds.setAttr(material + '.color', color[0], color[1], color[2], type='double3')  # Set the color of the material
        cmds.select(duplicated_object)
        cmds.hyperShade(assign=material)  # Assign the material to the duplicated object
    else:
        print(f"Error: '{terrain_object}' object does not exist.")
    # Tree Generation
    tree_count = cmds.intSliderGrp(slider1, q=True, v=True)
    season_val = cmds.radioButtonGrp(season, q=True, select=True)


    if season_val in [1, 2]:  # Spring (1) and Summer (2)
        for _ in range(tree_count):
            new_tree = cmds.duplicate('c_green')[0]
            x, y, z = getRandomCoordinatesForTerrain()
            cmds.move(x, y, z, new_tree)

    elif season_val == 3:  # Fall (3)
        half_count = tree_count // 2
        for _ in range(half_count):
            new_tree = cmds.duplicate('c_green')[0]
            x, y, z = getRandomCoordinatesForTerrain()
            cmds.move(x, y, z, new_tree)

        for _ in range(tree_count - half_count):
            new_tree = cmds.duplicate('b_bare')[0]
            x, y, z = getRandomCoordinatesForTerrain()
            cmds.move(x, y, z, new_tree)


    if season_val == 4:  # Assuming 4 is the value for Winter
        if cmds.objExists('b_bare'):  # Check if the 'b_bare' object exists
            for _ in range(tree_count):
                new_tree = cmds.duplicate('b_bare')[0]  # Duplicate the tree
                x, y, z = getRandomCoordinatesForTerrain()  # Get random coordinates
                cmds.move(x, y, z, new_tree)  # Move the tree to the random coordinates
        else:
            print("Error: 'b_bare' tree object does not exist.")



def getRandomCoordinatesForTerrain():
    # Define the bounds of your terrain here
    x_min, x_max = -10, 10
    z_min, z_max = -10, 10
    y = 0  # Assuming the terrain is flat at y = 0

    x = random.uniform(x_min, x_max)
    z = random.uniform(z_min, z_max)

    return x, y, z


    # Rest of the code for printing slider values
    print("Trees:", cmds.intSliderGrp(slider1, q=True, v=True))
    print("Rocks:", cmds.intSliderGrp(slider2, q=True, v=True))
    weather_vals = cmds.checkBoxGrp(weather, q=True, va3=True)
    print("Weather:", "Sunny" if weather_vals[0] else "Rainy" if weather_vals[1] else "Snowy")





# Button with command using lambda for passing arguments
cmds.button(label='Generate', command=lambda _: printVal(slider1, slider2, radioGrp, weather, season))

# Display window
cmds.showWindow(smtb)
