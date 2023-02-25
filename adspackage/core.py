def my_func():
  """Example function with types documented in the docstring.

  An example `PEP 484`_ type annotations are supported. If attribute,
  parameter, and return types are annotated according to `PEP 484`_, they 
  do not need to be included in the docstring:
  
  Parameters
  ----------
  lat_series : pandas.Series
      Latitude values.
  lon_series : pandas.Series
      Longitude values.

  Returns
  -------
  pandas.Series
      Point-to-point displacements in meters.
  
  Notes
  -----

  Assumptions:
      * Earth is a perfect sphere, with radius = EARTH_RADIUS_METERS.
      * The point-to-point distances are sufficiently short (so that
        latitude distortion and curvature have limited effects).
      * Both lat_series and lon_series units are degrees.
  
  `Numpy docstring ref`_

  `Numpy docstring example`_

  `Google docstring example`_

  `Sphinx todos`_  

  Todo: 
      * Update these assumpts!
      * Figure out `Sphinx todos`_!


  .. _PEP 484:
      https://www.python.org/dev/peps/pep-0484/
      
  .. _Numpy docstring ref:
      https://numpydoc.readthedocs.io/en/latest/format.html

  .. _Numpy docstring example:
      https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

  .. _Google docstring example:
      https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

  .. _Sphinx todos:
      https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

  """
  return