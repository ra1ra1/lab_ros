#!/bin/sh

# values.csvを描画
gnuplot -e "
  set terminal vttek;
  set datafile separator ',';
  plot 'fvalue_with_time.csv' using 1:2 with line, 'fvalue_with_time.csv' using 1:3 with line,'fvalue_with_time.csv' using 1:4 with line;
  "
