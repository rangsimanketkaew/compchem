BEGIN{
print "#Gaussian 09 run ";\
print "#!!!!Missing Experimental  Geometry!! ";\
print "@<TRIPOS>MOLECULE";\
print "Experimental Geometry replace nm below by number of atoms";\
print "nm      0     0     0";\
print "SMALL\nNO_CHARGES\n\n";\
print "@<TRIPOS>ATOM";\
print "\n";\
print " 	REPLACE BY EXPERIMENTAL GEOMETRY!!!!	";\
print " 	REPLACE BY EXPERIMENTAL GEOMETRY!!!!	";\
print " 	REPLACE BY EXPERIMENTAL GEOMETRY!!!!	";\
print "\n";}
$0~/Stationary point found/{\
print "#Gaussian 09 run ";\
print "#!!!!Missing Experimental  Geometry!! ";\
print "@<TRIPOS>MOLECULE";\
print "Computational Geometry replace nm below by number of atoms";\
print "nm      0     0     0";\
print "SMALL\nNO_CHARGES\n\n";\
print "@<TRIPOS>ATOM";\
while($0!~/Input orientation/){\
getline;\
}
getline;\
getline;\
getline;\
getline;\
getline;\
while($1~/[0-9]/){\
tmp=$2
gsub("1","H",$2);\
gsub("3","Li",$2);\
gsub("4","Be",$2);\
gsub("5","B",$2);\
gsub("6","C",$2);\
gsub("7","N",$2);\
gsub("8","O",$2);\
gsub("9","F",$2);\
gsub("11","Na",$2);\
gsub("12","Mg",$2);\
gsub("13","Al",$2);\
gsub("14","Si",$2);\
gsub("15","P",$2);\
gsub("16","S",$2);\
gsub("17","Cl",$2);\
printf "%2u    %3s     %9f     %9f    %9f     %s   %s    %f \n", $1, $2,  $4 , $5, $6, $2, "SSNAME", 0.0000; \
getline;\
}
print "\n\n";\
}
