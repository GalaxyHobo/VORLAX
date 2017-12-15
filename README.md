# VORLAX

Version of NASA public-domain vortex lattice code VORLAX.

vorlax2017.f is latest version. Older versions like vorlax2014working.f kept in repo for quick reference. However, future versions need to let Git do its job handling versioning and history.

To compile exe using MinGW gfortran that uses DLL's (smaller exe, but DLL's must be installed on host machine): 
gfortran vorlax2017.f -o vorlax.exe

To compile exe using MinGW gfortran with static libraries (bigger exe, but will run on machines without DLL's): 
gfortran -static vorlax2017.f -o vorlax.exe

