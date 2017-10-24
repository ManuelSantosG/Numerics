# Numerics
MPE CDT Numerical Methods


October 25 2017 (First submission)

The file linear_swe contains the first method presented in the MPE book to solve the shallow water equations. The file linear_swe_collocated_implicite contains the code for the collocated implicit scheme given in page 312 of the MPE book. For the latter method, only a solution for h has been computed.

In the implicit scheme, a circulant matrix (full rank) has been created and its corresponding linear equation has been solved using the in-built python command linalg.solve. This command is fed with a matrix and a vector and computes the solution of the associated linear equation using a LU decomposition with partial pivoting.
