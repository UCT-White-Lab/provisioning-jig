$fs = 0.1;

difference() {
    cube([15, 15, 0.5], center=true);
    cube([2.44, 1.85,1], center=true);
    cube([1.9, 3.4,1], center=true);
    translate([0, -1.5, -2]){
        cylinder(5, 0.95, 0.95);
    }
    translate([0, 1.5, -2]){
        cylinder(5, 0.95, 0.95);
    }
}

