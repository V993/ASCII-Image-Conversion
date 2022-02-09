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

./start [image: str] [size: int] [inverted: bool] [monochrome: bool] [bump: int]

**Inverted** and **monochrome** are set to False by default. The program works best with subjects against a black background. Images with white backgrounds can easily be converted to a black background with the **inverted** flag.

Some subjects have little to no coloration. These subjects look far better in text with a monochrome display as the colors available now are only RGB. This can easily be done with the use of the **monochrome** flag.

**Bump** is the argument which designates how far down the image should be pushed. This is best for phone backgrounds where the image in question needs to be stretched out. It takes an integer value which corresponds to the number of lines the image is pushed down.

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
                                    

### Monochrome Sunflowers Example:
                                
                                
./start test_images/sunflowers_bunch.webp 60 false true

                  ;;;;                                                                                                  
              ;;**))oo;;                                                                                                
          ,,**oo))oo))**                                                    **;;  ;;                                    
            oooooo))oo,,          ;;      ;;                          ;;;;oo))))oooo                          ;;        
            oooooo**;;;;      ****oo**;;,,  ,,                      ;;oo))))oooooooo;;                          ;;      
            oooooo**;;,,      oo))oooooooo****                    ****oooooooooooo));;                                  
            oo))oo**;;**,,  ;;))oooooooooo)),,                    **oooooo****oooo;;                                    
            **oo;;      **  ;;))oo**oooooooooo;;                  **oooooo**oooo;;        ;;,,,,,,                      
              ;;        ;;,,  oooooooooooo))))oo                  oooooooooooo**;;      ;;;;;;**;;                      
            ;;;;;;;;;;    ;;  **oo))****oooo))oo                  oooooooooo**;;**;;    ;;;;**;;                        
            ;;**;;;;;;;;  ;;;;;;**oooo;;**oo))**                  **))))))**;;;;,,;;;;  ,,;;;;                          
              ;;**;;;;,,  ;;  ;;;;oo))oo**oooo));;                ,,;;****          ;;;;                                
                ;;;;,,  ,,;;,,;;;;**oooooooooo));;                              ;;;;,,;;                                
                        ;;****,,,,;;;;oooooo))**                          ,,;;;;;;;;;;;;                                
                        **;;        ,,oooooo));;                ;;**;;****;;**;;**;;,,;;;;      ,,                      
                      ;;;;  ,,;;;;    ;;oooooo**              **oo))oo))))oooo;;;;,,  ,,;;    ;;;;;;                    
        ,,;;;;        ;;  ,,;;;;;;;;                      ,,**))oooooooooooo))oo        ;;    ;;;;oo**,,                
      ,,;;;;;;;;    ;;;;    ;;;;;;;;,,                    ;;))))oooooooooooooo));;      ;;    ;;))oo))**                
    ;;;;;;;;;;;;    ;;,,    ;;****;;**,,                ;;;;oooooooo****oooooooo)),,  ;;      oo))oooo))**              
    ;;********    ,,;;          ;;;;;;                  **))oooooooooooooooooooo))**  ;;      oooo**oooooo;;            
        **;;        ;;                                  **))oooooooo****oooo))oo))**;;,,  ,,;;**))oooooooo**            
          ,,      ,,******;;**;;,,                      **))oooooooo;;;;oooooo))))));;      ;;**oo****oooo;;            
              oo**oooo))oo))**;;;;                      **))oooo**oo**oooooooooooooo;;,,;;**;;**))****oo))**            
              **oooooooooooo**;;;;;;,,                  ,,oooooooo**oooo**oooooooo**;;;;  ,,;;**oooooooooo;;            
            oooooooooooooo))oo**;;;;;;                  ;;oooooooooooooooooooo))oo;;;;,,      ;;oooooo))**              
          oooo))oooooooooo))**                        ;;;;**oo))oooooo))))oooooo))oo;;;;;;    **))oooo))**              
          **))oooo****))oooo                          ,,******oo))oooooooooooooooo))**;;;;    ;;))))oo;;                
          oo))oo**;;oooo**;;                              ,,;;****oo))oooooooooooooooo;;**;;    ,,oo;;                  
        **))oooo**oo))oo;;;;;;                              ;;;;;;**oooooo****oooooooo                                  
        **))oooooooooo;;;;;;    ;;;;;;,,                    ;;**;;;;oooooooo**oooooooo,,                                
          **oooooo**;;**;;      ;;;;;;;;,,                  ,,,,    oooooooooooooo))**                                  
          oo))oo))**,,,,**      ;;;;;;;;**;;                        **oooooooooooooo;;                                  
          **oooooo      **;;    ,,;;;;;;,,                          ;;**))oooooooo****                                  
              ;;;;;;      **                                      ,,****;;,,;;      ,,                                  
            ;;;;;;;;,,    **                                        ,,                                                  
          ;;**;;;;;;,,    ;;                                                                                            
        ,,********;;    ,,**                                                          ,,                                
              ,,          **        ;;;;  ;;                                          **,,                    ;;        
                      ,,;;**;;,,;;;;**;;    ;;                                      ,,**;;;;                    ;;      
                ;;,,oo))oooooo))**;;**;;                          **;;;;**;;**      ,,**;;;;;;            ,,            
        ;;;;;;oo))))oo))oo))oooooooooo                        ;;**oo))oooo))**,,      **;;;;;;          ;;;;            
        ;;****oo))oooooooooooooo))))oo                        ;;))oooooooooooooo;;    ;;;;;;;;        ;;**;;            
          ;;oo))))))oooooooooooooo))oooo**;;;;                ;;oooooooooooo))oo));;      ,,          **;;;;            
          **oooooooooooooooooooooooo))**;;****                ;;))oo**oo****oooo));;                ,,**;;;;,,          
          oo))oooooooo********oooooooooooooo                    oooooo))**;;**oooo))**                ;;;;;;,,          
        **))oooooooo**oooooooo**oooo))oo))**                      **oooooo****oooo))oo;;;;;;;;        ,,;;;;            
        ,,oooooooo**oooo****oooo**oooooo))oo,,          ;;;;    ,,;;;;**oo))oooooo));;    ,,;;**;;,,                    
        oo))oooooo**oo**;;;;**oo**oooooooo**;;        ,,**;;    ,,,,;;;;**oooooooo));;          ,,**,,                  
        **))oooooo**oooo******oo**oooooooo****;;      ;;;;;;,,      **;;;;;;**))oo))oo      ,,;;,,,,**,,                
      ;;**oooooooooo**oooooooo**oooooooooo**;;,,      **;;;;;;    ,,;;,,      oooo**        **;;;;,,,,**;;    ,,;;      
          oo))oooooo****oooo****oooooo))**            ;;;;;;;;    **;;,,;;;;              ;;**;;;;,,  ;;;;;;**oooo      
          **))oooooooooo****oooooooooooooo;;          ,,;;;;,,  ****;;;;;;;;**;;  ,,,,****;;;;;;;;    ;;;;**))oooo      
            ;;))))oooooooooooooooooo))oo;;;;;;;;            ;;**,,  ,,;;;;    **;;;;**))))oo**;;    ,,**oooooooo**      
            **oooooooooooooooooooo))oo**;;;;****;;******;;;;;;    ,,;;;;;;;;  ,,;;**oooooo**;;,,    oooooooooo));;      
        ;;****;;**oooo))oooo))))oooo,,  ******;;    ,,              **;;;;;;;;**oooooooo)),,        oo))))oo))**        
          oo**;;;;,,**;;))oooooo**      ,,**;;**,,                  ;;****;;  oo))oooo))oo          ;;******;;          
          **,,          oo****;;                                      ,,;;****))oooooooo;;                              
                            **                                                ;;;;;;;;    
