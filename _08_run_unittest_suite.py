import doctest
import unittest

from _06_external_doc import _01_external_doc_test
import _01_first_step, _02_more_complex_object_to_test, _03_blank_line_management

suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(_01_external_doc_test))
suite.addTest(doctest.DocTestSuite(_01_first_step))
suite.addTest(doctest.DocTestSuite(_02_more_complex_object_to_test))
suite.addTest(doctest.DocTestSuite(_03_blank_line_management))
suite.addTest(doctest.DocFileSuite('_07_structured_doctest/main_doctest.rst'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
