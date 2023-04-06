A = [1e-12 20 3;...
     2.001 1e-5 -1;
     4 -2 1]
b=[-1 -2 0.1]'
E = [A b]
cond(A)

n=size(E,1)

%para baixo
for i=1:n-1
  if (abs(E(i,i)) < 1e-15)
    for j=i+1:n
      if (abs(E(j,i)) > 1e-15)
        break
      end
    endfor
    aux=E(i,:);
    E(i,:)=E(j,:);
    E(j,:)=aux;
  end
  E(i+1:n,:) -= E(i+1:n,i)/E(i,i)*E(i,:);
endfor
E

%para cima
for i=n:-1:2
  E(i,:) = E(i,:)/E(i,i);
  E(1:i-1,:) -= E(1:i-1,i)*E(i,:);
endfor

format short e
E(1,:) = E(1,:)/E(1,1)
x1=E(:,4)
abs(A*x1-b)
x2=rref([A b])(:,4)
abs(A*x2-b)




