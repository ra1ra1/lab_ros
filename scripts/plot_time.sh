#!/bin/sh

# values.csvを描画
gnuplot -e "
  set terminal vttek;
  set datafile separator ',';
  plot 'fvalue_with_time.csv' with line
  "
