Jenny Zeng
52082740
zhaohuaz@uci.edu
# 1. gradient code
![mag result](result_mag.jpg)
![ori result](result_ori.jpg)

# 2. test detect code
## input1:
![input](inputimg.jpg)
![temp](temp.jpg)
### result:
![result_1](result1.jpg)
![result_2](result_2.jpg)
![result_3](result3.jpg)
![result_4](result4.jpg)
![result_5](result5.jpg)

## input2:
![input2](inputimg2.jpg)
![temp2](temp2.jpg)
### result:
![result_cat2.jpg](result_cat2.jpg)
![result_cat3.jpg](result_cat3.jpg)
![result_cat4.jpg](result_cat4.jpg)

# 3. Discussion:
Just as what we discussed in the class, since an elephant can be rotated and the body shape may be different, it is hard to detect if the angle changes.
Also, because we get black and white images, we lost information in colors.

To get a better result, we can:
1. Use part Model: use a template to detect each part. 
2. use more images as input images and extract their features as average. (More samples for training)
