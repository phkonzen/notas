A = [-2 -3 2 3; ...
     -4 -6 6 6; ...
     -2 0 4 6; ...
     4 3 -8 -6]
b = [10 20 10 -17]'
E = [A b]
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
E(1,:) = E(1,:)/E(1,1)
