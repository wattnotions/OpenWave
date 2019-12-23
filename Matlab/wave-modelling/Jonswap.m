function [S,Amp,t]=Jonswap(varargin )
% Create Jonswap/Pierson-Moskowitz spectrum and a wave based on that
% Sayyed Mohsen Vazirizade
% The University of Arizona
% smvazirizade@email.arizona.edu

%%
   p = inputParser;
%Required   
   addParameter(p,'Omega',@isrow); 
   addParameter(p,'Hs',@isnumeric);% significant wave height
   addParameter(p,'Tm',0);         % Peak period (s)
   addParameter(p,'Tz',0);
%Optional
   addParameter(p,'Type',1); %type 1 is Jonswapis and type 2  Pierson-Moskowitz
   addParameter(p,'Cap',2); %Getting rid of the end of the spectrum 
   addParameter(p,'TEnd',3600*3/15);  % The duration of a the signal
   addParameter(p,'FiguringSpectrum',1);  % if this one is set to 1, nothing happens, if 2 it will draw the spectrum
   
   parse(p,varargin{:});   
   Omega=p.Results.Omega;
   Hs=p.Results.Hs;
   Tm=p.Results.Tm;
   Tz=p.Results.Tz;
   Type=p.Results.Type;   
   TEnd=p.Results.TEnd;  
   Cap=p.Results.Cap; 
   FiguringSpectrum=p.Results.FiguringSpectrum;
   
%Default Value
g=9.806;     %Gravitational acceleration  m/s^2
%g=32.74    %Gravitational acceleration  ft/s^2
if Type==1
 disp('JONSWAP Method')
 Gamma=3.3;   %peakedness parameter    for Pierson-Moskowitz Gamma=1
elseif Type==2
 disp('Cautrion: Pierson-Moskowitz')
 Gamma=1;
end
if Tz~=0    %there are two methods for converting Tz to Tm
       Tm= Tz*(0.327*exp(-0.315*Gamma)+1.17);
       %Tm= Tz*((11+gamma)./(5+Gamma)).^.5
       disp('Caution! You are Using Tz')
end
Beta=5/4;
SigmaA=0.07;  %spectral width parameter
SigmaB=0.09;  %spectral width parameter
format short
%%
OmegaGap = Omega(2)-Omega(1); 
%----- Jonswap spectrum ------
Omegam    = 2*pi/Tm;
sigma = (Omega<=Omegam)*SigmaA+(Omega>Omegam)*SigmaB;
A     = exp(-((Omega/Omegam-1)./(sigma*sqrt(2))).^2);  
alphabar = 5.058*(1-.287*log(Gamma))*(Hs/Tm^2)^2  ;                                     %modified Phillips constant
alpha=0.0081;
fprintf('alphabar= %d, alpha= %d \n',alphabar,alpha)
S     = alphabar*g^2 .* Omega.^-5 .* exp(-(Beta*(Omega/Omegam).^-4)) .* Gamma.^A;      %spectra m^2.s
S(Omega>Cap)=0;
Amp   = (2*S.*OmegaGap).^.5    ;                                                    % Amplitude m
t = linspace(0,TEnd,length(Omega));
%%
if FiguringSpectrum==2
figure
    plot(Omega,S)
ylabel('Spectrum (m/s')
xlabel('Omega (rad/s)');ylabel('Spectrum (m^2.s)');
grid;
if Type==1
 ti1=('JONSWAP Spectrum, ');
elseif Type==2
 ti1=('Pierson-Moskowitz Spectrum, ');
end
if Tz==0    %there are two methods for converting Tz to Tm
    ti2=sprintf('Tm=%d, ', Tm);   
    Tm= Tz*(0.327*exp(-0.315*Gamma)+1.17);
       %Tm= Tz*((11+gamma)./(5+Gamma)).^.5
       disp('Caution! You are Using Tz')
else
   ti2=sprintf('Tz=%d, ', Tz); 
end
ti3 = sprintf('Hs=%d', Hs);
title([ti1,ti2,ti3]);
end

fprintf('The default values: \n g=%d \n Gamma=%d \n Beta=%d \n SigmaA=%d \n SigmaB=%d \n TEnd=%d, \n Cap=%d \n', g, Gamma, Beta, SigmaA, SigmaB, TEnd, Cap )
