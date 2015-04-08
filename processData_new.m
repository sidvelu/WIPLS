
arg_list = argv()
filename = arg_list{1}
dir = filename;
%dir = input('Please enter the directory: ', "s");
files = readdir(dir);
files = files(3:length(files));
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
overangles = sum(fftpb(:,13500:16500), 2);
t = 10^-5 * (1:60000);


A = [angles';overangles'];

[M,I] = max(overangles)
maxAngle = angles(I)

fileID = fopen('/root/angle.txt', 'w');
fprintf(fileID, '%f', maxAngle)
%fprintf(fileID, '%6s %12s \n', 'Angles', 'Magnitude');
%fprintf(fileID, '%f   %f\n', A);
