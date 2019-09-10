;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)

(define (unique s)
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (cons (car s) (filter(
      lambda(x)(
        not (
          eq? x (
            car s
            )
          )
        )
      )(
      unique(cdr s)
      )
      )
    )
    )
)

(define (cons-all first rests)
  (map(lambda (lsts) (cons first lsts))
    rests
)
  )

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  'YOUR-CODE-HERE
  (if (null? denoms)
    nil
    (if (= total 0)
      '(())
      (if (< total (car denoms))
        (list-change total (cdr denoms))
        (append
          (cons-all (car denoms)(list-change(- total(car denoms))denoms))(list-change total(cdr denoms))
          )
        )
      )
    )
  )

; Tail recursion

(define (replicate x n)
  (define(help_rep lst n) (
    if (= n 0) lst (
      help_rep(
        append lst (list x)
        )
      (- n 1)
      )
    )
  )
  (help_rep (list) n)
  )

(define (accumulate combiner start n term)
  (if (= n 0) start
    (combiner (accumulate combiner start (- n 1) term)
      (term n)
      )
    )
)

(define (accumulate-tail combiner start n term)
    (if (= n 0)
      start
      (accumulate-tail combiner (combiner (term n) start)(- n 1) term)
      )
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)

)