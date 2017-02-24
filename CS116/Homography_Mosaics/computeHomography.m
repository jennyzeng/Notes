function [H] = computeHomography( x1,y1,x2,y2)
% computeHomography: estimates the transformation vector H given pairs of points
%%% (x1,y1): moving points (points in baseim)
%%% x1: 4x1 vector, each represent the x1 in point(x1,y1)
%%% y1: 4x1 vector, each represent the y1 in point(x1,y1)
%%% (x2, y2): fixed points (points in other imgs)
%%% x2: 4x1 vector, each represent the x2 in point(x2,y2)
%%% y2: 4x1 vector, each represent the y2 in point(x2,y2)
%%% 
%%% 4 rows for a single image (4 different points)
%%% H: a transformation matrix
A = [];
for i = 1:numel(x1)
    x_1 = x1(i);
    y_1 = y1(i);
    x_2 = x2(i);
    y_2 = y2(i);
    A = [A; x_2, y_2, 1, 0, 0, 0, -x_1*x_2, -x_1*y_2, -x_1;...
         0, 0, 0, x_2, y_2, 1, -y_1*x_2, -y_1*y_2, -y_1]; 
end
[~,~,V] = svd(A);
h = V(:,9);
H = reshape(h, 3,3)';


end

