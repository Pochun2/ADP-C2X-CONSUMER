import unittest
from consumer_example.event_counter import count_events

class SeedBaselineTests(unittest.TestCase):
    def test_api_exists_but_is_not_a_completed_model_task(self):
        with self.assertRaisesRegex(NotImplementedError, 'OWNER_GRANT_REQUIRED'):
            count_events([{'type': 'A'}])

    def test_no_account_or_order_in_fixture(self):
        self.assertFalse(hasattr(count_events, 'submit_order'))

if __name__ == '__main__':
    unittest.main()
