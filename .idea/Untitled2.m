clear
clc
% MATLAB 批量将灰度图变为三通道的灰度图
% Author：kailugaji https://www.cnblogs.com/kailugaji/
% 数据来源：https://www.cnblogs.com/kailugaji/p/11801649.html
N=128;
for i=1:N
    I=imread(['C:\\Users\\lc\\pic\\v_2\\urban\\s1\\ROIs1970_fall_s2_8_p1', int2str(i), '.png']);
    original(i, 1:2)=size(I);
    I3(:, :, 1)=I;
    I3(:, :, 2)=I;
    I3(:, :, 3)=I;
    imshow(I3);
    imwrite(I3, ['.\results\', int2str(i), '.bmp']);
    new(i, 1:3)=size(I3);
end
 
% 举个例子，看看结果
j=1;
B=imread(['C:\\Users\\lc\\pic\\result', int2str(j), '.png']);