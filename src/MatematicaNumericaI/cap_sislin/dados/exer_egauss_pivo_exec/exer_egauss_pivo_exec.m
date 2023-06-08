A = [-2e-12 10 3e-4;...
     1e5 1e-13 -1;
     1 -2 3e-7]
b=[2 -1 4]'
E = [A b]

n=size(E,1)

%para baixo
[s,j] = max(abs(E(:,1:n)'));
for i=1:n-1
  [aux,j] = max(abs(E(i:n,i))./s(i:n)');
  j+=i-1;
  
  aux=E(i,:);
  E(i,:)=E(j,:);
  E(j,:)=aux;

  E(i+1:n,:) -= E(i+1:n,i)/E(i,i)*E(i,:)
endfor

%para cima
for i=n:-1:2
  E(i,:) = E(i,:)/E(i,i);
  E(1:i-1,:) -= E(1:i-1,i)*E(i,:);
endfor
E(1,:) = E(1,:)/E(1,1)

rref([A b])


