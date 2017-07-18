

difference() {
    cube([15, 15, 0.5], center=true);
    cube([8, 3.7,1], center=true);
    translate([0, -1, -2]){
        cylinder(5, 2, 2);
    }
}

