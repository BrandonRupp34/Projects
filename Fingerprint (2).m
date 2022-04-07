close all;
clc;

%% find the Sampling frequency and load information about each audio
info = audioinfo('Shelter.mp3');
info2 = audioinfo('Red Right Hand.mp3');
info3 = audioinfo('Pour Some Sugar On Me.mp3');
info4 = audioinfo('Good Life.mp3');

%% Read the audio files as signals
Fs1 = 44100;
y1 = audioread('Shelter.mp3');
y2 = audioread('Red Right Hand.mp3');
y3 = audioread('Pour Some Sugar On Me.mp3');
y4 = audioread('Good Life.mp3');

y5 = audioread('sample shelter.mp3');
%% Keep only the first collumn vector, then apply the wavelet decomp.
y1 = y1(:,1);
y2 = y2(:,1);
y3 = y3(:,1);
y4 = y4(:,1);

y5 = y5(:,1);

[c1,l1] = wavedec(y1,3,'haar');
w1 = detcoef(c1,l1,3);


[c2,l2] = wavedec(y2,3,'haar');
w2 = detcoef(c2,l2,3);


[c3,l3] = wavedec(y3,3,'haar');
w3 = detcoef(c3,l3,3);


[c4,l4] = wavedec(y4,3,'haar');
w4 = detcoef(c4,l4,3);


[c5,l5] = wavedec(y5,3,'haar');
wSample = detcoef(c5,l5,3);


