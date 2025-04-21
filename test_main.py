import pytest
from main import add

def test_add_empty():
  assert add("") == 0

def test_add_single():
  assert add("3") == 3

def test_add_multiple():
  assert add("89,2,34") == 125

def test_add_newline():
  assert add("1\n2,3\n4") == 10

def test_change_delimiter():
  assert add("//*\n1*2*34") == 37

def test_show_negative():
  with pytest.raises(Exception) as ex:
    add("-1")
  assert str(ex.value) == "negative numbers not allowed -1"
  with pytest.raises(Exception) as ex:
    add("//;-1;8;-10;-20")
  assert str(ex.value) == "negative numbers not allowed -1,-10,-20"

def test_greater_than_1000():
  assert add("//;10;1001;2") == 12

def test_multichar_delimiter():
  assert add("//[***]\n10***12***31***46***53") == 152




