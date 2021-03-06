E = [-3 2 0 -5 1 -23; ...
     0  -1 -3 0 0 9; ...
     -2 -1 1 0 0 -1;...
     0 2 -4 3 0 8; ...
     1 0 -3 0 -1 11]
      
 E(2:5,:) -= E(2:5,1)/E(1,1)*E(1,:)
 E(3:5,:) -= E(3:5,2)/E(2,2)*E(2,:)
 E(4:5,:) -= E(4:5,3)/E(3,3)*E(3,:)
 E(5,:) -= E(5,4)/E(4,4)*E(4,:)
 
 E(1:4,:) -= E(1:4,5)/E(5,5)*E(5,:)
 E(1:3,:) -= E(1:3,4)/E(4,4)*E(4,:)
 E(1:2,:) -= E(1:2,3)/E(3,3)*E(3,:)
 E(1,:) -= E(1,2)/E(2,2)*E(2,:)
 
 for i=1:5
  E(i,:) /= E(i,i);
 endfor
 
E