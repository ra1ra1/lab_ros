#!/bin/sh

# values.csvを描画
gnuplot -e "
  set terminal vttek;
  plot 'values.csv' with line
  "
