# Numerics
MPE CDT Numerical Methods


October 25 2017 (First submission)

The file linear_swe contains the first method presented in the MPE book to solve the shallow water equations. The file linear_swe_collocated_implicite contains the code for the collocated implicit scheme given in page 312 of the MPE book. For the latter method, only a solution for h has been computed.

In the implicit scheme, a circulant matrix (full rank) has been created and its corresponding linear equation has been solved using the in-built python command linalg.solve. This command is fed with a matrix and a vector and computes the solution of the associated linear equation using a LU decomposition with partial pivoting.


November 29 2017 (Final code submission)

The main_algorithm file contains the function maincode() that generates different plots in the console that illustrate the behaviour of the different schemes used to solve the Shallow Water Equations. In this exercise, we have stuck to the case where the initial condition is the squared sine. This is because an analytical solution can be easily coded from it and because its periodic extension is smooth (unlike a sine wave for instance). Other initial conditions have been considered and their analytical solutions have been coded (see initialconditions.py and SqWave.py).

Having defined the initial conditions and setting the spacegrid, maincode() calls the functions solving the SWE using a collocated explicit scheme, a collocated implicit scheme and a staggered grid. Each method will produce several plots of the solution at several times, a graph of the L2 error with respect to the analytical solution and the evolution of the total mass of the system.
