#!/bin/sh

export CFLAGS='-mno-outline-atomics'

apk add --no-cache build-base python3 perl

cd /builder/build
cargo build --release

cd /builder
./collect.py $BINS $LICENSE aarch64-unknown-linux-musl ./build ./build/target/release
