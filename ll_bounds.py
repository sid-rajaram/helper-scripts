def poly_from_bounds(pts):
  poly = []
  poly.append([pts['E'], pts['N']])
  poly.append([pts['E'], pts['S']])
  poly.append([pts['W'], pts['S']])
  poly.append([pts['W'], pts['N']])
  return poly

mainland_pts = dict()
mainland_pts['N'] = 49.384472
mainland_pts['S'] = 25.118333
mainland_pts['E'] = -66.949778
mainland_pts['W'] = -124.733056

alaska_pts = dict()
alaska_pts['N'] = 71.388889
alaska_pts['S'] = 51.219444
alaska_pts['E'] = -129.974194
alaska_pts['W'] = -179.108611

hawaii_pts = dict()
hawaii_pts['N'] = 22.228
hawaii_pts['S'] = 18.908885
hawaii_pts['E'] = -154.806032
hawaii_pts['W'] = -160.241518

puget_sound_pts = dict()
puget_sound_pts['N'] = 48.5
puget_sound_pts['S'] = 46.5
puget_sound_pts['E'] = -121.5
puget_sound_pts['W'] = -123.5

alaska_poly = poly_from_bounds(alaska_pts)
hawaii_poly = poly_from_bounds(hawaii_pts)
mainland_poly = poly_from_bounds(mainland_pts)
puget_sound_poly = poly_from_bounds(puget_sound_pts)

