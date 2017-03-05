%% Main function to generate tests
function tests = gradientTest
tests = functiontests(localfunctions);
end
% test for mygradient function
%% Test Functions
function testFunctionOne(testCase)
    Itrain = im2double(rgb2gray(imread('test2.jpg')));
    [mag,ori] = mygradient(Itrain);
    imagesc(ori)
    colorbar
    colormap jet
    title('gradient orientation')
%     figure;
%     imshow(Gdir);
%     testCase.verifyEqual(mag,Gmag);
%     testCase.verifyEqual(ori, Gdir);
end

% results = run(gradientTest)
