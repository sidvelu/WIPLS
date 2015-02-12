function target_loc = Triangulate(angle1, coords1, angle2, coords2)
d2 = ((sind(angle1) * (coords1(1) - coords2(1))) + (cosd(angle1) * (coords2(2) - coords1(2)))) / (sind(angle1) * cosd(angle2) - cosd(angle1) * sind(angle2));
targx = coords2(1) + (cosd(angle2) * d2);
targy = coords2(2) + (sind(angle2) * d2);
target_loc = [targx targy];