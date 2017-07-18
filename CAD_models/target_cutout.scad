$fs = 0.1;

difference() {
    cube([15, 15, 0.5], center=true);
    cube([6.26, 1.93,1], center=true);
    cube([2.5, 3,1], center=true);
    translate([0, -1.5, -2]){
        cylinder(5, 1.25, 1.25);
    }
    translate([0, 1.5, -2]){
        cylinder(5, 1.25, 1.25);
    }
}

