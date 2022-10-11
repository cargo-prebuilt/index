#!/bin/sh

export CFLAGS='-mno-outline-atomics'

apk add --no-cache build-base perl openssl-dev

cd /builder/build
cargo build --release
