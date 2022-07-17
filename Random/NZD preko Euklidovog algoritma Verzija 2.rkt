#lang racket
(print " Da bismo proverili NZD za 2 broja, trebamo da pozovemo funkciju (f2) i unesemo ta 2 broja u nju")
(define (f1 a b)
  ( if ( > a b)
  (if (= ( remainder a b)0)
      b
      (f1 b ( remainder a b))
      )                
  ( if ( > b a)
  (if (= ( remainder b a)0)
      a
      (f1 a ( remainder b a))
       )
  a
  )
  )
  )
 
(define (f2 a b)
  (string-append " NZD je " (number->string(f1 a b)))
  )
