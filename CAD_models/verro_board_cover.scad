$fs = 0.1;

//This is all in cm

sheet_thickness = 5;
pin_pitch = 2.54;


projection(){
    difference() {
        cube([100, 150, sheet_thickness], center=true);
        translate([3.5, 55, 0]){
            target_cutout();
        }
        translate([0, -10*pin_pitch, 0]){
            translate([3.5, 55, 0]){
                target_cutout();
            }
        }
        
       
        translate([-14, -28, 0]){
             rotate(90){debug_cutout();}
        }
        
        translate([0, 11*pin_pitch, 0]){
             translate([-14, -28, 0]){
                rotate(90){debug_cutout();}
            }
        }
        translate([0, -67.5, 0]){
            cube([80, 28, 10], center=true);
        }
        
    }
}

module debug_cutout () {
    cube([24.4, 18.5,10], center=true);
    cube([19, 34,10], center=true);
    translate([0, -15, -20]){
        cylinder(50, 9.5, 9.5);
    }
    translate([0, 15, -20]){
        cylinder(50, 9.5, 9.5);
    }
}

// Edit this
module target_cutout () {
    cube([62.6, 19.3,10], center=true);
    cube([25, 30,10], center=true);
    cube([75, 14,10], center=true);
    translate([35, 0, -20]){
        cylinder(50, 7, 7);
    }
    translate([-35, 0, -20]){
        cylinder(50, 7, 7);
    }
}
