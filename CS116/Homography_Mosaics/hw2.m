%% Load in images
imnames = {'atrium/IMG_1347.JPG','atrium/IMG_1348.JPG','atrium/IMG_1349.JPG'};
% imnames = {'shelf/1.JPG','shelf/2.JPG','shelf/3.JPG'};
nimages = length(imnames);
% baseim = 1; %index of the central "base" image
baseim = 1;
for i = 1:nimages
  ims{i} = im2double(imread(imnames{i}));
  ims_gray{i} = rgb2gray(ims{i});
  [h(i),w(i),~] = size(ims{i});
end

%% %%%%%%%%%%%%% for finding points %%%%%%%%%%%%%%%%

x1={};y1={};% x1, y1 for moving points (points in baseim)
x2={};y2={};% x2, y2 for fixed points (points in other imgs)
% get corresponding points between each image and the central base image
for i = 1:nimages
   if (i ~= baseim)
%      run interactive select tool to click corresponding points on base and non-base image
     [moving_out,fixed_out] = cpselect(ims{baseim},ims{i},'Wait',true);
     x2{i} = fixed_out(:,1);
     y2{i} =  fixed_out(:,2);

%      refine the user clicks using cpcorr
     movingPointsAdjusted = cpcorr(moving_out,fixed_out,ims_gray{i},ims_gray{baseim});
     x1{i} = movingPointsAdjusted(:,1);
     y1{i} = movingPointsAdjusted(:,2);
   end
end



% verify that the points are good!
% some example code to plot some points, you will need to modify
% this based on how you are storing the points etc.
%

for i = 1:nimages
    if (i ~= baseim)
        figure;
        subplot(2,1,1); 
        imagesc(ims{baseim});
        hold on;
        plot(x1{i}(1),  y1{i}(1),'r*',...
            x1{i}(2),    y1{i}(2),'b*',...
            x1{i}(3), y1{i}(3),'g*',...
            x1{i}(4), y1{i}(4),'y*');
        subplot(2,1,2);
        imshow(ims{i});
        hold on;
        plot(x2{i}(1),  y2{i}(1),'r*',...
            x2{i}(2),    y2{i}(2),'b*',...
            x2{i}(3), y2{i}(3),'g*',...
            x2{i}(4), y2{i}(4),'y*');
        
    end 
end
% 
% % at this point it is probably a good idea to save the results of all your clicking
% % out to a file so you can easily load them in again later on
% 
% 
save atrium1.mat;
% % save woodbridge.mat;

%% load points
load atrium1.mat
% load woodbridge.mat;
% load bike.mat
% estimate homography for each image
for i = 1:nimages
   if (i ~= baseim)
     H{i} = computeHomography(x1{i}, y1{i}, x2{i}, y2{i});
   else
     H{i} = eye(3); %homography for base image is just the identity matrix
   end
end

%% compute where corners of each warped image end up

for i = 1:nimages
  cx = [1;1;w(i);w(i)];  %corner coordinates based on h,w for each image
  cy = [1;h(i);1;h(i)];
  [cx_warped{i},cy_warped{i}] = applyHomography(H{i},cx,cy);
end


%% find corners of a rectangle
% that contains all the warped image corner points

xmin = min(cx_warped{1});
xmax = max(cx_warped{1});
ymin = min(cy_warped{1});
ymax = max(cy_warped{1});

for i = 2:nimages
    xmin = min(xmin, min(cx_warped{i}));
    xmax = max(xmax, max(cx_warped{i}));
    ymin = min(ymin, min(cy_warped{i}));
    ymax = max(ymax, max(cy_warped{i}));
end
% 
% %% Use H and interp2 to perform inverse-warping of the source image to align it with the base image
% 
[xx,yy] = meshgrid(xmin:xmax,ymin:ymax);  %range of meshgrid should be the containing rectangle
%%% In order to determine the color for each of these pixels, you should first 
%%% apply the inverse of each homography in order to determine their coordinates 
%%% with respect to the original source images.
for i = 1:nimages
   [target_x, target_y] = applyHomography(inv(H{i}),xx,yy);
  	R = interp2(ims{i}(:,:,1),target_x, target_y);
    G = interp2(ims{i}(:,:,2),target_x, target_y);
    B = interp2(ims{i}(:,:,3),target_x, target_y);
   J{i} = cat(3,R,G,B);
    
   mask{i} = ~isnan(J{i});  %interp2 puts NaNs outside the support of the warped image

   J{i}(isnan(J{i})) = 0;
   
%    figure;
%    imshow(J{i});
end
% 
%% blur and clip mask{i} to get an alpha map for each image
sum = 0;
for i = 1:nimages
   h = fspecial('gaussian',[3,3],0.5);
   alpha{i} = imfilter(mask{i}, h);
   sum = sum + alpha{i};
end
% % % 
% % % scale alpha maps to sum to 1 at every pixel location
% % 
for i = 1:nimages
    alpha{i} = alpha{i}./(sum + (sum==0));
end
% % 
% % % finally blend together the resulting images into the final mosaic
% % 
K = 0;
for i = 1:nimages
    K = K + J{i}.*alpha{i};
end
% % 
% % % display the result
figure(); 
imagesc(K); axis image;
% % 
% % % save the result to include in your writeup
imwrite(K, 'final/s_final.jpg');
imwrite(J{1},'final/s_1.jpg');
imwrite(J{2},'final/s_2.jpg');
imwrite(J{3},'final/s_3.jpg');
% % 
% % 
