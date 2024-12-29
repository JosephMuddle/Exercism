#lang racket
(require )
(provide acronym)

(define (acronym string)
  (define tokens (string-split (string-upcase string) #rx"[ -]"))
  (apply string-append (map (lambda (in-str)
                              (define in-str-two (string-replace in-str #rx"[^a-zA-Z]" ""))
                              (substring in-str-two 0 1))
                            (filter (lambda (in-str) (> (string-length in-str) 0)) tokens))
  ))
