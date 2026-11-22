# S16 Activity - IFCOpenShell
# Make sure AC20-FZK-Haus.ifc is in the same folder as activity.py

# import the ifcopenshell library so we can open, read and edit IFC files
import ifcopenshell

# 3. Load the IFC file
# ifcopenshell.open() opens the IFC file and stores it in the ifc_file variable
ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")

# 3a. Print the schema (IFC version) of the file, e.g. IFC2X3 or IFC4
print("IFC file loaded:", ifc_file.schema)

# 9. Stretch Goal: Get and print the project name
# [0] gets the first (and only) IfcProject in the file
project = ifc_file.by_type("IfcProject")[0]
print("Project Name:", project.Name)

# 4. Find all IfcStair elements and print their names and ids
# by_type() returns every entity of the given IFC type
stairs = ifc_file.by_type("IfcStair")
print(f"\nNumber of stairs: {len(stairs)}")

# loop through each stair and print its GlobalId and Name
for stair in stairs:
    print(stair.GlobalId, stair.Name)

# 5. Find all IfcSlab elements and print their names and ids
slabs = ifc_file.by_type("IfcSlab")
print(f"Number of slabs: {len(slabs)}")

for slab in slabs:
    print(slab.GlobalId, slab.Name)

# 6. Rename all slabs
# enumerate(slabs, 1) gives a counter (i) starting at 1 plus the current slab
for i, slab in enumerate(slabs, 1):
    slab.Name = f"Renamed_Slab_{i}"
    print(f"Updated slab: {slab.GlobalId} -> {slab.Name}")

# 7. Print the building storeys (name and elevation of each floor)
# Spatial structure: project -> site -> building -> storey
print("\nSpatial Structure:")
for site in project.IsDecomposedBy[0].RelatedObjects:
    for building in site.IsDecomposedBy[0].RelatedObjects:
        for storey in building.IsDecomposedBy[0].RelatedObjects:
            print("Storey", storey.Name, "Elevation", storey.Elevation)

# 8. List all object types in the file
# set() keeps only unique values, so each IFC type appears once
# is_a() returns the IFC type of an element (e.g. "IfcWall")
types = set()
for element in ifc_file:
    types.add(element.is_a())

print("\nObject types in file:", types)

# 10. Save the updated IFC file with the renamed slabs
# write() creates a new IFC file with the given name
ifc_file.write("AC20-FZK-Haus_renamed.ifc")
print("\nSaved renamed slabs to: AC20-FZK-Haus_renamed.ifc")
