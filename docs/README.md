Are you looking to create a web application instead of a document?
Is CSS with its multiple layout engines too complicated for your needs? 

ui4 provides an alternative for placing UI elements on the screen. Let's look at some examples:

#### Connect to the sides

**Example 1**
```html
<div id="square" top="root.top" left="root.left"></div>
```
<iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0001.html"></iframe>
<button onclick="location.href='examples/example0001.html'">Open in full screen</button>

Pretty close to CSS `top` or `left`, just with the little gaps added between the element and the
edges of the parent.

In addition to `top` and `left`, you can also use `bottom`, `right`, `centerx` and `centery`.

#### Connect to another element

**Example 2**
```html
<div id="square" top="root.top" left="root.left"></div>
<div id="friend" top="square.bottom" left="square.left"></div>
```
<iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0002.html"></iframe>
<button onclick="location.href='examples/example0002.html'">Open in full screen</button>

Same `top` and `left` work with peer elements.

#### Just put it in the center

**Example 3**
```html
<div id="centered" dock="center"></div>
```
<iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0003.html"></iframe>
<button onclick="location.href='examples/example0003.html'">Open in full screen</button>

Instead of using the primitives (like `centerx` and `centery` in this case), `dock` provides
convenient shorter versions: 


(Still easily doable with CSS top/right styles.)

Place (and keep) this button in the middle of the parent:


Place this button below the previous one:


Make this div fill the top of the parent and be 100px in height:


Place this div between A and B: