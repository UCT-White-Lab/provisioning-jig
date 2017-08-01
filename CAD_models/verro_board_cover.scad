$fs = 0.1;

difference() {
    cube([10, 15, 0.5], center=true);
    translate([0.35, 5.5, 0]){
        target_cutout();
    }
    translate([0.35, 3.5, 0]){
        target_cutout();
    }
   
    translate([-1.4, -2.8, 0]){
         rotate(90){debug_cutout();}
    }
    
    translate([-1.4, 0, 0]){
         rotate(90){debug_cutout();}
    }
    translate([0, -6.75, 0]){
        cube([8, 2.5, 1], center=true);
    }
    
}

module debug_cutout () {
    cube([2.44, 1.85,1], center=true);
    cube([1.9, 3.4,1], center=true);
    translate([0, -1.5, -2]){
        cylinder(5, 0.95, 0.95);
    }
    translate([0, 1.5, -2]){
        cylinder(5, 0.95, 0.95);
    }
}

// Edit this
module target_cutout () {
    cube([6.26, 1.93,1], center=true);
    cube([2.5, 3,1], center=true);
    translate([0, -1.5, -2]){
        cylinder(5, 1.25, 1.25);
    }
    translate([0, 1.5, -2]){
        cylinder(5, 1.25, 1.25);
    }
}