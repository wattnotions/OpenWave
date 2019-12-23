clear;clc;%close all
%%
%%input data
Hs=12; %                                                                         significant wave height (m)
%Tm=10*(0.327*exp(-0.315*3.3)+1.17); %                                            Peak period (s)                       Tm=Tp=T0
Tz=10;                          %                                                zero-crossing period (s)
Omega=[0.01:0.01:3];
Cap=2                           %this is the maximum considered Omega
TEnd=90;

%type 1 is Jonswap and type 2 is Pierson-Moskowitz
[S,Amp,t]=Jonswap('Omega', Omega ,'Hs', Hs,'Tz' ,Tz, 'Type', 1, 'TEnd',TEnd,'Cap',Cap,'FiguringSpectrum',2);
%%
%Generating signal using first method
OmegaGap = Omega(2)-Omega(1); 
rng(1)                                         % setting seed number
PhaseDiff=2*pi*rand(1,length(Omega)) ;         % random phase, no phase difference
Signal1=sum(Amp' .* cos(Omega'.*t+PhaseDiff'));
%Generating signal using Second method
rng(1)   
Cn=randn(1,length(Omega));
Dn=randn(1,length(Omega));
AmpA=(S.*OmegaGap).^.5.*Cn;
AmpB=(S.*OmegaGap).^.5.*Dn;
Signal2=sum(AmpA' .* cos(Omega'.*t)  +   AmpB' .* sin(Omega'.*t));
%%
figure
YRange=max(max(abs(Signal1)),max(abs(Signal2)));
subplot(4,1,1)
hold on 
plot(Omega,S)
xlabel('Omega (rad/s)');ylabel('Spectrum (m^2.s)');
xlim([0, Cap])
grid;

subplot(4,1,2)
plot(Omega,Amp)
xlabel('Omega (rad/s)');ylabel('Amplitude (m)');
xlim([0, Cap])
grid;

subplot(4,1,3)
plot(t,Signal1)
xlabel('time (s)');ylabel('Magnitude (m)');
title('sum(Amp.* cos(Omega.*t+PhaseDiff)')
grid;
ylim(1.2*[-YRange,YRange])

subplot(4,1,4)
plot(t,Signal2)
xlabel('time (s)');ylabel('Magnitude (m)');
title('Signal2=sum(AmpA .* cos(Omega.*t)+AmpB .* sin(Omega.*t)')
ylim(1.2*[-YRange,YRange])
grid;