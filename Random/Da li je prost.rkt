#lang racket
(print " Da bismo dobili odgovor na pitanje da li je prost broj trebamo da pozovemo funkciju
 (f2) i unesemo taj isti broj u nju")

(define ( f1 y z)
  (if ( < z 1)
      (- 1) 
      ( if (=(remainder y z)0)
      ( + z ( f1 y ( - z 1)))
      (f1 y ( - z 1))
       )         
  )         
 )    
  
           
( define ( f2 x)      
  ( if (or ( = x ( f1 x x))(= x 1))
       (print "Prost je")
       (print "Nije prost")
       )
   )
  
