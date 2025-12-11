function imageOutline = outlineWithPrewittOperator(pathImg)
    p = imread(pathImg);
    p = rgb2gray(p);
    p1 = double(p);
    Xmask = [-1 0 1 ; 
              -1 0 1;
              -1 0 1];
    Ymask = [-1 -1 -1;
              0 0 0;
              1 1 1];
    
    kx= conv2(p1, Xmask, 'same');
    ky= conv2(p1, Ymask, 'same');
    
    
    imageOutline =sqrt(kx.^2 + ky.^2);
    
    imageViewer(p);
    %imageViewer(kx);
    %imageViewer(ky);
    %imageViewer(imageOutline);
    imageViewer(abs(imageOutline));
    %saveas(imageOutline,"G:\facultate\anul 3 sem 1\Retele neuronale\proiect-Clasificator de piese\data\processed\ceva.png");
   
    %ked  =pathImg * 3; testare functie 
end
