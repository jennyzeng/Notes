function [result] = stitch(leftI,rightI,overlap);

% 
% stitch together two grayscale images with a specified overlap
%
% leftI : the left image of size (H x W1)  
% rightI : the right image of size (H x W2)
% overlap : the width of the overlapping region.
%
% result : an image of size H x (W1+W2-overlap)
%
if (size(leftI,1)~=size(rightI,1)) % make sure the images have compatible heights
  error('left and right image heights are not compatible');
end

% dummy code that produces result by 
% simply pasting the left image over the
% right i
% mage. replace this with your own
% code!
[H,W1,~] = size(leftI);
W2 = size(rightI,2);
W = W1+W2-overlap;

%% first extract the overlapping strips from the two input images 
% and then compute a cost array given by the absolute value of their difference. 
strip = abs(leftI(:,W1-overlap+1:W1) - rightI(:, 1:overlap));
%%  find the seam along which to stitch the images where they differ the least in brightness. 
path = shortest_path(strip);

%% creating alpha masks
maskL = ones(H,W);
maskR = ones(H,W);
for i=1:H
    maskL(i,W1-overlap+path(i)) = 0.5;
    maskL(i,W1-overlap+path(i)+1:W) = 0;

end
maskR = maskR-maskL;
leftI = [leftI,zeros(H, W2-overlap)];
rightI = [zeros(H, W1-overlap),rightI];

result = leftI.*maskL + rightI.*maskR;



