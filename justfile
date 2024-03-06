default:
    just -l

lint:
    ruff format
    taplo fmt
    ruff check
