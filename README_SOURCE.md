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
<div id="square" top="root.top" left="root.left">B</div>
<div id="friend" top="square.bottom" left="square.left">A</div>
```

Same `top` and `left` work with peer elements.

#### Just put it in the center

```html example solid_sized
<div id="centered" dock="center"></div>
```

Instead of using the primitives (like `centerx` and `centery` in this case), `dock` provides
convenient and easier to read options.


(Still easily doable with CSS top/right styles.)

Place (and keep) this button in the middle of the parent:


Place this button below the previous one:


Make this div fill the top of the parent and be 100px in height:


Place this div between A and B:
