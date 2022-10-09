Are you looking to create a web application instead of a document?
Is CSS with its multiple layout engines too complicated for your needs? 

ui4 provides an alternative for placing UI elements on the screen. Let's look at some examples:

#### "Connect this to the corner"

<table><th><td>This is a test</td></th><tr><td>This is a test></td></tr></table>
```html
<div id="square" top="root.top" left="root.left"></div>
```
<SUP>EXAMPLE 1</SUP>
<iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0001.html"></iframe>
<button onclick="location.href='examples/example0001.html'">Open in full screen</button>

Pretty close to CSS `top` or `left`, just with the little gaps added between the element and the
edges of the parent.

In addition to `top` and `left`, you can also use `bottom`, `right`, `width`, `height`, `centerx`
and `centery`.

#### "Connect A to B"

<table><th><td>This is a test</td></th><tr><td>This is a test></td></tr></table>
```html
<div id="b" top="root.top" left="root.left">B</div>
<div id="a" top="square.bottom" left="square.left">A</div>
```
<SUP>EXAMPLE 2</SUP>
<iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0002.html"></iframe>
<button onclick="location.href='examples/example0002.html'">Open in full screen</button>

Same `top` and `left` work with peer elements in an intuitive way.

#### "Just put it in the center"

<table><th><td>This is a test</td></th><tr><td>This is a test></td></tr></table>
```html
<div id="centered" dock="center"></div>
```
<SUP>EXAMPLE 3</SUP>
<iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0003.html"></iframe>
<button onclick="location.href='examples/example0003.html'">Open in full screen</button>

Instead of using the primitives (like `centerx` and `centery` in this case), `dock` provides
convenient and easier to read options.

#### "This is a top banner"



Place this div between A and B: