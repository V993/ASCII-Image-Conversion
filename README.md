# ASCII-Image-Conversion                         
                                                                                                                    ,,;;**;;      
                                                                                                      ,,**oo;;  ))0000))))00      
                                                                                            ;;;;      ))$$$$;;;;**$$00**,,**;;    
                                                                      ,,                oo00$$))    ;;//0000;;  **0000;;;;;;      
                                                                      ,,,,  ;;))//oo    **$$0000;;  **0000$$**  **00$$;;  **      
                                                                    ,,    **00**))$$oo  ;;0000$$oo  ))////$$**  **0000oooo))      
                                                              **oo//**  ,,00//;;**0000  ;;00))0000;;//oo//$$**  ;;0000//////      
                                                            oo00;;oo**  oo$$)),,**0000;;;;00**00$$))00**))$$oo  ;;00$$))  oo      
                                                ;;        ;;$$**;;;;,,,,))00))  **00$$**  $$;;oo$$$$//;;))$$))  ;;//$$))**;;      
                            ,,              **////        ))00;;  ;;  ;;//$$))  **00$$**  00oo;;0000oo  ))$$))  ;;//$$))          
                        ,,//;;    ;;**))oo  **00))      ;;//00;;      ;;//$$))  **00$$**  00oo,,))$$;;;;))$$))  ;;))$$//          
      ;;oo**    ;;oo    ;;))  ;;////**;;**  **00))      **0000;;      ;;//$$))  **00$$**  $$**;;**00  ;;oo$$//  ;;))00//    ;;**  
      ;;))oo    oo//    **oo  ;;//))  ;;    **00))      **0000;;      ;;//$$))  **00$$;;  $$**;;**;;  ;;oo00//  ;;))$$00****00**  
      ;;))oo  ,,))))    oo**  **//))        oo00))      **0000;;      ;;//$$))  **0000;;  00**  ;;    ;;oo$$00;;;;))00////////;;;;
      ;;))oo  ;;))));;  ));;  **//oo  **    oo00))      **0000;;  ;;;;;;))00))  **00//    $$oo    ;;  ;;oo))oo;;************  ;;;;
      ;;))oo  **))));;,,))    **//))))oo    oo00oo      **0000,,  oo//,,oo$$//  oo$$**  ;;00))  ;;  ,,****;;;;  ;;;;;;;;;;        
      ;;))oo  oo))));;;;))    **//))**oo    oo00oo    ,,;;0000,,,,oo));;,,//$$))00))  ,,****    ,,,,,,                            
      ;;))oo  oooo//****oo    oo//oo        oo00oo    ;;;;//00;;  ))oo  **;;oo))**    ;;;;                                        
      ;;))oo;;****//**oo**    oo00**        ))00oo    oo;;;;$$//oo))    ;;**;;                                                    
      ;;))oo******//oooo      oo//;;      ,,))00**  oooo;;;;;;))oo                                                                
      ;;))oooo;;**//))))      oo//;;    ;;  ))00))oo//;;  **;;                                                                    
      ;;oo))oo  **))//oo      ))//;;  ))  ;;))))oo**                                                                              
      ;;oo))**  ;;))//**    ;;))//oo))oo  ;;;;                                                                                    
      ;;))));;  ;;))//;;    ;;oo****;;                                                                                            
        oooo    ;;****      ;;  
      
      
### Using this REPO:
The current project consists of a few python scripts which parse images and return ASCII images. 

To use, clone the repo and run the following command in the root directory:

./setup

This will install all relevant dependencies.

The only required arguments are the image and size, which will distort depending on your terminal size.

All arguments are as follows:

## ./start [image: str] [size: int] [inverted: bool] [monochrome: bool] [bump_down: int] [bump_right: int]

**Inverted** and **monochrome** are set to False by default. The program works best with subjects against a black background. Images with white backgrounds can easily be converted to a black background with the **inverted** flag.

Some subjects have little to no coloration. These subjects look far better in text with a monochrome display as the colors available now are only RGB. This can easily be done with the use of the **monochrome** flag.

**bump_down** is the argument which designates how far down the image should be pushed. This is best for phone backgrounds where the image in question needs to be stretched out. It takes an integer value which corresponds to the number of lines the image is pushed down.

**bump_right** is the argument which designates how far the image should be pushed to the right. Similar to bump_up, this is best for desktop background where the image in question needs to be stretched out, width wise. It takes an integer value which corresponds to the number of chars the image is pushed right.

### Apple Example:

./start test_images/apple.jpg 50 false true

With an adequately sized window, this should produce the following output (in color):                                                    
                                             
                                                                                    
                                                          **;;                                      
                                                          oo**                                      
                                                        oo**                                        
                                        ,,;;;;******  **//                                          
                                    ,,;;****oooooooo;;));;                                          
                                  ,,**;;**oooooo**;;oooo                                            
                                ;;****oo))))oo**;;,,))                                              
                              ;;**oo))))oo**;;,,  **;;                                              
                            ,,oooo))))**;;,,      oo                                                
                                **oo****oooo**;;**oo**oooooo**;;                                    
                              ,,oooo))))))))))oooooooo))))))))))**                                  
                            ,,))))))))))))))oo))oooooo))))))))oo))oo                                
                            oo))))))))))))))))))))oooooo))))))))oo//**                              
                          **))))oo))))))))))))))))))))))))//////))00**                              
                          oooooo))))//))))))))))))))))))))////////**                                
                        ;;))oo))))))////////))))))oooo))////////00                                  
                        **oo))))))////////))))))))))oo))))))////))                                  
                        **oo))))))////////))))oooo))oo))))))////,,                                  
                        **oooo))))))////))))))oooooooooo))))))00                                    
                        **oo**))))))//))))))oooooooooooo))))))00**                                  
                        **oooooo))))))))))oooooooooooooo))oooo//;;                                  
                        ;;oooooo))oo))oooo******oo**oooooooooo//;;                                  
                        ,,oooooooooooooooooo******oooooooooooo//))                                  
                          **oo******oooooooo******oooooooooooo))$$oo                                
                          ;;oo********oo******;;********oooo**oo0000                                
                          ,,oo********oo********;;********oooooooo//oo                              
                            ;;**;;****oo**;;;;**;;;;************oooo**                              
                              ************;;;;;;;;;;;;;;********oo**                                
                                ****;;;;****;;;;;;;;;;;;********;;                                  
                                  ;;**;;;;**;;;;;;;;;;;;;;,,,,                                      
                                    ,,;;;;,,,,,,         
                                    

### RGB Sunflowers Example:
(You'll probably want to make the font-size small for images upwards of 100 in resolution)
                                                      
./start test_images/sunflowers_bunch.webp 140

<img width="1097" alt="image" src="https://user-images.githubusercontent.com/47122021/153256653-3f57639f-60ad-4912-9b62-1bf23d5dc341.png">
 

