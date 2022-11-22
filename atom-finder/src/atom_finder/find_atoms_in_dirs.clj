(ns atom-finder.find-atoms-in-dirs
  (:require
    [swiss.arrows :refer :all]
    [atom-finder.util :refer :all]
    [atom-finder.classifier :refer :all]
    [atom-finder.atoms-in-dir :refer :all])
  )

(defn -main [& args]

  (doseq [dir args]
    (-<>> dir
          atom-finder.util/expand-home
          clojure.java.io/file
          .getCanonicalPath
          (atom-finder.atoms-in-dir/atoms-in-dir <> atom-finder.classifier/atoms)
          (map prn)
          dorun))

  (shutdown-agents))

