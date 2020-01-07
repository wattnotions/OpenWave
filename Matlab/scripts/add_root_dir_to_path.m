%{
This script adds the 'Matlab' folder to matlabs search path
Change root dir variable to reflect the location on your PC
root dir should point to the 'matlab' folder
%}

root_dir = 'C:\Users\User1\Documents\OpenWave\Matlab';
addpath(genpath(root_dir)); %add matlab folder and all sub folders
