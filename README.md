# Mini Expense Tracker

A local SQLite CLI to record expenses and total them by currency. It does not make FX assumptions.

## Requirements

- Python 3.10+
- Standard library only; no `pip install` step required.

## Run

```bash
python main.py --help
```

## Example

`python main.py add --db expenses.db --day 2026-10-25 --amount 12.50 --currency USD --category food` then `python main.py --db expenses.db total`

## Tests

```bash
python -m unittest discover -s tests -v
```

## Safety notes

Use copies of important files. Review output before using it in production. Do not add credentials, private data, or real customer files to Git.

## License

MIT. See [LICENSE](LICENSE).
