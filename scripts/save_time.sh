#!/bin/sh

# values.csvを描画
gnuplot -e "
  set terminal png;
  set output 'graph.png';
  set datafile separator ',';
  plot 'fvalue_with_time.csv' with line
  "
