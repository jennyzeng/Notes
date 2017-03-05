function [mag,ori] = mygradient(I)
%
% compute image gradient magnitude and orientation at each pixel
%
sqrt2 = sqrt(2);
fx = [-sqrt2,0, sqrt2;-1, 0, 1;-sqrt2, 0, sqrt2];
fy = [sqrt2, 1, sqrt2; 0,0,0;-sqrt2,-1,-sqrt2];
dx = imfilter(I, fx,'replicate');
dy = imfilter(I, fy, 'replicate');

mag = sqrt(dx.^2 + dy.^2);
ori = atan2(dy,dx);
