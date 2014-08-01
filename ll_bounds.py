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

washington_pts = dict()
washington_pts['N'] = 45.55
washington_pts['S'] = 49
washington_pts['E'] = -116.916
washington_pts['W'] = -124.77

texas_pts = dict()
texas_pts['N'] = 25.83
texas_pts['S'] = 36.5
texas_pts['E'] = -93.5
texas_pts['W'] = -106.65

newyork_pts = dict()
newyork_pts['N'] = 40.5
newyork_pts['S'] = 45.017
newyork_pts['E'] = -71.85
newyork_pts['W'] = -79.77

california_pts = dict()
california_pts['N'] = 32.53
california_pts['S'] = 42
california_pts['E'] = -114.13
california_pts['W'] = -124.44

kansas_pts = dict()
kansas_pts['N'] = 37
kansas_pts['S'] = 40
kansas_pts['E'] = -94.58
kansas_pts['W'] = -102.05

alaska_poly = poly_from_bounds(alaska_pts)
hawaii_poly = poly_from_bounds(hawaii_pts)
mainland_poly = poly_from_bounds(mainland_pts)
puget_sound_poly = poly_from_bounds(puget_sound_pts)
washington_poly = poly_from_bounds(washington_pts)
texas_poly = poly_from_bounds(texas_pts)
newyork_poly = poly_from_bounds(newyork_pts)
california_poly = poly_from_bounds(california_pts)
kansas_poly = poly_from_bounds(kansas_pts)
