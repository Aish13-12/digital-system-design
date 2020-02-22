import numpy as np
import matplotlib.pyplot as plt
from coeffs import*

A=np.array([2,0.009704163250003148])
B=np.array([6,0.00973465070000202])
C=np.array([10,0.009806122820000382])
D=np.array([14,0.009700995920002242])
E=np.array([18,0.00971965704000013])
F=np.array([22,0.009704549170000973])


AB=line_gen(A,B)
BC=line_gen(B,C)
CD=line_gen(C,D)
DE=line_gen(D,E)
EF=line_gen(E,F)



plt.plot(AB[0,:],AB[1,:])
plt.plot(BC[0,:],BC[1,:])
plt.plot(CD[0,:],CD[1,:])
plt.plot(DE[0,:],DE[1,:])
plt.plot(EF[0,:],EF[1,:])





plt.text(A[0] * (1 + 0.5), A[1] * (1 - 0.1) , 'A')
plt.text(B[0] * (1 + 0.5), B[1] * (1 - 0.1) , 'B')
plt.text(C[0] * (1 + 0.5), C[1] * (1 - 0.1) , 'C')
plt.text(D[0] * (1 + 0.5), D[1] * (1 - 0.1) , 'D')
plt.text(E[0] * (1 + 0.5), E[1] * (1 - 0.1) , 'E')
plt.text(F[0] * (1 + 0.5), F[1] * (1 - 0.1) , 'F')



plt.plot(A[0], A[1], 'o')
plt.plot(B[0], B[1], 'o')
plt.plot(C[0], C[1], 'o')
plt.plot(D[0], D[1], 'o')
plt.plot(E[0], E[1], 'o')
plt.plot(F[0], F[1], 'o')


plt.axis()
plt.xlabel('Number of Terms');plt.ylabel('Time taken by the code to give the output(In Python)')
plt.grid()
plt.show()



