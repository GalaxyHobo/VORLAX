# VORLAX

Version of NASA public-domain vortex lattice code VORLAX.

vorlax2017.f is latest version. Older versions like vorlax2014working.f kept in repo for quick reference. However, future versions need to let Git do its job handling versioning and history.

To compile exe using MinGW gfortran that uses DLL's (smaller exe, but DLL's must be installed on host machine): 
gfortran vorlax2017.f -o vorlax.exe

To compile exe using MinGW gfortran with static libraries (bigger exe, but will run on machines without DLL's): 
gfortran -static vorlax2017.f -o vorlax.exe

To run: copy a properly formatted input file to the name "vorlax.in" and type "vorlax" (or whatever the exe was named during compilation - see above) at the command prompt. Alternatively, the code can be run from the VorPlot python script (currently requires that the input file be collocated with the exe and named "vorlax.in"). 

Aero coefficients will appear in VORLAX.OUT, coordinates for a 3-D wireframe will appear in VORLAX.WIRE, and detailed spanwise and chordwise characteristics will appear in VORLAX.LOG. See the CR for a comprehensive explanation of the input file and the underlying vortex-lattice theory. See https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19780008059.pdf and https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19780017111.pdf
