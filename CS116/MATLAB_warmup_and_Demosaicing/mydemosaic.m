function [J] = mydemosaic(I)
% mydemosaic - demosaic a Bayer RG/GB image to an RGB image
%
% I: RG/GB mosaic image  of size  HxW
% J: RGB image           of size  HxWx3


red = zeros(size(I));
red(1:2:end,1:2:end) = I(1:2:end,1:2:end);
green = zeros(size(I));
green(1:2:end,2:2:end) = I(1:2:end,2:2:end);
green(2:2:end, 1:2:end) = I(2:2:end, 1:2:end);
blue = zeros(size(I));
blue(2:2:end,2:2:end) = I(2:2:end,2:2:end);

% for red
hred1 = [0.25,0,0.25;0,0,0; 0.25,0, 0.25];
hred2 = [0,0.5,0;0,0,0;0,0.5,0];
hred3 = [0,0,0;0.5,0,0.5;0,0,0];
red = red + imfilter(red,hred1,'conv')+imfilter(red, hred2, 'conv')+imfilter(red,hred3,'conv');

% for green
hgreen = [0,0.25,0; 0.25,0,0.25; 0,0.25,0];
green = green + imfilter(green, hgreen,'conv');

% for blue
blue = blue + imfilter(blue,hred1,'conv')+imfilter(blue, hred2, 'conv')+imfilter(blue,hred3,'conv');

% Recombine separate color channels into an RGB image.
J = cat(3, red, green, blue);

