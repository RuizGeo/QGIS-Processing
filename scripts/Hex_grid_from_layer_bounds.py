##Polygons=group
##input=vector
##cellsize=number 1000.0
##grid=output vector

input = processing.getObject(input)

centerx = (input.extent().xMinimum() + input.extent().xMaximum()) / 2
centery = (input.extent().yMinimum() + input.extent().yMaximum()) / 2
width = input.extent().xMaximum() - input.extent().xMinimum() + cellsize
height = input.extent().yMaximum() - input.extent().yMinimum() + cellsize

processing.runalg('qgis:creategrid', cellsize, cellsize, width, height,
                  centerx, centery, 3, input.crs().authid(), grid)
