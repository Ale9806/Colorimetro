close all; clear all; clc;
x=[ 0.016, 0.235, 0.698];

x_hsv=rgb2hsv(x)

x_yiq=rgb2ntsc(x)

x_lab=rgb2lab(x,'ColorSpace','adobe-rgb-1998','WhitePoint','d65')


%Adicionales
x_ycbcr = rgb2ycbcr(x)
x_xyz = rgb2xyz(x,'ColorSpace','adobe-rgb-1998','WhitePoint','d65')
x_hsi=convertionRgb2Hsi(x)
