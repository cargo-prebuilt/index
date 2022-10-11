#!/bin/sh

cd /builder/build
cargo build --release

cd /builder
./collect.py $BINS $LICENSE aarch64-unknown-linux-gnu ./build ./build/target/release
