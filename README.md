Just a test for roughly simulating the arena for Robocon, probably doesn't work very well  
  
We implement ActorManager to manage IDs and references and stuff as I want to avoid potential collisions and confusion accessing things  
I'm working on a system for allowing implementing operational logic inside an algorithm class which we tick every second or so  
I'll try and simulate ultrasonic using RayCasting  
  
actortypes:  
robot  
sheep  
gem (Not Implemented)  
arena (Not Implemented)  
  
Putting this here so I don't forget:  
Everything outside of ActorClass.py MUST call an AM to do it what it wants and cannot call anything else directly  
AM manages EVERYTHING  
IDs are created randomly using a oneliner I found on StackOverflow, may be glitchy  
Why are there so many subclasses? I don't know  
  
TODO:  
Logging  
Arena  
Gems  
CRITCAL: Custom control algorithms  
Raycasting for sensing  
