import tempfile,unittest
from pathlib import Path
from main import add_expense,totals
class ExpenseTests(unittest.TestCase):
    def test_totals_are_grouped_by_currency(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/"e.db"; add_expense(db,"2026-10-25",10,"USD","food"); add_expense(db,"2026-10-25",5,"USD","bus"); add_expense(db,"2026-10-25",4,"TRY","food")
            self.assertEqual(totals(db),{"TRY":4.0,"USD":15.0})
    def test_invalid_currency(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): add_expense(Path(d)/"e.db","2026-10-25",2,"US D","food")
if __name__=="__main__": unittest.main()
