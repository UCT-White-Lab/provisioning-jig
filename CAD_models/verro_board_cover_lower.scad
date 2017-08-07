$fs = 1;

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
        
        translate([-14, -28+11*pin_pitch, 0]){
            rotate(90){debug_cutout();}
        }
        
        translate([-14+18*pin_pitch, -28, 0]){
             rotate(90){debug_cutout();}
        }
        // the built in debugger
        translate([0, -67.5, 0]){
            cube([80, 25, 10], center=true);
        }
        // USB cutouts
        translate([32.5, -67.5, 0]){
            cube([15, 32, 10], center=true);
        }
        translate([-32.5, -67.5, 0]){
            cube([15, 32, 10], center=true);
        }
        
        translate([13.5, 55, 0]){
            cube([63, 10,10], center=true);
        }
        
    }
}

module debug_cutout () {
    cube([24.4, 18.5,10], center=true);
}

// Edit this
module target_cutout () {
    cube([63, 19.3,10], center=true);
    
}
