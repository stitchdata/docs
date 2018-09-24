(ns runner
  (:require [clojure.test :refer [run-tests]]
            [tap-generate-docs-test]))

(defn -main [& _]
  (let [results (run-tests 'tap-generate-docs-test)]
    (def results results)
    (if (some (comp (partial not= 0) results)
              [:fail :error])
      (System/exit 1)
      (System/exit 0))))
