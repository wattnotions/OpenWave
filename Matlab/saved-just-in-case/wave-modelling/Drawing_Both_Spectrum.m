clear;clc;%close all
%input data
Hs=12; %                                                                         significant wave height (m)
Tm=10*(0.327*exp(-0.315*3.3)+1.17); %                                            Peak period (s)                       Tm=Tp=T0
Tm=10*(0.327*exp(-0.315*1)+1.17); %     
Tz=10;                          %                                                zero-crossing period (s)
% Hs=59*.3048
% Tm=19
Omega=[0.01:0.01:3];
Cap=2                           %this is the maximum considered Omega
%type 1 is Jonswap and type 2  Pierson-Moskowitz
[S1,Amp1,t1]=Jonswap('Omega', Omega ,'Hs', Hs,'Tz' ,Tz, 'Type', 1, 'TEnd',3600*3/15,'Cap',Cap,'FiguringSpectrum',2);


%%
[S2,Amp2,t2]=Jonswap('Omega', Omega ,'Hs', Hs,'Tz' ,Tz, 'Type', 2, 'TEnd',3600*3/15,'Cap',Cap,'FiguringSpectrum',2);
figure
hold on 
plot(Omega,S1)
xlabel('Omega (rad/s)');ylabel('Spectrum (m^2.s)');
grid;
hold on
plot(Omega,S2)
legend( 'Jonswap',  'Pierson-Moskowitz')