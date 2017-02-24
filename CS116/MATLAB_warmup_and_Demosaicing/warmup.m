I = rgb2gray(imread('anteater.jpg')); %if the image is color
I = im2double(I); %covert to double.

% Now create an array A that contains the pixels in a 100x100 
% sub-region of your image. Write code to perform the following
% operations on this sub-image. Each of these can be written as 
% just a couple lines of code without using any for-loops.
A = I(1:100, 1:100);
imshow(A);

% a.
%Sort all the intensities in A, 
% put the result in a single 10,000-dimensional vector x. 
% Plot this sorted vector in a figure.
x = reshape(sort(A),1,10000);
figure;
plot(x);
title('a.');

% b.
% Display a figure showing a histogram of 
% A's intensities with 32 bins using the hist function.
figure;
h = histogram(A);
h.NumBins = 32;
title('b.');

% c.
% Create and display a new binary image the same size as A, 
% which is white wherever the intensity in A is greater than 
% a threshold t, and black everywhere else. Choose a value 
% for the threshold which makes the image roughly half-white 
% and half-black.
C = A;
t = 0.5;
C(C>t) = 1;
C(C<=t) = 0;
figure;
imshow(C);
title('c.');

% d.
% Generate a new image (matrix), which is the same as A, 
% but with A's mean intensity value subtracted from each pixel.
% After subtracting the mean, set any negative values to 0 
% and display the result.
m = mean(mean(A));
D = A - m; 
D(D<0) = 0;
figure;
imshow(D);
title('d');


% e.
% Let y be the vector: y = [1:6]. Use the reshape command to
% form a new matrix z whose first column is [1, 2, 3]', and whose
% second column is [4, 5, 6]'.
y = [1:6];
z = reshape(y, 3, 2);

% f.
% Use the min and find functions to set a variable x to the minimum 
% value that occurs in A, and set r to the row it occurs in and c 
% to the column that this value occurs in. If there is more than 
% one minima then return the first one.
x = min(min(A));
[r,c] = find(A==x,1);

% g.
% Let v be the vector: v = [1 8 8 2 1 3 9 8]. Using the unique 
% function, compute the total number of unique values that occur in v.
v = [1 8 8 2 1 3 9 8];
size(unique(v), 2); % total number of unique values that occur in v.

