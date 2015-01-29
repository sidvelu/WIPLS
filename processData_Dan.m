
dir = input('Please enter the directory: ', "s");
files = readdir(dir);
files = files(3:(2 + ((length(files)-2) / 2)));
angles_text = strrep(strrep(files, "passband_signal_", ""), ".0.bin", "");
angles_text = angles_text;
angles = str2num(char(angles_text));
for n = 1:length(angles)
  PBPATH = strcat(dir, '/passband_signal_', char(angles_text(n,:)), '.0.bin');
  PBFID = fopen(PBPATH, 'r');
  [pbsignal(n,:), pblength(n)] = fread(PBFID, Inf, "float");
  fclose(PBFID);
end
fftpb = abs(fftshift(fft(pbsignal), 1) .^ 2);
overangles = sum(fftpb(:,23500:36500), 2);
t = 10^-5 * (1:60000);