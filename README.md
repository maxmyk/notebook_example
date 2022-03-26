# notebook_example

This is a simple Python program that allows you to create notes.

## Installation

```bash
git clone https://github.com/maxmyk/notebook_example
```

## Usage

```
cd notebook_example
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Research results:
### Object: 
Object is a model that can do something and there are things that can be done for it and with it. In other words we can create a separate instance of Class.
#### Examples: 
https://github.com/maxmyk/notebook_example/blob/34b9e4db6e069d279251c2ce7cfdbb8f4e662391/main.py#L269
https://github.com/maxmyk/notebook_example/blob/34b9e4db6e069d279251c2ce7cfdbb8f4e662391/main.py#L278
Also we can pass data when creating objects.

### Class Attributes: 
Class Attributes are those values that are stored in the object. They can be accessed and modified at any time. They are created inside `__init__` method when object is created.
#### Examples:
https://github.com/maxmyk/notebook_example/blob/34b9e4db6e069d279251c2ce7cfdbb8f4e662391/main.py#L8-L21
Starting from line 16 we are creating class attributes and assigning some values to them

We can find all object attributes using dir() function
https://github.com/maxmyk/notebook_example/blob/5e0492e452b1d58e61f3a537bbe18c5638995bdb/main.py#L298
This line of code prints out
```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'content', 'created_at', 'is_pinned', 'label', 'modified_at', 'modify', 'tags']
```


### Class Methods: 
Class Methods are functions inside class that can get external data and manipulate object's attributes. We can use them like class attributes and adding brackets to the end
#### Examples:
https://github.com/maxmyk/notebook_example/blob/34b9e4db6e069d279251c2ce7cfdbb8f4e662391/main.py#L113-L118
https://github.com/maxmyk/notebook_example/blob/34b9e4db6e069d279251c2ce7cfdbb8f4e662391/main.py#L251

### self:
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
This parameter references to current object (instance of the class). We use it to access object (class) variables.
#### Examples:
https://github.com/maxmyk/notebook_example/blob/34b9e4db6e069d279251c2ce7cfdbb8f4e662391/main.py#L113-L118
This example works perfectly well, but
```
def delete_note(whatever_value_i_want, note_id) -> None:
    """
    delete_note method
    Deletes certain note
    """
    whatever_value_i_want.notes.pop(note_id)
```
this code would also work. So, main requirement is that __self__ (or whatever word you want to use instead) must be first parameter.

### `__init__` Method
It is used to assign values to class attributes. Also it is executed when object is created.
#### Examples:
https://github.com/maxmyk/notebook_example/blob/34b9e4db6e069d279251c2ce7cfdbb8f4e662391/main.py#L67-L72

### `__str__` Method
It is used to return a string when object is accessed as `str(my_object)`
#### Examples:
https://github.com/maxmyk/notebook_example/blob/5e0492e452b1d58e61f3a537bbe18c5638995bdb/main.py#L280
https://github.com/maxmyk/notebook_example/blob/5e0492e452b1d58e61f3a537bbe18c5638995bdb/main.py#L301
Last line prints
```

Label:       My first note;
Content:     Just changed my first note :^);
Tags:        ['101', '123'];
Is Pinned:   False;
Created at:  26_03_2022-19:09:50:067264;
Modified at: 26_03_2022-19:09:50:067411.
```
