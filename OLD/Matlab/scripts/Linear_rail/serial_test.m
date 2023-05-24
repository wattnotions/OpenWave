if ~isempty(instrfind)
     fclose(instrfind);
     delete(instrfind);
end
delete(s)
s = serialport("COM11",115200);

writeline(s,"TEST")
s.NumBytesAvailable



while 1
    
    write(s,"r","uint8")
        
    
    
    pause(1)
    
end
        
    