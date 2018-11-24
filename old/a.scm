(define (fac n) (if (= n 1) 1 (* n (fac (- n 1)))))
(display "hell world\n")
(display (fac 10))
(display "\n")

(display (map fac '(2 3 4 5)))
