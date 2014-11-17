AI-RTS - AI Real-Time Strategy Sandbox
======================================

The end goal of AI-RTS is to provide a software "sandbox" in which multiple separate programmable artificial intelligences can compete against each other in a 2D/3D real-time strategy environment.

AI-RTS will be written in a mixture of Python, C++, SDL and OpenGL leading to a fully cross-platform codebase. It will consist of the following separated components:

* External faction, unit and structure definition and configuration
* Asynchronous, incremental time-step approach allowing incorporation of physical models (such as projectile motion) and expensive AI routines
* Order-based mechanics allowing full separation of AI strategy routines from low-level game mechanics AI (such as pathfinding)
* Order-based mechanics allows incorporation of human player interaction (future feature!)
* 2D/3D graphical overlay, which allows visual reply of simulation model, with adjustable speeds

Changelog
---------

17/10/2014 - Basic order mechanics, game loop and single vehicle in a time-step simulation.