%% I. Manipulando MATRICES.
% 1) Realice las transformaciones lineales (a) $*q*= Q*x*$ y b) $*x* = Q^{-1}$
% 
% $Q = \begin{bmatrix} 5/6 & 1/6 & 0\\ 5/6 & 0 & 1/6\\ 0 & 5/6 & 1/6
% \end{bmatrix} x = \begin{bmatrix} 56\\ 14\\ 0.005 \end{bmatrix}$

Q = [5/6 1/6 0; 5/6 0 1/6; 0 5/6 1/6];
x = [56;14;0.005];

q = Q*x;
x = q/Q;

% Se puede observar como ambas dan exactamente lo mismo dado que una forma
% es el despeje de la otra.

% 2) Importe los datos de un archivo .csv, .xls o .xlsx como una matrix a
% su plataforma de preferencia y despliegue las primeras 15 filas y
% columnas


