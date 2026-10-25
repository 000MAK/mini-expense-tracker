# Mini Expense Tracker

A local command-line expense tracker built with Python and SQLite. It records expenses and calculates totals grouped by currency code without assuming or applying foreign-exchange rates.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Stores expense entries in a local SQLite database.
- Captures a date, amount, three-letter currency code, category, and optional note.
- Rejects non-positive amounts and invalid currency-code lengths.
- Calculates totals separately for each currency.
- Runs locally; it does not connect to a bank, payment processor, or FX service.

## Requirements

- Python 3.10 or later
- No third-party package installation required

## Quick start

Show available commands:

```bash
python main.py --help
```

Add a sample expense to a local database:

```bash
python main.py add --db expenses.db --day 2026-10-25 --amount 12.50 --currency USD --category food
```

Display totals by currency:

```bash
python main.py --db expenses.db total
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Limitations and privacy

This is a minimal local record-keeping example, not accounting, tax, or financial advice. It does not verify dates against a calendar, manage budgets, reconcile transactions, or convert currencies. Keep the generated database private if it contains real financial records; use synthetic data in public demonstrations.

## Related Quantix projects

- [Mini Freelance Rate Calculator](https://github.com/000MAK/mini-freelance-rate-calculator)
- [Quantix — 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)

## License

MIT. See [LICENSE](LICENSE).
