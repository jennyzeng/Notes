
%
% Some sketch of how to do two-band blending for a pair of warped images.  
%
% Thise example is just for two images.  Once you get this working
% you will need to incorporate this into the code you wrote in part 1 & 2
% for blending together multiple images where you loops over all the images
%
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

% %% %%%%%%%%%%%%% for finding points %%%%%%%%%%%%%%%%
% 
% x1={};y1={};% x1, y1 for moving points (points in baseim)
% x2={};y2={};% x2, y2 for fixed points (points in other imgs)
% % get corresponding points between each image and the central base image
% for i = 1:nimages
%    if (i ~= baseim)
% %      run interactive select tool to click corresponding points on base and non-base image
%      [moving_out,fixed_out] = cpselect(ims{baseim},ims{i},'Wait',true);
%      x2{i} = fixed_out(:,1);
%      y2{i} =  fixed_out(:,2);
% 
% %      refine the user clicks using cpcorr
%      movingPointsAdjusted = cpcorr(moving_out,fixed_out,ims_gray{i},ims_gray{baseim});
%      x1{i} = movingPointsAdjusted(:,1);
%      y1{i} = movingPointsAdjusted(:,2);
%    end
% end
% 
% 
% %
% % % verify that the points are good!
% % % some example code to plot some points, you will need to modify
% % % this based on how you are storing the points etc.
% % %
% 
% for i = 1:nimages
%     if (i ~= baseim)
%         figure;
%         subplot(2,1,1); 
%         imagesc(ims{baseim});
%         hold on;
%         plot(x1{i}(1),  y1{i}(1),'r*',...
%             x1{i}(2),    y1{i}(2),'b*',...
%             x1{i}(3), y1{i}(3),'g*',...
%             x1{i}(4), y1{i}(4),'y*');
%         subplot(2,1,2);
%         imshow(ims{i});
%         hold on;
%         plot(x2{i}(1),  y2{i}(1),'r*',...
%             x2{i}(2),    y2{i}(2),'b*',...
%             x2{i}(3), y2{i}(3),'g*',...
%             x2{i}(4), y2{i}(4),'y*');
%         
%     end 
% end
% % % 
% % % % at this point it is probably a good idea to save the results of all your clicking
% % % % out to a file so you can easily load them in again later on
% % % 
% % % 
% % save atrium1.mat;
% % save woodbridge.mat;
% % save bike.mat
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
   I{i} = cat(3,R,G,B);
    % Let I1 and I2 be the warped images
    % Let M1 and M2 be the correpsonding masks
   M{i} = ~isnan(I{i});  %interp2 puts NaNs outside the support of the warped image

   I{i}(isnan(I{i})) = 0;
   
%    figure;
%    imshow(J{i});
end
% 


% % 
% % % % save the result to include in your writeup
% imwrite(K, 'final/s_final.jpg');
% imwrite(J{1},'final/s_1.jpg');
% imwrite(J{2},'final/s_2.jpg');
% imwrite(J{3},'final/s_3.jpg');
% % 
% % 



%
%% separate out frequency bands for the image and mask
%



h = fspecial('gaussian',[49,49],12);
for i=1:nimages
    % low frequency band is just blurred version of the image
    I_L{i} = imfilter(I{i},h); 
    % high frequency band is whatever is left after subtracting the low frequencies
    I_H{i} = I{i}-I_L{i};
    % low frequency alpha should be feathered version of M1 & M2
    A_L{i} = imfilter(M{i},h);

end


%% normalize the alpha masks to sum to 1 at every pixel location
% (we avoid dividing by zero by adding a term to the denominator 
% anyplace the sum is 0)
Asum = 0;
for i = 1:nimages
    Asum = Asum+ A_L{i};  
end

for i = 1:nimages

     A_L{i} = A_L{i} ./ (Asum + (Asum==0));
end
%% for high frequencies use a very sharp alpha mask which is 
% alpha=1 for which ever image has the most weight at each 
% location
for i = 1:nimages
%     A_H{i} = A_L{i};
    for j = 1:nimages
        if j ~= i
            A_H{i} = A_L{i}>A_L{j};
        end
    end
    A_H{i} = double(A_H{i});
end
%% normalize the alpha masks to sum to 1 
% technically we shouldn't have to do this the way we've constructed
% A1_H and A2_H above, but just to be safe.
Asum = 0;
for i = 1:nimages
    Asum = Asum+ A_H{i};
end

for i = 1:nimages
    A_H{i} = A_H{i} ./ (Asum + (Asum==0));
    figure();
    imshow(A_H{i});
end

%
%% now combine the results using alpha blending
%

J_L = 0; J_H = 0;
for i = 1:nimages
    J_L = J_L + A_L{i} .* I_L{i}; % low frequency band blend result
    J_H = J_H + A_H{i} .* I_H{i};  % high frequency band blend result
end
J = J_L + J_H; % combined bands

fig = figure();
subplot(1,3,1);imshow(J_L);  title('low frequency band');
subplot(1,3,2);imshow(J_H); title('high frequency band');
subplot(1,3,3);imshow(J); title('combined');
imwrite(J,'2-band-atrium.JPG');
% cpselect(ims{J},ims{i},'Wait',true);
%
% % display some of the intermediate results 
% %
% figure();
% counter = 1;

% figure();
% subplot(nimages,3,counter); imshow(J_L);  title('low frequency band');
% counter= counter+1;
% subplot(nimages,3,counter); imshow(J_H); title('high frequency band');
% counter= counter+1;
% subplot(nimages,3,counter); imshow(J); title('combined');
% figure(1);
% subplot(3,3,1); imshow(I1_L); 
% subplot(3,3,2); imshow(I2_L);
% subplot(3,3,3); imshow(J_L);  title('low frequency band');
% 
% subplot(3,3,4); imshow(I1_H);
% subplot(3,3,5); imshow(I2_H);
% subplot(3,3,6); imshow(J_H); title('high frequency band');
% 
% subplot(3,3,4); imshow(I1);
% subplot(3,3,5); imshow(I2);
% subplot(3,3,6); imshow(J); title('combined');


