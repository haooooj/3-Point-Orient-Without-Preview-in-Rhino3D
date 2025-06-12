import rhinoscriptsyntax as rs
import Rhino

def orient_3pt_no_preview():
    # Select objects to orient
    obj_ids = rs.GetObjects("Select objects to orient", preselect=True)
    if not obj_ids:
        return

    # Get the three reference points
    base_pt1 = rs.GetPoint("First reference point")
    if not base_pt1:
        return
    base_pt2 = rs.GetPoint("Second reference point", base_pt1)
    if not base_pt2:
        return
    base_pt3 = rs.GetPoint("Third reference point", base_pt2)
    if not base_pt3:
        return

    # Get the three target points
    target_pt1 = rs.GetPoint("First target point")
    if not target_pt1:
        return
    target_pt2 = rs.GetPoint("Second target point", target_pt1)
    if not target_pt2:
        return
    target_pt3 = rs.GetPoint("Third target point", target_pt2)
    if not target_pt3:
        return

    # Define the source and target planes using the three points
    source_plane = Rhino.Geometry.Plane(base_pt1, base_pt2 - base_pt1, base_pt3 - base_pt1)
    target_plane = Rhino.Geometry.Plane(target_pt1, target_pt2 - target_pt1, target_pt3 - target_pt1)

    # Create the transformation matrix
    xform = Rhino.Geometry.Transform.PlaneToPlane(source_plane, target_plane)

    # Apply the transformation to the selected objects
    for obj_id in obj_ids:
        rs.TransformObject(obj_id, xform)

if __name__ == "__main__":
    orient_3pt_no_preview()
