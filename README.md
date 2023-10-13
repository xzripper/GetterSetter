<h1 align="center">GetterSetter.</h1>
<p align="center"><b>Getter/Setter. Implements new syntax so you can implement getter and setter in one line.</b></p><br>

From this:
```python
class X:
  def set_text(self, text: str) -> None:
    """Set text."""
    self.o_text.setText(text)

  def get_text(self) -> str:
    """Get text."""
    return self.o_text.text
```

Later...:
```python
text = X()

text.set_text('x')

print(text.get_text())
```

<br>

To this:
```python
self.text = GetterSetter("default value", lambda new_text: self.o_text.setText(new_text))
```

Later...:
```python
my_text = X()

my_text.text[SET, 'my_text']

print(my_text.text[GET])
```

Installation:
```pip install getter_setter``` (not implemented)
<br><b>or</b><br>
install ```getter_setter.py``` and move into your project directory.

<hr><p align="center"><b><i>GetterSetter v1.0.</i></b></p>
