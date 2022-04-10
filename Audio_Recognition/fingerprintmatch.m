%Perform cross correlation between each song and the sample
xw1 = xcorr(w1,wSample);
xw2 = xcorr(w2,wSample);
xw3 = xcorr(w3,wSample);
xw4 = xcorr(w4,wSample);
%Find the maximum of each cross correlation and make them a percent of the
%total
max1 = (max(abs(xw1)));
max2 = (max(abs(xw2)));
max3 = (max(abs(xw3)));
max4 = (max(abs(xw4)));
total = max1+max2+max3+max4;
%Display the results
disp(strcat("Shelter [",string((max1/total)*100),"%]"));
disp(strcat("Red Right Hand [",string((max2/total)*100),"%]"));
disp(strcat("Pour Some Sugar On Me [",string((max3/total)*100),"%]"));
disp(strcat("Good Life [",string((max4/total)*100),"%]"));




