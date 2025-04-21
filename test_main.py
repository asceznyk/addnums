from main import add

def test_add_empty():
  assert add("") == 0

def test_add_single():
  assert add("3") == 3

def test_add_multiple():
  assert add("89,2,34") == 125

