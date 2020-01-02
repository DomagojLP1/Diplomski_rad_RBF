%  *********************************************************
%
% Funkcija za odredjivanje frekvencijskog spektra signala zasnovana na FFT 
%
% [frekvencija, amplituda, snaga] = ftran(signal, period snimanja)
%
%  *********************************************************

function [frekv, ampl, power]=ftran(x, period_snimanja)

X=fft(x);
aps = abs(X);
ampl = aps(1:floor(length(aps)/2))/floor(length(x)/2); 
ampl(1) = ampl(1)/2;  % DC offset
Pyy = X.*conj(X);  % aps*aps
power = Pyy(1:floor(length(aps)/2));
frekv(1:length(ampl),1)=0;
for i=0:length(ampl)-1
    frekv(i+1,1)=i/period_snimanja;
end

% komentar- veza izmedju kruzne frekvencije [rad/s] i frekvencije: w=2*pi*f


% Drugi naèin  --> diskretna FFT

if 0
    
    n = ceil(log2(length(x)));
    X = fft(x,2^n);
    
    aps = abs(X);
    ampl = aps(1:2^(n-1))/(length(x)/2);
    
    Pyy = X.*conj(X);
    power = Pyy(1:2^(n-1));
    
    fs = length(x)/period_snimanja;  % sampling_frequency
    frekv = fs*(0:2^(n-1)-1)/2^n;
    
end