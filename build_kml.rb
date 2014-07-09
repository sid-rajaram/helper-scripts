#!/usr/bin/env ruby

##
# Usage: cat example_locations.txt | ./build_kml.rb > output.kml

def print_kml_start
  puts "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://www.opengis.net/kml/2.2\"
     xmlns:gx=\"http://www.google.com/kml/ext/2.2\">
  <Document>
    <Style id=\"transBluePoly\"> 
      <LineStyle>
        <width>1.5</width>
      </LineStyle>
      <PolyStyle>  
        <color>7dff0000</color>
        <outline>0</outline>
      </PolyStyle>
    </Style>"
end

def print_kml_end
  puts "  </Document>
</kml>"
end

def draw_point name, latitude, longitude
  puts "  <Placemark>
    <name>#{name}</name>
    <Point>
      <coordinates>#{longitude},#{latitude},0</coordinates>
    </Point>
  </Placemark>"

end

def draw_polygon polygon
  puts "  <Placemark>
    <styleUrl>\#transBluePoly</styleUrl>
    <Polygon>
      <extrude>1</extrude>
      <altitudeMode>relativeToGround</altitudeMode>
      <outerBoundaryIs>
        <LinearRing>
          <coordinates>"
  polygon.each do |point|
    puts "          #{point[1]},#{point[0]},5"  
  end
  puts "          </coordinates>
        </LinearRing>
      </outerBoundaryIs>"
  puts "    </Polygon>
  </Placemark>"
end

print_kml_start

STDIN.each_line do |line|
  lat, lng = line.chomp.split /\t/
  draw_point "foo", lat, lng
end  

print_kml_end

