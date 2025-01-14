;sbcl --script main.lisp
(load "~/quicklisp/setup.lisp")
(ql:quickload "split-sequence")

(defun is-decreasing (numbers)
  (loop for i from 1 below (length numbers)
        always (let ((prev (nth (1- i) numbers))
                     (curr (nth i numbers)))
                 (and (< curr prev)
                      (>= (abs (- curr prev)) 1)
                      (<= (abs (- curr prev)) 3)))))

(defun is-increasing (numbers)
  (loop for i from 1 below (length numbers)
        always (let ((prev (nth (1- i) numbers))
                     (curr (nth i numbers)))
                 (and (> curr prev)
                      (>= (abs (- curr prev)) 1)
                      (<= (abs (- curr prev)) 3)))))

(defun cherry-pick (numbers)
    (loop for i from 0 below (length numbers)
        thereis (let ((modified-numbers
            (append (subseq numbers 0 i)
                    (subseq numbers (1+ i)))))
                  (or (is-increasing modified-numbers)
                      (is-decreasing modified-numbers))))) 

(defun process-file (file-path)
  (let ((total 0))
    (with-open-file (in file-path)
      (loop for line = (read-line in nil)
            while line do
            (let* ((numbers (mapcar #'parse-integer (split-sequence:split-sequence #\Space line))))
              (when (or (is-increasing numbers)
                        (is-decreasing numbers)
                        (cherry-pick numbers))
                (incf total))))
    (format t "ANSWERs: ~A~%" total)))
)

;(process-file "in/in.test")
(process-file "in/in.pub")
