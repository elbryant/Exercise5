my_name = "Erica Bryant";
my_age = 28 # not a lie;
my_height = (63*2.54) # inches;
my_weight = (155*0.453592) # lbs;
my_eyes = "Brown";
my_teeth = "White";
my_hair = "Black";

print "Let's talk about %s." % my_name;
print "She's %d centimeters tall." % my_height;
print "She's %d kilos heavy." % my_weight;
print "Actually, that's not too heavy.";
print "She's got %s eyes and %s hair." % (my_eyes, my_hair);
print "Her teeth are usually %s because she doesn't like coffee." % my_teeth;

#this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight);