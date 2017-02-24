function [x2,y2] = applyHomography(H, x1, y1)
%% applyHomography: applies the transformation to a set of points.

[w,h,~] = size(x1);
x1 = x1(:)';
y1 = y1(:)';
xy = H*[x1;y1;ones(1,size(x1,2))];

x2 = xy(1,:)./xy(3,:);
y2 = xy(2,:)./xy(3,:);
x2 = reshape(x2,w,h);
y2 = reshape(y2,w,h);

end

