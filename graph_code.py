import numpy as np
import matplotlib.pyplot as plt
from coeffs import*

A=np.array([2,0.01216])
B=np.array([3,0.01210])
C=np.array([4,0.01231])
D=np.array([5,0.01228])
E=np.array([6,0.01210])
F=np.array([7,0.01229])
G=np.array([8,0.01257])
H=np.array([9,0.01231])
I=np.array([10,0.01227])

AB=line_gen(A,B)
BC=line_gen(B,C)
CD=line_gen(C,D)
DE=line_gen(D,E)
EF=line_gen(E,F)
FG=line_gen(F,G)
GH=line_gen(G,H)
HI=line_gen(H,I)



plt.plot(AB[0,:],AB[1,:])
plt.plot(BC[0,:],BC[1,:])
plt.plot(CD[0,:],CD[1,:])
plt.plot(DE[0,:],DE[1,:])
plt.plot(EF[0,:],EF[1,:])
plt.plot(FG[0,:],FG[1,:])
plt.plot(GH[0,:],GH[1,:])
plt.plot(HI[0,:],HI[1,:])



plt.text(A[0] * (1 + 0.5), A[1] * (1 - 0.1) , 'A')
plt.text(B[0] * (1 + 0.5), B[1] * (1 - 0.1) , 'B')
plt.text(C[0] * (1 + 0.5), C[1] * (1 - 0.1) , 'C')
plt.text(D[0] * (1 + 0.5), D[1] * (1 - 0.1) , 'D')
plt.text(E[0] * (1 + 0.5), E[1] * (1 - 0.1) , 'E')
plt.text(F[0] * (1 + 0.5), F[1] * (1 - 0.1) , 'F')
plt.text(G[0] * (1 + 0.5), G[1] * (1 - 0.1) , 'G')
plt.text(H[0] * (1 + 0.5), H[1] * (1 - 0.1) , 'H')
plt.text(I[0] * (1 + 0.5), I[1] * (1 - 0.1) , 'I')


plt.plot(A[0], A[1], 'o')
plt.plot(B[0], B[1], 'o')
plt.plot(C[0], C[1], 'o')
plt.plot(D[0], D[1], 'o')
plt.plot(E[0], E[1], 'o')
plt.plot(H[0], H[1], 'o')
plt.plot(F[0], F[1], 'o')
plt.plot(G[0], G[1], 'o')
plt.plot(I[0], I[1], 'o')

plt.axis()
plt.xlabel('Number of Variables');plt.ylabel('Time taken by the code to give the output(In python)')
plt.grid()
plt.show()



