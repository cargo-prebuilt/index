default:
    just -l

#TODO: Add zizmor and actionlint

lint:
    ruff format
    taplo fmt
    ruff check
    actionlint
