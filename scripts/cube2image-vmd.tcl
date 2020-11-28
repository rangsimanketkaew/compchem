# Generate Image file from several gaussian cube files on VMD program.

display resetview
display projection Orthographic
display shadows on
display ambientocclusion on
display aoambient 0.800000
display aodirect 0.300000
display cuemode Linear
display backgroundgradient on
material add copy AOChalky
material change diffuse Material23 1.000000
material change opacity Material23 0.400000
material change specular Material23 0.570000

#########################
### Set number of first file
set a 1
### Set no. of final file
set b 100
#########################

for { set p $a ; set id 0} { $p <= $b } {incr p; incr id} {

set filename [format %s.cube $p]

mol new $filename
puts "|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|  IMPORT $filename"
#mol showrep $p 0 0

rotate y by 90
rotate z by 90
scale by 0.8

mol showrep $id 0 0
mol showrep $id 0 1
mol modstyle 0 $id CPK 1.000000 0.300000 12.000000 12.000000
mol modcolor 0 $id Element
mol modmaterial 0 $id AOChalky

mol addrep $id
mol modstyle 1 $id Isosurface 0.00001 0 0 0 1 1
mol modcolor 1 $id ColorID 1
mol modmaterial 1 $id Material23

render snapshot Frame_$id.bmp 

#render TachyonInternal Frame_$id.ppm
#render Tachyon vmdscene.dat "/usr/local/lib/vmd/tachyon_LINUXAMD64" -aasamples 12 %s -format TARGA -o %s.tga -res 4096 4096

mol delete $id

}

