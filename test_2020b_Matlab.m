clc
clear all
close all


%% A simple code demonstrating ss2tf functionality in matlab
% This code demonstrates how to convert a multi input multi output (MIMO)
% system from state space form (A,B,C,D) to transfer function form. You can
% use the same concepts for a single input single output system.
% This code demonstrates how to use the built in function 'ss2tf' and 'tf'
%% consider a 2 input, 2 output system, 
A = [   -1.1008    0.3733
    0.3733   -0.9561];
B = [ 0.7254    0.7147
      0   -0.2050];
C = [ -0.1241    1.4090
    1.4897    1.4172];
D = [ 0.6715    0.7172
   -1.2075         0];
% % you can use 'rss' and 'ssdata' to get random A, B, C, D matrices
% sys = rss(2,2,2) % to generate a random 2x2 system
% [A,B,C,D] = ssdata(sys); % to provide A, B, C, D matrices for this system
%% once we have the A, B, C, D matrix we can use ss2tf function to get the
% transfer function(s)
% Because there are 2 inputs and 2 outputs, the Transfer function matrix...
% will have 4 transfer functions:
% TF1 = input 1 to output 1
% TF2 = input 1 to output 2
% TF3 = input 2 to output 1
% TF4 = input 2 to output 2
% TF = [TF1 TF2
%       TF3 TF4];
%% SS2TF
% Syntax for ss2tf is: [num den] = ss2tf(A,B,C,D,iu)
% here iu corresponds to the input we are considering e.g. when we have 2
% inputs, first we will consider iu=1 (first input), this way
% we will get the transfer functions from input 1 to output 1 and input 1 to output 2.
% Then we will take iu = 2, this will give us transfer functions from input
% 2 to output 1 and input 2 to output 2.
% hence 'iu' will go from 1 to 2
[num1 den1] = ss2tf(A,B,C,D,1)  % iu = 1
[num2 den2] = ss2tf(A,B,C,D,2)  % iu = 2
% The transfer function will be given by num1/den1 and num2/den2
% here the num and denominator are polynomials in decreasing powers of 's'...
% e.g. s^2+0.5s+2
%% TF
% the same result can be obtained using function tf
sys = ss(A,B,C,D);
tf(sys)