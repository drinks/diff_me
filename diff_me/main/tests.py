from django.test import TestCase
from diff_me.main import models
import difflib

class DiffTest(TestCase):
    def test_differ(self):
    '''
    Ensure that diffs work correctly
    '''
    differ = difflib.HtmlDiff(tabsize=4)
    
    fromlines = ['The quick brown fox jumed over', 'the lazy dog.']
    tolines = ['The quack brown fox jumed over', 'the lazy dog.']
    table = differ.make_table(fromlines ,tolines)
    control = '\n    <table class="diff" id="difflib_chg_to0__top"\n           cellspacing="0" cellpadding="0" rules="groups" >\n        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>\n        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>\n        \n        <tbody>\n            <tr><td class="diff_next" id="difflib_chg_to0__0"><a href="#difflib_chg_to0__top">t</a></td><td class="diff_header" id="from0_1">1</td><td nowrap="nowrap">The&nbsp;qu<span class="diff_chg">i</span>ck&nbsp;brown&nbsp;fox&nbsp;jumped&nbsp;over</td><td class="diff_next"><a href="#difflib_chg_to0__top">t</a></td><td class="diff_header" id="to0_1">1</td><td nowrap="nowrap">The&nbsp;qu<span class="diff_chg">a</span>ck&nbsp;brown&nbsp;fox&nbsp;jumped&nbsp;over</td></tr>\n            <tr><td class="diff_next"></td><td class="diff_header" id="from0_2">2</td><td nowrap="nowrap">the&nbsp;lazy&nbsp;dog.</td><td class="diff_next"></td><td class="diff_header" id="to0_2">2</td><td nowrap="nowrap">the&nbsp;lazy&nbsp;dog.</td></tr>\n        </tbody>\n    </table>'
    
    self.failUnlessEqual(table, control)
