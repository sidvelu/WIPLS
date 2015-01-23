%dir = '/home/daniel/WIPLS/rlib_step_tlibcl/' %for first test
%angles_text = ['100'; '104'; '107'; '109'; '112'; '115'; '119'; '120'; '123'; '128'; '131'; '134'; '137'; '140'; '143'; '147'; '148'; '154'; '157'; '164'; '167'; '171'; '179'; '188'; '199'; '212'; '225'; '243'; '262'; '263'; '283'; '299']; %for first test
%angles = [100 104 107 109 112 115 119 120 123 128 131 134 137 140 143 147 148 154 157 164 167 171 179 188 199 212 225 243 262 263 283 299]; %for first test

dir = '/home/daniel/WIPLS/rlib_step_tportal/' %for second test
angles_text = ['0'; '5'; '12'; '16'; '19'; '23'; '24'; '26'; '31'; '37'; '41'; '47'; '53'; '59'; '64'; '69'; '74'; '79'; '83'; '89'; '283'; '284'; '285'; '286'; '287'; '291'; '303'; '307'; '315'; '325'; '331'; '336'; '339'; '340'; '345'; '347'; '351'; '359']; %for second test
angles = [0 5 12 16 19 23 24 26 31 37 41 47 53 59 64 69 74 79 83 89 283 284 285 286 287 291 303 307 315 325 331 336 339 340 345 347 351 359]; %for second test

for n = 1:length(angles)
  PBPATH = strcat(dir, 'passband_signal_', angles_text(n,:), '.0.bin');
  PBFID = fopen(PBPATH, 'r');
  [pbsignal(n,:), pblength(n)] = fread(PBFID, Inf, "float");
  fclose(PBFID);
end
fftpb = abs(fftshift(fft(pbsignal), 1) .^ 2);
overangles = sum(fftpb(:,23500:36500), 2);
t = 10^-5 * (1:60000);