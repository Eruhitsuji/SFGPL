#!/bin/bash

#https://github.com/frozenbonito/docker-pandoc-eisvogel-ja
#https://qiita.com/frozenbonito/items/10a38c5fd4ba97a9bef0

md_path_name=($1)
img_dir=${2:-$(pwd)}
out_dir=${3:-"./"}
tmp_dir=${4:-".tmp"}
filter_path_name=${5:-"img_filter.sh"}

c_dir=$(pwd)

base_path_name=$(basename $md_path_name)

mkdir -p $tmp_dir
cp $md_path_name.md $tmp_dir
cp -r $img_dir/. $tmp_dir
cp $filter_path_name $tmp_dir
cd $tmp_dir

docker run --rm -v $(pwd):/data frozenbonito/pandoc-eisvogel-ja:plantuml \
    --listings \
    --filter=$filter_path_name \
    -N \
    --toc \
    -V linkcolor=blue \
    -V table-use-row-colors=true \
    -V titlepage=true \
    -V toc-own-page=true \
    -o $base_path_name.pdf \
    $base_path_name.md \

cp $base_path_name.pdf $c_dir/$out_dir

cd $c_dir
rm -rf $tmp_dir
