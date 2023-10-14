#!/bin/bash

set -euxo pipefail

rustup update

exec cargo +stable "$@"
