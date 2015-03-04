from os import listdir

dir = raw_input("Please enter the directory: ")
files = listdir(dir)
files = files[2:files.length()]
angles_text = str.replace(str.replace(files, "passband_signal_", ""), ".0.bin", "")
angles = float(angles_text)
'''for n = 1:length(angles)
  PBPATH = strcat(dir, '/passband_signal_', char(angles_text(n,:)), '.0.bin');
  PBFID = fopen(PBPATH, 'r');
  [pbsignal(n,:), pblength(n)] = fread(PBFID, Inf, "float");
  fclose(PBFID);
end
fftpb = abs(fftshift(fft(pbsignal), 1) .^ 2);
overangles = sum(fftpb(:,13500:16500), 2);
t = 10^-5 * (1:60000);'''