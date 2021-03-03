# Doctest

-----
 Small repository to play with the [Doctest](https://docs.python.org/3/library/doctest.html)

you can find several examples on how to use doctest:

* 01: small classic example on an easy function
* 02: a function a bit more complex to test
* 03: an example on how to handle blank line in the test
* 04: an example on how to test an exception
* 05: an example of doctest in a class
* 06: an example to launch test oustide the file
* 07: an example with the test outside the function, and in a RST file
* 08: an example on how to launch all the doctest, Usefull for the CI pipeline

----- 
## How to launch the doctest: 

```shell
python3 _01_first_step.py -v
python3 _02_more_complex_object_to_test.py.py -v
python3 _03_blank_line_management.py -v
python3 _04_test_an_exception.py -v
python3 _05_work_with_class.py -v
python3 _06_external_doc/_01_external_doc_test.py -v 
python3 -m doctest -v _07_structured_doctest/main_doctest.rst
python3 _08_run_unittest_suite.py -v
```


## Coming soon

Explanation on how to launch tests with pytest -> no need for ` __name__ == "__main__"` anymore
