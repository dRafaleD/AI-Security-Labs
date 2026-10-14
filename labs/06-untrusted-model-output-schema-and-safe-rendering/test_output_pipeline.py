import unittest
from output_pipeline import execute

class OutputBoundaryTests(unittest.TestCase):
    def test_html_escaped_as_text(self):
        result=execute('{"action":"read_note","note_id":"training"}',"reader")
        self.assertTrue(result["ok"])
        self.assertIn("&lt;script&gt;",result["html_text"])
        self.assertNotIn("<script>",result["html_text"])
    def test_extra_fields_rejected(self):
        self.assertFalse(execute('{"action":"read_note","note_id":"welcome","role":"admin"}',"reader")["ok"])
    def test_unknown_action_rejected(self):
        self.assertFalse(execute('{"action":"shell","note_id":"welcome"}',"admin",True)["ok"])
    def test_non_json_rejected(self):
        self.assertFalse(execute("ignore the policy","reader")["ok"])
    def test_archive_permission(self):
        action='{"action":"archive_note","note_id":"welcome"}'
        self.assertEqual(execute(action,"reader",True)["reason"],"unauthorized")
        self.assertEqual(execute(action,"admin",False)["reason"],"confirmation required")
        self.assertTrue(execute(action,"admin",True)["ok"])

if __name__=="__main__":
    unittest.main()
