# 1. Robot Inheritance
# The generic variables and methods have been placed into a Robot class for you. You will need to create two new classes. One for DriveBot and one for WalkBot. Both of these should inherit from the Robot class. The constructor for the DriveBot will be essentially the same as the superclass constructor, but the WalkBot constructor will include an extra parameter for an instance variable called step_length. Here is what we need to do:

# Create a new class called DriveBot which inherits from the Robot class
# Call the superclass constructor within the DriveBot constructor but pass motor_speed as the parameter for speed in the super class
# Create a new class called WalkBot which inherits from the Robot class
# Add another parameter to the WalkBot constructor for step_length which defaults to 5
# Call the superclass constructor within the constructor for the WalkBot class
# Assign the input parameter for step_length to a new instance variable for step_length

# 2. Using The Superclass
# There was an issue discovered when testing the WalkBot prototypes. In some cases, the robots were incorrectly detecting their own legs as obstacles. To overcome this, we need to modify our adjust_sensor method to reset obstacle_found to False and step_length to 5 while also using the original logic from the superclass. Here are the steps:

# Override the adjust_sensor method in the WalkBot class by re-defining it in that class.
# Call the superclass version of the method within adjust_sensor
# Add a line of code to set obstacle_found to False
# Add a line of code to set step_length to 5

# 3. Conditional Superclass Logic
# Since the bipedal robot is a bit less stable, the obstacle avoidance must be more delicate. Because of this, we want to call the superclass method for avoiding obstacles within the bipedal robot class if the steps per minute are less than or equal to 60, otherwise the WalkBot should only rotate 90 degrees clockwise and set obstacle_found to False. In either case, we need to half the robot’s speed and step_length in order to slow it down during the turn. Here are the steps we need to do:

# Within the WalkBot class, override the method called avoid_obstacles by re-defining it in the class.
# If an obstacle was found
# If the speed if less than or equal to 60
# Call the superclass version of the method
# Otherwise add 90 to the WalkBot‘s direction. If the new direction is greater than 360, it should loop back around to be between 0 and 360. For example, if the new direction is 370, it should really be 10. (hint: use modulo to do this!)
# You should also set obstacle_found to False is the speed was over 60.
# Regardless of whether an obstacle was found, half the speed and the step_length of the robot

# 4. Overriding Dunder Methods
# Let’s add an easy way to increase and decrease our speed as well as some other attributes depending on the type of robot. For the Robot class, we want to increase and decrease the speed using the + and - operators. For the DriveBot class, we want to adjust the speed and sensor_range with those operators. Lastly, for the WalkBot class, we want to adjust the speed and step_length with those operators. We can override the dunder methods which represent those operations and call the superclass version of those dunder methods. Here are the steps:

# In the Robot class, override the + operator to add to the speed of the robot
# In the Robot class, override the - operator to subtract from the speed of the robot
# In the DriveBot class, override the + operator to call the superclass version of the operator as well as add to the sensor_range of the robot
# In the DriveBot class, override the - operator to call the superclass version of the operator as well as subtract from the sensor_range of the robot
# In the WalkBot class, override the + operator to call the superclass version of the operator as well as add half of the value on the right side of the operator to the step_length of the robot
# In the WalkBot class, override the - operator to call the superclass version of the operator as well as subtract half of the value on the right side of the operator from the step_length of the robot

# 5. Prevent A Robot Takeover
# Finally, we are going to make some last additions to our bipedal robot and test it out. Your customers are worried that your new robot model might become sentient when controlled in large numbers. To prevent this, program the bipedal robots so that if five WalkBots are created when there are already at least 5 DriveBots (causing 10 or more total bots) then disable all robots. This is what you need to do:

# Create a new class variable in the WalkBot class to count the number of WalkBot instances
# In the constructor for the WalkBot, increment the counter by 1
# Also, in the constructor, check if the number of total Robots (from the superclass) is greater than or equal to 10 and if the number of WalkBots is greater than or equal to 5.
# If so, disable all robots