Are you looking to create a web application instead of a document?
Is CSS with its multiple layout engines too complicated for your needs? 

ui4 provides an alternative for placing UI elements on the screen. Let's look at some examples:

#### "Connect this to the corner"

```html example solid_sized
<div id="square" top="root.top" left="root.left"></div>
```

Pretty close to CSS `top` or `left`, just with the little gaps added between the element and the
edges of the parent.

In addition to `top` and `left`, you can also use `bottom`, `right`, `width`, `height`, `centerx`
and `centery`.

#### "Connect A to B"

```html example solid_sized
<div id="b" top="root.top" left="root.left">B</div>
<div id="a" top="b.bottom" left="b.left">A</div>
```

Same `top` and `left` work with peer elements in an intuitive way, "pushing" against them instead
of aligning with the edge.

#### "Just put it in the center"

```html example solid_sized
<div id="centered" dock="center"></div>
```

Instead of using the primitives (like `centerx` and `centery` in this case), `dock` provides
convenient and easier to read options.

#### "This is a top banner"

```html example solid
<div id="topBanner" dock="top" height="30"></div>
```

Docking to the top connects the left, top and right edges of the element; bottom or height is set
separately.

All the options for docking to the parent are:
- `top`, `left`, `right`, `bottom`
- `topleft`, `topright`, `bottomleft`, `bottomright`
- `topcenter`, `leftcenter`, `rightcenter`, `bottomcenter`
- `all`

#### "Put A above B"

```html example solid
<div id="b" dock="center" width="50" height="30"></div>
<div id="a" dock="b.above" height="30"></div>
```

These convenience docking options, `above`, `below`, `rightof` and `leftof`, place the element
besides another one and set the shared dimension (width in the example above) to be the same.

Place this div between A and B:
