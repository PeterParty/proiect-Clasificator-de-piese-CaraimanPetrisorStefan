%Bibliografie : https://www.geeksforgeeks.org/software-engineering/edge-detection-using-prewitt-scharr-and-sobel-operator/
%Edge detection using Prewitt Operator 

k = imread("G:\facultate\anul 3 sem 1\Retele neuronale\proiect-Clasificator de piese\data\raw\bucse\bucsa (3).jpg" );
k = rgb2gray(k);
k1 = double(k);
x_mask = [-1 0 1; -1 0 1; -1 0 1]; %matrice 3*3
y_mask = [-1 -1 -1;
          0 0 0; 
          1 1 1];
kx = conv2(k1,x_mask,'same');
ky = conv2(k1,y_mask,'same');
ked = sqrt(kx.^2 + ky.^2);
pathToProject = "G:\facultate\anul 3 sem 1\Retele neuronale\proiect-Clasificator de piese";
pathToProcesing = pathToProject+"\processed";

%ped = outlineWithPrewittOperator("G:\facultate\anul 3 sem 1\Retele neuronale\proiect-Clasificator de piese\data\raw\bucse\bucsa (3).jpeg");
red =outlineWithPrewittOperator(pathToProject+"\data\raw\flanse\flansa (1).png");

imwrite(red,pathToProcesing+"\flansa_processed(1).png");
imsave
%imtool(k,[]);
%imageViewer(k);

%imtool(abs(kx),[]);
%imageViewer(abs(kx));

%imtool(abs(ky),[]);
%imageViewer(abs(ky));

%imtool(abs(ked),[]);
%imageViewer(abs(ked));

